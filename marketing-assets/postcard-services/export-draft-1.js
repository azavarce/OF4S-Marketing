const { chromium } = require('playwright');

async function exportPanel(page, selector, outPath) {
  await page.evaluate((sel) => {
    document.querySelectorAll('.card').forEach(c => c.style.display = 'none');
    document.querySelectorAll('.panel-label').forEach(c => c.style.display = 'none');
    const target = document.querySelector(sel);
    target.style.display = 'block';
    target.classList.remove('guides');
    document.body.style.background = 'white';
    document.body.style.padding = '0';
    document.body.style.margin = '0';
    target.style.boxShadow = 'none';
    target.style.margin = '0';
  }, selector);

  await page.pdf({
    path: outPath,
    width: '10.25in',
    height: '5.25in',
    printBackground: true,
    margin: { top: '0in', bottom: '0in', left: '0in', right: '0in' },
  });
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  await page.goto('file://' + __dirname + '/postcard-draft-1.html', { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);

  await exportPanel(page, '.card.front', 'postcard-draft-1-front-print.pdf');

  await page.goto('file://' + __dirname + '/postcard-draft-1.html', { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  await exportPanel(page, '.card.back', 'postcard-draft-1-back-print.pdf');

  await browser.close();
  console.log('done');
  process.exit(0);
})();
