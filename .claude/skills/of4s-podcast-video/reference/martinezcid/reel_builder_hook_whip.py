# Martinez-Cid Law · Reel 2 "Talent comes before clients" — adapted from the EPGD build recipe (TECH.md)
import json, subprocess, os, sys, numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
R=S+'/r4/build'; os.makedirs(R,exist_ok=True)
FPS=30; SR=48000; SPF=SR//FPS; O=4.871            # Client.MOV time = master (George audio) time + O
CLIENT=S+'/src/Client.MOV'; GEORGE=S+'/src/George.MOV'
STEP=sys.argv[1] if len(sys.argv)>1 else 'all'
OUT=os.environ.get('OUTNAME','MartinezCid_reel2_talent_v1.mp4')
def run(c): subprocess.run(c,check=True)
def nfr(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]).strip())

# ---------- timeline (master times; audio always from George's file) ----------
HD=json.load(open(S+'/r2/head.json'))
def J(seg,tight=False): return dict(cam='J',top=HD[seg]['top_med'],x=HD[seg]['x_med'],tight=tight)
G1=dict(cam='G',top=1344,x=1080); G2=dict(cam='G',top=1320,x=1320)
SPL=dict(cam='S',gtop=1330,gx=1320,jtop=HD['C3']['top_med'],jx=HD['C3']['x_med'])
GQ=dict(cam='G',top=1344,x=1320); G3=dict(cam='G',top=1340,x=1290)
# base lines (cleanly cut, verified at word boundaries)
SPL1=dict(cam='S',gtop=1300,gx=1330,jtop=1500,jx=760)
BASE=[('H1',42.84,46.66,J('S1a',True),'J'),('H2',121.88,127.20,J('S1a',True),'J'),('BLACK',0,0.6,dict(cam='K'),'K'),
   ('S3b',39.74,42.40,J('S1a'),'J'),
   ('S4a',101.66,104.60,J('S1a'),'J'),('S4b1',104.60,105.64,SPL1,'S'),('S4b2',105.97,108.33,SPL1,'S'),
   ('S5a1',112.10,115.94,J('S1a'),'J'),('S5a2',117.44,120.17,J('S1a'),'J'),('S5b',121.88,127.58,J('S1a'),'J'),
   ('S6',127.58,130.89,SPL1,'S'),('S7a',130.89,131.90,SPL1,'S'),('S7b',131.90,141.90,J('S1a'),'J'),
   ('S8a',143.62,147.40,J('S1a'),'J'),('S8b',147.98,149.44,J('S1a'),'J'),('S8c',150.24,153.01,J('S1a'),'J'),
   ('S9a',155.66,160.82,J('S1a'),'J'),('S9b',162.34,163.80,J('S1a'),'J')]
# George listening cutaways (master times; he is attentive and never looking down here)
CUT=[]
_sr,_a=wavfile.read(S+'/long/a1.wav'); _a=_a.astype(np.float32)/32768
if _a.ndim>1: _a=_a.mean(1)
def _lv(s,e):
    n=int(.01*_sr); return np.array([20*np.log10(np.sqrt(np.mean(_a[i:i+n]**2))+1e-9) for i in range(int(s*_sr),int(e*_sr),n)])
def pauses(s,e,minp,keep):
    L=_lv(s,e); q=L<-42; out=[]; i=0
    while i<len(L):
        if q[i]:
            j=i
            while j<len(L) and q[j]: j+=1
            if (j-i)*0.01>=minp and i>0 and j<len(L): out.append((s+i*0.01+keep/2,s+j*0.01-keep/2))
            i=j
        else: i+=1
    return out
T=[]
for name,s,e,v,who in BASE:
    if who=='K': T.append(('WHIP',0.0,0.3,v)); continue
    pc=pauses(s,e,0.24,0.20)
    pts=[s]+[x for c in pc for x in c]+[e]
    for k in range(0,len(pts),2):
        a,b=pts[k],pts[k+1]
        # split at cutaway edges
        edges=sorted({a,b}|{x for c0,c1,_ in CUT for x in (c0,c1) if a<x<b})
        for u,w in zip(edges,edges[1:]):
            vv=next((g for c0,c1,g in CUT if c0<=u and w<=c1),v) if who=='J' else v
            T.append((f"{name}_{len(T)}",round(u,3),round(w,3),vv))
