// Screenshot a single page of the catalog PDF (via the built-in PDF.js
// viewer) for visual verification after an edit.
// Usage: node tools/pdfshot_page.js <pageNum> <outputPngPath>
// Run from anywhere; paths below are absolute.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

(async () => {
  const pageNum = process.argv[2] || '1';
  const outPath = process.argv[3] || `/tmp/pdf-page-${pageNum}.png`;
  const pdfPath = path.resolve(__dirname, '..', 'of4s-wholesale-seating-catalog-2026.pdf');

  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1000, height: 1300 } });
  await page.goto(`file://${pdfPath}#page=${pageNum}`, { waitUntil: 'load', timeout: 30000 });
  // Larger PDFs take longer to render in the viewer — tune this if screenshots come back blank/loading.
  await page.waitForTimeout(2500);
  await page.screenshot({ path: outPath });
  await browser.close();
  console.log('saved', outPath);
})();
