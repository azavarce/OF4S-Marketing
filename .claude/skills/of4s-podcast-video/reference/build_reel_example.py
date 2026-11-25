# Reel 1 (Networking) v2 — everything in one pass:
# new hook -> black beat -> body; HDR->SDR; frame-exact video; sample-exact voice;
# approved B-roll + word-of-mouth animation; new caption style; music (buildup + bed); real SFX; logo end card.
import json, subprocess, os, sys, numpy as np
from scipy.io import wavfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S='/tmp/claude-0/-home-user-OF4S-Marketing/94d491a9-d326-522d-bff4-7538a8d94c4a/scratchpad'
R=S+'/R10'; FPS=30; GOFF=-3.25; SR=48000; SPF=SR//FPS
CLIENT=S+'/raw2_4k/client_4k.mov'; GEORGE=S+'/raw2/george.mov'   # Shot 2: Eric from the 4K original
A=S+'/audiodl'
STEP=sys.argv[1] if len(sys.argv)>1 else 'all'
def run(c): subprocess.run(c,check=True)
def nfr(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]).strip())

# ---------- 1. segments ----------
segs=json.load(open(R+'/segs_r10.json'))
AW=json.load(open(S+'/words2_aligned.json'))
for s in segs: s['nf']=round((s['en']-s['st'])*FPS)
HOOK=0; BLACKF=0; ENDF=78   # Reel 6: hook A -> dramatic black beat (rewind into the conversation) -> George's question

# ---------- 2. video ----------
TMF="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
EC=lambda dx=0,dy=0,oy=0: (f"crop=1600:2400:480:{600+oy},rotate=-3*PI/180:ow=iw:oh=ih:c=black,crop=1040:1849:{310+2*dx}:{60+2*dy},scale=1080:1920:flags=lanczos,"
                        +TMF+",colorchannelmixer=rr=1.049:gg=1.057:bb=1.110,eq=saturation=1.153,unsharp=3:3:0.3")
GGo=lambda oy=0: ("crop=1411:2508:205:"+str(671+oy)+",scale=1080:1920:flags=lanczos,"+TMF+",format=rgb24,lutrgb=r='clip((val-143.6)*0.975+150.9,0,255)':g='clip((val-150.4)*0.957+156.2,0,255)':b='clip((val-161.1)*0.976+164.4,0,255)',format=yuv420p,unsharp=3:3:0.4"); GG=GGo()
C0="[0:v]setpts=PTS-STARTPTS,fps=30,"; G0="[1:v]setpts=PTS-STARTPTS,fps=30,"
def lay_graph(lay,o):
    E=EC(o.get('dx',0),o.get('dy',0),o.get('oy',0))
    if lay=='Gz': return f"{G0}{GGo(o.get('goy',-200))},crop=880:1564:{o.get('gx',100)}:0,scale=1080:1920:flags=lanczos[v]"
    if lay=='Cz': z=o.get('z',0.86); w=int(1080*z)//2*2; h=int(1920*z)//2*2; return f"{C0}{E},crop={w}:{h}:{(1080-w)//2+o.get('zx',0)}:{o.get('zy',0)},scale=1080:1920:flags=lanczos[v]"
    return {'C':f"{C0}{E}[v]",'Ct':f"{C0}{E},crop=964:1714:58:90,scale=1080:1920:flags=lanczos[v]",
            'Gt':f"{G0}{GG},crop=940:1671:70:60,scale=1080:1920:flags=lanczos[v]",'G':f"{G0}{GG}[v]",
            'S':f"{G0}{GG},crop=1080:960:0:330[g];{C0}{E},crop=1080:960:0:{o.get('sy',300)}[c];[g][c]vstack,drawbox=x=0:y=957:w=1080:h=6:color=0x15273f:t=fill[v]"}[lay]