print('timeline items',len(T),'voice length',round(sum(w-u for _,u,w,_ in T),2))
def measure(st,en):
    r=subprocess.run(['ffmpeg','-v','error','-ss',f"{st+O:.2f}",'-t',f"{max(en-st,0.3):.2f}",'-i',CLIENT,'-vf','fps=6,scale=540:960,format=gray','-f','rawvideo','-'],capture_output=True).stdout
    F=np.frombuffer(r,np.uint8).reshape(-1,960,540); tops=[];xs=[];ext=[]
    for f in F:
        reg=f[150:460,30:450]<70; rows=np.where(reg.sum(1)>10)[0]
        if len(rows)==0: continue
        t0=rows[0]; tops.append((t0+150)*4); xs.append((reg[t0:t0+40].nonzero()[1].mean()+30)*4)
        cols=np.where((f[150:700,0:540]<60).sum(0)>25)[0]          # dark suit/hair/sleeve columns = his body + arms
        if len(cols): ext.append((cols.min()*4,cols.max()*4))
    tops=np.array(tops); xs=np.array(xs); ext=np.array(ext) if ext else np.array([[600,1400]])
    return dict(top=float(np.percentile(tops,30)),xlo=float(min(np.percentile(xs,5),np.percentile(ext[:,0],10)+150)),xhi=float(max(np.percentile(xs,95),np.percentile(ext[:,1],90)-150)),hx=float(np.median(xs)))
for k,(n,s,e,v) in enumerate(T):
    if v['cam']=='J':
        m=measure(s,e)
        wide=(s<265 or 276<s<282); T[k]=(n,s,e,dict(v,top=m['top'],cx=m['hx']+110,H=2050))
# one steady, wider framing for the whole "two things / money / vibes / law firms" stretch (source 256-276.3)
_m=measure(256.17,276.20)
for k,(n,s,e,v) in enumerate(T):
    if v['cam']=='J' and 256<=s<276.3: T[k]=(n,s,e,dict(v,top=_m['top'],cx=_m['hx']+60,H=2150,hp=0.30))
_o=0
for n,s,e,v in T:
    if v['cam']=='J' and 256<=s<276.3: print('steady',n,round(_o,2)); 
    _o+=e-s
# ONE locked framing for Jordi across the reel: no re-centering between pieces
_J=[v for n,s,e,v in T if v['cam']=='J']
_lock=dict(top=float(np.median([v['top'] for v in _J])),cx=float(np.median([v['cx'] for v in _J])),H=2050)
T=[(n,s,e,dict(v,**_lock) if v['cam']=='J' else v) for n,s,e,v in T]
# whip breathing room: hook's last word ends, hold 0.2 s (voice muted), 0.3 s whip, story speaker talks 0.1 s after he is on screen
_kw=[k for k,(n,s,e,v) in enumerate(T) if v['cam']=='K'][0]
def _spk(t): return 20*np.log10(np.sqrt(np.mean(_a[int(t*_sr):int(t*_sr)+int(.01*_sr)]**2))+1e-9)>-38
n_,s_,e_,v_=T[_kw-1]; _lw=max(t for t in np.arange(e_-0.6,e_-0.005,0.01) if _spk(t))+0.01
T[_kw-1]=(n_,s_,round(_lw+0.2,3),dict(v_,mute_after=round(_lw+0.03,3)))
n_,s_,e_,v_=T[_kw+1]; _fw=min(t for t in np.arange(s_-0.05,s_+0.6,0.01) if _spk(t))
T[_kw+1]=(n_,round(_fw-0.1,3),e_,v_)
T[_kw]=(T[_kw][0],0.0,0.3,dict(cam='K',a_st=round(_lw+0.2,3),a_v=T[_kw-1][3],b_st=round(_fw-0.4,3),b_v=T[_kw+1][3]))
print('whip: hook last word ends',round(_lw,2),'story first word',round(_fw,2))
segs=[dict(name=n,st=s,en=e,v=v) for n,s,e,v in T]
_h1=[k for k,s in enumerate(segs) if s['name'].startswith('H1')][-1]; _h2=[k for k,s in enumerate(segs) if s['name'].startswith('H2')][0]
# frame-exact: carry rounding so total stays in sync with audio
acc=0.0; f=0; off=[]
for s in segs:
    acc+=s['en']-s['st']; nf=round(acc*FPS)-f; s['nf']=nf; off.append(f); f+=nf
