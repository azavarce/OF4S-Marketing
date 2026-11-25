# Martínez-Cid Law × OF4S — YouTube full episode v2 (16:9). v1 builder: yt/yt_build.py (kept).
import json, os, sys, subprocess, numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
Y=S+'/yt2'; R=Y+'/build'; os.makedirs(R,exist_ok=True)
FPS=30; SR=48000; SPF=SR//FPS; O=4.871
CL=S+'/src/Client.MOV'; GE=S+'/src/George.MOV'
STEP=sys.argv[1] if len(sys.argv)>1 else 'all'
def run(c): subprocess.run(c,check=True)
def nfr(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]).strip())
ENC=['-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r','30']
TMF="zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,eq=brightness=0.015"
sr_,A=wavfile.read(S+'/long/a1.wav'); A=A.astype(np.float32)/32768
if A.ndim>1: A=A.mean(1)
_n=int(.01*sr_); LV=lambda t: 20*np.log10(np.sqrt(np.mean(A[int(t*sr_):int(t*sr_)+_n]**2))+1e-9)
def snap(t,lo,hi):
    ts=np.arange(t+lo,t+hi,0.01); return float(ts[np.argmin([LV(x) for x in ts])])
def tighten(s,e,minp,keep):
    lv=np.array([LV(t) for t in np.arange(s,e,0.01)]); q=lv<-40; out=[]; i=0
    while i<len(q):
        if q[i]:
            j=i
            while j<len(q) and q[j]: j+=1
            if (j-i)*0.01>minp and i>0 and j<len(q): out.append((s+i*0.01+keep/2,s+j*0.01-keep/2))
            i=j
        else: i+=1
    pts=[s]+[x for c in out for x in c]+[e]; return [(pts[k],pts[k+1]) for k in range(0,len(pts),2)]

# ---------- framing (16:9) ----------
_GH=json.load(open(Y+'/ghead.json'))            # George head track from his camera: [t, head_x, head_top] (2160x3840 frame)
_gt=np.array([r[0] for r in _GH]); _gxs=np.array([r[1] for r in _GH]); _gys=np.array([r[2] for r in _GH])
def _gx(t): return float(np.interp(t,_gt,_gxs))
def _gtop(t): return float(np.interp(t,_gt,_gys))
_HOLD={}
def gx(t): return _HOLD.get(round(t,3),(_gx(t),_gtop(t)))[0]
def gtop(t): return _HOLD.get(round(t,3),(_gx(t),_gtop(t)))[1]
JX=756; JT=1544   # Jordi head (measured on his camera)
def crop(cx,top,W,H,hp):
    W=int(W)//2*2; H=int(H)//2*2; x0=int(min(max(cx-W/2,0),2160-W)); y0=int(min(max(top-hp*H,0),3840-H)); return f"crop={W}:{H}:{x0}:{y0}"
def graph(lay,t,z=1.0):
    # z>1: slightly tighter punch-in, used to hide jump cuts where a filler/stutter was removed
    if lay=='J': return f"[0:v]setpts=PTS-STARTPTS,fps=30,{crop(JX+200,JT,1920/z,1080/z,0.15)},scale=1920:1080:flags=lanczos,{TMF}[v]"
    if lay=='G': return f"[1:v]setpts=PTS-STARTPTS,fps=30,{crop(gx(t)-30,gtop(t),1920/z,1080/z,0.15)},scale=1920:1080:flags=lanczos,{TMF}[v]"
    return (f"[0:v]setpts=PTS-STARTPTS,fps=30,{crop(JX+150,JT,1280/z,1440/z,0.13)},scale=960:1080:flags=lanczos,{TMF}[j];"
            f"[1:v]setpts=PTS-STARTPTS,fps=30,{crop(gx(t)-40,gtop(t),1280/z,1440/z,0.13)},scale=960:1080:flags=lanczos,{TMF}[g];"
            "[j][g]hstack,drawbox=x=957:y=0:w=6:h=1080:color=0x15273f:t=fill[v]")