ENC=['-c:v','libx264','-preset','medium','-crf','17','-pix_fmt','yuv420p','-r','30']
MT=3   # Eric starts his story: music drops into the background here
DIP={}   # no visual transition in this reel
def seg_video(k,s):
    p=f"{R}/v{k:02d}.mp4"
    if os.path.exists(p) and nfr(p)==s['nf']: return p
    d=s['nf']/FPS+0.5; o=s.get('opt',{})
    vC=o['vt'] if o.get('cam')=='C' else s['st']; vG=(o['vt'] if o.get('cam')=='G' else s['st'])+GOFF   # cutaways borrow video from another moment
    run(['ffmpeg','-v','error','-y','-ss',f"{vC:.4f}",'-t',f"{d:.3f}",'-i',CLIENT,'-ss',f"{vG:.4f}",'-t',f"{d:.3f}",'-i',GEORGE,
         '-filter_complex',lay_graph(s['lay'],o),'-map','[v]','-frames:v',str(s['nf']),'-an']+ENC+[p])
    assert nfr(p)==s['nf'],p
    return p
if STEP in ('all','video'):
    parts=[]
    for k,s in enumerate(segs):
        parts.append(seg_video(k,s)); print('seg',k,s['nf'],flush=True)
    run(['ffmpeg','-v','error','-y','-i',S+'/hf/logoend_v2.mp4','-vf','fps=30,scale=1080:1920,format=yuv420p','-frames:v',str(ENDF),'-an']+ENC+[R+'/end.mp4'])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=black:s=1080x1920:r=30','-frames:v',str(BLACKF)]+ENC+[R+'/black.mp4'])
    order=(parts[:HOOK]+[R+'/black.mp4']+parts[HOOK:] if BLACKF else parts)+[R+'/end.mp4']
    open(R+'/list.txt','w').write(''.join(f"file '{p}'\n" for p in order))
    run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',R+'/list.txt','-c','copy',R+'/body.mp4'])
    print('body frames',nfr(R+'/body.mp4'),flush=True)

# ---------- timeline ----------
off=[]; f=0
for k,s in enumerate(segs):
    if k==HOOK: BLACK0=f; f+=BLACKF
    off.append(f); f+=s['nf']
END0=f; TOTALF=f+ENDF; TOT=TOTALF/FPS
t_of=lambda k,src: off[k]/FPS+(src-segs[k]['st'])     # source time in seg k -> output time

# ---------- B-roll re-anchored from C13 (same source moment) ----------
TW=[w for s_ in json.load(open(S+'/work/transcript.json'))['segments'] for w in s_['words']]
PD=json.load(open(S+'/planD.json'))
def c13segs():
    fr=lambda t:round(t*FPS)/FPS; wi=lambda t:min(range(len(TW)),key=lambda i:abs(TW[i][0]-t)); out=[]
    for row in PD:
        name,a,b,lay=row[:4]; i,j=wi(a),wi(b); st=TW[i][0]-0.10; en=TW[j][1]+0.15
        if i>0: st=max(st,(TW[i-1][1]+TW[i][0])/2)
        if len(row)>4: st=row[4]
        if j+1<len(TW): en=min(en,(TW[j][1]+TW[j+1][0])/2)
        out.append((fr(st),fr(en)))
    return out
C=c13segs(); co=np.cumsum([0]+[e-s for s,e in C])
def c13_to_new(t):
    k=max(i for i in range(len(C)) if co[i]<=t); src=C[k][0]+(t-co[k])
    kn=k                                      # same structure as C13 (two-part hook restored)
    return t_of(kn,src)
BR=[]
H_=S+'/hf/'
H_=S+'/hf/'
H_=S+'/hf/'
_o=lambda n:off[[x['name'] for x in segs].index(n)]/FPS
BRN=[(H_+'r10prose.mov',_o('S2')-0.12),(H_+'r10pages.mov',_o('S13')+0.6),(H_+'r10check.mov',_o('S14')+3.37)]
FULL=set(f for f,_ in BRN)   # floating cards sit where captions go: captions pause while they're up
BRD={f:float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f])) for f,_ in BRN}
WOM=(-1.0,-1.0)
NOCAP=[(t,t+BRD[f]) for f,t in BRN if f in FULL]   # no captions over full-screen animations
print('BROLL',[(os.path.basename(f),t) for f,t in BRN])

