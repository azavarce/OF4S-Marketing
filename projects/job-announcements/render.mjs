import pw from "/opt/node22/lib/node_modules/playwright/index.js";
const { chromium } = pw;
import { fileURLToPath } from "node:url";
import path from "node:path";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
// Usage: node render.mjs [flyer.html] [output/Name.png]  (defaults render the BDM flyer)
const htmlArg = process.argv[2] || "flyer.html";
const outArg = process.argv[3] || "output/OF4S-Business-Development-Manager.png";
const htmlPath = path.isAbsolute(htmlArg) ? htmlArg : path.join(__dirname, htmlArg);
const outPath = path.isAbsolute(outArg) ? outArg : path.join(__dirname, outArg);

// 8.5in x 11in @ 300 DPI = 2550 x 3300 px. CSS page is 816 x 1056 @ 96 DPI.
const DSF = 300 / 96; // 3.125

const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const page = await browser.newPage({
  viewport: { width: 816, height: 1056 },
  deviceScaleFactor: DSF,
});
await page.goto("file://" + htmlPath, { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(200);

const el = await page.$(".page");
await el.screenshot({ path: outPath });

await browser.close();
console.log("wrote", outPath);
