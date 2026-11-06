import numpy as np, subprocess, json
from scipy.io import wavfile
S='/tmp/claude-0/-home-user-OF4S-Marketing/94d491a9-d326-522d-bff4-7538a8d94c4a/scratchpad'
A=S+'/audiodl'; W=S+'/mixwork'; Y=S+'/long/yt2'; SR=48000
def load(path,ss=0,dur=None):
    c=['ffmpeg','-v','error','-ss',str(ss),'-i',path]+(['-t',str(dur)] if dur else [])+['-ac','2','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
def db(x): return 10**(x/20)
def fade(x,fi=0,fo=0):
    x=x.copy(); n=len(x)
    if fi: k=int(fi*SR); x[:k]*=np.linspace(0,1,k)[:,None]
    if fo: k=int(fo*SR); x[n-k:]*=np.linspace(1,0,k)[:,None]
    return x
def lufs(x):
    wavfile.write(W+'/_m.wav',SR,x.astype(np.float32))
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',W+'/_m.wav','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
sr,base=wavfile.read(Y+'/audio.wav'); base=base.astype(np.float32)/32768
N=len(base); mix=np.zeros_like(base)
def put(x,t,g):
    i=int(round(t*SR)); x=x[:max(0,N-i)]; mix[i:i+len(x)]+=x*db(g)
P=json.load(open(S+'/long/mixparams.json')); M=json.load(open(Y+'/marks.json'))
cE,sS,mS=M['coldEnd'],M['showStart'],M['mainStart']
VL=lufs(base[:int(cE*SR)])
# 1) cold open: trailer track, its first big hit lands on the ChatGPT line, drops away under the last two lines,
#    its final hit lands on the title card
trk=A+'/music/audioatlant-revolution-epic-action-cinematic-trailer-short-1-494839.mp3'
M0=18.3-M['c5']-0.05; a_=load(trk,M0,cE); t=np.arange(len(a_))/SR
c7=M['drop']   # music drops away under "Don't work from home..."
ea=np.interp(t,[0,c7-0.3,c7+0.8,cE],[1,1,0.15,0.0])
gm=VL-7-lufs(load(trk,8,10)); put(fade(a_*ea[:,None],0.02,0.1),0,gm)
b_=load(trk,29.70,3.2); put(fade(b_,0.01,1.0),cE-0.02,gm+2)
sw=load(A+'/sfx/swoosh05.mp3')
for c in M['cuts']: put(sw,c-0.30,P['whoosh_db']-8)          # light whoosh on each cut
# 2) showcase: the podcast title music (same sting the episode already uses) starts here and carries into the conversation
sg=load(A+'/music/'+P['sting_track']); fl=load(A+'/music/'+P['title_track'])
h=int(P['handoff']*SR); k=int(0.05*SR); f0=int((P['handoff']+P['full_off'])*SR); w=np.linspace(0,1,k)[:,None]
st=np.concatenate([sg[:h], sg[h:h+k]*(1-w)+fl[f0:f0+k]*w, fl[f0+k:]])
T0=mS-sS; H=P['tail_hold']; FO=P['tail_fade']; D=db(P['duck_db'])
tt=np.arange(len(st))/SR; env=np.interp(tt,[0,T0,T0+0.6,T0+H,T0+H+FO],[1,1,D,D,0])
put(st*env[:,None],sS,P['sting_db'])
pp=load(A+'/sfx/pop.mp3'); wd=load(A+'/sfx/whoosh_ds.mp3')
put(sw,sS-0.05,P['whoosh_db']-4)                                 # divider + tags slide in
for d_ in (0.25,0.55): put(sw,sS+d_-0.15,P['whoosh_db']-6)
put(sw,sS+2.0,P['whoosh_db']-8)                                  # tags out
for d_ in (2.6,2.9,3.2,3.5): put(pp,sS+d_-0.05,P['pop_db']-2)     # promise items
# 3) end screen (unchanged)
E=M['endStart']; Ln=N/SR-E
om=load(A+'/music/'+P['outro_track'])[int(P['outro_off']*SR):int((P['outro_off']+Ln)*SR)]
put(fade(om,0.3,3.0),E,P['outro_db'])
put(load(A+'/sfx/'+P['shimmer']+'.mp3'),E+0.70,P['shimmer_db'])
put(pp,E+3.68,P['pop_db'])
y=base+mix
I=lufs(y); g=P['target']-I; y*=db(g); print('measured',I,'gain',round(g,2),'M0',round(M0,2))
wavfile.write(W+'/mix.wav',SR,y.astype(np.float32))
subprocess.run(['ffmpeg','-v','error','-y','-i',W+'/mix.wav','-af','alimiter=limit=0.89:attack=1:release=60:level=false','-c:a','pcm_s16le',W+'/mix16.wav'],check=True)
out=S+'/long/EPGD_Podcast_YouTube_v7.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-i',Y+'/video.mp4','-i',W+'/mix16.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
  '-bsf:v','h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1','-movflags','+faststart',out],check=True)
print('OUT',out)
