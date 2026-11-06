# YouTube v7: trailer-style cold open (captioned) -> title on the hit -> George|Eric showcase + promise -> episode -> end screen
import json,subprocess,os,re,sys
import numpy as np
from scipy.io import wavfile
from PIL import Image,ImageDraw,ImageFont,ImageFilter
S='/tmp/claude-0/-home-user-OF4S-Marketing/94d491a9-d326-522d-bff4-7538a8d94c4a/scratchpad'; L=S+'/long'; Y=L+'/yt2'; FPS=30
ENC=['-c:v','libx264','-preset','faster','-b:v','2400k','-maxrate','3500k','-bufsize','7000k','-pix_fmt','yuv420p','-r','30','-an']
def run(c): subprocess.run(c,check=True)
W=json.load(open(L+'/wordmap.json'))
# (master start, master end, gold phrase, small line above gold or None)
CL=[(724.66,728.50,['the','consequences'],'not thinking about'),
    (945.38,948.05,['plumbing','school'],'go to'),
    (565.60,569.90,['pro','non','compete','state'],'and a'),
    (666.80,668.42,None,None),(669.70,671.95,['wrong','industry'],'for the'),
    (353.08,354.22,['get','clients'],'how am I going to'),
    (407.60,410.80,['get','a','promotion'],"where you're trying to"),
    (1076.52,1078.05,['work','from','home'],"Don't"),
    (1080.86,1082.05,['no','clients'],"There's")]
HIT_I=5; DROP_I=7
norm=lambda x:re.sub(r"[^a-z0-9']","",x.lower())
FP=S+'/fontsb/package/files/schibsted-grotesk-latin-%d-normal.woff'
fb=ImageFont.truetype(FP%700,60); fg=ImageFont.truetype(FP%700,94)
WHITE=(250,248,244,255); GOLD=(246,181,96,255)
def card(lines):   # lines: [(text,font,color)] stacked, bottom of block at y=930
    im=Image.new('RGBA',(1920,1080),(0,0,0,0)); d=ImageDraw.Draw(im)
    hs=[f.getbbox(t)[3]+14 for t,f,c in lines]; y=930-sum(hs)
    pos=[]
    for (t,f,c),h in zip(lines,hs): pos.append(((1920-d.textlength(t,font=f))/2,y,t,f,c)); y+=h
    sh=Image.new('RGBA',im.size,(0,0,0,0)); ds=ImageDraw.Draw(sh)
    for x,y,t,f,c in pos: ds.text((x,y+4),t,font=f,fill=(0,0,0,150))
    sh=sh.filter(ImageFilter.GaussianBlur(7)); im=Image.alpha_composite(im,sh); d=ImageDraw.Draw(im)
    for x,y,t,f,c in pos: d.text((x,y),t,font=f,fill=c)
    return im
