const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1123, height: 794 }, deviceScaleFactor: 2 });
  await p.goto('file://' + d + '/table-tent-scan-to-apply.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('fonts:', await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).join(',')));
  console.log('overflow:', await p.evaluate(() => { const o=[]; const s=document.querySelector('.sheet'); o.push(s.scrollHeight-s.clientHeight); document.querySelectorAll('.panel,.jobs,.job,.lead').forEach(e=>o.push(e.scrollHeight-e.clientHeight, e.scrollWidth-e.clientWidth)); return o.join(','); }));
  await p.locator('.sheet').screenshot({ path: d + '/table-tent-scan-to-apply.png' });
  await p.pdf({ path: d + '/OF4S-Scan-to-Apply-Table-Tent-A4.pdf', format: 'A4', landscape: true, printBackground: true });
  await b.close();
})();
