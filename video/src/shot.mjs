// shot.mjs <page.html> <out.png> [width] [height]: one full-page screenshot with headless Chrome.
import { chromium } from '/Users/maurits.visser/Movies/fsm-upgrade-build/hero-v8/proofhtml/node_modules/playwright-core/index.mjs';
import { mkdtempSync } from 'node:fs'; import { tmpdir, homedir } from 'node:os'; import path from 'node:path';
const [html, out, w = '2400', h = '1400'] = process.argv.slice(2);
const exe = path.join(homedir(), 'Library/Caches/ms-playwright/chromium-1254/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
const ctx = await chromium.launchPersistentContext(mkdtempSync(path.join(tmpdir(), 'osme-shot-')), { executablePath: exe, headless: true,
  viewport: { width: +w, height: +h }, args: ['--use-mock-keychain', '--password-store=basic', '--allow-file-access-from-files'] });
const page = ctx.pages()[0] || await ctx.newPage();
await page.goto('file://' + path.resolve(html)); await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: out, fullPage: true }); await ctx.close();