def piece(name,st,en,lay,z=1.0):
    nf=round((en-st)*FPS); p=f"{R}/{name}.mp4"
    if os.path.exists(p) and nfr(p)==nf: return p,nf
    d=nf/FPS+0.4
    run(['ffmpeg','-v','error','-y','-ss',f"{st+O:.4f}",'-t',f"{d:.3f}",'-i',CL,'-ss',f"{st:.4f}",'-t',f"{d:.3f}",'-i',GE,
         '-filter_complex',graph(lay,st,z),'-map','[v]','-frames:v',str(nf),'-an']+ENC+[p])
    assert nfr(p)==nf,p
    return p,nf

# ---------- 1) cold open ----------
CO=json.load(open(Y+'/co.json'))   # [name, start, end, layout] in master time, checked cut by cut
COS=[]; CO_MUTE=[]
for c in CO:
    nm,s,e,lay=c[:4]
    if len(c)==6:   # breathing room: picture runs s..e, voice only inside c[4]..c[5] (a short pause before and after the line)
        COS.append((f"{nm}_0",s,e,lay,nm)); CO_MUTE+=[(s-0.05,c[4]),(c[5],e+0.05)]; continue
    for k,(a,b) in enumerate(tighten(s,e,0.30,0.14)): COS.append((f"{nm}_{k}",a,b,lay,nm))
# ---------- 2) body: whole conversation minus the confidential-cases section, fillers/stutters cut ----------
KEEP=[(6.40,965.70),(1056.20,1212.20)]            # starts on "Hi, Jordi" (not "All right. So, yeah, okay.")
CUTS=json.load(open(Y+'/cuts.json'))              # [start,end] spans removed: um/uh, stutters, false starts (energy-checked)
SPK=json.load(open(Y+'/speaker.json'))            # per 0.1 s: 'G' George talking, 'J' Jordi talking, '-' silence (smoothed)
LOOKDOWN=[(95.0,106.0),(1058.0,1062.5)]           # George glancing down at notes
def spk(t): i=int(round(t*10)); return SPK[i] if 0<=i<len(SPK) else '-'
_RL=[0]*len(SPK); _s0=0
for _k in range(1,len(SPK)+1):
    if _k==len(SPK) or SPK[_k]!=SPK[_s0]:
        for _q in range(_s0,_k): _RL[_q]=(_k-_s0)/10
        _s0=_k
def runlen(t): i=int(round(t*10)); return _RL[i] if 0<=i<len(_RL) else 0
def lay_at(t,run_start):
    sp=spk(t)
    if t<KEEP[0][0]+7.0: return 'S'                                   # opening showcase: side by side with name tags
    if runlen(t)<2.0: return 'S'                                       # short interjections / doubtful spots: show both
    if sp=='G' : return 'G'
    if sp=='J' and any(a<=t<b for a,b in LOOKDOWN): return 'J'
    if sp=='J':
        k=t-run_start
        return 'S' if k>=12 and ((k-12)%20)<4 else 'J'                # long answers: a 4 s two-shot every ~20 s
    return 'S'
def segs_of(a,b):
    out=[]; cur=a
    for c0,c1 in sorted(CUTS):
        if c1<=a or c0>=b: continue
        out.append((cur,max(cur,c0))); cur=c1
    out.append((cur,b)); return [(x,y) for x,y in out if y-x>0.05]
BODY=[]; prev_end=None; prev_lay=None; z=1.0
for a,b in KEEP:
    for s0,e0 in segs_of(a,b):
        for s,e in tighten(s0,e0,0.45,0.25):
            # layout by speaker, re-evaluated every 0.1 s; a layout must hold >= 1.2 s
            t=s; st=s; cur=None; rs=s
            while t<e-1e-6:
                sp=spk(t)
                if cur is None: cur=lay_at(t,rs)
                l=lay_at(t,rs)
                if spk(t)!=spk(t-0.1): rs=t
                if l!=cur and e-t>=0.4 and (t-st>=1.2 or runlen(t)>=2.0):
                    if t-st<0.4: cur=l                                # speaker changes right at the piece start: just relabel
                    else: BODY.append([st,t,cur]); st=t; cur=l
                t+=0.1
            BODY.append([st,e,cur])
