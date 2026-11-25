# Finish Joanne's manual cuts: captions + keyword clicks, camera-switch swooshes, music bed, cards, OF4S end card.
import json, subprocess, os, sys, numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S='/tmp/claude-0/-home-user-OF4S-Marketing/915db505-5c90-5c27-94f4-cf4a8187b153/scratchpad'
M=S+'/manual'; NAME=sys.argv[1]; CFG=json.load(open(M+'/cfg.json'))[NAME]
R=M+'/build_'+NAME; os.makedirs(R,exist_ok=True)
FPS=30; SR=48000; SPF=SR//FPS; ENDF=78
SRC=M+f'/{NAME}.mp4'; E=CFG['end']; NF=round(E*FPS); TOTALF=NF+ENDF; END0=NF
def run(c): subprocess.run(c,check=True)
def nfr(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]).strip())
ENC=['-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-r','30']

# ---------- cards (PIL, paper card style, timed to words) ----------
FS=S+'/fonts/fontsource-schibsted-grotesk-5.3.0/files/schibsted-grotesk-latin-%d-normal.woff'
PAPER=(250,248,244); NAVY=(21,39,63); RED=(214,69,69); GREEN=(47,179,106)
fonts={}
def F(wt,sz):
    if (wt,sz) not in fonts: fonts[(wt,sz)]=ImageFont.truetype(FS%wt,sz)
    return fonts[(wt,sz)]
