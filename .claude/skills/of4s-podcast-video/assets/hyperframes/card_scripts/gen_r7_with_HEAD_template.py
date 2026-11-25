import os,shutil,sys
S='/tmp/claude-0/-home-user-OF4S-Marketing/94d491a9-d326-522d-bff4-7538a8d94c4a/scratchpad'
HEAD='''<!doctype html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=1080, height=1920" /><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>@font-face { font-family: "SG"; font-weight: 800; src: url("assets/schibsted-grotesk-latin-800-normal.woff") format("woff"); } * { margin: 0; padding: 0; box-sizing: border-box; } html, body { width: 1080px; height: 1920px; overflow: hidden; background: transparent; } #main { position: relative; width: 100%; height: 100%; } #stage { perspective: 1400px; }
.card { position: absolute; border-radius: 28px; background: #faf8f4; box-shadow: 0 40px 90px rgba(15,29,51,.40), 0 8px 20px rgba(15,29,51,.20); transform-origin: 50% 70%; overflow: hidden; font-family: "SG"; font-weight: 800; color: #15273f; }
.lab { font-size: 30px; letter-spacing: .12em; color: #466489; }
.red { color: #d64545; } .green { color: #2fb36a; } .navy { color: #15273f; } .muted { color: #8fa9c7; }
%CSS%
</style></head><body>
<div id="main" data-composition-id="main" data-start="0" data-duration="%D%" data-width="1080" data-height="1920">
<div id="stage" class="clip" data-start="0" data-duration="%D%" data-track-index="0">
%BODY%
</div></div>
<script>
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const IN = (sel, t) => tl.fromTo(sel, { rotationX: 70, y: 220, scale: 0.85, opacity: 0 }, { rotationX: 0, y: 0, scale: 1, opacity: 1, duration: 0.45, ease: "power3.out" }, t);
const OUT = (sel, t) => tl.to(sel, { scale: 0.92, y: 30, opacity: 0, duration: 0.2, ease: "power2.in" }, t);
const POP = (sel, t) => tl.fromTo(sel, { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.28, ease: "back.out(2.5)", immediateRender: false }, t);
%JS%
window.__timelines["main"] = tl;
</script></body></html>'''
cards={}
# 1 hook: California <-> Florida slider (pin slides to Florida; tags pop on 'employer' and 'non-compete')
FLD=open(S+'/R7/cards/fl_path.txt').read()
cards['r7slider']=dict(D=4.3,CSS='''#card{left:110px;top:1130px;width:860px;height:330px}
#map{position:absolute;left:36px;top:30px;width:300px;height:270px;overflow:visible}
#fl{position:absolute;left:380px;top:44px;font-size:76px;line-height:1}
#t1,#t2{position:absolute;left:380px;height:64px;line-height:64px;padding:0 28px;border-radius:32px;background:#15273f;color:#faf8f4;font-size:32px;letter-spacing:.06em}
#t1{top:146px} #t2{top:226px}''',
BODY='''<div class="card" id="card"><svg id="map"><path id="flp" d="'''+FLD+'''" fill="#15273f" fill-opacity="0" stroke="#15273f" stroke-width="2.2" stroke-linejoin="round"/></svg>
<div id="fl" class="navy">Florida</div><div id="t1">PRO-EMPLOYER</div><div id="t2">PRO NON-COMPETE</div></div>''',
JS='''const P=document.getElementById("flp"), B=P.getBBox(), pad=4;
document.getElementById("map").setAttribute("viewBox",(B.x-pad)+" "+(B.y-pad)+" "+(B.width+2*pad)+" "+(B.height+2*pad));
const L=P.getTotalLength(); gsap.set(P,{strokeDasharray:L,strokeDashoffset:L});
gsap.set(["#fl","#t1","#t2"],{opacity:0});
IN("#card",0.0);
tl.to(P,{strokeDashoffset:0,duration:0.7,ease:"power2.inOut"},0.15);
tl.to(P,{attr:{"fill-opacity":1},duration:0.3},0.7);
tl.fromTo("#fl",{opacity:0,x:-20},{opacity:1,x:0,duration:0.3,ease:"power3.out",immediateRender:false},0.2);
POP("#t1",1.62); POP("#t2",3.62);
OUT("#card",4.08);''')
# 2 price tags: $1,500 -> FREE online? -> $500 review
cards['r7price']=dict(D=9.5,CSS='''#card{left:90px;top:1100px;width:900px;height:300px}
.col{position:absolute;top:44px;width:280px;text-align:center}
#c1{left:20px} #c2{left:310px} #c3{left:600px}
.amt{font-size:76px;line-height:1.15}
.sub{font-size:28px;color:#466489;margin-top:6px}
#x2{position:absolute;left:330px;top:60px;width:240px;height:150px}''',
BODY='''<div class="card" id="card"><div class="col" id="c1"><div class="lab">LAWYER</div><div class="amt navy">$1,500</div><div class="sub">non-compete</div></div>
<div class="col" id="c2"><div class="lab">INTERNET</div><div class="amt muted">FREE?</div><div class="sub">download</div></div>
<div class="col" id="c3"><div class="lab">REVIEW IT</div><div class="amt green">$500</div><div class="sub">Eric's offer</div></div></div>''',
JS='''gsap.set(["#c1","#c2","#c3"],{opacity:0});
IN("#card",0.0); POP("#c1",0.80); POP("#c2",4.02); POP("#c3",8.0);
OUT("#card",9.25);''')
# 3 two years later
cards['r7years']=dict(D=1.9,CSS='''#card{left:290px;top:1180px;width:500px;height:170px}
#n{position:absolute;left:0;width:500px;top:22px;text-align:center;font-size:84px;line-height:1}
#l{position:absolute;left:0;width:500px;top:112px;text-align:center}''',
BODY='''<div class="card" id="card"><div id="n">2 YEARS</div><div id="l" class="lab">LATER</div></div>''',
JS='''IN("#card",0.0);
tl.fromTo("#n",{yPercent:60,opacity:0},{yPercent:0,opacity:1,duration:0.3,ease:"power4.out",immediateRender:false},0.15);
OUT("#card",1.68);''')
# 4a math: $500,000/yr x 50% margin
cards['r7math1']=dict(D=5.9,CSS='''#card{left:90px;top:1100px;width:900px;height:250px}
.col{position:absolute;top:40px;text-align:center}
#c1{left:30px;width:470px} #op{position:absolute;left:500px;top:86px;width:80px;text-align:center;font-size:56px;color:#8fa9c7} #c2{left:580px;width:290px}
.amt{font-size:84px;line-height:1.15}''',
BODY='''<div class="card" id="card"><div class="col" id="c1"><div class="lab">REVENUE / YEAR</div><div class="amt navy" id="rev">$500,000</div></div><div id="op">×</div><div class="col" id="c2"><div class="lab">MARGIN</div><div class="amt navy">50%</div></div></div>''',
JS='''gsap.set(["#c1","#op","#c2"],{opacity:0});
IN("#card",0.0); POP("#c1",0.30);
const o={v:0}; tl.to(o,{v:500000,duration:0.6,ease:"power2.out",onUpdate:()=>{document.getElementById("rev").textContent="$"+(Math.round(o.v/1000)*1000).toLocaleString("en-US")}},0.32);
POP("#op",3.0); POP("#c2",4.72);
OUT("#card",5.65);''')
# 4b = -$250,000 a year
cards['r7math2']=dict(D=2.6,CSS='''#card{left:140px;top:1100px;width:800px;height:240px}
#l{position:absolute;left:0;width:800px;top:36px;text-align:center}
#a{position:absolute;left:0;width:800px;top:78px;text-align:center;font-size:104px;line-height:1.1}''',
BODY='''<div class="card" id="card"><div id="l" class="lab">HIS FAMILY LOSES</div><div id="a" class="red">−$250,000<span style="font-size:44px;color:#466489"> /yr</span></div></div>''',
JS='''gsap.set("#a",{opacity:0});
IN("#card",0.0); POP("#a",0.50);
tl.to("#card",{keyframes:{x:[0,-10,8,-4,0]},duration:0.25},0.6);
OUT("#card",2.38);''')
# 5 dentist: industry check (S layout -> sits on George's chest, above the seam)
cards['r7dentist']=dict(D=4.5,CSS='''#card{left:140px;top:560px;width:800px;height:330px}
.row{position:absolute;left:50px;width:700px;height:110px}
#r1{top:40px} #r2{top:170px}
.k{font-size:30px;letter-spacing:.12em;color:#466489}
.v{font-size:58px;margin-top:4px}
.ic{position:absolute;right:0;top:20px;font-size:70px;line-height:1}
#stamp{position:absolute;left:470px;top:180px;padding:6px 22px;border:7px solid #d64545;border-radius:12px;color:#d64545;font-size:44px;letter-spacing:.08em;transform:rotate(-10deg)}''',
BODY='''<div class="card" id="card"><div class="row" id="r1"><div class="k">THEIR INDUSTRY</div><div class="v navy">Office furniture</div><div class="ic green">✓</div></div>
<div class="row" id="r2"><div class="k">THE CONTRACT SAYS</div><div class="v red">Dentist 🦷</div></div><div id="stamp">WRONG</div></div>''',
JS='''gsap.set(["#r1","#r2","#stamp"],{opacity:0});
IN("#card",0.0); POP("#r1",0.42); POP("#r2",2.55);
tl.fromTo("#stamp",{opacity:0,scale:2.4},{opacity:1,scale:1,duration:0.18,ease:"power4.in",immediateRender:false},3.55);
tl.to("#card",{keyframes:{x:[0,-12,9,-5,0]},duration:0.25},3.73);
OUT("#card",4.28);''')
# 6 demand letter: Bluff? $2,500
cards['r7letter']=dict(D=4.3,CSS='''#card{left:110px;top:1080px;width:860px;height:300px}
#env{position:absolute;left:50px;top:60px;width:220px;height:150px}
#t{position:absolute;left:300px;top:50px;width:520px}
#t .v{font-size:46px;line-height:1.1}
#bl{position:absolute;left:300px;top:178px;font-size:48px;line-height:72px;color:#466489}
#pr{position:absolute;left:560px;top:170px;font-size:72px;line-height:84px}''',
BODY='''<div class="card" id="card"><svg id="env" viewBox="0 0 220 150"><rect x="8" y="8" width="204" height="134" rx="10" fill="#fff" stroke="#15273f" stroke-width="10"/><path id="flap" d="M10,12 L110,82 L210,12" fill="none" stroke="#15273f" stroke-width="10" stroke-linejoin="round"/></svg>
<div id="t"><div class="lab">DEMAND LETTER</div><div class="v navy">Strongly worded</div></div><div id="bl">Bluff?</div><div id="pr" class="red">$2,500</div></div>''',
JS='''gsap.set(["#t","#bl","#pr"],{opacity:0});
IN("#card",0.0); POP("#t",0.22); POP("#bl",1.12); POP("#pr",3.45);
OUT("#card",4.08);''')
# 7 scoreboard
cards['r7score']=dict(D=3.4,CSS='''#card{left:110px;top:1080px;width:860px;height:330px}
.row{position:absolute;left:50px;width:760px;height:80px;font-size:40px;line-height:80px;border-bottom:3px solid #dde5ee}
.row b{float:right;font-size:52px}
#r1{top:30px} #r2{top:118px} #r3{top:206px;border-bottom:none}''',
BODY='''<div class="card" id="card"><div class="row" id="r1">Could have paid <b class="green">$1,500</b></div><div class="row" id="r2">Paid for a bluff <b class="red">$2,500</b></div><div class="row" id="r3">At risk every year <b class="red">$250K</b></div></div>''',
JS='''gsap.set(["#r1","#r2","#r3"],{opacity:0});
IN("#card",0.0); POP("#r1",0.25); POP("#r2",1.05); POP("#r3",1.85);
OUT("#card",3.18);''')
only=sys.argv[1:] or list(cards)
for name in only:
    c=cards[name]; d=f"{S}/hf/{name}"
    if not os.path.exists(d): shutil.copytree(S+'/hf/r6money',d,ignore=shutil.ignore_patterns('index*.html','render.log'))
    h=HEAD.replace('%CSS%',c['CSS']).replace('%BODY%',c['BODY']).replace('%JS%',c['JS']).replace('%D%',str(c['D']))
    open(d+'/index.html','w').write(h); print('wrote',name)
