import sys, pathlib
S = pathlib.Path(sys.argv[1])

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>OF4S Now Hiring Sign</title>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --navy-800:#15273f; --navy-300:#8fa9c7; --paper-50:#faf8f4;
    --display:'Schibsted Grotesk','Geist',sans-serif;
    --sans:'Geist',system-ui,sans-serif;
    --mono:'Geist Mono',Menlo,monospace;
  }
  @page { size: A4; margin: 0; }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { background: var(--navy-800); }
  body { font-family: var(--sans); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  em { font-style: normal; color: var(--navy-300); }

  /* Headline on top, logo at the bottom. The bottom padding keeps the logo
     clear of a sign holder's front lip. */
  .page { width: 210mm; height: 297mm; overflow: hidden; display: flex; flex-direction: column; background: var(--navy-800); color: var(--paper-50); padding: 16mm 15mm 26mm; }
  .heads { flex: 1; display: flex; flex-direction: column; }
  h1 { font-family: var(--display); font-weight: 800; line-height: 0.86; letter-spacing: -0.045em; }
  .rule { height: 4px; width: 48px; background: var(--navy-300); }
  .foot { padding-top: 10mm; border-top: 1px solid rgba(143,169,199,0.35); }
  .brand { font-family: var(--display); font-weight: 700; font-size: 64px; letter-spacing: -0.02em; line-height: 1; }
  .brand .four { color: var(--navy-300); font-weight: 600; }
  .brand-cap { font-family: var(--mono); font-size: 13px; letter-spacing: 0.22em; text-transform: uppercase; color: var(--navy-300); margin-top: 10px; }
%s
</style>
</head>
<body>
<div class="page">
  <div class="heads">
%s
  </div>
  <footer class="foot">
    <div class="brand">OF<span class="four">4</span>S</div>
    <div class="brand-cap">Office Furniture 4 Sale · Since 2005</div>
  </footer>
</div>
%s
</body>
</html>
"""

FIT = """<script>
  // Size each headline line so it spans the full content width.
  document.fonts.ready.then(() => {
    const target = document.querySelector('.heads').clientWidth;
    document.querySelectorAll('h1 span').forEach(el => {
      el.style.fontSize = '100px';
      el.style.fontSize = (100 * target / el.getBoundingClientRect().width) + 'px';
    });
    document.body.dataset.fitted = '1';
  });
</script>"""
DONE = "<script>document.fonts.ready.then(() => { document.body.dataset.fitted = '1'; });</script>"

variants = {
  # Original: big English headline, Spanish as a smaller line under it.
  "original": ("""  .heads { gap: 12mm; }
  h1 { font-size: 244px; }
  .sub { font-family: var(--display); font-size: 52px; font-weight: 600; letter-spacing: -0.02em; color: var(--navy-300); display: flex; align-items: center; gap: 18px; }
  .sub::before { content: ""; width: 48px; height: 4px; background: var(--navy-300); }""",
   """    <h1 lang="en">Now<br><em>Hiring</em></h1>
    <div class="sub" lang="es">Estamos contratando</div>""", DONE),
  # A: every line stretched to the full width.
  "A": ("""  .heads { gap: 9mm; }
  h1 span { display: block; white-space: nowrap; width: max-content; }""",
   """    <h1 lang="en"><span>Now</span><em><span>Hiring</span></em></h1>
    <div class="rule"></div>
    <h1 lang="es"><span>Estamos</span><em><span>contratando</span></em></h1>""", FIT),
  # B: all four lines the same size (limited by "contratando").
  "B": ("""  .heads { gap: 12mm; }
  h1 { font-size: 98px; }""",
   """    <h1 lang="en">Now<br><em>Hiring</em></h1>
    <div class="rule"></div>
    <h1 lang="es">Estamos<br><em>contratando</em></h1>""", DONE),
}

for name, (css, body, script) in variants.items():
    (S / f"sign-{name}.html").write_text(HEAD % (css, body, script))
