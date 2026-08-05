const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium',
    proxy: { server: process.env.HTTPS_PROXY },
  });
  const page = await browser.newPage();
  await page.goto('file://' + __dirname + '/postcard-draft-3.html', { waitUntil: 'load' });
  await page.waitForTimeout(1000);
  await page.evaluate(() => document.fonts.ready);
  await page.setViewportSize({ width: 1100, height: 1450 });
  await page.screenshot({ path: 'preview-draft-3.png', fullPage: true });
  await browser.close();
  process.exit(0);
})();