def ease(x): x=min(1,max(0,x)); return 1-(1-x)**3
def card_frame(c,t):
    """t = seconds since card start. Returns RGBA 1080x1920 or None."""
    D=c['dur']
    if t<0 or t>D: return None
    a_in=ease(t/0.28); a_out=1-ease((t-(D-0.25))/0.25) if t>D-0.25 else 1
    a=min(a_in,a_out); dy=int(60*(1-a_in))
    W,H=1080,1920; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    cw,ch=c.get('w',760),c.get('h',300); x0=(W-cw)//2; y0=c.get('y',1180)+dy
    # shadow + paper card
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh); ds.rounded_rectangle([x0,y0+14,x0+cw,y0+ch+14],28,fill=(0,0,0,int(110*a)))
    sh=sh.filter(ImageFilter.GaussianBlur(18)); lay=Image.alpha_composite(lay,sh); d=ImageDraw.Draw(lay)
    d.rounded_rectangle([x0,y0,x0+cw,y0+ch],28,fill=PAPER+(int(255*a),))
    if c['kind']=='stack':
        # photos snapping in fast, piling on top of each other (slight offsets/rotations), all clear together at the end
        if 'imgs' not in c:
            import random; rnd=random.Random(7); c['imgs']=[]
            for i,pth in enumerate(c['paths']):
                im=Image.open(pth).convert('RGB'); r=im.width/im.height
                im=im.crop(((im.width-im.height*4/3)/2,0,(im.width+im.height*4/3)/2,im.height)) if r>4/3 else im.crop((0,(im.height-im.width*3/4)/2,im.width,(im.height+im.width*3/4)/2))
                pw,ph=600,450; im=im.resize((pw,ph),Image.LANCZOS); bx=12
                fr=Image.new('RGBA',(pw+2*bx,ph+2*bx),PAPER+(255,)); fr.paste(im,(bx,bx))
                rot=rnd.uniform(-7,7); fr=fr.rotate(rot,resample=Image.BICUBIC,expand=True)
                c['imgs'].append((fr,rnd.randint(-70,70),rnd.randint(-50,50)))
        lay=Image.new('RGBA',(W,H),(0,0,0,0)); fade_out=1-ease((t-(D-0.2))/0.2) if t>D-0.2 else 1
        for i,(fr,ox,oy) in enumerate(c['imgs']):
            ti=t-i*c['every']
            if ti<0: break
            p_=ease(ti/0.10); sc=1+0.12*max(0,1-ti/0.12)
            f2=fr.resize((int(fr.width*sc),int(fr.height*sc)),Image.BILINEAR) if sc>1.001 else fr
            al=f2.split()[3].point(lambda v:int(v*p_*fade_out)); f2=f2.copy(); f2.putalpha(al)
            sh=Image.new('RGBA',(W,H),(0,0,0,0)); x1=W//2-f2.width//2+ox; y1=c.get('y',1180)-f2.height//2+oy
            shm=Image.new('L',f2.size,0); shm.paste(al,(0,0)); s_=Image.new('RGBA',f2.size,(0,0,0,int(120*p_*fade_out))); sh.paste(s_,(x1,y1+14),shm)
            lay=Image.alpha_composite(lay,sh.filter(ImageFilter.GaussianBlur(14)))
            lay.alpha_composite(f2,(max(0,x1),max(0,y1)))
        return lay
    if c['kind']=='photo':
        # 4:3 photo as a floating card (paper border), below the faces
        if 'img' not in c: c['img']=Image.open(c['path']).convert('RGB')
        pw,ph=c.get('w',640),c.get('w',640)*3//4; bx=14
        ph_im=c['img'].copy(); r=ph_im.width/ph_im.height
        ph_im=ph_im.crop(((ph_im.width-ph_im.height*4/3)/2,0,(ph_im.width+ph_im.height*4/3)/2,ph_im.height)) if r>4/3 else ph_im.crop((0,(ph_im.height-ph_im.width*3/4)/2,ph_im.width,(ph_im.height+ph_im.width*3/4)/2))
        ph_im=ph_im.resize((pw,ph),Image.LANCZOS)
        lay2=Image.new('RGBA',(W,H),(0,0,0,0)); x1=(W-pw)//2; y1=c.get('y',960)+dy
        sh2=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh2).rounded_rectangle([x1-bx,y1-bx+16,x1+pw+bx,y1+ph+bx+16],24,fill=(0,0,0,int(120*a)))
        lay2=Image.alpha_composite(lay2,sh2.filter(ImageFilter.GaussianBlur(18))); d2=ImageDraw.Draw(lay2)
        d2.rounded_rectangle([x1-bx,y1-bx,x1+pw+bx,y1+ph+bx],24,fill=PAPER+(int(255*a),))
        pa=ph_im.convert('RGBA'); pa.putalpha(int(255*a)); m=Image.new('L',(pw,ph),0); ImageDraw.Draw(m).rounded_rectangle([0,0,pw,ph],14,fill=int(255*a))
        lay2.paste(pa,(x1,y1),m)
        return lay2
    if c['kind']=='filing':
        f1=F(700,104); f2=F(600,40)
        txt='100 pages'; tw=d.textlength(txt,font=f1); d.text(((W-tw)/2,y0+52),txt,font=f1,fill=NAVY+(int(255*a),))
        s2='one court filing'; tw2=d.textlength(s2,font=f2); d.text(((W-tw2)/2,y0+178),s2,font=f2,fill=(90,104,124,int(255*a)))
        tx=c['x_at']
        if t>=tx:   # red cross pops on "cannot"
            p=ease((t-tx)/0.16); sc=1+0.25*max(0,1-(t-tx)/0.2)
            cx,cy,r=x0+cw-70,y0+60,int(40*sc)
            d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=RED+(int(255*a*p),))
            w_=max(6,int(9*sc)); k=int(r*0.45)
            d.line([cx-k,cy-k,cx+k,cy+k],fill=(255,255,255,int(255*a*p)),width=w_); d.line([cx-k,cy+k,cx+k,cy-k],fill=(255,255,255,int(255*a*p)),width=w_)
    if c['kind']=='quote':
        f1=F(700,62); f2=F(600,36)
        lines=['“What incredible','attention to detail.”']; yy=y0+46
        for L in lines:
            tw=d.textlength(L,font=f1); d.text(((W-tw)/2,yy),L,font=f1,fill=NAVY+(int(255*a),)); yy+=78
        s2='— chief compliance officer of a multinational'; tw2=d.textlength(s2,font=f2); d.text(((W-tw2)/2,yy+18),s2,font=f2,fill=(90,104,124,int(255*a)))
        tg=c['check_at']
        if t>=tg:
            p=ease((t-tg)/0.16); sc=1+0.25*max(0,1-(t-tg)/0.2); cx,cy,r=x0+cw-58,y0+52,int(34*sc)
            d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=GREEN+(int(255*a*p),))
            d.line([cx-int(r*.45),cy,cx-int(r*.1),cy+int(r*.38),cx+int(r*.5),cy-int(r*.35)],fill=(255,255,255,int(255*a*p)),width=max(6,int(8*sc)),joint='curve')
    return lay
CARDS=CFG.get('cards',[])

