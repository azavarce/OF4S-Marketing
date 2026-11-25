import subprocess,json,sys
import numpy as np
S='/tmp/claude-0/-home-user-OF4S-Marketing/94d491a9-d326-522d-bff4-7538a8d94c4a/scratchpad'
f=S+'/raw2/client_cfr.mov'
# background patch on the client camera (whiteboard/wall area, left of Eric), small and gray
t0,t1=float(sys.argv[1]),float(sys.argv[2])
raw=subprocess.run(['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',f,'-vf','crop=1000:1000:0:500,scale=160:160,format=gray','-f','rawvideo','-'],capture_output=True).stdout
v=np.frombuffer(raw,np.uint8).reshape(-1,160,160).astype(np.float32)
def shift(a,b):
    A=np.fft.fft2(a-a.mean()); B=np.fft.fft2(b-b.mean()); R=A*np.conj(B); R/=np.abs(R)+1e-9
    r=np.fft.ifft2(R).real; y,x=np.unravel_index(np.argmax(r),r.shape)
    if y>80: y-=160
    if x>80: x-=160
    return np.hypot(x,y)
mv=np.array([shift(v[i],v[max(0,i-9)]) for i in range(1,len(v))])
json.dump({'t0':t0,'mv':mv.tolist()},open(S+'/camshake.json','w'))
# report seconds with movement
sec=[(t0+i/30) for i in range(len(mv))]
bad=[]; cur=None
for i,m in enumerate(mv):
    if m>=0.8:
        if cur is None: cur=[sec[i],sec[i]]
        else: cur[1]=sec[i]
    else:
        if cur and sec[i]-cur[1]>0.4: bad.append(cur); cur=None
if cur: bad.append(cur)
print('camera moving (source seconds):',[(round(a,1),round(b,1)) for a,b in bad if b-a>0.1])