cold=[]; n=0; os.makedirs(Y+'/cap',exist_ok=True)
for ci,(s,e,gold,small) in enumerate(CL):
    ws=[[a,b,t] for a,b,t,*_ in W if s-0.02<=a<e-0.03]
    toks=[norm(w[2]) for w in ws]; chunks=[]; i=0
    gi=None
    if gold:
        for k in range(len(toks)):
            if toks[k:k+len(gold)]==gold: gi=k; break
        assert gi is not None,(ci,gold,toks)
        sl=small.split() if small else []; si=gi-len(sl)
        if small: assert [norm(x) for x in toks[si:gi]]==[norm(x) for x in sl],(ci,toks[si:gi],sl)
    else: si=gi=None
    while i<len(ws):
        if si is not None and i==si:
            j=gi+len(gold); chunks.append((ws[i][0],[(small,fb,WHITE)] if small else [],' '.join(w[2] for w in ws[gi:j]))); i=j; continue
        j=i; cur=[]
        while j<len(ws) and len(cur)<3 and (si is None or i>si or j<si):
            cur.append(ws[j]); j+=1
            if cur[-1][2][-1] in ',.?!': break
        chunks.append((ws[i][0],None,' '.join(w[2] for w in cur))); i=j
    nf=round((e-s)*FPS); k=int(s//200); ss=s-200*k
    pngs=[]; flt=[]; t_prev=None
    for q,(t0,smalls,txt) in enumerate(chunks):
        txt=txt.replace(' ,',',').replace(' -','-').replace('$250 ,000','$250,000').replace('$250,000.','$250,000').replace('pro employer','pro-employer')
        txt=txt[0].upper()+txt[1:] if q==0 and smalls is None else txt
        if smalls is None: im=card([(txt,fb,WHITE)])
        else:
            big=txt if not txt.startswith('250') else '$250,000'
            big=big.replace('ChatGPT','ChatGPT').rstrip('.,')
            sm=[(smalls[0][0][0].upper()+smalls[0][0][1:] if q==0 else smalls[0][0],fb,WHITE)] if smalls else []
            im=card(sm+[(big,fg,GOLD)])
        p=f'{Y}/cap/c{ci}_{q}.png'; im.save(p); pngs.append(p)
        a=max(0,t0-s-0.05); b=(chunks[q+1][0]-s-0.05) if q+1<len(chunks) else nf/FPS
        flt.append((a,b))
    inp=['-ss',f'{ss:.4f}','-i',f'{L}/yt/main_{k}.mp4']; fc=''; last='0:v'
    for q,p in enumerate(pngs):
        inp+=['-i',p]; a,b=flt[q]; fc+=f"[{last}][{q+1}:v]overlay=enable='between(t,{a:.3f},{b:.3f})'[v{q}];"; last=f'v{q}'
    run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',fc.rstrip(';'),'-map',f'[{last}]','-frames:v',str(nf)]+ENC+[f'{Y}/cold_{ci}.mp4'])
    cold.append([s,e,nf]); print('clip',ci,nf,[c[2] for c in chunks],flush=True)
json.dump(cold,open(Y+'/cold.json','w'))
# title: hard cut on the music hit, 3 s
run(['ffmpeg','-v','error','-y','-loop','1','-i',L+'/yt/title.png','-vf','fps=30,format=yuv420p,fade=t=out:st=2.75:d=0.25','-frames:v','90']+ENC+[Y+'/title.mp4'])
# showcase: George|Eric two-shot + names + promise line
run(['ffmpeg','-v','error','-y','-ss','127.4','-i',L+'/yt/main_0.mp4','-i',S+'/hf/ytshow.mov','-filter_complex','[0:v][1:v]overlay=format=auto','-frames:v','150']+ENC+[Y+'/show.mp4'])
vids=[f'{Y}/cold_{i}.mp4' for i in range(len(cold))]+[Y+'/title.mp4',Y+'/show.mp4']+[Y+'/main_0.mp4']+[f'{L}/yt/main_{i}.mp4' for i in range(1,6)]+[L+'/yt/endscreen.mp4']
open(Y+'/list.txt','w').write(''.join(f"file '{v}'\n" for v in vids))
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',Y+'/list.txt','-c','copy',Y+'/video.mp4'])
# voice track, sample-exact to the frames
sr,a=wavfile.read(L+'/yt/master_audio.wav'); a=a.astype(np.float32); out=[]
for s,e,nf in cold:
    i=int(round(s*sr)); x=a[i:i+nf*1600].copy(); f=int(0.02*sr); x[:f]*=np.linspace(0,1,f)[:,None]; x[-f:]*=np.linspace(1,0,f)[:,None]; out.append(x)
out.append(np.zeros(((90+150)*1600,2),np.float32))
MAINF=33471; out.append(a[:MAINF*1600]); out.append(np.zeros((600*1600,2),np.float32))
y=np.concatenate(out); wavfile.write(Y+'/audio.wav',sr,np.clip(y,-32768,32767).astype(np.int16))
coldEnd=sum(n for *_,n in cold)/FPS; showStart=coldEnd+3.0; OFF=showStart+5.0
cuts=list(np.cumsum([n for *_,n in cold])[:-1]/FPS)
json.dump(dict(coldEnd=coldEnd,showStart=showStart,mainStart=OFF,endStart=OFF+MAINF/FPS,cuts=cuts,c5=sum(n for *_,n in cold[:HIT_I])/FPS,drop=sum(n for *_,n in cold[:DROP_I])/FPS),open(Y+'/marks.json','w'),indent=1)
# chapters + SRT with the new intro offset
fmt=lambda t:f"{int(t//60)}:{int(t%60):02d}"
ch=json.load(open(L+'/yt_marks.json'))['chapters']
txt=["0:00 Highlights"]+[f"{fmt(OFF+max(0,t-0.5) if i else OFF-5.0)} {name}" for i,(name,t) in enumerate(ch)]
open(L+'/EPGD_Podcast_YouTube_v7_chapters.txt','w').write('\n'.join(txt)+'\n')
def ts(t): h=int(t//3600); m=int(t%3600//60); s_=t%60; return f"{h:02d}:{m:02d}:{int(s_):02d},{int(round((s_%1)*1000))%1000:03d}"
def _brand(W):   # company name is one word: OfficeFurniture4Sale
    out=[];i=0
    while i<len(W):
        t=[re.sub(r"[^a-z]","",x[2].lower()) for x in W[i:i+4]]
        if t[:4]==['office','furniture','for','sale']: out.append([W[i][0],W[i+3][1],'OfficeFurniture4Sale'+re.sub(r"[A-Za-z]","",W[i+3][2])]+list(W[i][3:])); i+=4; continue
        if t[:3]==['office','furniture','sale']: out.append([W[i][0],W[i+2][1],'OfficeFurniture4Sale'+re.sub(r"[A-Za-z]","",W[i+2][2])]+list(W[i][3:])); i+=3; continue
        out.append(W[i]); i+=1
    return out
cues=[];cur=[]
for w in _brand(W):
    if cur and (w[0]-cur[-1][1]>0.6 or len(' '.join(x[2] for x in cur+[w]))>42 or cur[-1][2][-1] in '.?!' and len(cur)>3): cues.append(cur); cur=[]
    cur.append(w)
cues.append(cur); srt=[]
for k_,c in enumerate(cues,1):
    a0=OFF+c[0][0]; b0=OFF+min(c[-1][1]+0.3, cues[k_][0][0] if k_<len(cues) else c[-1][1]+0.3)
    srt.append(f"{k_}\n{ts(a0)} --> {ts(b0)}\n{' '.join(x[2] for x in c).replace(' ,',',').replace(' -','-')}\n")
open(L+'/EPGD_Podcast_YouTube_v7_captions.srt','w').write('\n'.join(srt))
print('coldEnd',round(coldEnd,2),'main at',round(OFF,2)); print('\n'.join(txt))
