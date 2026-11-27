#!/usr/bin/env python3
"""Export the site's best pieces as standalone 1920x1080 dark slides in shared/site/.

Each file is self-contained (embed-html) and scales to fit any window or iframe.
The pieces are the same components as the site (build.py), so they stay in step.
Run: python3 docs/_src/shared.py
"""
import os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

OUT = os.path.join(B.ROOT, "shared/site")

STAGE_CSS = """
html,body{height:100%;overflow:hidden;background:#0B0B0D}
body{display:grid;place-items:center}
.stage{width:1920px;height:1080px;flex:none;position:relative;overflow:hidden;transform-origin:center center;
  background:radial-gradient(ellipse 60% 70% at 70% 40%,rgba(242,163,58,.07),rgba(61,186,155,.035) 55%,transparent 80%),#0B0B0D}
.inner{zoom:var(--z,1.5);width:calc(1920px / var(--z,1.5));height:calc(1080px / var(--z,1.5));padding:0 56px;display:flex;flex-direction:column;justify-content:center}
.inner .eyebrow{font-size:12px}
.mark{position:absolute;right:56px;bottom:44px;height:44px;width:auto;opacity:.9}
section{border:0;padding:0}
"""

FIT_JS = """
function fit(){var s=document.querySelector('.stage');var k=Math.min(innerWidth/1920,innerHeight/1080);s.style.transform='scale('+k+')';}
addEventListener('resize',fit);fit();
"""

def stage(fname, title, inner, z=1.5, js="", mark=True):
    css = B.rd(B.SRC, "base.css") + B.rd(B.SRC, "shop.css") + STAGE_CSS
    logo = f'<svg class="mark" viewBox="{VBS["osme-lockup"]}" aria-label="OSME"><use href="#osme-lockup"/></svg>' if mark else ""
    doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · OSME shared</title>
<style>
@font-face{{font-family:"Jost";src:url(../../brand/assets/fonts/jost-latin.woff2) format("woff2");font-weight:300 700;font-display:block}}
{css}
</style></head>
<body>{LOGO_DEFS}
<div class="stage"><div class="inner" style="--z:{z}">{inner}</div>{logo}</div>
<script>(function(){{"use strict";
var reduce=false; var Q=new URLSearchParams(location.search);
{FIT_JS}
{js}
}})();</script>
</body></html>
'''
    p = os.path.join(OUT, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(doc)
    return p

# ---------------------------------------------------------------- the pieces
def hero_cup():
    inner = f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
  <div><div class="eyebrow"><b>Now</b> · the art, back in the bag</div>
  <h1 style="font-size:64px;line-height:1.02;margin:16px 0 20px">Every tea has<br><span class="arc-text">its temperature.</span></h1>
  <p class="oneliner">A tea bag that <em>opens only at its perfect temperature.</em></p>
  <p class="muted" style="margin-top:16px;font-size:15px">Sencha: opens at {B.deg(80)}, seals below {B.deg(70)} · cooling sped up</p></div>
  <div class="hero-visual">{B.rd(B.SRC, "hero-cup.svg")}</div>
</div>'''
    solo = f'<div class="hero-visual" style="width:560px;margin:0 auto">{B.rd(B.SRC, "hero-cup.svg")}</div>'
    js = B.rd(B.SRC, "hero.js")
    return [stage("hero-cup.html", "Hero cup with temperature arc", inner, 1.45, js),
            stage("hero-cup-solo.html", "Hero cup, cup only", solo, 1.6, js, mark=False)]

def timeline():
    inner = f'''<div class="eyebrow">Our story</div>
<h1 style="font-size:58px;margin:12px 0 10px">1,200 years of temperature.</h1>
<p class="lead" style="max-width:760px">Every great tea culture learned to read its water. The tea bag made tea easy and forgot the art. OSME brings the art back, inside the bag.</p>
<div class="timeline">
  <div class="tl"><div class="yr">760s</div><h3>Lu Yu reads the water</h3><p>China’s <em>Classic of Tea</em> judges water by its bubbles: three stages, three moments.</p></div>
  <div class="tl"><div class="yr">1908</div><h3>The tea bag trades art for ease</h3><p>One temperature, no stop, one cup. Today 96% of UK tea is brewed from a bag.</p></div>
  <div class="tl"><div class="yr arc-text">Now</div><h3>The art, back in the bag</h3><p>It opens at its tea’s temperature, closes when done, and keeps the scent.</p></div>
</div>'''
    return [stage("timeline.html", "1,200 years of temperature", inner, 1.55)]

