# Rebuild the audio of one of Joanne's exported cuts from the declipped master: find, every 0.1 s, where her audio sits in the master,
# group into runs with a constant offset, and splice the clean master audio along that map (20 ms crossfades at each splice).
import numpy as np, json, sys, subprocess
from scipy.io import wavfile
from scipy.signal import correlate
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'; name=sys.argv[1]
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{S}/manual/{name}.mp4','-vn','-ac','1','-ar','48000','-c:a','pcm_f32le',f'{S}/nr/her_{name}.wav'],check=True)
sr,h=wavfile.read(f'{S}/nr/her_{name}.wav'); sr,m=wavfile.read(S+'/long/a1_dc.wav')
SH=json.load(open(S+'/manual/shotmap.json'))[name]; T=len(h)/sr
def shot_raw(t):
    for t0,t1,raw,x in SH:
        if t0<=t<t1+1e-6: return raw+(t-t0)
    return SH[-1][2]+(t-SH[-1][0])
W=int(0.5*sr); rows=[]
for t in np.arange(0,T-0.5,0.1):
    a=h[int(t*sr):int(t*sr)+W]
    if np.sqrt(np.mean(a**2))<10**(-40/20): rows.append((t,None,0)); continue
    c0=shot_raw(t); w=int(2.5*sr); b=m[max(0,int(c0*sr)-w):int(c0*sr)+W+w]
    cc=correlate(b,a,mode='valid'); k=int(np.argmax(np.abs(cc)))
    nc=abs(cc[k])/np.sqrt((a**2).sum()*(b[k:k+W]**2).sum()+1e-12)
    rows.append((t,(max(0,int(c0*sr)-w)+k)/sr-t,nc))
# second pass: windows that didn't match nearby get a wide search (+-60 s), in case she took the line from elsewhere
for i,(t,off,nc) in enumerate(rows):
    if off is None or nc>0.8: continue
    a=h[int(t*sr):int(t*sr)+W]; c0=shot_raw(t); w=int(60*sr); lo=max(0,int(c0*sr)-w); b=m[lo:int(c0*sr)+W+w]
    cc=correlate(b,a,mode='valid',method='fft'); k=int(np.argmax(np.abs(cc)))
    n2=abs(cc[k])/np.sqrt((a**2).sum()*(b[k:k+W]**2).sum()+1e-12)
    if n2>nc: rows[i]=(t,(lo+k)/sr-t,n2)
# offsets: keep confident ones, fill gaps with neighbours
d=[r[1] if (r[1] is not None and r[2]>0.8) else None for r in rows]
last=None
for i in range(len(d)):
    if d[i] is None: d[i]=last
    else: last=d[i]
nxt=None
for i in range(len(d)-1,-1,-1):
    if d[i] is None: d[i]=nxt
    else: nxt=d[i]
# median-smooth and quantise into runs
d=np.array(d,float); from scipy.ndimage import median_filter; d=median_filter(d,5)
runs=[[0.0,d[0]]]
for i in range(1,len(d)):
    if abs(d[i]-runs[-1][1])>0.004: runs.append([rows[i][0],d[i]])
print('splices',len(runs)-1, [ (round(a,2),round(b,3)) for a,b in runs])
# refine each splice to 5 ms: her audio switches from offset A to offset B where B starts explaining it better
k_=np.dot(h[int(2*sr):int(8*sr)],m[int((2+runs[0][1])*sr):int((8+runs[0][1])*sr)])/np.dot(m[int((2+runs[0][1])*sr):int((8+runs[0][1])*sr)],m[int((2+runs[0][1])*sr):int((8+runs[0][1])*sr)])
for j in range(1,len(runs)):
    A=runs[j-1][1]; B=runs[j][1]; tb=runs[j][0]; ts=np.arange(max(runs[j-1][0]+0.05,tb-0.6),min(tb+0.3,(runs[j+1][0] if j+1<len(runs) else T)-0.05),0.005)
    w=int(0.01*sr); eA=[];eB=[]
    for t in ts:
        i=int(t*sr); hh=h[i:i+w]
        eA.append(np.sum((hh-k_*m[int((t+A)*sr):int((t+A)*sr)+w])**2)); eB.append(np.sum((hh-k_*m[int((t+B)*sr):int((t+B)*sr)+w])**2))
    eA=np.array(eA); eB=np.array(eB); cost=[eA[:q].sum()+eB[q:].sum() for q in range(len(ts))]
    runs[j][0]=float(ts[int(np.argmin(cost))])
print('refined splices',[round(a,3) for a,b in runs])
low=[r for r in rows if r[1] is not None and r[2]<=0.8]; print('low-confidence windows',len(low),'of',sum(1 for r in rows if r[1] is not None))
# splice
y=np.zeros(len(h),np.float32); XF=int(0.02*sr)
for j,(ts,off) in enumerate(runs):
    te=runs[j+1][0] if j+1<len(runs) else T
    i0=int(ts*sr); i1=int(te*sr); pa=XF if j>0 else 0; pb=XF if j+1<len(runs) else 0
    s0=int((ts+off)*sr)-pa; x=m[s0:s0+(i1-i0)+pa+pb].astype(np.float32).copy()
    if pa: x[:2*pa]*=np.sin(np.linspace(0,np.pi/2,2*pa))
    if pb: x[-2*pb:]*=np.cos(np.linspace(0,np.pi/2,2*pb))
    y[i0-pa:i0-pa+len(x)]+=x[:len(y)-(i0-pa)]
# match her overall level so the music balance stays as she had it, but with headroom (loudness is normalised later)
y*=np.sqrt(np.mean(h**2))/np.sqrt(np.mean(y**2)+1e-12)*0.5
# check: the rebuilt track should match hers closely everywhere
seg=[np.corrcoef(h[i:i+sr],y[i:i+sr])[0,1] for i in range(0,len(h)-sr,sr) if np.sqrt(np.mean(h[i:i+sr]**2))>0.01]
print('per-second match: min',round(min(seg),3),'median',round(float(np.median(seg)),3))
wavfile.write(f'{S}/nr/clean_{name}.wav',sr,y)
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{S}/manual/{name}.mp4','-i',f'{S}/nr/clean_{name}.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','pcm_s24le',f'{S}/manual/{name}_clean.mov'],check=True)
