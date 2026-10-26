const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + d + '/sign-now-hiring.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('overflow:', await p.evaluate(() => { const pg=document.querySelector('.page'); return pg.scrollHeight - pg.clientHeight; }));
  await p.locator('.page').screenshot({ path: d + '/sign-now-hiring.png' });
  await p.pdf({ path: d + '/OF4S-Now-Hiring-Sign-A4.pdf', format: 'A4', printBackground: true });
  await b.close();
})();