# ---------- captions ----------
W_=[[float(a),float(b),w] for a,b,w in json.load(open(M+f'/{NAME}_words.json')) if a<E-0.05]
WHITE=(250,248,244); GOLD=(246,181,96); B=64; K=int(B*1.6)
norm=lambda x:''.join(c for c in x.lower() if c.isalnum() or c=="'").strip("'")
toks=[norm(w[2]) for w in W_]; used=[False]*len(W_); hl=[]
for m,sm,big in CFG['hl']:
    m=[norm(x) for x in m.split()]; nsm=len(sm.split()) if sm else 0
    for n in range(len(W_)):
        if toks[n:n+len(m)]==m and not any(used[max(0,n-nsm):n+len(m)]):
            a0=n-nsm if sm and [norm(x) for x in sm.split()]==toks[max(0,n-nsm):n] else n
            for q in range(a0,n+len(m)): used[q]=True
            hl.append((a0,n+len(m),sm if a0<n else None,big)); break
    else: print('HL MISS',m)
groups=[]
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
        groups.append(dict(t0=c[0][0],t1=c[-1][1],kind='plain',text=' '.join(w[2] for w in c).strip(' ,.?'),endp=c[-1][2][-1] in '.?!'))
n=0; wr=[]
while n<len(W_):
    h=[x for x in hl if x[0]==n]
    if h:
        if wr: plain_run(wr); wr=[]
        a,b,sm,big=h[0]; tb=W_[b-len(big.split())][0]
        groups.append(dict(t0=W_[a][0],tbig=tb,t1=W_[b-1][1],kind='tier' if sm else 'big',small=sm,big=big,endp=W_[b-1][2][-1] in '.?!')); n=b; continue
    wr.append(W_[n]); n+=1
if wr: plain_run(wr)
groups.sort(key=lambda g:g['t0'])
for i,g in enumerate(groups):
    if i+1<len(groups) and groups[i+1]['t0']<=g['t0']+0.25: groups[i+1]['t0']=g['t0']+0.25
for i,g in enumerate(groups):
    e=max(g['t1'],g['t0']+0.3)+0.45
    if i+1<len(groups): e=min(e,groups[i+1]['t0'])
    g['t1']=min(e,E)
NOCAP=[(c['t'],c['t']+c['dur']) for c in CARDS if c['kind']!='photo']   # photo cards keep captions (raised above the photo)
for a,b in NOCAP:
    for g in groups:
        if g['t0']<a<g['t1']: g['t1']=a
groups=[g for g in groups if not any(a<=g['t0']<b for a,b in NOCAP)]
sr_,av=wavfile.read(M+f'/{NAME}.wav'); av=av.astype(np.float32)
def onset(src):
    sg=av[int(max(0,src-0.35)*sr_):int((src+0.15)*sr_)]; n=int(0.01*sr_)
    L=np.array([20*np.log10(np.sqrt(np.mean(sg[q:q+n]**2))+1e-9) for q in range(0,len(sg)-n,n)])
    if len(L)<36: return src
    pk=L[25:].max(); base=np.percentile(L[:20],20); q=35
    while q>0 and L[q-1]>base+0.5*(pk-base): q-=1
    return src-0.35+q*0.01
for g in groups:
    if g['kind']!='plain': g['tbig']=max(g['t0'],onset(g['tbig'])-1/FPS)
prev=True
for g in groups:
    if g['kind']=='plain' and g['text']: g['text']=(g['text'][0].upper()+g['text'][1:]) if prev else g['text']
    elif g.get('small') and prev: g['small']=g['small'][0].upper()+g['small'][1:]
    prev=g['endp']
json.dump(groups,open(R+'/caps.json','w'),indent=0)
def layout_lines(g,show_big):
    if g['kind']=='plain': return [[(g['text'],B,GOLD if False else WHITE)]]
    if g['kind']=='big': return [[(g['big'],K,GOLD)]]
    return [[(g['small'],B,WHITE)]]+([[(g['big'],K,GOLD)]] if show_big else [])
