cards={}
# 1 nine-year client badge
cards['r9years']=dict(D=2.3,CSS='''#card{left:240px;top:1150px;width:600px;height:220px}
#n{position:absolute;left:0;width:600px;top:26px;text-align:center;font-size:104px;line-height:1}
#l{position:absolute;left:0;width:600px;top:140px;text-align:center}''',
BODY='''<div class="card" id="card"><div id="n" class="navy">9 YEARS</div><div id="l" class="lab">OF4S CLIENT</div></div>''',
JS='''gsap.set(["#n","#l"],{opacity:0});
IN("#card",0.0);
tl.fromTo("#n",{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.3,ease:"back.out(2.5)",immediateRender:false},0.62);
tl.to("#l",{opacity:1,duration:0.2},0.8);
OUT("#card",2.08);''')
# 2 moved in 2018, fully furnished
cards['r9move']=dict(D=5.6,CSS='''#card{left:140px;top:1120px;width:800px;height:260px}
.row{position:absolute;left:60px;width:680px;height:90px}
#r1{top:36px} #r2{top:134px}
.k{font-size:28px;letter-spacing:.12em;color:#466489}
.v{font-size:56px;line-height:1.05}
.ck{position:absolute;right:0;top:20px;font-size:64px;color:#2fb36a;line-height:1}''',
BODY='''<div class="card" id="card"><div class="row" id="r1"><div class="k">MOVED INTO THESE OFFICES</div><div class="v navy">2018</div></div>
<div class="row" id="r2"><div class="k">ALL OF IT</div><div class="v navy">Fully furnished</div><div class="ck">&#10003;</div></div></div>''',
JS='''gsap.set(["#r1","#r2"],{opacity:0});
IN("#card",0.0); POP("#r1",0.3); POP("#r2",3.6);
OUT("#card",5.38);''')
# 3 sixteen offices: a floor plan that fills in office by office
cards['r9sixteen']=dict(D=3.6,CSS='''#card{left:140px;top:1080px;width:800px;height:330px}
#plan{position:absolute;left:40px;top:40px;width:340px;height:250px;border:6px solid #15273f;border-radius:6px}
.o{position:absolute;width:76px;height:52px;background:#15273f;border-radius:4px}
#n{position:absolute;left:420px;top:70px;font-size:120px;line-height:1}
#l{position:absolute;left:424px;top:200px;font-size:34px;line-height:1.2;color:#466489}''',
BODY='''<div class="card" id="card"><div id="plan"></div><div id="n" class="navy">16</div><div id="l">offices<br>originally furnished</div></div>''',
JS='''const P=document.getElementById("plan");
for(let i=0;i<16;i++){const c=i%4,r=Math.floor(i/4);P.insertAdjacentHTML("beforeend",'<div class="o" style="left:'+(8+c*82)+'px;top:'+(8+r*58)+'px"></div>');}
gsap.set(".o",{opacity:0,scale:0.4}); gsap.set(["#n","#l"],{opacity:0});
IN("#card",0.0);
tl.to(".o",{opacity:1,scale:1,duration:0.16,stagger:0.045,ease:"back.out(2)"},0.15);
POP("#n",0.2); tl.to("#l",{opacity:1,duration:0.25},2.95);
OUT("#card",3.38);''')
# 4 closing checklist: NO background, white text + soft shadow, green checks, one line at a time as he says it
cards['r9check']=dict(D=5.4,CSS='''@font-face{font-family:"SGB";font-weight:700;src:url("assets/schibsted-grotesk-latin-700-normal.woff") format("woff");}
.cl{position:absolute;left:150px;height:96px;display:flex;align-items:center;font-family:"SGB";font-weight:700;font-size:58px;color:#faf8f4;text-shadow:0 4px 16px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.4);white-space:nowrap}
.cl svg{width:62px;height:62px;margin-right:26px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.4))}
#l1{top:1110px} #l2{top:1206px} #l3{top:1302px}''',
BODY='''<div class="cl" id="l1"><svg viewBox="0 0 62 62"><circle cx="31" cy="31" r="29" fill="#2fb36a"/><path d="M17,32 L27,42 L46,21" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>Individualized options</div>
<div class="cl" id="l2"><svg viewBox="0 0 62 62"><circle cx="31" cy="31" r="29" fill="#2fb36a"/><path d="M17,32 L27,42 L46,21" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>Customized for our needs</div>''',
JS='''gsap.set([".cl"],{opacity:0});
[["#l1",0.5],["#l2",3.2]].forEach(([s,t])=>tl.fromTo(s,{opacity:0,x:-40},{opacity:1,x:0,duration:0.3,ease:"power3.out",immediateRender:false},t));
tl.to(".cl",{opacity:0,duration:0.2},5.15);''')
