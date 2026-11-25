import re, json, numpy as np, librosa
from scipy.io import wavfile
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
sr,a=wavfile.read(S+'/long/a1_16k.wav'); a=a.astype(np.float32)/32768
if a.ndim>1: a=a.mean(1)
M=librosa.feature.mfcc(y=a,sr=sr,n_mfcc=20,n_fft=400,hop_length=160,n_mels=40)   # 100 frames/s
D=librosa.feature.delta(M); X=np.vstack([M,D]).T
rms=librosa.feature.rms(y=a,frame_length=400,hop_length=160)[0]; db=20*np.log10(rms+1e-9)
# labelled turns from the checked script
L=[l for l in open(S+'/deliverables/MartinezCid_full_script.md') if re.match(r'\*\*\d+:\d\d · (George|Jordi):',l)]
turns=[]
for l in L:
    m=re.match(r'\*\*(\d+):(\d\d) · (George|Jordi):',l); turns.append((int(m[1])*60+int(m[2]),m[3][0]))
turns=[(t,sp,turns[i+1][0] if i+1<len(turns) else t+20) for i,(t,sp) in enumerate(turns)]
def feat(t):
    i=int(t*100); f=X[i:i+100]; v=db[i:i+100]>-38
    if v.sum()<30: return None
    f=f[v]; return np.concatenate([f.mean(0),f.std(0)])
Xs=[];ys=[];gs=[]
for k,(t0,sp,t1) in enumerate(turns):
    for t in np.arange(t0+1.5,t1-2.5,0.5):
        f=feat(t)
        if f is not None: Xs.append(f); ys.append(sp=='J'); gs.append(k)
Xs=np.array(Xs); ys=np.array(ys); gs=np.array(gs); print('train windows',len(ys),'jordi share',ys.mean().round(2),'turns',len(turns))
# leave-turns-out check
acc=[]
for fold in range(5):
    te=gs%5==fold; sc=StandardScaler().fit(Xs[~te]); clf=LogisticRegression(max_iter=2000,C=0.5,class_weight='balanced').fit(sc.transform(Xs[~te]),ys[~te])
    acc.append((clf.predict(sc.transform(Xs[te]))==ys[te]).mean())
print('held-out accuracy',np.round(acc,3))
sc=StandardScaler().fit(Xs); clf=LogisticRegression(max_iter=2000,C=0.5,class_weight='balanced').fit(sc.transform(Xs),ys)
# predict every 0.1 s with a 1 s window centred on t
T=np.arange(0,len(a)/sr-1,0.1); P=np.full(len(T),np.nan)
for i,t in enumerate(T):
    f=feat(max(0,t-0.5))
    if f is not None: P[i]=clf.predict_proba(sc.transform(f[None]))[0,1]
np.save(S+'/yt2/spk_prob.npy',np.stack([T,P]))
# speech activity at 0.1 s
act=np.array([ (db[int(t*100):int(t*100)+10]>-40).mean()>0.3 for t in T])
# smooth probability (1.5 s median over speech windows), fill gaps
Pf=P.copy(); idx=np.where(~np.isnan(Pf))[0]; Pf=np.interp(np.arange(len(Pf)),idx,Pf[idx])
from scipy.ndimage import median_filter
Ps=median_filter(Pf,15)
lab=np.where(Ps>0.5,'J','G')
# hysteresis: a change must persist 1.0 s
out=list(lab); cur=out[0]; i=0
while i<len(out):
    if out[i]!=cur:
        j=i
        while j<len(out) and out[j]!=cur: j+=1
        if j-i<10: out[i:j]=[cur]*(j-i)
        else: cur=out[i]
        i=j
    else: i+=1
fin=[o if act[k] or True else '-' for k,o in enumerate(out)]
json.dump(fin,open(S+'/yt2/speaker.json','w'))
# compare with the script turns
agree=np.mean([fin[int(t*10)]==sp for t0,sp,t1 in turns for t in np.arange(t0+1,t1-1,0.5) if int(t*10)<len(fin)])
print('agreement with script turns',round(agree,3))
runs=[];s0=0
for k in range(1,len(fin)+1):
    if k==len(fin) or fin[k]!=fin[s0]: runs.append((round(s0/10,1),round(k/10,1),fin[s0])); s0=k
print(len(runs),'runs'); print(runs[:60])
