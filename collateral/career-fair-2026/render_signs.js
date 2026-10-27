const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  for (const v of ['original', 'A', 'B']) {
    const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
    await p.goto(`file://${d}/sign-${v}.html`, { waitUntil: 'networkidle' });
    await p.waitForSelector('body[data-fitted]', { timeout: 5000 });
    console.log(v, 'overflow:', await p.evaluate(() => { const pg = document.querySelector('.page'); return pg.scrollHeight - pg.clientHeight; }));
    await p.locator('.page').screenshot({ path: `${d}/sign-${v}.png` });
    await p.pdf({ path: `${d}/OF4S-Now-Hiring-Sign-${v}-A4.pdf`, format: 'A4', printBackground: true });
    await p.close();
  }
  await b.close();
})();
