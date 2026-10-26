const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.argv[2] + '/flyer-delivery-driver.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log('fonts:', await p.evaluate(() => [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).join(',')));
  console.log('overflow:', await p.evaluate(() => { const pg=document.querySelector('.page'); return pg.scrollHeight - pg.clientHeight; }));
  await p.screenshot({ path: process.argv[2] + '/flyer-delivery-driver.png', fullPage: true });
  await p.pdf({ path: process.argv[2] + '/OF4S-Delivery-Driver-Flyer-A4.pdf', format: 'A4', printBackground: true });
  await b.close();
})();
