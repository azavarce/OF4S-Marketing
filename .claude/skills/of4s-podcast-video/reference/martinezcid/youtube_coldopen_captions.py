# cold-open caption words: transcribe each clip on its own (a single pass over the joined clips invents "and"s between them)
import runpy,sys,json,numpy as np
sys.argv=['x','plan']
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
g=runpy.run_path(S+'/yt2/yt2_build.py'); COS=g['COS']; FPS=30
from scipy.io import wavfile
from faster_whisper import WhisperModel
_,a=wavfile.read(S+'/long/a1_16k.wav');a=a.astype(np.float32)/32768
a=a.mean(1) if a.ndim>1 else a
m=WhisperModel('large-v3',device='cpu',compute_type='int8',cpu_threads=4)
off=0; clips={}
for nm,s,e,lay,clip in COS:
    nf=round((e-s)*FPS); clips.setdefault(clip,[]).append((s,e,off/FPS)); off+=nf
W=[]
FIX={'i':'I','Equity':'equity','Partners':'partners','100-page':'hundred-page','argument.':'arguments.','OK,':'okay,','program':'approached me and'}
for clip,pcs in clips.items():
    y=np.concatenate([a[int(s*16000):int(s*16000)+int((e-s)*16000)] for s,e,_ in pcs]); t0=pcs[0][2]
    sg,_=m.transcribe(np.concatenate([np.zeros(3200,np.float32),y,np.zeros(8000,np.float32)]),beam_size=5,language='en',word_timestamps=True)
    ws=[[max(0,t0+w.start-0.2),t0+w.end-0.2,w.word.strip()] for z in sg for w in z.words]
    while ws and ws[0][2].lower().strip(',') in ('and','microsoft','then'): ws=ws[1:]   # clips start after these (checked on the waveform)
    for w in ws: w[2]=FIX.get(w[2],w[2])
    if ws: ws[0][2]=ws[0][2][0].upper()+ws[0][2][1:]
    W+=ws; print(clip,' '.join(w[2] for w in ws),flush=True)
json.dump(W,open(S+'/yt2/build/co_words.json','w'))