# ---------- captions ----------
FP=S+'/fontsb/package/files/schibsted-grotesk-latin-%d-normal.woff'
WHITE=(250,248,244); GOLD=(246,181,96); B=64; K=int(B*1.6)
# highlight spec per segment: (match tokens, small-line text, big text, big-gold, style)  style 'tier'=small over big, 'num'=big number + word on one line, 'big'=big only
_ix=lambda n:[x['name'] for x in segs].index(n)
_ix=lambda n:[x['name'] for x in segs].index(n)
_ix=lambda n:[x['name'] for x in segs].index(n)
HL={_ix('S5'):[(['you','have','to','get','a','lawyer'],'you have to','get a lawyer','tier')],
    _ix('S10'):[(['phony','pleadings'],None,'phony pleadings','big')],
    _ix('S12c'):[(['you','have','to','defend','yourself'],'you have to','defend yourself','tier')]}
norm=lambda x:''.join(c for c in x.lower() if c.isalnum() or c=="'").strip("'")
groups=[]   # dict(t0,t1,kind,lines,seg,click)
STOPEND=set("a an the to of and or but so is it it's i i'm you you're your he that this in on at for with as be are was if then well how am going get my me our their".split())
for k,s in enumerate(segs):
    ws=[[t_of(k,w[0]),t_of(k,w[1]),w[2]] for w in s['w']]
    ws=[[max(a,off[k]/FPS+0.02),b,t] for a,b,t in ws]
    toks=[norm(w[2]) for w in ws]; used=[False]*len(ws); hl=[]
    for m,sm,big,sty in HL.get(k,[]):
        for n in range(len(ws)):
            if toks[n:n+len(m)]==m and not any(used[n:n+len(m)]):
                for q in range(n,n+len(m)): used[q]=True
                hl.append((n,n+len(m),sm,big,sty)); break
        else: print('HL MISS',k,m,toks)
    def plain_run(run):
        # split a run of plain words into 2-3 word chunks at punctuation/pauses, never leave a lone word if avoidable
        ch=[]; cur=[]
        for w in run:
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
            txt=' '.join(w[2] for w in c).replace(' -','-').replace(' ,',',').strip(' ,.?')
            groups.append(dict(t0=c[0][0],t1=c[-1][1],kind='plain',text=txt,seg=k,lay=s['lay'],endp=c[-1][2][-1] in '.?!'))
    n=0; wrun=[]
    while n<len(ws):
        h=[x for x in hl if x[0]==n]
        if h:
            if wrun: plain_run(wrun); wrun=[]
            a,b,sm,big,sty=h[0]
            tb=ws[a+(len(sm.split()) if sm else 0)][0]
            groups.append(dict(t0=ws[a][0],tbig=tb,t1=ws[b-1][1],kind=sty,small=sm,big=big,seg=k,lay=s['lay'],endp=ws[b-1][2][-1] in '.?!')); n=b; continue
        wrun.append(ws[n]); n+=1
    if wrun: plain_run(wrun)
# end times: until next group starts (max +0.5s after last word), never past segment end
groups.sort(key=lambda g:g['t0'])
# merge lone one-word plain captions into the next plain caption (across segment cuts) so they read as phrases
i=0
while i+1<len(groups):
    g,n=groups[i],groups[i+1]
    if g['kind']=='plain' and len(g['text'].split())==1 and n['kind']=='plain' and n['t0']-g['t1']<0.8 and len((g['text']+' '+n['text']).split())<=4:
        n['text']=g['text']+' '+n['text']; n['t0']=g['t0']; groups.pop(i); continue
    i+=1
