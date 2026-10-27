// Usage: node render_flyer.js <dir> <html file> <pdf name> <png prefix>
const { chromium } = require('playwright');
(async () => {
  const [d, html, pdf, png] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto(`file://${d}/${html}`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  console.log(html, 'overflow:', await p.evaluate(() => [...document.querySelectorAll('.page')].map(pg => pg.scrollHeight - pg.clientHeight)));
  const pages = await p.$$('.page');
  for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: `${d}/${png}-${i ? 'back-es' : 'front-en'}.png` });
  await p.pdf({ path: `${d}/${pdf}`, preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