END0=f; ENDF=78; TOTALF=END0+ENDF
segs[_h1]['v']=dict(segs[_h1]['v'],post=f",fade=t=out:start_frame={segs[_h1]['nf']-4}:nb_frames=4")
segs[_h2]['v']=dict(segs[_h2]['v'],post=",scale=w='1080*(1+0.10*max(0\\,1-t/0.35))':h=-2:eval=frame,crop=1080:1920,fade=t=in:start_frame=0:nb_frames=3")

TMF=("zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,"
     "tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,eq=brightness=0.015,unsharp=3:3:0.35")
def crop(cx,top,H,headpos,aspect=9/16):
    W=int(H*aspect)//2*2; H=H//2*2
    x0=int(min(max(cx-W/2,0),2160-W)); y0=int(min(max(top-headpos*H,0),3840-H))
    return f"crop={W}:{H}:{x0}:{y0}"
def graph(v):
    if v['cam']=='J':
        H=int(v['H'])
        return f"[0:v]setpts=PTS-STARTPTS,fps=30,{crop(v['cx'],v['top'],H,v.get('hp',0.27))},scale=1080:1920:flags=lanczos,{TMF}{v.get('post','')}[v]"
    if v['cam']=='G':
        return f"[1:v]setpts=PTS-STARTPTS,fps=30,{crop(v['x']-110,v['top'],1900,0.22)},scale=1080:1920:flags=lanczos,{TMF}[v]"
    gc=crop(v['gx']-60,v['gtop'],1000,0.12,1080/960); jc=crop(v['jx']+150,v['jtop'],1000,0.12,1080/960)
    return (f"[1:v]setpts=PTS-STARTPTS,fps=30,{gc},scale=1080:960:flags=lanczos,{TMF}[g];"
            f"[0:v]setpts=PTS-STARTPTS,fps=30,{jc},scale=1080:960:flags=lanczos,{TMF}[c];"
            f"[g][c]vstack,drawbox=x=0:y=957:w=1080:h=6:color=0x15273f:t=fill[v]")
ENC=['-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-r','30']