# jump cuts (same layout on both sides of a removed span): alternate a slight punch-in so the cut reads as intentional
for i,x in enumerate(BODY):
    jump=i>0 and abs(BODY[i-1][1]-x[0])>0.05 and BODY[i-1][2]==x[2]
    x.append(1.0)                                                       # no zoom steps at pause/filler cuts: same framing both sides
BODY=[tuple(x) for x in BODY if x[1]-x[0]>0.05]
# hold George's framing across consecutive George/two-shot pieces (median over the run), so pause cuts never shift the frame
_i=0
while _i<len(BODY):
    _j=_i
    while _j+1<len(BODY) and BODY[_j+1][2]==BODY[_i][2]: _j+=1
    if BODY[_i][2] in ('G','S'):
        _ts=np.arange(BODY[_i][0],BODY[_j][1],0.5)
        _v=(float(np.median([_gx(t) for t in _ts])),float(np.median([_gtop(t) for t in _ts])))
        for _k in range(_i,_j+1): _HOLD[round(BODY[_k][0],3)]=_v
    _i=_j+1
print('cold open pieces',len(COS),'body pieces',len(BODY),flush=True)

if STEP in ('all','video'):
    parts=[]
    for nm,s,e,lay,_ in COS: parts.append(piece('co_'+nm,s,e,lay))
    for i,(s,e,l,zz) in enumerate(BODY):
        parts.append(piece(f"b{i:04d}",s,e,l,zz))
        if i%25==0: print('body',i,'/',len(BODY),flush=True)
    json.dump([[p,n] for p,n in parts],open(R+'/parts.json','w'))

# ---------- timeline ----------
parts=json.load(open(R+'/parts.json')) if os.path.exists(R+'/parts.json') else None
nCO=len(COS); coF=[round((b-a)*FPS) for _,a,b,_,_ in COS]; CO_F=sum(coF)
TITLEF=90; END_F=600; SHOWF=270
bodyF=[round((e-s)*FPS) for s,e,_,_ in BODY]; BODY_F=sum(bodyF)
T0_TITLE=CO_F; T0_BODY=CO_F+TITLEF; T0_END=T0_BODY+BODY_F; TOTALF=T0_END+END_F
print('cold open %.1fs  body %.1fs  total %.1fs'%(CO_F/FPS,BODY_F/FPS,TOTALF/FPS),flush=True)

# ---------- fonts / colours ----------
FS=S+'/fonts/fontsource-schibsted-grotesk-5.3.0/files/schibsted-grotesk-latin-%d-normal.woff'
FG=S+'/fonts/fontsource-geist-sans-5.3.0/files/geist-sans-latin-%d-normal.woff'
fonts={}
def F(path,wt,sz):
    k=(path,wt,sz)
    if k not in fonts: fonts[k]=ImageFont.truetype(path%wt,sz)
    return fonts[k]
PAPER=(250,248,244); N300=(143,169,199); N700=(30,53,84); N800=(21,39,63); N900=(15,29,51); WHITE=(250,248,244); GOLD=(246,181,96)
def ease(x): x=min(1,max(0,x)); return 1-(1-x)**3

