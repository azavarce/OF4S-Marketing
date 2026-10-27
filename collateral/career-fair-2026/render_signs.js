const { chromium } = require('playwright');
(async () => {
  const d = process.argv[2];
  const b = await chromium.launch();
  for (const v of ['original', 'A', 'B', 'es-landscape', 'en-landscape']) {
    const p = await b.newPage({ viewport: { width: 1123, height: 1123 }, deviceScaleFactor: 2 });
    await p.goto(`file://${d}/sign-${v}.html`, { waitUntil: 'networkidle' });
    await p.waitForSelector('body[data-fitted]', { timeout: 5000 });
    console.log(v, 'overflow:', await p.evaluate(() => [...document.querySelectorAll('.page')].map(pg => pg.scrollHeight - pg.clientHeight)));
    const pages = await p.$$('.page');
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${d}/sign-${v}${i ? '-p' + (i + 1) : ''}.png` });
    await p.pdf({ path: `${d}/OF4S-Now-Hiring-Sign-${v}-A4.pdf`, preferCSSPageSize: true, printBackground: true });
    await p.close();
  }
  await b.close();
})();