# ---------- end card (OF4S v3: navy gradient, mark, navy-300 rule, Geist URL) ----------
FS=S+'/fonts/fontsource-schibsted-grotesk-5.3.0/files/schibsted-grotesk-latin-%d-normal.woff'
FG=S+'/fonts/fontsource-geist-sans-5.3.0/files/geist-sans-latin-%d-normal.woff'
PAPER=(250,248,244); N300=(143,169,199); N800=(21,39,63); N900=(15,29,51)
def endcard():
    W,H=1080,1920; y=np.linspace(0,1,H)[:,None,None]
    bg=(np.array(N900)*(1-y)+np.array(N800)*y)*np.ones((1,W,1)); base=Image.fromarray(bg.astype(np.uint8))
    fM=ImageFont.truetype(FS%700,250); fU=ImageFont.truetype(FG%400,46)
    frames=[]
    for i in range(ENDF):
        t=i/FPS; a=min(1,max(0,(t-0.10)/0.45)); e=1-(1-a)**3; dy=int(40*(1-e))
        im=base.copy(); lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
        parts=[('OF',PAPER),('4',N300),('S',PAPER)]; ws=[d.textlength(p,font=fM) for p,_ in parts]; tw=sum(ws)-2*0.03*250
        x=(W-tw)/2; y0=760+dy
        for (p,c),w in zip(parts,ws): d.text((x,y0),p,font=fM,fill=c+(int(255*e),)); x+=w-0.03*250
        rw=int(300*min(1,max(0,(t-0.35)/0.4))); d.rectangle([(W-rw)//2,1080+dy,(W+rw)//2,1083+dy],fill=N300+(int(255*e),))
        a2=min(1,max(0,(t-0.55)/0.4)); u='officefurniture4sale.com'; uw=d.textlength(u,font=fU)
        d.text(((W-uw)/2,1120+dy),u,font=fU,fill=PAPER+(int(230*a2),))
        frames.append(Image.alpha_composite(im.convert('RGBA'),lay).convert('RGB'))
    return frames

if STEP in ('all','video'):
    parts=[]
    for k,s in enumerate(segs):
        p=f"{R}/v{k:02d}.mp4"
        if s['v']['cam']=='K':   # 0.3 s whip: hook shot slides out left, story shot slides in, horizontal motion blur
            v=s['v']; n=s['nf']; pa=f"{R}/wa.mp4"; pb=f"{R}/wb.mp4"
            for st_,vv,pp in [(v['a_st'],v['a_v'],pa),(v['b_st'],v['b_v'],pb)]:
                run(['ffmpeg','-v','error','-y','-ss',f"{st_+O:.4f}",'-t','1','-i',CLIENT,'-ss',f"{st_:.4f}",'-t','1','-i',GEORGE,
                     '-filter_complex',graph({**vv,'post':''}),'-map','[v]','-frames:v',str(n),'-an']+ENC+[pp])
            run(['ffmpeg','-v','error','-y','-i',pa,'-i',pb,'-filter_complex',
                 f"[0:v]format=gbrp[a];[1:v]format=gbrp[b];[a][b]xfade=transition=slideleft:duration={n/FPS-1/FPS:.4f}:offset=0,gblur=sigma=22:sigmaV=0.01,format=yuv420p,fps=30[v]",'-map','[v]','-frames:v',str(n)]+ENC+[p])
        elif not(os.path.exists(p) and nfr(p)==s['nf']):
            d=s['nf']/FPS+0.5
            run(['ffmpeg','-v','error','-y','-ss',f"{s['st']+O:.4f}",'-t',f"{d:.3f}",'-i',CLIENT,'-ss',f"{s['st']:.4f}",'-t',f"{d:.3f}",'-i',GEORGE,
                 '-filter_complex',graph(s['v']),'-map','[v]','-frames:v',str(s['nf']),'-an']+ENC+[p])
            assert nfr(p)==s['nf'],p
        parts.append(p); print('seg',k,s['name'],s['nf'],flush=True)
    pe=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','30','-i','-']+ENC+[R+'/end.mp4'],stdin=subprocess.PIPE)
    pe.stdin.close(); pe.wait(); run(['cp',S+'/epgd/logoend.mp4',R+'/end.mp4'])   # EPGD logo end card, exact
    open(R+'/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts+[R+'/end.mp4']))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/list.txt','-c','copy',R+'/body.mp4'])
    assert nfr(R+'/body.mp4')==TOTALF; print('body frames',TOTALF,flush=True)

# ---------- captions ----------
t_of=lambda k,src: off[k]/FPS+(src-segs[k]['st'])
AW=[w for z in json.load(open(S+'/long/a1.json'))['segments'] for w in z['words']]
FIX={(507.95,509.83):[[508.00,508.42,'I'],[508.42,508.68,'am'],[508.68,508.86,'a'],[508.86,509.42,'service'],[509.42,509.82,'profession']]}
def words(st,en):
    ws=[[w[0],w[1],w[2].strip()] for w in AW if w[1]>st+0.02 and w[0]<en-0.06]
    for (a,b),rep in FIX.items():
        if st<b and en>a: ws=[w for w in ws if not(a<=w[0]<b)]+[r for r in rep if st-0.05<=r[0]<en]
    return sorted(ws)
# captions from the reel's own voice track (what you actually hear), mapped back to segments
_vt=R+'/voice_words.json'
_sig=json.dumps([(s['st'],s['en'],s['nf']) for s in segs])
if not (os.path.exists(_vt) and json.load(open(_vt)).get('sig')==_sig):
    _sr,_a=wavfile.read(S+'/long/a1_16k.wav'); _a=_a.astype(np.float32)/32768
    _y=np.zeros(int(END0/FPS*16000)+16000,np.float32)
    for k,s in enumerate(segs):
        if s['v']['cam']=='K': continue
        i0=int(s['st']*16000); n_=int(s['nf']/FPS*16000); _y[int(off[k]/FPS*16000):int(off[k]/FPS*16000)+n_]=_a[i0:i0+n_]
    from faster_whisper import WhisperModel
    _m=WhisperModel('large-v3',device='cpu',compute_type='int8')
    _sg,_=_m.transcribe(_y,beam_size=5,language='en',word_timestamps=True,condition_on_previous_text=False)
    json.dump({'sig':_sig,'w':[[w.start,w.end,w.word.strip()] for z in _sg for w in z.words]},open(_vt,'w'))
_VW=json.load(open(_vt))['w']
# transcription slips, corrected to what he actually says (checked against the full-interview transcript)
for i,(w0,w1,tx) in enumerate(_VW):
    nx=_VW[i+1][2] if i+1<len(_VW) else ''
    if tx.lower().strip(',.')=='program': _VW[i][2]='approached me and'
    if tx=='To' and nx.startswith('Michigan'): _VW[i][2]='Went to'
    if tx.strip(',.')=='school': _VW[i][2]='school.'
    if tx.strip(',.') in ('Equity','Partners'): _VW[i][2]=tx.lower()
    if tx.strip(',.')=='talent' and nx.startswith("That's"): _VW[i][2]='talent retention.'
for k,s in enumerate(segs):
    a_=off[k]/FPS; b_=a_+s['nf']/FPS
    if s['v']['cam']=='K': s['w']=[]; continue
    if k>0 and segs[k-1]['v']['cam']=='K': a_=off[k-1]/FPS          # words heard over the black beat belong to the next shot
    s['w']=[[s['st']+max(0,w0-off[k]/FPS),s['st']+(w1-off[k]/FPS),tx] for w0,w1,tx in _VW if a_<=(w0+w1)/2<b_]
_seen=set()
for s in []:
    s['w']=[] if s['v']['cam']=='K' else [w for w in words(s['st'],s['en']) if (round(w[0],3),w[2]) not in _seen]
    _seen|={(round(w[0],3),w[2]) for w in s['w']}
WHITE=(250,248,244); GOLD=(246,181,96); B=64; K=int(B*1.6)
_ix=lambda n:n
HLALL=[(['flipping','burgers'],'practicing law or','flipping burgers','tier'),(['some','shares'],'give you','some shares','tier'),
    (['have','to','leave'],'then I','have to leave','tier'),(['equity'],"I didn't have any",'equity','tier'),
    (['marry','them'],'I could','marry them','tier'),(['so','far','so','good'],'I think','so far so good','tier')]
DONE=set()
norm=lambda x:''.join(c for c in x.lower() if c.isalnum() or c=="'").strip("'")
groups=[]
for k,s in enumerate(segs):
    ws=[[max(t_of(k,w[0]),off[k]/FPS+0.02),t_of(k,w[1]),w[2]] for w in s['w']]
    toks=[norm(w[2]) for w in ws]; used=[False]*len(ws); hl=[]
    for hi,(m,sm,big,sty) in enumerate(HLALL):
        if hi in DONE: continue
        nsm=len(sm.split())
        for n in range(len(ws)):
            if toks[n:n+len(m)]==m and not any(used[max(0,n-nsm):n+len(m)]):
                a0=max(0,n-nsm)
                if [norm(x) for x in sm.split()]!=toks[a0:n]: continue
                for q in range(a0,n+len(m)): used[q]=True
                hl.append((a0,n+len(m),sm,big,sty)); DONE.add(hi); break
    def plain_run(rn):
        ch=[]; cur=[]
        for w in rn:
            if cur and (w[0]-cur[-1][1]>0.5 or cur[-1][2][-1] in ',.?!' or len(cur)>=3): ch.append(cur); cur=[]
            cur.append(w)
        if cur: ch.append(cur)
        i=0
        while i<len(ch):
            if len(ch)>1 and len(ch[i])==1:
                if i+1<len(ch) and len(ch[i+1])<=3 and ch[i][0][2][-1] not in '.?!': ch[i]=ch[i]+ch.pop(i+1); continue
                if i>0 and len(ch[i-1])<=3: ch[i-1]=ch[i-1]+ch.pop(i); continue
            i+=1
        for c in ch:
            txt=' '.join(w[2] for w in c).strip(' ,.?')
            groups.append(dict(t0=c[0][0],t1=c[-1][1],kind='plain',text=txt,seg=k,cam=s['v']['cam'],endp=c[-1][2][-1] in '.?!'))
    n=0; wr=[]
    while n<len(ws):
        h=[x for x in hl if x[0]==n]
        if h:
            if wr: plain_run(wr); wr=[]
            a,b,sm,big,sty=h[0]; tb=ws[b-len(big.split())][0]
            groups.append(dict(t0=ws[a][0],tbig=tb,t1=ws[b-1][1],kind=sty if sm else 'big',small=sm,big=big,seg=k,cam=s['v']['cam'],endp=ws[b-1][2][-1] in '.?!')); n=b; continue
        wr.append(ws[n]); n+=1
    if wr: plain_run(wr)
groups.sort(key=lambda g:g['t0'])
i=0
while i+1<len(groups):
    g,nx=groups[i],groups[i+1]
    if g['kind']=='plain' and len(g['text'].split())==1 and nx['kind']=='plain' and nx['t0']-g['t1']<0.8 and len((g['text']+' '+nx['text']).split())<=4:
        nx['text']=g['text']+' '+nx['text']; nx['t0']=g['t0']; groups.pop(i); continue
    i+=1
for i,g in enumerate(groups):
    if i+1<len(groups) and groups[i+1]['t0']<=g['t0']+0.25: groups[i+1]['t0']=g['t0']+0.25
for i,g in enumerate(groups):
    segend=(off[g['seg']]+segs[g['seg']]['nf'])/FPS
    e=min(max(g['t1'],g['t0']+0.3)+0.45,segend if g['seg']+1<len(segs) and segs[g['seg']+1]['st']-segs[g['seg']]['en']>0.05 else 1e9)
    if i+1<len(groups): e=min(e,groups[i+1]['t0'])
    g['t1']=min(e,END0/FPS)
# keyword pops snapped to real voice onset, one frame early
sr_,av=wavfile.read(S+'/long/a1.wav'); av=av.astype(np.float32)
if av.ndim>1: av=av.mean(1)
def onset(src):
    sg=av[int((src-0.35)*sr_):int((src+0.15)*sr_)]; n=int(0.01*sr_)
    L=np.array([20*np.log10(np.sqrt(np.mean(sg[q:q+n]**2))+1e-9) for q in range(0,len(sg)-n,n)])
    pk=L[25:].max(); base=np.percentile(L[:20],20); q=35
    while q>0 and L[q-1]>base+0.5*(pk-base): q-=1
    return src-0.35+q*0.01
for g in groups:
    if g['kind']!='plain':
        k=g['seg']; tb=g['tbig']; src=segs[k]['st']+(tb-off[k]/FPS)
        g['tbig']=max(off[k]/FPS,g['t0'],t_of(k,onset(src))-1/FPS)
prev=True
for g in groups:
    if g['kind']=='plain' and g['text']: g['text']=(g['text'][0].upper()+g['text'][1:]) if prev else g['text']
    elif g.get('small') and prev: g['small']=g['small'][0].upper()+g['small'][1:]
    prev=g['endp']
for k,s in enumerate(segs):
    if s['v']['cam']=='K':
        b0=off[k]/FPS; b1=b0+s['nf']/FPS
        for g in groups:
            if g['t0']<b0<g['t1']: g['t1']=b0
        groups=[g for g in groups if not(b0<=g['t0']<b1)]
json.dump(groups,open(R+'/caps.json','w'),indent=0)

fonts={}
def F(wt,sz):
    if (wt,sz) not in fonts: fonts[(wt,sz)]=ImageFont.truetype(FS%wt,sz)
    return fonts[(wt,sz)]
def layout_lines(g,show_big):
    if g['kind']=='plain': return [[(g['text'],B,700,WHITE)]]
    if g['kind']=='big': return [[(g['big'],K,700,GOLD)]]
    return [[(g['small'],B,700,WHITE)]]+([[(g['big'],K,700,GOLD)]] if show_big else [])
_c={}
def cap_img(g,sc,show_big):
    key=(id(g),round(sc,3),show_big)
    if key in _c: return _c[key]
    W,H=1080,1920; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); rows=[]
    full=layout_lines(g,True)
    for parts in layout_lines(g,show_big):
        parts=[(t,int(sz*sc) if c==GOLD else sz,wt,c) for t,sz,wt,c in parts]
        ws_=[d.textlength(t,font=F(wt,sz)) for t,sz,wt,c in parts]; tw=sum(ws_)
        if tw>W*0.70:
            q=W*0.70/tw; parts=[(t,int(sz*q),wt,c) for t,sz,wt,c in parts]; ws_=[d.textlength(t,font=F(wt,sz)) for t,sz,wt,c in parts]; tw=sum(ws_)
        rows.append((parts,ws_,tw,max(p[1] for p in parts)))
    bh=sum(max(p[1] for p in r)*1.02 for r in full)          # reserve the full block so the small line doesn't jump
    top=960-bh/2-12 if g['cam']=='S' else min(H*0.62-bh/2,H*0.70-bh)
    y=top; items=[]
    for parts,ws_,tw,lh in rows:
        x=(W-tw)/2
        for (t,sz,wt,c),w in zip(parts,ws_): items.append((x,y+(lh-sz)*0.78,t,F(wt,sz),c)); x+=w
        y+=lh*1.02
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for x,yy,t,f,c in items: ds.text((x,yy+5),t,font=f,fill=(0,0,0,170))
    sh=sh.filter(ImageFilter.GaussianBlur(9))
    for x,yy,t,f,c in items: d.text((x,yy),t,font=f,fill=c+(255,))
    im=Image.alpha_composite(sh,lay); _c[key]=im; return im