for i,g in enumerate(groups):
    if i+1<len(groups) and groups[i+1]['t0']<=g['t0']+0.25: groups[i+1]['t0']=g['t0']+0.25   # overlapping word timings
for i,g in enumerate(groups):
    segend=(off[g['seg']]+segs[g['seg']]['nf'])/FPS
    e=min(max(g['t1'],g['t0']+0.3)+0.45,segend)
    if i+1<len(groups): e=min(e,groups[i+1]['t0'])
    g['t1']=e
# no captions over the word-of-mouth animation
# captions pause while a card is up; a caption already on screen when a card starts ends exactly at the card (hand-off)
for a,b in NOCAP:
    for g in groups:
        if g['t0']<a<g['t1']: g['t1']=a
groups=[g for g in groups if not any(a<=g['t0']<b for a,b in NOCAP)]
# keyword pops: snap to where his voice actually starts the word (transcript marks can run late), one frame early
from scipy.io import wavfile as _wf
_sr,_a=_wf.read(S+'/long/a2.wav'); _a=_a.astype(np.float32).mean(1)
def voice_onset(src):
    seg=_a[int((src-0.35)*_sr):int((src+0.15)*_sr)]; n=int(0.01*_sr)
    L=np.array([20*np.log10(np.sqrt(np.mean(seg[q:q+n]**2))+1e-9) for q in range(0,len(seg)-n,n)])
    pk=L[25:].max(); base=np.percentile(L[:20],20); q=35
    while q>0 and L[q-1]>base+0.5*(pk-base): q-=1
    return src-0.35+q*0.01
for g in groups:
    if g['kind']!='plain':
        k=g['seg']; tb=g.get('tbig',g['t0']); src=segs[k]['st']+(tb-off[k]/FPS)
        new=max(off[k]/FPS, t_of(k,voice_onset(src))-1/FPS); d_=new-tb
        g['tbig']=new
        if abs(g['t0']-tb)<1e-6: g['t0']=new
# sentence case: capitalize first word of a sentence
prev_end=True
for g in groups:
    if g['kind']=='plain':
        t=g['text']; g['text']=(t[0].upper()+t[1:]) if (prev_end or g['t0']<BLACK0/FPS+1.0 and g['t0']>BLACK0/FPS) and t else t
    prev_end=g['endp']
json.dump(groups,open(R+'/caps.json','w'),indent=0)

fonts={}
def F(wt,sz):
    if (wt,sz) not in fonts: fonts[(wt,sz)]=ImageFont.truetype(FP%wt,sz)
    return fonts[(wt,sz)]
def layout_lines(g):
    if g['kind']=='plain': return [[(g['text'],B,700,WHITE)]]
    if g['kind']=='num':   n_,wd=g['big']; return [[(n_,K,700,GOLD),(wd,B,700,WHITE)]]
    if g['kind']=='big':   return [[(g['big'],K,700,GOLD)]]
    return [[(g['small'],B,700,WHITE)],[(g['big'],K,700,GOLD)]]