_c={}
def cap_img(g,sc,show_big,above=None):
    key=(id(g),round(sc,3),show_big,above)
    if key in _c: return _c[key]
    W,H=1080,1920; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay); rows=[]
    full=layout_lines(g,True)
    for parts in layout_lines(g,show_big):
        parts=[(t,int(sz*sc) if c==GOLD else sz,c) for t,sz,c in parts]
        ws=[d.textlength(t,font=F(700,sz)) for t,sz,c in parts]; tw=sum(ws)
        if tw>W*0.70:
            q=W*0.70/tw; parts=[(t,int(sz*q),c) for t,sz,c in parts]; ws=[d.textlength(t,font=F(700,sz)) for t,sz,c in parts]; tw=sum(ws)
        rows.append((parts,ws,tw,max(p[1] for p in parts)))
    bh=sum(max(p[1] for p in r)*1.02 for r in full)
    sp=any(s[0] in SPLIT and s[0]<=g['t0']<s[1] for s in SH)
    y=(960-bh/2-12) if sp else min(H*0.62-bh/2,H*0.70-bh)
    if above is not None: y=above-bh-28          # a photo card is up: caption sits just above it, never over it
    items=[]
    for parts,ws,tw,lh in rows:
        x=(W-tw)/2
        for (t,sz,c),w in zip(parts,ws): items.append((x,y+(lh-sz)*0.78,t,F(700,sz),c)); x+=w
        y+=lh*1.02
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for x,yy,t,f,c in items: ds.text((x,yy+5),t,font=f,fill=(0,0,0,170))
    sh=sh.filter(ImageFilter.GaussianBlur(9))
    for x,yy,t,f,c in items: d.text((x,yy),t,font=f,fill=c+(255,))
    im=Image.alpha_composite(sh,lay); _c[key]=im; return im

# ---------- video: her cut + zoom steps on key lines + split screens on George's lines + EPGD end card ----------
SH=json.load(open(M+'/shotmap.json'))[NAME]; SPLIT=set(CFG.get('split',[])); O=4.871
TMF=("zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,"
     "tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,eq=brightness=0.035:contrast=1.04:saturation=1.08,unsharp=3:3:0.35")
def shot_of(t): return next(s for s in SH if s[0]<=t<s[1]+1e-6)
def headpos(t0,dur):
    r=subprocess.run(['ffmpeg','-v','error','-ss',f"{t0+O:.2f}",'-t',f"{dur:.2f}",'-i',S+'/src/Client.MOV','-vf','fps=4,scale=540:960,format=gray','-f','rawvideo','-'],capture_output=True).stdout
    Fr=np.frombuffer(r,np.uint8).reshape(-1,960,540); tops=[];xs=[]
    for f in Fr:
        reg=f[150:460,30:450]<70; rows=np.where(reg.sum(1)>10)[0]
        if len(rows): tops.append((rows[0]+150)*4); xs.append((reg[rows[0]:rows[0]+40].nonzero()[1].mean()+30)*4)
    return float(np.median(tops)),float(np.median(xs))
def crop(cx,top,H,hp,aspect):
    W=int(H*aspect)//2*2; H=H//2*2; x0=int(min(max(cx-W/2,0),2160-W)); y0=int(min(max(top-hp*H,0),3840-H)); return f"crop={W}:{H}:{x0}:{y0}"
# zoom windows from gold keywords
ZW=[]
for g in groups:
    if g['kind']=='plain': continue
    s=shot_of(g['tbig']); 
    if s[0] in SPLIT or any(c['t']-0.3<=g['tbig']<=c['t']+c['dur'] for c in CARDS): continue
    z=(g['tbig']-0.05,min(s[1],g['tbig']+2.6))
    if z[1]-z[0]>=1.5: ZW.append(z)