# ---------- cold-open captions (reel style, 16:9) ----------
from faster_whisper import WhisperModel
def co_words():
    p=R+'/co_words.json'
    if os.path.exists(p): return json.load(open(p))
    sr16,a16=wavfile.read(S+'/long/a1_16k.wav'); a16=a16.astype(np.float32)/32768
    y=np.concatenate([a16[int(a*16000):int(a*16000)+round((b-a)*FPS)*16000//FPS] for _,a,b,_,_ in COS])
    m=WhisperModel('large-v3',device='cpu',compute_type='int8')
    sg,_=m.transcribe(y,beam_size=5,language='en',word_timestamps=True,condition_on_previous_text=False)
    W=[[w.start,w.end,w.word.strip()] for z in sg for w in z.words]
    for w in W:   # transcription slips -> his actual words
        w[2]=w[2].replace('Equity','equity').replace('Partners','partners')
        if w[2].lower()=='program': w[2]='approached me and'
        if w[2]=='100': w[2]='hundred'
        if w[2].startswith('-page'): w[2]='page'
    if W and W[0][2]=='And': W=W[1:]
    for w in W: w[2]=w[2].replace('niches','niche')
    json.dump(W,open(p,'w')); return W
GOLDW={'true','soul','trust','later','for','filing','charge','leave'}   # last word of each line's key phrase
HLP=[("the weird",),("not quite true",),("own your soul",),("don't fully trust",),("a lot more later",),("the answer that you're looking for",),("hundred page filing",),("surgical",),("then I have to leave",)]
def co_groups():
    W=co_words(); norm=lambda x:''.join(c for c in x.lower() if c.isalnum() or c=="'")
    toks=[norm(w[2]) for w in W]; gold=set()
    for (ph,) in HLP:
        m=[norm(x) for x in ph.split()]
        for n in range(len(W)):
            if toks[n:n+len(m)]==m: gold|=set(range(n,n+len(m))); break
    G=[]; cur=[]
    def flush():
        if cur: G.append(dict(t0=W[cur[0]][0],t1=W[cur[-1]][1],ws=list(cur)))
    for i,w in enumerate(W):
        brk=cur and (w[0]-W[cur[-1]][1]>0.45 or W[cur[-1]][2][-1] in ',.?!' or len(cur)>=3 or ((i in gold)!=(cur[-1] in gold)))
        if brk: flush(); cur=[]
        cur.append(i)
    flush()
    for k,g in enumerate(G):
        g['gold']=all(i in gold for i in g['ws']); g['text']=' '.join(W[i][2] for i in g['ws']).strip(' ,')
        nxt=G[k+1]['t0'] if k+1<len(G) else 1e9; g['t1']=min(g['t1']+0.35,nxt)
    if G: G[0]['text']=G[0]['text'][0].upper()+G[0]['text'][1:]
    return G
def cap16(g,sc=1.0):
    W,H=1920,1080; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    sz=int((88 if g['gold'] else 60)*sc); f=F(FS,700,sz); txt=g['text']
    tw=d.textlength(txt,font=f)
    if tw>W*0.6: f=F(FS,700,int(sz*W*0.6/tw)); tw=d.textlength(txt,font=f)
    x=(W-tw)/2; y=H*0.80-f.size/2
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).text((x,y+5),txt,font=f,fill=(0,0,0,170)); sh=sh.filter(ImageFilter.GaussianBlur(9))
    d.text((x,y),txt,font=f,fill=(GOLD if g['gold'] else WHITE)+(255,)); return Image.alpha_composite(sh,lay)

# ---------- title card ----------
TITLE1='Talent, AI & Building a Law Firm:'; TITLE2='Advice for Miami Business Owners'
SUB='with Jordi Martínez-Cid, Partner, Martínez-Cid Law'
def title_frame():
    W,H=1920,1080; y=np.linspace(0,1,H)[:,None,None]; bg=(np.array(N900)*(1-y)+np.array(N800)*y)*np.ones((1,W,1))
    im=Image.fromarray(bg.astype(np.uint8)).convert('RGBA'); d=ImageDraw.Draw(im)
    f1=F(FS,700,62); f2=F(FG,400,26); fm=F(FS,700,58)
    for k,l in enumerate([TITLE1,TITLE2]):
        tw=d.textlength(l,font=f1); d.text(((W-tw)/2,330+k*78),l,font=f1,fill=WHITE)
    d.rectangle([W/2-60,520,W/2+60,523],fill=N300)
    tw=d.textlength(SUB,font=f2); d.text(((W-tw)/2,548),SUB,font=f2,fill=(200,210,224))
    parts_=[('OF',WHITE),('4',N300),('S',WHITE)]; ws=[d.textlength(p,font=fm) for p,_ in parts_]; x=(W-sum(ws)+2*0.03*58)/2
    for (p,c),w in zip(parts_,ws): d.text((x,690),p,font=fm,fill=c); x+=w-0.03*58
    return im.convert('RGB')

# ---------- showcase overlay: name tags + IN THIS EPISODE ----------
TOPICS=['Starting his own firm','Hiring the right people','AI and the courts']
def showcase(t):
    W,H=1920,1080; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    out=1-ease((t-(SHOWF/FPS-0.35))/0.35) if t>SHOWF/FPS-0.35 else 1
    for k,(nm,ti,x0) in enumerate([('Jordi Martínez-Cid','Partner, Martínez-Cid Law',60),('George Dargham','CEO, OfficeFurniture4Sale',1020)]):
        a=ease((t-0.3-k*0.25)/0.35)*out
        if a<=0: continue
        fn=F(FS,700,52); ft=F(FG,400,30); w=max(660,max(d.textlength(nm,font=fn),d.textlength(ti,font=ft))+110); dx=int(-40*(1-a))   # bigger text, longer box (Joanne)
        y0=712; bh_=148; d.rectangle([x0+dx,y0,x0+dx+w,y0+bh_],fill=N800+(int(235*a),)); d.rectangle([x0+dx,y0,x0+dx+8,y0+bh_],fill=N300+(int(255*a),))
        d.text((x0+dx+40,y0+18),nm,font=fn,fill=WHITE+(int(255*a),)); d.text((x0+dx+40,y0+92),ti,font=ft,fill=(200,210,224,int(255*a)))
    a=ease((t-2.4)/0.35)*out
    if a>0:
        bw,bh=1100,96; bx=(W-bw)//2; by=900; d.rounded_rectangle([bx,by,bx+bw,by+bh],14,fill=N900+(int(230*a),))
        fe=F(FG,600,15); e='IN THIS EPISODE'; d.text(((W-d.textlength(e,font=fe))/2,by+12),e,font=fe,fill=N300+(int(255*a),))
        ft=F(FS,700,30); items=[]; 
        for k,tp in enumerate(TOPICS):
            ak=ease((t-2.8-k*0.35)/0.25)*out
            items.append((tp,ak))
        sep='  ×  '; full=sep.join(tp for tp,_ in items); x=(W-d.textlength(full,font=ft))/2
        for k,(tp,ak) in enumerate(items):
            if k: d.text((x,by+42),sep,font=ft,fill=N300+(int(255*ak),)); x+=d.textlength(sep,font=ft)
            d.text((x,by+42),tp,font=ft,fill=WHITE+(int(255*ak),)); x+=d.textlength(tp,font=ft)
    return lay

if STEP in ('all','compose'):
    assert parts
    # cold open picture with captions
    open(R+'/co_list.txt','w').write(''.join(f"file '{p}'\n" for p,n in parts[:nCO]))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/co_list.txt','-c','copy',R+'/co_raw.mp4'])
    G=co_groups(); blank=bytes(1920*1080*4)
    pp=subprocess.Popen(['ffmpeg','-v','error','-y','-i',R+'/co_raw.mp4','-f','rawvideo','-pix_fmt','rgba','-s','1920x1080','-r','30','-i','-','-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-frames:v',str(CO_F)]+ENC+[R+'/co.mp4'],stdin=subprocess.PIPE)
    for fi in range(CO_F):
        t=fi/FPS; g=next((g for g in G if g['t0']<=t<g['t1']),None)
        if g is None: pp.stdin.write(blank); continue
        sc=1+0.10*max(0,1-(t-g['t0'])/0.10) if g['gold'] else 1
        pp.stdin.write(cap16(g,sc).tobytes())
    pp.stdin.close(); pp.wait()
    # title
    tf=title_frame(); pp=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-frames:v',str(TITLEF)]+ENC+[R+'/title.mp4'],stdin=subprocess.PIPE)
    for fi in range(TITLEF): pp.stdin.write(tf.tobytes())
    pp.stdin.close(); pp.wait()
    # body (showcase overlay on its first SHOWF frames)
    if not os.path.exists(R+'/body.mp4'):
     open(R+'/b_list.txt','w').write(''.join(f"file '{p}'\n" for p,n in parts[nCO:]))
     run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/b_list.txt','-c','copy',R+'/body_raw.mp4'])
     for p_,n_ in parts[nCO:]: os.remove(p_)   # free disk: pieces are inside body_raw now
     pp=subprocess.Popen(['ffmpeg','-v','error','-y','-i',R+'/body_raw.mp4','-f','rawvideo','-pix_fmt','rgba','-s','1920x1080','-r','30','-i','-','-filter_complex','[1:v]setpts=PTS-STARTPTS[o];[0:v][o]overlay=0:0:eof_action=pass:format=auto[v]','-map','[v]','-frames:v',str(BODY_F)]+ENC+[R+'/body.mp4'],stdin=subprocess.PIPE)
     for fi in range(SHOWF): pp.stdin.write(showcase(fi/FPS).tobytes())
     pp.stdin.close(); pp.wait()
     os.remove(R+'/body_raw.mp4')
    # end screen: the EPGD "Thanks for watching" card
    run(['ffmpeg','-v','error','-y','-sseof','-20.0','-i',S+'/epgd/full.mp4','-vf','fps=30,scale=1920:1080,format=yuv420p','-frames:v',str(END_F),'-an']+ENC+[R+'/end.mp4'])
    open(R+'/all.txt','w').write(''.join(f"file '{R}/{n}.mp4'\n" for n in ['co','title','body','end']))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/all.txt','-c','copy',R+'/picture.mp4'])
    print('picture frames',nfr(R+'/picture.mp4'),'expected',TOTALF,flush=True)

def load(path,ss=0,dur=None):
    c=['ffmpeg','-v','error','-ss',str(ss),'-i',path]+(['-t',str(dur)] if dur else [])+['-ac','2','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
def lufs(x):
    wavfile.write(R+'/_m.wav',SR,x.astype(np.float32))
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',R+'/_m.wav','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
if STEP in ('all','audio'):
    N=TOTALF*SPF; voice=np.zeros((N,2),np.float32); a1=load(S+'/long/'+os.environ.get('VOICE','a1_dc.wav'))
    def lay_voice(segs,f0,mute=None):
        f=f0
        XF=int(0.02*SR); r=int(0.012*SR)
        for j,(s,e) in enumerate(segs):
            n=round((e-s)*FPS)*SPF
            prev_c=j>0 and abs(segs[j-1][1]-s)<1e-3; next_c=j+1<len(segs) and abs(segs[j+1][0]-e)<1e-3
            pa=XF if (j>0 and not prev_c) else 0; pb=XF if (j+1<len(segs) and not next_c) else 0
            i0=int(s*SR)-pa; x=a1[i0:i0+n+pa+pb].copy()
            if pa: x[:2*pa]*=np.sin(np.linspace(0,np.pi/2,2*pa))[:,None]
            elif not prev_c: x[:r]*=np.linspace(0,1,r)[:,None]
            if pb: x[-2*pb:]*=np.cos(np.linspace(0,np.pi/2,2*pb))[:,None]
            elif not next_c: x[-r:]*=np.linspace(1,0,r)[:,None]
            for m0,m1 in (mute or []):          # silence outside the line (15 ms ramps)
                q0=max(0,int((m0-(s-pa/SR))*SR)); q1=min(len(x),int((m1-(s-pa/SR))*SR)); rr=int(0.015*SR)
                if q1>q0:
                    x[q0:q1]=0
                    if q0>=rr and m0>s: x[q0-rr:q0]*=np.linspace(1,0,rr)[:,None]
                    if q1+rr<=len(x) and m1<e: x[q1:q1+rr]*=np.linspace(0,1,rr)[:,None]
            voice[f*SPF-pa:f*SPF-pa+len(x)]+=x; f+=round((e-s)*FPS)
    lay_voice([(a,b) for _,a,b,_,_ in COS],0,CO_MUTE); lay_voice([(s,e) for s,e,_,_ in BODY],T0_BODY)
    VL=lufs(voice[T0_BODY*SPF:(T0_BODY+60*FPS)*SPF]); mix=np.zeros_like(voice)
    def put(x,t,gdb):
        i=int(round(t*SR))
        if i<0: x=x[-i:]; i=0
        x=x[:max(0,N-i)]; mix[i:i+len(x)]+=x*10**(gdb/20)
    def env(x,pts):
        t_=np.arange(len(x))/SR; return x*np.interp(t_,[p for p,_ in pts],[10**(g/20) for _,g in pts])[:,None]
    # trailer: its final hit (29.5 s) lands on the title card; the mid hit (18.2 s) lands on a cold-open cut
    tr=load(S+'/music/trailer.mp3'); HIT=29.5; tstart=T0_TITLE/FPS-HIT
    g_tr=VL-12-lufs(tr[int(1*SR):int(17*SR)])
    trx=env(tr,[(0,0),(HIT-0.2,0),(HIT,3),(len(tr)/SR,0)])
    put(trx,tstart,g_tr)
    if tstart>0:   # pre-roll so music runs under the whole cold open: the track's steady section, crossfading into the real start
        pre=tr[int(1.0*SR):int((1.0+tstart+0.4)*SR)].copy(); q=int(0.4*SR); pre[-q:]*=np.linspace(1,0,q)[:,None]; pre[:int(0.3*SR)]*=np.linspace(0,1,int(0.3*SR))[:,None]
        put(pre,0,g_tr)
    # podcast title music: starts on the showcase, then ducks under the conversation and fades out
    nw=load(S+'/music/news.mp3'); g_nw=VL-14-lufs(nw[int(1*SR):int(20*SR)]); tb=T0_BODY/FPS
    nwx=env(nw[:int(40*SR)],[(0,-60),(0.3,0),(SHOWF/FPS-0.5,0),(SHOWF/FPS+1.5,-10),(28,-10),(34,-60),(40,-60)])
    put(nwx,T0_TITLE/FPS,g_nw)
    # end screen music + whoosh
    nwe=env(nw[int(30*SR):int(51*SR)],[(0,-60),(1.0,0),(18.5,0),(20.5,-60),(21,-60)]); put(nwe,T0_END/FPS,g_nw+2)
    wh=load(S+'/sfx/whoosh_ds.mp3'); vpk=np.percentile(np.abs(voice[T0_BODY*SPF:]),99.9); G_=lambda x,r:20*np.log10(r*vpk/(np.abs(x).max()+1e-9))
    put(wh,T0_END/FPS-0.9,G_(wh,0.22))
    # keyword clicks in the cold open
    ck=load(S+'/sfx/click.mp3')
    for g in co_groups():
        if g['gold']: put(ck,g['t0']-0.08,G_(ck,0.25))
    y=voice+mix; I=lufs(y[T0_BODY*SPF:]); y*=10**((-14-I)/20)
    wavfile.write(R+'/mix.wav',SR,y.astype(np.float32))
    run(['ffmpeg','-v','error','-y','-i',R+'/mix.wav','-af','alimiter=limit=0.72:attack=1:release=60:level=false','-c:a','pcm_s16le',R+'/mix_final.wav'])
    print('trailer starts at',round(tstart,2),'mid hit at',round(tstart+18.2,2),'title at',round(T0_TITLE/FPS,2),flush=True)

if STEP in ('all','mux'):
    out=S+'/deliverables/MartinezCid_YouTube_full_v7.mp4'
    run(['ffmpeg','-v','error','-y','-i',R+'/picture.mp4','-i',R+'/mix_final.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
         '-bsf:v','h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1','-movflags','+faststart',out])
    print('OUT',out,flush=True)

if STEP in ('all','srt'):
    def ts(x): h=int(x//3600); m=int(x%3600//60); s=x%60; return f"{h:02d}:{m:02d}:{int(s):02d},{int((s%1)*1000):03d}"
    sr16,a16=wavfile.read(S+'/long/a1_16k.wav'); a16=a16.astype(np.float32)/32768
    y=np.concatenate([a16[int(s*16000):int(s*16000)+round((e-s)*FPS)*16000//FPS] for s,e,_,_ in BODY])
    m=WhisperModel('large-v3',device='cpu',compute_type='int8')
    sg,_=m.transcribe(y,beam_size=5,language='en',word_timestamps=True,condition_on_previous_text=False)
    W=[[w.start,w.end,w.word.strip()] for z in sg for w in z.words]
    fix=lambda s: (s.replace('Martinez Sid','Martínez-Cid').replace('Martinez-Cid','Martínez-Cid').replace('Martinez','Martínez')
                    .replace('office furniture for sale','OfficeFurniture4Sale').replace('Office furniture for sale','OfficeFurniture4Sale').replace('Jordy','Jordi'))
    cues=[]; cur=[]
    for w in W:
        if cur and (len(' '.join(x[2] for x in cur+[w]))>84 or w[0]-cur[-1][1]>0.8 or cur[-1][2][-1] in '.?!' and len(' '.join(x[2] for x in cur))>30): cues.append(cur); cur=[]
        cur.append(w)
    if cur: cues.append(cur)
    off=T0_BODY/FPS; out=[]
    for i,c in enumerate(cues):
        txt=fix(' '.join(x[2] for x in c)); 
        if len(txt)>42:
            sp=txt.rfind(' ',0,len(txt)//2+8); txt=txt[:sp]+'\n'+txt[sp+1:]
        out.append(f"{i+1}\n{ts(c[0][0]+off)} --> {ts(c[-1][1]+off+0.2)}\n{txt}\n")
    open(S+'/deliverables/MartinezCid_09_YouTube_v7_captions.srt','w').write('\n'.join(out))
    # chapters: master times -> output times
    def out_t(mt):
        f=T0_BODY
        for (s,e,_,_),n in zip(BODY,bodyF):
            if s<=mt<e: return (f+round((mt-s)*FPS))/FPS
            if mt<s: return f/FPS          # chapter start fell in a removed pause: use the next kept moment
            f+=n
        return None
    CH=[(0,'Trailer'),(None,'Meet Jordi Martínez-Cid'),(97.0,'Why he left to start his own firm'),(163.7,'Talent before clients'),(235.8,'Money vs. vibes: keeping great people'),
        (329.2,'Your office as a recruiting tool'),(449.3,'Growing without compromising talent'),(532.1,'Technology and AI at the firm'),(640.2,'Clients who "write it with AI"'),
        (742.0,'AI and the courts'),(848.9,'His niche: the weird cases'),(1056.3,'How we met and working with OfficeFurniture4Sale'),(1163.5,'The war room'),(None,'END')]
    lines=[]
    for mt,name in CH:
        if name=='END': break
        tt=0 if mt==0 else (T0_TITLE/FPS if mt is None else out_t(mt))
        lines.append(f"{int(tt//60):02d}:{int(tt%60):02d} {name}")
    open(S+'/deliverables/MartinezCid_09_YouTube_v7_chapters.txt','w').write('\n'.join(lines)+'\n'); print('\n'.join(lines))
