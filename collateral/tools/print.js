// Regenerate the wholesale catalog PDF from the HTML source.
// Usage: cd into collateral/ first (relative paths + relative image srcs
// depend on it), then: node tools/print.js
//
// Requires: /opt/node22/lib/node_modules/playwright (pre-installed),
// Chromium at /opt/pw-browsers/chromium-1194/chrome-linux/chrome
// (pre-installed, PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 — do not run
// `playwright install`).
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage();
  const filePath = 'file://' + path.resolve('of4s-wholesale-seating-catalog-2026.html');
  await page.goto(filePath, { waitUntil: 'networkidle', timeout: 60000 });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({
    path: 'of4s-wholesale-seating-catalog-2026.pdf',
    printBackground: true,
    preferCSSPageSize: false,
    width: '816px',
    height: '1056px',
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
  });
  await browser.close();
  console.log('done');
})();
