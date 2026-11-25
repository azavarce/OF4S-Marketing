# fillers / stutters / false starts -> removal spans, each checked against the waveform
import json, numpy as np
from scipy.io import wavfile
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
sr,a=wavfile.read(S+'/long/a1.wav'); a=a.astype(np.float32)/32768
a=a.mean(1) if a.ndim>1 else a
n=int(.01*sr); LV=lambda t: 20*np.log10(np.sqrt(np.mean(a[int(t*sr):int(t*sr)+n]**2))+1e-9)
def snap(t,lo,hi):
    ts=np.arange(t+lo,t+hi,0.01); v=[LV(x) for x in ts]; k=int(np.argmin(v)); return float(ts[k]),v[k]
W=json.load(open(S+'/yt2/disfl_words.json'))
A1=[w for z in json.load(open(S+'/long/a1.json'))['segments'] for w in z['words']]
norm=lambda x:''.join(c for c in x.lower() if c.isalnum() or c=="'")
FILL={'um','uh','umm','uhm','er','ah','hmm','mm','erm'}
EMPH={'very','really','so','no','yeah','okay','bye','right','odd','more','too','much','many','ha','yes','go','well','thank','you','oh'}
tok=[norm(w[2]) for w in W]
KEEP=[(6.30,965.70),(1056.20,1212.20)]
rm=[]   # (first removed word idx, last removed word idx, reason)
i=0
while i<len(W):
    if tok[i] in FILL: rm.append((i,i,'filler')); i+=1; continue
    done=False
    for L in (3,2,1):
        a_,b_=tok[i:i+L],tok[i+L:i+2*L]
        if len(b_)==L and a_==b_ and all(a_) and W[i+2*L-1][0]-W[i][0]<3.0:
            if L==1 and a_[0] in EMPH: break
            if W[i+L-1][2].rstrip()[-1:] in '.?!': break        # emphatic repeated sentence ("It's odd. It's odd.") stays
            rm.append((i,i+L-1,'repeat:'+' '.join(a_))); i+=L; done=True; break
    if not done: i+=1
cuts=[]; log=[]
for i0,i1,why in rm:
    if i1+1>=len(W): continue
    ws,nx=W[i0][0],W[i1+1][0]
    if not any(a<=ws and nx<=b for a,b in KEEP): continue
    c0,l0=snap(ws,-0.20,0.06); c1,l1=snap(nx,-0.25,0.03)
    ok=l0<-32 and l1<-32 and 0.10<=c1-c0<=2.5
    # safety: the normal transcript must not have a real word in the span (other than the removed tokens)
    rem={tok[k] for k in range(i0,i1+1)}
    bad=[w[2] for w in A1 if c0+0.05<(w[0]+w[1])/2<c1-0.05 and norm(w[2]) not in rem|FILL]
    if bad: ok=False
    log.append((round(c0,2),round(c1,2),why,round(l0),round(l1),'OK' if ok else 'SKIP',' '.join(bad)))
    if ok: cuts.append([round(c0,3),round(c1,3)])
# merge overlapping
cuts.sort(); M=[]
for c in cuts:
    if M and c[0]<=M[-1][1]+0.02: M[-1][1]=max(M[-1][1],c[1])
    else: M.append(c)
json.dump(M,open(S+'/yt2/cuts.json','w'))
for l in log: print(*l)
print('cuts',len(M),'removed seconds',round(sum(b-a for a,b in M),1),'skipped',sum(1 for l in log if l[5]=='SKIP'))
