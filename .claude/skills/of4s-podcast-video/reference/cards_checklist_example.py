cards={}
# 1 what "pro se" means
cards['r10prose']=dict(D=2.9,CSS='''#card{left:140px;top:1110px;width:800px;height:270px}
#t{position:absolute;left:0;width:800px;top:30px;text-align:center;font-size:96px;line-height:1}
#d1,#d2{position:absolute;left:0;width:800px;text-align:center;font-size:40px;color:#466489}
#d1{top:146px} #d2{top:198px}''',
BODY='''<div class="card" id="card"><div id="t" class="navy">PRO SE</div><div id="d1">No lawyer.</div><div id="d2">They represent themselves.</div></div>''',
JS='''gsap.set(["#t","#d1","#d2"],{opacity:0});
IN("#card",0.0); POP("#t",0.2); POP("#d1",1.6); POP("#d2",2.2);
OUT("#card",2.65);''')
# 2 200 pages that cost them nothing (+ "full of nonsense" stamp)
cards['r10pages']=dict(D=4.6,CSS='''#card{left:140px;top:1080px;width:800px;height:330px}
#stack{position:absolute;left:60px;top:46px;width:200px;height:240px}
.pg{position:absolute;width:150px;height:196px;background:#fff;border:5px solid #15273f;border-radius:6px}
.pg i{position:absolute;left:22px;right:22px;height:6px;border-radius:3px;background:#8fa9c7}
#n{position:absolute;left:320px;top:40px;font-size:112px;line-height:1}
#nl{position:absolute;left:326px;top:150px;font-size:30px;letter-spacing:.12em;color:#466489}
#c{position:absolute;left:326px;top:206px;font-size:52px}
#stamp{position:absolute;left:300px;top:118px;padding:6px 20px;border:7px solid #d64545;border-radius:12px;color:#d64545;font-size:40px;letter-spacing:.06em;transform:rotate(-8deg);background:rgba(250,248,244,.9)}''',
BODY='''<div class="card" id="card"><div id="stack"></div><div id="n" class="navy">0</div><div id="nl">PAGE BRIEFS</div><div id="c" class="navy">Cost them: <span class="green">$0</span></div></div>''',
JS='''const st=document.getElementById("stack");
for(let i=0;i<5;i++){st.insertAdjacentHTML("beforeend",'<div class="pg" style="left:'+(i*10)+'px;top:'+(36-i*9)+'px"><i style="top:40px"></i><i style="top:70px"></i><i style="top:100px;right:50px"></i><i style="top:130px"></i></div>');}
gsap.set(".pg",{opacity:0,y:30}); gsap.set(["#nl","#c"],{opacity:0});
IN("#card",0.0);
tl.to(".pg",{opacity:1,y:0,duration:0.18,stagger:0.12,ease:"back.out(2)"},0.35);
const o={v:0}; tl.to(o,{v:200,duration:0.7,ease:"power2.out",onUpdate:()=>{document.getElementById("n").textContent=Math.round(o.v)}},0.42);
tl.to("#nl",{opacity:1,duration:0.2},0.5);
POP("#c",3.25);
OUT("#card",4.38);''')
# 3 closing checklist: NO background, white text + soft shadow, green checks, one at a time
cards['r10check']=dict(D=5.1,CSS='''@font-face{font-family:"SGB";font-weight:700;src:url("assets/schibsted-grotesk-latin-700-normal.woff") format("woff");}
.cl{position:absolute;left:170px;height:96px;display:flex;align-items:center;font-family:"SGB";font-weight:700;font-size:60px;color:#faf8f4;text-shadow:0 4px 16px rgba(0,0,0,.55),0 1px 3px rgba(0,0,0,.4);white-space:nowrap}
.cl svg{width:62px;height:62px;margin-right:26px;filter:drop-shadow(0 3px 8px rgba(0,0,0,.4))}
#hd{position:absolute;left:170px;top:1060px;font-family:"SGB";font-weight:700;font-size:32px;letter-spacing:.14em;color:#dde5ee;text-shadow:0 3px 10px rgba(0,0,0,.6)}
#l1{top:1110px} #l2{top:1206px}''',
BODY='''<div id="hd">JUDGES ARE NOW</div>
<div class="cl" id="l1"><svg viewBox="0 0 62 62"><circle cx="31" cy="31" r="29" fill="#2fb36a"/><path d="M17,32 L27,42 L46,21" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>Sanctioning them</div>
<div class="cl" id="l2"><svg viewBox="0 0 62 62"><circle cx="31" cy="31" r="29" fill="#2fb36a"/><path d="M17,32 L27,42 L46,21" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>Dismissing cases faster</div>''',
JS='''gsap.set([".cl","#hd"],{opacity:0});
tl.to("#hd",{opacity:1,duration:0.25},0.3);
[["#l1",0.52],["#l2",3.6]].forEach(([s,t])=>tl.fromTo(s,{opacity:0,x:-40},{opacity:1,x:0,duration:0.3,ease:"power3.out",immediateRender:false},t));
tl.to([".cl","#hd"],{opacity:0,duration:0.2},4.85);''')
