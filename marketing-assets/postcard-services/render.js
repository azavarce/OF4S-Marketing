const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    proxy: { server: process.env.HTTPS_PROXY },
  });
  const page = await browser.newPage();
  await page.goto('file://' + __dirname + '/postcard.html', { waitUntil: 'load' });
  await page.waitForTimeout(1500);
  const fontStatus = await page.evaluate(async () => {
    await document.fonts.ready;
    return Array.from(document.fonts).map(f => `${f.family} ${f.weight} ${f.status}`);
  });
  console.log(JSON.stringify(fontStatus, null, 2));
  await page.setViewportSize({ width: 1100, height: 1450 });
  await page.screenshot({ path: 'preview.png', fullPage: true });
  await browser.close();
  process.exit(0);
})();
