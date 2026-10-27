const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + d + '/flyer-delivery-driver.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('overflow:', await p.evaluate(() => [...document.querySelectorAll('.page')].map(pg => pg.scrollHeight - pg.clientHeight)));
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${d}/flyer-driver-${i ? 'back-es' : 'front-en'}.png` });
  await p.pdf({ path: d + '/OF4S-Delivery-Driver-Flyer-A4.pdf', format: 'A4', printBackground: true });
  await b.close();
})();
