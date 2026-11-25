cards={}
STRIKE='''.chip{position:absolute;height:84px;line-height:84px;padding:0 34px;border-radius:42px;background:#dde5ee;color:#15273f;font-size:44px;white-space:nowrap}
.chip .ln{position:absolute;left:22px;right:22px;top:40px;height:6px;border-radius:3px;background:#d64545;transform-origin:0 50%;transform:scaleX(0)}
'''
# 1 jobs going away: "intake" / "data entry" struck as he says them
cards['r8jobs']=dict(D=5.1,CSS=STRIKE+'''#card{left:140px;top:1100px;width:800px;height:270px}
#hd{position:absolute;left:0;width:800px;top:34px;text-align:center}
#c1{left:70px;top:120px} #c2{left:400px;top:120px}''',
BODY='''<div class="card" id="card"><div id="hd" class="lab">GOING AWAY FIRST</div><div class="chip" id="c1">Intake<div class="ln"></div></div><div class="chip" id="c2">Data entry<div class="ln"></div></div></div>''',
JS='''gsap.set(["#c1","#c2"],{opacity:0});
IN("#card",0.0); POP("#c1",2.05); POP("#c2",3.65);
tl.to("#c1 .ln",{scaleX:1,duration:0.22,ease:"power2.out"},2.5); tl.to("#c1",{color:"#8fa9c7",duration:0.2},2.6);
tl.to("#c2 .ln",{scaleX:1,duration:0.22,ease:"power2.out"},4.1); tl.to("#c2",{color:"#8fa9c7",duration:0.2},4.2);
OUT("#card",4.85);''')
# 2 summer law clerks: 10 -> 6-7
cards['r8clerks']=dict(D=7.0,CSS='''#card{left:110px;top:1090px;width:860px;height:340px}
#hd{position:absolute;left:0;width:860px;top:30px;text-align:center}
#row{position:absolute;left:62px;top:84px;width:750px;height:120px}
.p{position:absolute;top:0;width:60px;height:110px}
#n{position:absolute;left:0;width:860px;top:216px;text-align:center;font-size:62px;line-height:1.1}
#n .a{color:#15273f} #n .ar{color:#8fa9c7;margin:0 18px} #n .b{color:#d64545}
#n2{position:absolute;left:0;width:860px;top:292px;text-align:center;font-size:24px;color:#466489;letter-spacing:.08em}''',
BODY='''<div class="card" id="card"><div id="hd" class="lab">SUMMER LAW CLERKS</div><div id="row"></div>
<div id="n"><span class="a">10</span><span class="ar">&#8594;</span><span class="b">6&#8211;7</span></div><div id="n2">LAST 5&#8211;6 SUMMERS &#8594; THIS SUMMER (PREDICTED)</div></div>''',
JS='''const row=document.getElementById("row");
for(let i=0;i<10;i++){row.insertAdjacentHTML("beforeend",'<svg class="p" id="p'+i+'" style="left:'+(i*75)+'px" viewBox="0 0 60 110"><circle cx="30" cy="22" r="18" fill="#15273f"/><path d="M6,108 L6,66 Q6,46 30,46 Q54,46 54,66 L54,108 Z" fill="#15273f"/></svg>');}
gsap.set(".p",{opacity:0}); gsap.set(["#n .a","#n .ar","#n .b","#n2"],{opacity:0});
IN("#card",0.0);
tl.fromTo(".p",{opacity:0,y:20},{opacity:1,y:0,duration:0.22,stagger:0.08,ease:"back.out(2)",immediateRender:false},2.0);
POP("#n .a",2.85);
tl.to(["#p6","#p7","#p8","#p9"],{opacity:0.15,y:12,duration:0.3,stagger:0.08},5.85);
POP("#n .ar",5.85); POP("#n .b",6.0); tl.to("#n2",{opacity:1,duration:0.2},6.05);
OUT("#card",6.78);''')
# 3 law school x / plumbing school check
cards['r8school']=dict(D=2.6,CSS='''#card{left:140px;top:1100px;width:800px;height:300px}
.col{position:absolute;top:30px;width:360px;text-align:center}
#c1{left:20px} #c2{left:420px}
.ic{width:140px;height:140px;margin:0 auto;display:block}
.t{font-size:40px;margin-top:10px}
.mk{position:absolute;top:10px;right:60px;font-size:64px;line-height:1}''',
BODY='''<div class="card" id="card">
<div class="col" id="c1"><svg class="ic" viewBox="0 0 140 140"><path d="M20,70 L70,30 L120,70 L70,105 Z" fill="none" stroke="#15273f" stroke-width="10" stroke-linejoin="round"/><path d="M38,84 L38,108 Q70,126 102,108 L102,84" fill="none" stroke="#15273f" stroke-width="10" stroke-linejoin="round"/><path d="M120,70 L120,104" stroke="#15273f" stroke-width="8" stroke-linecap="round"/></svg><div class="t navy">Law school</div><div class="mk red" id="m1">&#10005;</div></div>
<div class="col" id="c2"><svg class="ic" viewBox="0 0 140 140"><path d="M44,96 L92,48" stroke="#15273f" stroke-width="18" stroke-linecap="round"/><path d="M84,24 a26,26 0 1,0 32,32 l-14,4 -10,-10 4,-14 z" fill="#15273f"/><circle cx="40" cy="100" r="16" fill="#15273f"/></svg><div class="t navy">Plumbing school</div><div class="mk green" id="m2">&#10003;</div></div></div>''',
JS='''gsap.set(["#c1","#c2","#m1","#m2"],{opacity:0});
IN("#card",0.0); POP("#c1",0.1); POP("#c2",0.55); POP("#m2",0.62);
tl.fromTo("#m1",{opacity:0,scale:2.2},{opacity:1,scale:1,duration:0.16,ease:"power4.in",immediateRender:false},1.65);
tl.to("#c1",{opacity:0.45,duration:0.2},1.8);
OUT("#card",2.38);''')
# 4 still in demand (split screen: sits on George's chest, above the seam)
cards['r8demand']=dict(D=4.1,CSS='''#card{left:140px;top:580px;width:800px;height:310px}
#hd{position:absolute;left:0;width:800px;top:28px;text-align:center}
.row{position:absolute;left:90px;width:620px;height:72px;font-size:46px;line-height:72px}
.row b{float:right;color:#2fb36a;font-size:44px}
#r1{top:72px} #r2{top:148px} #r3{top:224px}''',
BODY='''<div class="card" id="card"><div id="hd" class="lab">STILL IN DEMAND</div><div class="row" id="r1">Plumbing <b>&#8593;</b></div><div class="row" id="r2">Data centers <b>&#8593;</b></div><div class="row" id="r3">Electricians <b>&#8593;</b></div></div>''',
JS='''gsap.set(["#r1","#r2","#r3"],{opacity:0});
IN("#card",0.0); POP("#r1",0.3); POP("#r2",1.25); POP("#r3",3.45);
OUT("#card",3.88);''')
# 5 same task with AI: 2 hours -> 30 minutes
cards['r8time']=dict(D=2.8,CSS='''#card{left:140px;top:1100px;width:800px;height:280px}
#hd{position:absolute;left:0;width:800px;top:30px;text-align:center}
#a{position:absolute;left:40px;top:96px;width:300px;text-align:center;font-size:84px;line-height:1.1;color:#8fa9c7}
#ar{position:absolute;left:350px;top:110px;width:100px;text-align:center;font-size:70px;color:#466489}
#b{position:absolute;left:460px;top:96px;width:300px;text-align:center;font-size:84px;line-height:1.1;color:#2fb36a}
.u{display:block;font-size:30px;letter-spacing:.12em;color:#466489;margin-top:4px}''',
BODY='''<div class="card" id="card"><div id="hd" class="lab">SAME TASK, WITH AI</div><div id="a">2<span class="u">HOURS</span></div><div id="ar">&#8594;</div><div id="b">30<span class="u">MINUTES</span></div></div>''',
JS='''gsap.set(["#a","#ar","#b"],{opacity:0});
IN("#card",0.0); POP("#a",0.67);
tl.fromTo("#ar",{opacity:0,x:-30},{opacity:1,x:0,duration:0.25,ease:"power3.out",immediateRender:false},1.45);
POP("#b",1.75);
OUT("#card",2.58);''')