ZW+=[tuple(z) for z in CFG.get('force_zoom',[])]   # zoom step that hides a same-camera jump cut
bounds=sorted({0,NF}|{round(s[0]*FPS) for s in SH}|{round(s[1]*FPS) for s in SH if s[1]<E}|{round(a*FPS) for a,b in ZW}|{round(b*FPS) for a,b in ZW})
bounds=[b for b in bounds if 0<=b<=NF]
def piece(k,f0,f1):
    t0=f0/FPS; n=f1-f0; p=f"{R}/p{k:03d}.mp4"; s=shot_of(t0+1e-3); mode='split' if s[0] in SPLIT else ('zoom' if any(round(a*FPS)<=f0<round(b*FPS) for a,b in ZW) else 'plain')
    if os.path.exists(p) and nfr(p)==n: return p,mode
    if mode=='split':
        tm=s[2]+(t0-s[0]); jt,jx=headpos(tm,n/FPS+0.3)
        jc=crop(jx+150,jt,1000,0.12,1080/960)
        GRADE="format=rgb24,lutrgb=r='clip(val*1.02-61\\,0\\,255)':g='clip(val*0.98-53\\,0\\,255)':b='clip(val*0.85-20\\,0\\,255)',format=yuv420p"
        # top: George straight from Joanne's own cut (her grade); bottom: Jordi from the raw camera, matched to her grade
        fc=(f"[1:v]setpts=PTS-STARTPTS,fps=30,crop=2160:1920:0:560,scale=1080:960:flags=lanczos,format=yuv420p[g];"
            f"[0:v]setpts=PTS-STARTPTS,fps=30,{jc},scale=1080:960:flags=lanczos,{TMF},{GRADE}[c];"
            "[g][c]vstack,drawbox=x=0:y=957:w=1080:h=6:color=0x15273f:t=fill[v]")
        run(['ffmpeg','-v','error','-y','-ss',f"{tm+O:.4f}",'-t',f"{n/FPS+0.5:.3f}",'-i',S+'/src/Client.MOV','-ss',f"{t0:.4f}",'-t',f"{n/FPS+0.5:.3f}",'-i',SRC,
             '-filter_complex',fc,'-map','[v]','-frames:v',str(n),'-an']+ENC+[p])
    else:
        vf='fps=30,'+('crop=iw/1.12:ih/1.12:(iw-ow)/2:ih*0.015,' if mode=='zoom' else '')+'scale=1080:1920:flags=lanczos,format=yuv420p'
        run(['ffmpeg','-v','error','-y','-ss',f"{t0:.4f}",'-i',SRC,'-vf',vf,'-frames:v',str(n),'-an']+ENC+[p])
    assert nfr(p)==n,p
    return p,mode
STEP=sys.argv[2] if len(sys.argv)>2 else 'all'
if STEP in ('all','video'):
    parts=[]
    for k,(f0,f1) in enumerate(zip(bounds,bounds[1:])):
        p,mode=piece(k,f0,f1); parts.append(p); print('piece',k,round(f0/FPS,2),round(f1/FPS,2),mode,flush=True)
    open(R+'/list.txt','w').write(''.join(f"file '{p}'\n" for p in parts)+f"file '{S}/epgd/logoend.mp4'\n")
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/list.txt','-c','copy',R+'/body.mp4'])
    assert nfr(R+'/body.mp4')==TOTALF
if STEP in ('all','compose'):
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-i',R+'/body.mp4','-f','rawvideo','-pix_fmt','rgba','-s','1080x1920','-r','30','-i','-',
        '-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-frames:v',str(TOTALF),'-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r','30',R+'/picture.mp4'],stdin=subprocess.PIPE)
    blank=Image.new('RGBA',(1080,1920),(0,0,0,0))
    for fi in range(TOTALF):
        t=fi/FPS; im=blank
        g=next((g for g in groups if g['t0']<=t<g['t1']),None)
        _bw=CFG.get('black') or CFG.get('whip')
        if g is not None and t<E and not (_bw and _bw[0]-0.02<=t<_bw[1]):
            tb=g.get('tbig',g['t0']); sb=t>=tb
            sc=1.0+0.12*max(0,1-(t-tb)/0.10) if g['kind']!='plain' and sb else 1.0
            up=[c for c in CARDS if c['kind']=='photo' and c['t']-0.05<=t<=c['t']+c['dur']]
            im=cap_img(g,sc,sb,(up[0].get('y',960)-14) if up else None)
        for c in CARDS:
            cf=card_frame(c,t-c['t'])
            if cf is not None: im=Image.alpha_composite(im,cf)
        p.stdin.write(im.tobytes())
    p.stdin.close(); p.wait(); assert p.returncode==0 and nfr(R+'/picture.mp4')==TOTALF

# ---------- audio ----------
def load(path,ss=0,dur=None):
    c=['ffmpeg','-v','error','-ss',str(ss),'-i',path]+(['-t',str(dur)] if dur else [])+['-ac','2','-ar','48000','-f','f32le','-']
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
def lufs(x):
    wavfile.write(R+'/_m.wav',SR,x.astype(np.float32))
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',R+'/_m.wav','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
    return float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