def sealed_open_sealed():
    inner = f'''<div class="eyebrow">How it works · <b>Sencha</b>, Japan</div>
<h2 style="margin:12px 0 0">Sealed. Open. Sealed.</h2>
{B.three_steps().replace('margin-top:48px', '')}'''
    return [stage("sealed-open-sealed.html", "Sealed · Open · Sealed", inner, 1.42)]

def six_tins():
    tins = "".join(f'''<div style="text-align:center">{B.tin_svg(t).replace('viewBox="0 0 400 480"', 'viewBox="60 44 280 410"')}<div style="font-family:var(--font-display);font-size:19px;letter-spacing:.05em;margin-top:4px">{t["name"]}</div>
<div class="muted" style="font-size:13px">{t["country"]} · opens at {B.deg(t["open"])}</div></div>''' for t in B.TEAS)
    inner = f'''<div class="eyebrow">The teas</div>
<h2 style="margin:12px 0 26px">Six teas. Six temperatures.</h2>
<div style="display:grid;grid-template-columns:repeat(6,1fr);gap:22px">{tins}</div>'''
    return [stage("six-tins.html", "Six tinted tins", inner, 1.25)]

def slider():
    inner = f'''<div style="max-width:820px;margin:0 auto;width:100%">
<div class="panel" style="padding:40px">
  <div class="eyebrow">Try it · drag the water temperature</div>
  <input id="tSlider" type="range" min="60" max="100" step="1" value="68" aria-label="Water temperature in degrees Celsius">
  <div class="range-labels"><span>100&nbsp;°C</span><span>60&nbsp;°C</span></div>
  <div class="slider-row" style="margin-top:26px">
    <div class="readout" id="tRead">92<small>°C</small></div>
    <div><div class="sstate" id="tState">Sealed · too hot</div><div class="sdesc" id="tDesc"></div></div>
  </div>
</div>
<p class="muted" style="text-align:center;margin-top:14px;font-size:13px">Sencha · opens at {B.deg(80)}, seals below {B.deg(70)}</p></div>'''
    # ?auto sweeps 100 -> 60 -> 100 °C for recordings
    auto = '''
if (Q.has("auto")) { var s = document.getElementById("tSlider"), t0 = performance.now();
  (function step(now){ var ph = ((now - t0) / 9000) % 1, v = 100 - 40 * (ph < .5 ? ph * 2 : 2 - ph * 2);
    s.value = 160 - Math.round(v); s.dispatchEvent(new Event("input")); requestAnimationFrame(step); })(t0); }'''
    return [stage("slider.html", "Temperature slider", inner, 1.6, B.rd(B.SRC, "slider.js") + auto)]

def bubbles_row():
    row = [("#3DBA9B", 22, "Fish eyes", "the first small bubbles"), ("#D9C46B", 32, "String of pearls", "beads rising from the bottom"), ("#F2A33A", 44, "Rolling waves", "the full boil")]
    cells = "".join(f'''<div style="text-align:center"><div style="height:70px;display:grid;place-items:center"><i style="display:block;width:{d}px;height:{d}px;border-radius:50%;background:{c};box-shadow:0 0 {d}px {c}66"></i></div>
<div style="font-family:var(--font-display);font-size:22px;letter-spacing:.14em;text-transform:uppercase;margin-top:16px">{n}</div><div class="muted" style="font-size:14px;margin-top:4px">{s}</div></div>''' for c, d, n, s in row)
    inner = f'''<div style="text-align:center"><div class="eyebrow">Since the eighth century</div>
<p style="font-family:var(--font-display);font-size:46px;line-height:1.12;margin:16px 0 44px">Lu Yu read water by its bubbles.<br><span class="arc-text">OSME reads it for you.</span></p>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:30px;max-width:900px;margin:0 auto;position:relative">
<div style="position:absolute;left:16%;right:16%;top:35px;height:2px;background:var(--brand-arc);opacity:.5"></div>{cells}</div></div>'''
    return [stage("bubbles-row.html", "Lu Yu's three bubbles", inner, 1.45)]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    LOGO_DEFS, VBS = B.logo_symbols()
    B.LOGO_DEFS = LOGO_DEFS
    files = hero_cup() + timeline() + sealed_open_sealed() + six_tins() + slider() + bubbles_row()
    bad = 0
    for p in files:
        subprocess.run([B.EMBED, p], check=True, capture_output=True)
        r = subprocess.run([B.EMBED, "--check", p], capture_output=True, text=True)
        bad += r.returncode != 0
        print("OK  " if r.returncode == 0 else "FAIL", os.path.relpath(p, B.ROOT), os.path.getsize(p) // 1024, "KB", "" if r.returncode == 0 else r.stdout + r.stderr)
    sys.exit(1 if bad else 0)
