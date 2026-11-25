# Cut her footage into pieces (one ffmpeg at a time), crossfade the audio at every pause cut (40 ms, equal power), speed 1.1x.
import numpy as np, subprocess, json, os, sys
from scipy.io import wavfile
M='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad/manual'
def nfr(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]).strip())
def build(src,seg,out,work,reuse_video=None,SP=1.1,FPS=30,SR=48000):
    os.makedirs(work,exist_ok=True); lst=[]; nfs=[]
    for i,(s,e) in enumerate(seg):
        p_=reuse_video[i] if reuse_video else f"{work}/p{i:02d}.mp4"
        if not reuse_video:
            subprocess.run(['ffmpeg','-v','error','-y','-ss',f"{s:.3f}",'-t',f"{e-s+0.2:.3f}",'-i',src,'-vf','scale=1080:1920:flags=lanczos,fps=30','-frames:v',str(round((e-s)*FPS)),
                '-an','-c:v','libx264','-crf','14','-preset','medium','-pix_fmt','yuv420p',p_],check=True)
        nfs.append(nfr(p_)); lst.append(f"file '{p_}'\n")
    open(work+'/list.txt','w').write(''.join(lst))
    au=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-vn','-ac','2','-ar',str(SR),'-f','f32le','-'],capture_output=True).stdout,np.float32).reshape(-1,2)
    SPF=SR//FPS; N=sum(nfs)*SPF; y=np.zeros((N+SR,2),np.float32); XF=int(0.02*SR); r=int(0.012*SR); f=0
    for i,((s,e),nf) in enumerate(zip(seg,nfs)):
        n=nf*SPF; pa=XF if i>0 else 0; pb=XF if i+1<len(seg) else 0
        i0=int(round(s*SR))-pa; x=au[max(0,i0):i0+n+pa+pb].copy()
        if len(x)<n+pa+pb: x=np.pad(x,((0,n+pa+pb-len(x)),(0,0)))
        if pa: x[:2*pa]*=np.sin(np.linspace(0,np.pi/2,2*pa))[:,None]
        else: x[:r]*=np.linspace(0,1,r)[:,None]
        if pb: x[-2*pb:]*=np.cos(np.linspace(0,np.pi/2,2*pb))[:,None]
        else: x[-r:]*=np.linspace(1,0,r)[:,None]
        y[f*SPF-pa:f*SPF-pa+len(x)]+=x; f+=nf
    wavfile.write(work+'/a.wav',SR,y[:N])
    subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',work+'/list.txt','-i',work+'/a.wav','-filter_complex',f"[0:v]setpts=PTS/{SP},fps=30[v];[1:a]atempo={SP}[a]",
        '-map','[v]','-map','[a]','-c:v','libx264','-crf','14','-preset','medium','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k',out],check=True)
    subprocess.run(['ffmpeg','-v','error','-y','-i',out,'-ac','1','-ar','16000',out.replace('.mp4','.wav')],check=True)
    t=0; mp=[]
    for (s,e),nf in zip(seg,nfs): d=nf/FPS/SP; mp.append([s,e,round(t,4),round(t+d,4)]); t+=d
    return mp
if __name__=='__main__':
    job=sys.argv[1]
    if job=='laborpool':
        # same pieces as laborpool2 (lp_edit.py), audio rebuilt with crossfades
        exec(open(M+'/lp_edit.py').read().split("import os;")[0])
        vids=[M+f'/lp2/p{i:02d}.mkv' for i in range(len(seg))]
        mp=build(M+'/laborpool.mp4',seg,M+'/laborpool3.mp4',M+'/lp3',reuse_video=vids)
    if job=='employees':
        sr,a=wavfile.read(M+'/employees.wav'); a=a.astype(float)/32768; n=int(.01*sr)
        L=lambda t: 20*np.log10(np.sqrt(np.mean(a[int(t*sr):int(t*sr)+n]**2))+1e-9)
        seg=[]
        for s2,e2 in [(0.0,10.72),(15.14,28.24),(29.00,31.86)]:
            lv=np.array([L(t) for t in np.arange(s2,e2,0.01)]); q=lv<-40; cuts=[]; i=0
            while i<len(q):
                if q[i]:
                    j=i
                    while j<len(q) and q[j]: j+=1
                    if (j-i)*0.01>0.22 and i>0 and j<len(q): cuts.append((s2+i*0.01+0.06,s2+j*0.01-0.06))
                    i=j
                else: i+=1
            pts=[s2]+[x for c in cuts for x in c]+[e2]; seg+=[(round(pts[k],3),round(pts[k+1],3)) for k in range(0,len(pts),2)]
        mp=build(M+'/employees.mp4',seg,M+'/employees5.mp4',M+'/emp5')
    json.dump(mp,open(M+f'/{job}_xfmap.json','w')); print(job,'pieces',len(mp),'total',mp[-1][3])