if STEP in ('all','audio'):
    N=TOTALF*SPF; v=load(SRC)[:NF*SPF]; q=int(0.04*SR); v[-q:]*=np.linspace(1,0,q)[:,None]
    voice=np.zeros((N,2),np.float32); voice[:len(v)]=v; mix=np.zeros_like(voice)
    def put(x,t,gdb):
        i=int(round(t*SR))
        if i<0: x=x[-i:]; i=0
        x=x[:max(0,N-i)]; mix[i:i+len(x)]+=x*10**(gdb/20)
    def fade(x,fi=0,fo=0):
        x=x.copy(); n=len(x)
        if fi: q=int(fi*SR); x[:q]*=np.linspace(0,1,q)[:,None]
        if fo: q=int(fo*SR); x[n-q:]*=np.linspace(1,0,q)[:,None]
        return x
    vpk=np.percentile(np.abs(voice[:NF*SPF]),99.9); G=lambda x,r:20*np.log10(r*vpk/(np.abs(x).max()+1e-9))
    ck=load(S+'/sfx/click.mp3'); sw=load(S+'/sfx/swoosh05.mp3'); pp=load(S+'/sfx/pop.mp3'); wh=load(S+'/sfx/whoosh_ds.mp3')
    for g in groups:
        if g['kind']!='plain': put(ck,g['tbig']-0.10,G(ck,0.30))
    for t in CFG['switches']:
        if t>0.5: put(sw,t-0.18,G(sw,0.10))          # soft swoosh on each George/Jordi camera switch
    for c in CARDS:
        put(sw,max(0,c['t']-0.20),G(sw,0.18))
        if c['kind']=='stack':
            sn=load(S+'/sfx/click.mp3')   # click per photo (Joanne)
            for i in range(len(c['paths'])): put(sn,c['t']+i*c['every']-0.03,G(sn,0.16))
        if c['kind']=='photo': put(ck,c['t']+0.02,G(ck,0.30))
        for k in ('x_at','check_at'):
            if k in c: put(ck,c['t']+c[k]-0.07,G(ck,0.30))   # click, not the bubble pop
    put(wh,E-0.9,G(wh,0.22))
    VL=lufs(voice[:NF*SPF])
    if not CFG.get('music'): bed=np.zeros((N,2),np.float32)   # no music bed for this video
    else: bed=load(S+'/music/'+CFG['music'],CFG.get('music_ss',0),TOTALF/FPS+1)[:N]
    gb=(VL-CFG.get('beddb',20)-lufs(bed[:min(len(bed),20*SR)])) if CFG.get('music') else 0
    t_=np.arange(len(bed))/SR
    if 'black' in CFG:   # rewind beat after the hook: music swells into the black, impact on the cut, dips back under the story
        tB,tBe=CFG['black']
        e=np.interp(t_,[0,0.3,tB,tBe,tBe+0.6,TOTALF/FPS-1.2,TOTALF/FPS],[0,10**(1/20),10**(2/20),10**(-4/20),1,1,0])
        VLh=lufs(voice[:int(tB*SR)])
        rs=load(S+'/sfx/swooshriser.mp3',0,2.6); put(fade(rs,0,0.6),tB-1.8,VLh-6-lufs(rs[:int(1.9*SR)]))
        im=load(S+'/sfx/impact.mp3',0,3.0); put(fade(im,0,1.6),tB,VLh-3-lufs(im[:int(1.0*SR)]))
    elif 'whip' in CFG:  # 0.3 s whip after the hook: whoosh only inside the hold+whip, soft music hit mid-whip
        tB,tBe=CFG['whip']
        e=np.interp(t_,[0,0.3,tB+0.15,tBe+0.4,TOTALF/FPS-1.2,TOTALF/FPS],[0,1,10**(2/20),1,1,0])
        VLh=lufs(voice[:int(tB*SR)])
        whs=fade(wh[int(0.50*SR):int(1.05*SR)],0.03,0.15); put(whs,tB-0.20,G(wh,0.22))
        im=load(S+'/sfx/impact.mp3',0,3.0); put(fade(im,0,1.2),tB+0.15,VLh-9-lufs(im[:int(1.0*SR)]))
    else: e=np.interp(t_,[0,0.5,TOTALF/FPS-1.2,TOTALF/FPS],[0,1,1,0])
    put(bed*e[:,None],0,gb)
    y=voice+mix; I=lufs(y); y*=10**((-14-I)/20)
    wavfile.write(R+'/mix.wav',SR,y.astype(np.float32))
    run(['ffmpeg','-v','error','-y','-i',R+'/mix.wav','-af','alimiter=limit=0.72:attack=1:release=60:level=false','-c:a','pcm_s16le',R+'/mix_final.wav'])
if STEP in ('all','mux'):
    out=S+'/deliverables/'+CFG['out']
    run(['ffmpeg','-v','error','-y','-i',R+'/picture.mp4','-i',R+'/mix_final.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
         '-bsf:v','h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1','-movflags','+faststart',out])
    print('OUT',out,'%.2fs'%(TOTALF/FPS))
