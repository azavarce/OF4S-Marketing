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
exec(open(S+'/R8/cards/cards8.py').read())
only=sys.argv[1:] or list(cards)
for name in only:
    c=cards[name]; d=f"{S}/hf/{name}"
    if not os.path.exists(d): shutil.copytree(S+'/hf/r6money',d,ignore=shutil.ignore_patterns('index*.html','render.log'))
    h=HEAD.replace('%CSS%',c['CSS']).replace('%BODY%',c['BODY']).replace('%JS%',c['JS']).replace('%D%',str(c['D']))
    open(d+'/index.html','w').write(h); print('wrote',name)
