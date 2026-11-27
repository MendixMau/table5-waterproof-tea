// render.mjs <page.html> <out.mp4|stills-dir> [--stills t1,t2,...] [--crf N] [--dur S]
// Renders an HTML page frame by frame (window.setT) into ffmpeg: 1920x1080, 30 fps, H.264, BT.709.
// Injects the CURRENT logo files from brand/identity/ at render time (logo v4 lands under the same names).
import { chromium } from '/Users/maurits.visser/Movies/fsm-upgrade-build/hero-v8/proofhtml/node_modules/playwright-core/index.mjs';
import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { tmpdir, homedir } from 'node:os';
import path from 'node:path';

const here = path.dirname(new URL(import.meta.url).pathname);
const repo = path.resolve(here, '../..');
const [html, out] = process.argv.slice(2);
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d };
const FPS = 30, CRF = arg('--crf', '16'), STILLS = arg('--stills', null);
const exe = path.join(homedir(), 'Library/Caches/ms-playwright/chromium-1254/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
const ctx = await chromium.launchPersistentContext(mkdtempSync(path.join(tmpdir(), 'osme-video-')), {
  executablePath: exe, headless: true, viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1,
  args: ['--use-mock-keychain', '--password-store=basic', '--allow-file-access-from-files'] });
const page = ctx.pages()[0] || await ctx.newPage();
await page.goto('file://' + path.resolve(html));
await page.evaluate(() => document.fonts.ready);
console.log('Jost:', await page.evaluate(() => document.fonts.check('500 40px Jost')));
const logo = f => readFileSync(path.join(repo, 'brand/identity', f), 'utf8');
const info = await page.evaluate(([s, w]) => window.loadLogos ? window.loadLogos(s, w) : null, [logo('logo-symbol.svg'), logo('logo-wordmark.svg')]);
console.log('logos:', JSON.stringify(info));
const DUR = Number(arg('--dur', await page.evaluate(() => window.DUR)));
const shot = async t => { await page.evaluate(t => window.setT(t), t); return page.screenshot({ type: 'png' }) };
if (STILLS) {
  mkdirSync(out, { recursive: true });
  for (const t of STILLS.split(',').map(Number)) writeFileSync(path.join(out, `f_${t.toFixed(2)}.png`), await shot(t));
} else {
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-c:v', 'png', '-r', String(FPS), '-i', '-',
    '-vf', 'scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', CRF, '-tune', 'film', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
    '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
    '-r', String(FPS), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const N = Math.round(DUR * FPS);
  for (let n = 0; n < N; n++) { const b = await shot(n / FPS); if (!ff.stdin.write(b)) await new Promise(r => ff.stdin.once('drain', r)) }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); console.log(out, DUR, 's', N, 'frames');
}
await ctx.close(); process.exit(0);