_cache={}
def cap_img(g,scale=1.0,show_big=True):
    key=(id(g),round(scale,3),show_big)
    if key in _cache: return _cache[key]
    W,H=1080,1920; lay=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(lay)
    lines=layout_lines(g)
    if not show_big and g['kind']=='tier': lines=lines[:1]
    rows=[]
    for parts in lines:
        parts=[(t,int(sz*scale) if c==GOLD else sz,wt,c) for t,sz,wt,c in parts]
        sp=18; ws_=[d.textlength(t,font=F(wt,sz)) for t,sz,wt,c in parts]; tw=sum(ws_)+sp*(len(parts)-1)
        if tw>W*0.70:                                   # IG + TikTok safe width (clear of right-side buttons)
            q=W*0.70/tw; parts=[(t,int(sz*q),wt,c) for t,sz,wt,c in parts]
            ws_=[d.textlength(t,font=F(wt,sz)) for t,sz,wt,c in parts]; tw=sum(ws_)+sp*(len(parts)-1)
        rows.append((parts,ws_,tw,max(p[1] for p in parts)))
    bh=sum(r[3]*1.02 for r in rows)
    if g['lay'] in ('S','P'): top=960-bh/2-12                       # split screen: on the seam, between the two faces
    else: top=min(H*0.62-bh/2,H*0.70-bh)                  # lower third, inside IG + TikTok safe zone
    y=top; items=[]
    for parts,ws_,tw,lh in rows:
        x=(W-tw)/2
        for (t,sz,wt,c),w in zip(parts,ws_): items.append((x,y+(lh-sz)*0.78,t,F(wt,sz),c)); x+=w+18
        y+=lh*1.02
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for x,yy,t,f,c in items: ds.text((x,yy+5),t,font=f,fill=(0,0,0,170))
    sh=sh.filter(ImageFilter.GaussianBlur(9))
    for x,yy,t,f,c in items: d.text((x,yy),t,font=f,fill=c+(255,))
    im=Image.alpha_composite(sh,lay); _cache[key]=im; return im

if STEP in ('all','compose'):
    # caption overlay stream (RGBA raw) -> final picture with B-roll
    cmd=['ffmpeg','-v','error','-y','-i',R+'/body.mp4']
    for f,t in BRN: cmd+=['-i',f]
    cmd+=['-f','rawvideo','-pix_fmt','rgba','-s','1080x1920','-r','30','-i','-']
    fc=[]; last='0:v'
    for n,(f,t) in enumerate(BRN):
        dd=BRD[f]
        fc.append(f"[{n+1}:v]setpts=PTS-STARTPTS,fps=30,format=yuva420p,fade=t=in:st=0:d=0.14:alpha=1,fade=t=out:st={dd-0.14:.3f}:d=0.14:alpha=1,setpts=PTS+{t:.4f}/TB[b{n}]")
        fc.append(f"[{last}][b{n}]overlay=0:0:eof_action=pass[o{n}]"); last=f"o{n}"
    ci=len(BRN)+1
    fc.append(f"[{last}][{ci}:v]overlay=0:0:format=auto[v]")
    p=subprocess.Popen(cmd+['-filter_complex',';'.join(fc),'-map','[v]','-frames:v',str(TOTALF)]+['-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r','30',R+'/picture.mp4'],stdin=subprocess.PIPE)
    blank=bytes(1080*1920*4)
    for fi in range(TOTALF):
        t=fi/FPS; g=next((g for g in groups if g['t0']<=t<g['t1']),None)
        if g is None: p.stdin.write(blank); continue
        tb=g.get('tbig',g['t0']); show_big=t>=tb
        age=t-(tb if g['kind']!='plain' else g['t0'])
        sc=1.0+0.12*max(0,1-age/0.10) if g['kind']!='plain' else 1.0     # quick 'pop' on keywords only
        p.stdin.write(cap_img(g,sc,show_big).tobytes())
        if fi%300==0: print('frame',fi,'/',TOTALF,flush=True)
    p.stdin.close(); p.wait(); assert p.returncode==0
    print('picture frames',nfr(R+'/picture.mp4'),flush=True)

