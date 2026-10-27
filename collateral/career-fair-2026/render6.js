const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
  await p.goto('file://' + d + '/signup-sheet-letter.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('fonts:', await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).join(',')));
  console.log('overflow:', await p.evaluate(() => { const o=[]; const s=document.querySelector('.page'); o.push(s.scrollHeight-s.clientHeight); document.querySelectorAll('.page,table').forEach(e=>o.push(e.scrollHeight-e.clientHeight, e.scrollWidth-e.clientWidth)); return o.join(','); }));
  await p.locator(".page").screenshot({ path: d + '/signup-sheet-letter.png' });
  await p.pdf({ path: d + '/OF4S-Signup-Sheet-Letter.pdf', format: "Letter", printBackground: true });
  await b.close();
})();