if STEP in ('all','compose'):
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-i',R+'/body.mp4','-f','rawvideo','-pix_fmt','rgba','-s','1080x1920','-r','30','-i','-',
        '-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-frames:v',str(TOTALF),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r','30',R+'/picture.mp4'],stdin=subprocess.PIPE)
    blank=bytes(1080*1920*4)
    for fi in range(TOTALF):
        t=fi/FPS; g=next((g for g in groups if g['t0']<=t<g['t1']),None)
        if g is None: p.stdin.write(blank); continue
        tb=g.get('tbig',g['t0']); sb=t>=tb; age=t-tb
        sc=1.0+0.12*max(0,1-age/0.10) if g['kind']!='plain' and sb else 1.0
        p.stdin.write(cap_img(g,sc,sb).tobytes())
    p.stdin.close(); p.wait(); assert p.returncode==0
    assert nfr(R+'/picture.mp4')==TOTALF; print('picture ok',flush=True)

# ---------- audio ----------
def lufs(x):
    wavfile.write(R+'/_m.wav',SR,x.astype(np.float32))
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',R+'/_m.wav','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
def load(path,ss=0,dur=None):
    c=['ffmpeg','-v','error','-ss',str(ss),'-i',path]+(['-t',str(dur)] if dur else [])+['-ac','2','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
if STEP in ('all','audio'):
    a1=load(S+'/long/'+os.environ.get('VOICE','a1_dc.wav')); N=TOTALF*SPF; voice=np.zeros((N,2),np.float32)   # declipped master voice; voice=np.zeros((N,2),np.float32)
    BOOST=[]          # 'support' is spoken ~15 dB softer than the words around it
    for b0,b1,db in BOOST:
        i0,i1=int(b0*SR),int(b1*SR); r=int(0.03*SR); g_=np.ones(i1-i0)*10**(db/20)
        g_[:r]=np.linspace(1,g_[r],r); g_[-r:]=np.linspace(g_[-r-1],1,r); a1[i0:i1]*=g_[:,None]
    for k,s in enumerate(segs):
        if s['v']['cam']=='K': continue
        n=s['nf']*SPF
        prev_c=k>0 and abs(segs[k-1]['en']-s['st'])<1e-3; next_c=k+1<len(segs) and abs(segs[k+1]['st']-s['en'])<1e-3
        r=int(0.012*SR); XF=int(0.02*SR)
        # pause cuts: 40 ms equal-power crossfade between the two takes (no dip to silence); next to the whip / reel edges: short fade
        pa=XF if (k>0 and not prev_c and segs[k-1]['v']['cam']!='K') else 0
        pb=XF if (k+1<len(segs) and not next_c and segs[k+1]['v']['cam']!='K') else 0
        i0=int(round(s['st']*SR))-pa; x=a1[i0:i0+n+pa+pb].copy()
        if pa: x[:2*pa]*=np.sin(np.linspace(0,np.pi/2,2*pa))[:,None]
        elif not prev_c: x[:r]*=np.linspace(0,1,r)[:,None]
        if pb: x[-2*pb:]*=np.cos(np.linspace(0,np.pi/2,2*pb))[:,None]
        elif not next_c: x[-r:]*=np.linspace(1,0,r)[:,None]
        if 'mute_after' in s['v']:
            q=int((s['v']['mute_after']-s['st'])*SR)+pa; x[q:q+r]*=np.linspace(1,0,r)[:,None]; x[q+r:]=0
        voice[off[k]*SPF-pa:off[k]*SPF-pa+len(x)]+=x[:max(0,len(voice)-(off[k]*SPF-pa))]
    mix=np.zeros_like(voice)
    def fade(x,fi=0,fo=0):
        x=x.copy(); n=len(x)
        if fi: q=int(fi*SR); x[:q]*=np.linspace(0,1,q)[:,None]
        if fo: q=int(fo*SR); x[n-q:]*=np.linspace(1,0,q)[:,None]
        return x
    def put(x,t,gdb):
        i=int(round(t*SR)); x=x[:max(0,N-i)]; mix[i:i+len(x)]+=x*10**(gdb/20)
    vpk=np.percentile(np.abs(voice[:END0*SPF]),99.9); G=lambda x,r:20*np.log10(r*vpk/(np.abs(x).max()+1e-9))
    rng=np.random.default_rng(3)
    # soft click (synthesised, no licence needed): 18 ms band-limited tick
    from scipy.signal import butter,sosfilt
    ck=load(S+'/sfx/click.mp3')   # EPGD click
    for g in groups:
        if g['kind']!='plain': put(ck,g['tbig']-0.10,G(ck,0.30))
    # whoosh into the end card: noise with a rising band-pass sweep
    L=int(0.9*SR); nz=rng.standard_normal(L).astype(np.float32); out=np.zeros(L,np.float32); hop=1024
    for q in range(0,L,hop):
        fc=300+3500*(q/L)**1.5; sos=butter(2,[fc*0.6,fc*1.6],'bp',fs=SR,output='sos'); out[q:q+hop]=sosfilt(sos,nz[q:q+hop])
    wh=load(S+'/sfx/whoosh_ds.mp3')   # EPGD whoosh
    put(wh,END0/FPS-0.9,G(wh,0.22))
    MUS=os.environ.get('BED')
    if MUS:
        bed=load(MUS,float(os.environ.get('BEDSS','0')),TOTALF/FPS+1)[:N]
        VL=lufs(voice[:END0*SPF]); gb=VL-float(os.environ.get('BEDDB','14'))-lufs(bed[:20*SR])
        t_=np.arange(len(bed))/SR
        kb=[k for k,s in enumerate(segs) if s['v']['cam']=='K'][0]; tB=off[kb]/FPS; tBe=tB+segs[kb]['nf']/FPS
        DT=float(os.environ.get('DUCK_T','0')); DD=10**(-float(os.environ.get('DUCK_DB','0'))/20)   # music lower once George's question ends (Joanne)
        if DT>0: e=np.interp(t_,[0,0.3,tB+0.15,tBe+0.4,DT,DT+0.5,TOTALF/FPS-1.2,TOTALF/FPS],[0,1,10**(2/20),1,1,DD,DD,0])
        else: e=np.interp(t_,[0,0.3,tB+0.15,tBe+0.4,TOTALF/FPS-1.2,TOTALF/FPS],[0,1,10**(2/20),1,1,0])
        put(bed*e[:,None],0,gb)
        L=int(1.6*SR); nz=rng.standard_normal(L).astype(np.float32); out=np.zeros(L,np.float32)
        for q in range(0,L,1024):
            fc=200+5000*(q/L)**2; out[q:q+1024]=sosfilt(butter(2,[fc*0.6,fc*1.5],'bp',fs=SR,output='sos'),nz[q:q+1024])
        sw5=load(S+'/sfx/swoosh05.mp3'); put(fade(sw5[:int(0.45*SR)],0.01,0.12),tB-0.08,G(sw5,0.12))   # soft swoosh only (Joanne disliked the whoosh+hit), ends before the next word
        tH2=next(off[k]/FPS for k,s in enumerate(segs) if s['name'].startswith('H2')); Lw=int(0.8*SR); nz2=rng.standard_normal((Lw,2)).astype(np.float32); o2=np.zeros_like(nz2)
        for q in range(0,Lw,512):
            fc=250+3800*np.sin(np.pi*q/Lw)**1.5; sos=butter(2,[fc*0.55,fc*1.7],'bp',fs=SR,output='sos'); o2[q:q+512]=sosfilt(sos,nz2[q:q+512],axis=0)
        envw=(np.sin(np.linspace(0,np.pi,Lw))**3)[:,None]; pan=np.stack([np.linspace(1,0.4,Lw),np.linspace(0.4,1,Lw)],1); w2=o2*envw*pan
        put(wh,tH2-0.45,G(wh,0.22))
        print('black beat at',round(tB,2),'hook whoosh at',round(tH2,2))
    y=voice+mix; I=lufs(y); y*=10**((-14-I)/20); print('mix LUFS',I,flush=True)
    wavfile.write(R+'/mix.wav',SR,y.astype(np.float32))
    run(['ffmpeg','-v','error','-y','-i',R+'/mix.wav','-af','alimiter=limit=0.72:attack=1:release=60:level=false','-c:a','pcm_s16le',R+'/mix_final.wav'])
    assert len(y)==N

if STEP in ('all','mux'):
    out=S+'/deliverables/'+OUT; os.makedirs(os.path.dirname(out),exist_ok=True)
    run(['ffmpeg','-v','error','-y','-i',R+'/picture.mp4','-i',R+'/mix_final.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
         '-bsf:v','h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1','-movflags','+faststart',out])
    print('OUT',out)
print('TOTAL %.2f s (%d frames), end card at %.2f'%(TOTALF/FPS,TOTALF,END0/FPS))