# ---------- audio ----------
if STEP in ('all','audio'):
    sr,a1=wavfile.read(S+'/long/a2.wav'); a1=a1.astype(np.float32)/32768
    N=TOTALF*SPF; voice=np.zeros((N,2),np.float32)
    for k,s in enumerate(segs):
        i0=int(round(s['st']*SR)); n=s['nf']*SPF; x=a1[i0:i0+n].copy()
        r=int(0.012*SR); x[:r]*=np.linspace(0,1,r)[:,None]; x[-r:]*=np.linspace(1,0,r)[:,None]
        voice[off[k]*SPF:off[k]*SPF+n]=x
    def load(path,ss=0,dur=None):
        c=['ffmpeg','-v','error','-ss',str(ss),'-i',path]+(['-t',str(dur)] if dur else [])+['-ac','2','-ar','48000','-f','f32le','-']
        return np.frombuffer(subprocess.run(c,capture_output=True).stdout,np.float32).reshape(-1,2).copy()
    def lufs(x):
        wavfile.write(R+'/_m.wav',SR,x.astype(np.float32))
        r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',R+'/_m.wav','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
        return float([l for l in r.splitlines() if l.strip().startswith('I:')][-1].split()[1])
    VL=lufs(voice[:END0*SPF]); print('voice LUFS',VL)
    mix=np.zeros_like(voice)
    def put(x,t,gain_db):
        i=int(round(t*SR));
        if i<0: x=x[-i:]; i=0
        x=x[:max(0,N-i)]; mix[i:i+len(x)]+=x*10**(gain_db/20)
    def fade(x,fi=0,fo=0):
        x=x.copy(); n=len(x)
        if fi: q=int(fi*SR); x[:q]*=np.linspace(0,1,q)[:,None]
        if fo: q=int(fo*SR); x[n-q:]*=np.linspace(1,0,q)[:,None]
        return x
    def at_lufs(x,target):  # gain to bring x to target LUFS
        return target-lufs(x)
    tB=BLACK0/FPS; tBody=(BLACK0+BLACKF)/FPS; tEnd=END0/FPS
    MUS=A+'/music/nastelbom-motivation-motivation-background-617070.mp3'; LON=1.325; PER=8.8889
    ph=load(MUS,LON,PER+0.05); xf=int(0.04*SR)
    def looped(L):
        n=int(L*SR); out=np.zeros((n+len(ph),2),np.float32); pos=0; P=int(PER*SR)
        while pos<n:
            seg=ph[:P+xf].copy(); seg[:xf]*=np.linspace(0,1,xf)[:,None]; seg[P:]*=np.linspace(1,0,len(seg)-P)[:,None]
            out[pos:pos+len(seg)]+=seg; pos+=P
        return out[:n]
    g_bed=at_lufs(looped(20),VL-11)
    tM=off[MT]/FPS
    # hook: nastelbom motivation-cinematic - steady, pulls back (tension) under part 2, its hit (33.25 s) lands on the black beat
    CIN=A+'/music/nastelbom-motivation-motivation-cinematic-617063.mp3'
    hk=load(CIN,33.25-tB,tB+0.6); g_cin=at_lufs(load(CIN,22,7),VL-13)
    th=np.arange(len(hk))/SR; eh=np.interp(th,[0,tB,tB+0.6],[1,10**(5/20),0])   # louder for its hit on the black, gone by George
    # riser peaking on the black beat + deep impact
    if os.environ.get('BED'):
        # TEST: one track from the black beat to the end, low and steady under Eric (no muffling)
        trk=A+'/music/'+os.environ['BED']; full=load(trk)
        e_=np.sqrt(np.convolve(full.mean(1)**2,np.ones(480)/480,'same')); on=int(np.argmax(e_>0.2*e_.max()))
        src=full[on:]; bl=tEnd+ENDF/FPS-tBody; need=int(bl*SR)+SR
        if os.environ.get('BESTWIN') and len(src)>need+10*SR:
            # use the steadiest window of the track (lowest loudness swing)
            m1=src.mean(1); L1=np.array([10*np.log10(np.mean(m1[k:k+SR]**2)+1e-12) for k in range(0,len(m1)-SR,SR)])
            W1=int(bl)+1; cand=[(L1[k:k+W1].std(),k) for k in range(0,len(L1)-W1,2)]; sd,k0=min(cand)
            print('steadiest window starts',k0,'s, loudness swing',round(sd,1),'dB'); src=src[k0*SR:]
        if len(src)<need:
            # loop on the best-matching repeat point (period 3-20 s), 0.3 s crossfade
            m=src.mean(1); ref=m[SR:4*SR]; best=(0,None)
            for P in range(int(3*SR),int(min(45*SR,len(m)-5*SR)),240):
                seg=m[SR+P:4*SR+P]; cc=float(np.dot(ref,seg)/(np.linalg.norm(ref)*np.linalg.norm(seg)+1e-9))
                if cc>best[0]: best=(cc,P)
            P=best[1]; print('loop period',P/SR,'corr',round(best[0],3))
            unit=src[:P]; xf=int(0.3*SR); out=src[:P+xf].copy()
            while len(out)<need:
                nxt=src[:P+xf].copy(); w_=np.linspace(0,1,xf)[:,None]
                out[-xf:]=out[-xf:]*(1-w_)+nxt[:xf]*w_; out=np.concatenate([out,nxt[xf:]])
            src=out
        bed=src[:int(bl*SR)]
        gb2=at_lufs(bed[:int(20*SR)],VL-float(os.environ.get('BEDDB','13')))
        tb_=np.arange(len(bed))/SR
        DROP=10**(-float(os.environ.get('DROPDB','5'))/20); x0=(off[3]+segs[3]['nf'])/FPS-tBody+0.4   # lower the music right after 'I spent over five years at that firm'
        e2=np.interp(tb_,[0,x0-0.4,x0+0.6,tEnd-tBody,tEnd-tBody+0.3,bl-1.2,bl],[1,1,DROP,DROP,DROP*10**(5/20),DROP*10**(5/20),0])
        put(fade(bed*e2[:,None],0.35,0),tBody,gb2)
        if os.environ.get('HOOKCIN'):
            # hook: cinematic track, its hit lands on the black beat; riser into it + deep impact (as Reel 1)
            put(fade(hk*eh[:,None],0.2,0),0,g_cin+float(os.environ.get('HOOKBOOST','4')))
            rs=load(A+'/sfx/swooshriser.mp3',0,2.6); put(fade(rs,0,0.6),tB-1.8,VL-6-lufs(rs[:int(1.9*SR)]))
            im=load(A+'/sfx_new/black_kumizhi-huge-cinematic-reverb-impact-506132.mp3',0,3.0); put(fade(im,0,1.6),tB,VL-3-lufs(im[:int(1.0*SR)]))
        if os.environ.get('HOOKM'):
            # hook gets its own, more driving track; it hands off to the bed as George asks his question
            hm=load(A+'/music/'+os.environ['HOOKM'],float(os.environ.get('HOOKMS','1.0')),tB+0.45)
            put(fade(hm,0.03,0.45),0.0,at_lufs(hm,VL-float(os.environ.get('HOOKDB','15'))))
    else:
        # one continuous bed (the phrase Joanne liked) from George's question to the end;
        # at "I listened to my mentor" it drops into the background: muffled (low-pass sweep) + 5 dB down, hidden by the whoosh
        from scipy.signal import butter,sosfilt
        bl=tEnd+ENDF/FPS-tBody; bed=looped(bl)
        muf=sosfilt(butter(4,700,'lp',fs=SR,output='sos'),bed,axis=0).astype(np.float32)
        tb_=np.arange(len(bed))/SR; x0=tM-tBody
        w=np.clip((tb_-(x0-0.3))/1.0,0,1)[:,None]                     # gentle 1 s sweep as Eric starts his story
        gpost=10**(-5/20)*1.35                                         # 5 dB down (+ make-up for the energy the filter removes)
        bed=bed*(1-w)+muf*w*gpost
        e2=np.interp(tb_,[0,tEnd-tBody,tEnd-tBody+0.3,bl-1.2,bl],[1,1,10**(3/20),10**(3/20),0])
        put(fade(bed*e2[:,None],0.12,0),tBody,g_bed)
    # clicks on keyword pops (soft, short)
    ck=load(A+'/sfx_new/justsomesounds-click-sound-432501.mp3'); ckpk=np.abs(ck).max(); vpk=np.percentile(np.abs(voice[:END0*SPF]),99.9)
    cg=20*np.log10(0.30*vpk/ckpk)
    for g in groups:
        if g['kind']!='plain': put(ck,g.get('tbig',g['t0'])-0.10,cg)
    # B-roll entries: soft swoosh; word-of-mouth bubbles: tiny pops
    sw=load(A+'/sfx/swoosh05.mp3'); swg=20*np.log10(0.22*vpk/np.abs(sw).max())
    pp=load(A+'/sfx/pop.mp3'); ppg=20*np.log10(0.16*vpk/np.abs(pp).max())
    vpk=np.percentile(np.abs(voice[:END0*SPF]),99.9); G=lambda x,r:20*np.log10(r*vpk/np.abs(x).max())
    sw=load(A+'/sfx/swoosh05.mp3'); pp=load(A+'/sfx/pop.mp3'); ck=load(A+'/sfx_new/justsomesounds-click-sound-432501.mp3')
    hit=fade(load(A+'/sfx_new/black_kumizhi-huge-cinematic-reverb-impact-506132.mp3',0,1.2),0,0.7)
    T=dict((os.path.basename(f),t) for f,t in BRN)
    vpk=np.percentile(np.abs(voice[:END0*SPF]),99.9); G=lambda x,r:20*np.log10(r*vpk/np.abs(x).max())
    sw=load(A+'/sfx/swoosh05.mp3'); pp=load(A+'/sfx/pop.mp3'); ck=load(A+'/sfx_new/justsomesounds-click-sound-432501.mp3'); wd=load(A+'/sfx/whoosh_ds.mp3')
    T=dict((os.path.basename(f),t) for f,t in BRN); sn=load(A+'/sfx/snap.mp3')
    def card(name,pops=(),clicks=(),sw_=True):
        t0=T[name]
        if sw_: put(sw,max(0,t0-0.20),G(sw,0.18))
        for d_ in pops: put(pp,t0+d_-0.07,G(pp,0.24))
        for d_ in clicks: put(ck,t0+d_-0.10,G(ck,0.30))
    card('r10prose.mov',pops=(0.2,1.6,2.2))
    card('r10pages.mov',pops=(0.35,3.25))
    card('r10check.mov',clicks=(0.52,3.6),sw_=False)
    # end card: whoosh in, chime on the logo shine
    wh=load(A+'/sfx/whoosh_ds.mp3'); put(wh,tEnd-0.9,20*np.log10(0.22*vpk/np.abs(wh).max()))
    # (logo-card chime removed per Joanne)
    y=voice+mix
    wavfile.write(R+'/mix_pre.wav',SR,y.astype(np.float32))
    I=lufs(y); g=-14-I; y*=10**(g/20); print('mix LUFS',I,'gain',round(g,2))
    wavfile.write(R+'/mix.wav',SR,y.astype(np.float32))
    run(['ffmpeg','-v','error','-y','-i',R+'/mix.wav','-af','alimiter=limit=0.84:attack=1:release=60:level=false','-c:a','pcm_s16le',R+'/mix_final.wav'])
    print('audio samples',len(y),'expected',N)

if STEP in ('all','mux'):
    out=S+'/EPGD_reel10_ai_lawsuits/'+os.environ.get('OUTNAME','EPGD_reel10_ai_lawsuits_v1.mp4'); os.makedirs(os.path.dirname(out),exist_ok=True)
    run(['ffmpeg','-v','error','-y','-i',R+'/picture.mp4','-i',R+'/mix_final.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k',
         '-bsf:v','h264_metadata=colour_primaries=1:transfer_characteristics=1:matrix_coefficients=1','-movflags','+faststart',out])
    print('OUT',out)
print('TIMELINE hook 0-%.2f black %.2f-%.2f body-%.2f end %.2f total %.2f'%(BLACK0/FPS,BLACK0/FPS,(BLACK0+BLACKF)/FPS,END0/FPS,END0/FPS,TOT))
