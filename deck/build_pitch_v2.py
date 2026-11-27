#!/usr/bin/env python3
"""Build deck/pitch.html v2: the 8-slide OSME pitch as a brand launch, not a consulting deck.

One motion language for every slide (arc sweep, scent rise, steep reveal, count-ups,
ambient steam) lives here. Each slide is a fragment in deck/v2/sN.html; this script
stitches them, embeds every asset as a data URI and adds speaker notes from deck/script.md.

Fragment contract (deck/v2/sN.html):
- exactly one <div class="slide ..." id="sN" data-title="..." [data-steps="k"]> ... </div>
- optional <style> (scope selectors with #sN) and <script> (register hooks:
  window.ENTER[N] = el => {...}; window.LEAVE[N] = el => {...}; window.STEP[N] = (el, step) => {...})
- assets: __ASSET:path/from/repo__ becomes a data URI (svg, png, jpg, mp4, woff2)
- motion classes from the engine: .draw (SVG path with pathLength="1", draws on entry),
  .steep (children reveal blur to sharp with a stagger), [data-count] count-ups,
  .rv[data-s=k] click builds, .amb ambient layer, style="--dl:.6s" delays one element
- numbers: __NUM:key__ (price, cup, infusions, tin, ritual, cost1, cost3, margin, margin_pct, y3, share,
  sam, tam, rit_m, tins_m, ret_m, ritual_avg) and __LADDER_JSON__, all from model_business.py at PRICE
- an <aside class="notes"> with sources; the spoken script is added by this builder

Run: python3 deck/build_pitch_v2.py [--out /tmp/mine.html]   (default deck/pitch.html)
"""
import re
import sys

import json

import build_pitch as bp
import model_business as m

# The one price constant: switch the whole pitch to $2.00 here (team locked $1.50 at 10:23).
PRICE = m.PRICE

R, D = bp.R, bp.D
V2 = D / "v2"
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".mp4": "video/mp4", ".woff2": "font/woff2", ".webp": "image/webp", ".html": "text/html"}
FONTX = bp.b64(D / "assets-src" / "jost-latin-ext.woff2", "font/woff2")
TIMES = ["0:00 to 0:27", "0:27 to 0:45", "0:45 to 1:27", "1:27 to 1:42",
         "1:42 to 2:03", "2:03 to 2:17", "2:17 to 2:30", "2:30 to 2:50", "Q&A"]
TITLES = ["Company: the film", "Problem", "Solution, live demo", "Customer", "Market", "Business", "Competition", "The ask", "Backup: what is inside"]


def film_path():
    """Film v03 once the video thread logs it, else the current master file."""
    log = (R / "ops" / "log.md").read_text(encoding="utf8")
    v3 = R / "video" / "renders" / "osme-film_v03.mp4"
    if v3.exists() and re.search(r"video-lead \| (PREVIEW|DONE|PROGRESS)[^\n]*film[^\n]*v03", log):
        return "video/renders/osme-film_v03.mp4"
    return "video/osme-film.mp4"


def nums():
    """Number tokens __NUM:key__ for fragments, all computed from deck/model_business.py at PRICE."""
    w = m.walk(PRICE)
    c3 = m.cogs(3)
    return {
        "price": f"{PRICE:.2f}", "cup": f"{PRICE / m.INFUSIONS:.2f}", "infusions": str(m.INFUSIONS),
        "tin": f"{m.TIN_PRICE:.0f}", "ritual": f"{m.RITUAL_PRICE:.0f}",
        "cost3": f"{c3:.2f}", "cost1": f"{m.cogs(1):.2f}",
        "margin": f"{PRICE - c3:.2f}", "margin_pct": f"{(PRICE - c3) / PRICE * 100:.0f}",
        "y3": f"{w['total'] / 1e6:.1f}", "share": f"{w['share'] * 100:.1f}",
        "sam": f"{m.SAM / 1e6:.0f}", "tam": "7.1",
        "rit_m": f"{w['rev_ritual'] / 1e6:.1f}", "tins_m": f"{w['rev_tins'] / 1e6:.1f}", "ret_m": f"{w['rev_retail'] / 1e6:.1f}",
        "ritual_avg": f"{m.RITUAL_AVG / 1e3:.0f}", "end_y2": f"{m.END_Y2 / 1e3:.0f}", "end_y3": f"{m.END_Y3 / 1e3:.0f}",
        "tins_k": f"{m.TINS / 1e3:.0f}", "retail_bags": f"{m.RETAIL_BAGS / 1e6:.1f}",
        "buyers": f"{(m.END_Y3 + m.TINS) / 1e3:.0f}", "buyers_pct": f"{(m.END_Y3 + m.TINS) / 159e6 * 100:.1f}",
    }


def ladder_json():
    rows = [dict(name=n, cup=round(PRICE / m.INFUSIONS, 2) if n.startswith("OSME") else c, note=(f"${PRICE:.2f} a bag" if n.startswith("OSME") else t), label=l)
            for n, c, t, l in m.LADDER]
    return json.dumps(rows)


def asset(m):
    rel = m.group(1)
    if rel == "FILM":
        rel = film_path()
    p = R / rel
    if not p.exists():
        print("  missing asset:", rel, file=sys.stderr)
        return ""
    return bp.b64(p, MIME.get(p.suffix.lower(), "application/octet-stream"))


def fragment(n):
    p = V2 / f"s{n}.html"
    if p.exists():
        return p.read_text(encoding="utf8")
    return (f'<div class="slide" id="s{n}" data-title="{TITLES[n - 1]}"><div class="head"><div class="label">'
            f'Slide {n} · {TITLES[n - 1]}</div><div class="h1">In progress</div></div></div>')


def spoken(n):
    s = bp.script_lines().get(n, "")
    return f'<div class="spoken" hidden>{s}</div>'


CSS = r"""
@font-face{font-family:"Jost";src:url(__FONT__) format("woff2");font-weight:300 700;font-display:block}
@font-face{font-family:"Jost";src:url(__FONTX__) format("woff2");font-weight:300 700;unicode-range:U+0100-02BA,U+1E00-1EFF}
:root{
  --bg:#0B0B0D;--surface:#17171B;--line:#2A2A30;
  --amber:#F2A33A;--mid:#D9C46B;--jade:#3DBA9B;--text:#F3EEE6;--muted:#8E8A83;
  --arc:linear-gradient(90deg,#F2A33A 0%,#D9C46B 48%,#3DBA9B 100%);
  --ease:cubic-bezier(.2,.7,.3,1);--col:min(1240px,74vw);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;background:var(--bg);color:var(--text);font-family:"Jost","Futura","Avenir Next",sans-serif}
em{font-style:normal;color:var(--amber)}
.amber{color:var(--amber)}.jade{color:var(--jade)}.mid{color:var(--mid)}.muted{color:var(--muted)}

/* ambient: steam and bubble texture behind every slide, so no slide is flat black */
#ambient{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden}
#ambient .tex{position:absolute;inset:0;background:url(__PATTERN__) center/420px repeat;opacity:.035}
#ambient .st{position:absolute;width:70vw;height:70vw;border-radius:50%;filter:blur(90px);opacity:.16;mix-blend-mode:screen;animation:drift 26s ease-in-out infinite alternate}
#ambient .st.a{background:radial-gradient(circle,#F2A33A 0%,transparent 62%);left:-22vw;top:-30vw}
#ambient .st.b{background:radial-gradient(circle,#3DBA9B 0%,transparent 62%);right:-26vw;bottom:-36vw;animation-duration:31s;animation-delay:-9s}
#ambient .st.c{background:radial-gradient(circle,#D9C46B 0%,transparent 60%);left:30vw;top:40vh;width:40vw;height:40vw;opacity:.07;animation-duration:22s}
@keyframes drift{0%{transform:translate(0,0) scale(1)}50%{transform:translate(6vw,4vh) scale(1.12)}100%{transform:translate(-4vw,8vh) scale(.94)}}

/* slides */
.deck{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;opacity:0;pointer-events:none;display:flex;flex-direction:column;align-items:center;
  padding:6vh 72px 7vh;overflow:hidden;transition:opacity .3s var(--ease)}
.slide.active{opacity:1;pointer-events:auto}
.slide.full{padding:0}
.head{width:var(--col);flex:0 0 auto;position:relative;z-index:3}
.body{width:var(--col);flex:1;display:flex;flex-direction:column;justify-content:center;min-height:0;position:relative;z-index:3}
.label{font-size:20px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--amber);margin-bottom:14px}
.h1{font-size:clamp(34px,2.6vw,52px);font-weight:500;line-height:1.18;letter-spacing:-.005em;max-width:24em}
.lead{font-size:clamp(28px,1.75vw,34px);line-height:1.4;color:rgba(243,238,230,.84)}
.big{font-size:clamp(96px,9vw,180px);font-weight:500;line-height:.95;letter-spacing:-.02em}
.cap{font-size:clamp(22px,1.25vw,26px);color:var(--muted);line-height:1.4}
.amb{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;pointer-events:none}

/* motion 1: arc sweep, the signature; .draw paths need pathLength="1" */
.draw{stroke-dasharray:1;stroke-dashoffset:1}
.slide.play .draw{animation:drawin var(--d,1.4s) var(--ease) var(--dl,0s) both}
@keyframes drawin{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
.sig{position:absolute;left:50%;bottom:-38vh;width:120vw;height:70vh;transform:translateX(-50%);z-index:1;pointer-events:none;opacity:.55;overflow:visible}

/* motion 2: steep reveal, like tea into water: blur to sharp with a warm bleed */
.slide.play .steep>*{animation:steep .9s var(--ease) both;animation-delay:calc(var(--dl,0s) + var(--i,0) * 130ms)}
@keyframes steep{0%{opacity:0;filter:blur(14px) sepia(1) saturate(2.2) brightness(1.2);transform:translateY(22px)}
  60%{opacity:1;filter:blur(2px) sepia(.35) saturate(1.3)}100%{opacity:1;filter:none;transform:none}}
.rv{opacity:0;filter:blur(12px) sepia(1);transform:translateY(18px);transition:opacity .7s var(--ease),filter .9s var(--ease),transform .7s var(--ease)}
.rv.on{opacity:1;filter:none;transform:none}

/* chrome */
#bar{position:fixed;top:0;left:0;height:3px;background:var(--arc);width:0;transition:width .5s var(--ease);z-index:20}
#wipe{position:fixed;inset:0;z-index:15;pointer-events:none;opacity:0}
#wipe.go{animation:wipefade .75s ease both}
#wipe.go path{animation:drawin .6s var(--ease) both}
@keyframes wipefade{0%{opacity:0}15%{opacity:1}70%{opacity:1}100%{opacity:0}}
#dots{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:9px;z-index:20}
.dot{width:7px;height:7px;border-radius:50%;background:rgba(243,238,230,.22);cursor:pointer;transition:all .3s}
.dot.on{background:var(--amber);width:22px;border-radius:4px}
#snum{position:fixed;right:28px;bottom:18px;font-size:14px;color:rgba(243,238,230,.32);z-index:20;letter-spacing:.06em}
#brandmark{position:fixed;left:26px;bottom:16px;height:30px;opacity:.55;z-index:20}
body.s0 #brandmark,body.s2 #brandmark{opacity:0}
body.s2 #snum{opacity:0}
#timer{position:fixed;right:28px;top:20px;font-size:28px;font-variant-numeric:tabular-nums;padding:6px 16px;border-radius:12px;background:rgba(11,11,13,.7);border:1px solid var(--line);z-index:30;display:none}
#timer.on{display:block}#timer.low{color:var(--amber)}#timer.over{color:#ff6b5b}
#timer small{display:block;font-size:13px;color:var(--muted);letter-spacing:.08em}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:42vh;overflow:auto;background:rgba(11,11,13,.94);border-top:1px solid var(--line);
  padding:18px 72px 26px;font-size:20px;line-height:1.55;color:rgba(243,238,230,.9);z-index:40;display:none}
#notes.on{display:block}
#notes .nh{font-size:14px;letter-spacing:.18em;text-transform:uppercase;color:var(--amber);margin:6px 0}
#notes ul{padding-left:1.2em;color:var(--muted);font-size:16px}
#help{position:fixed;left:50%;top:20px;transform:translateX(-50%);background:rgba(11,11,13,.9);border:1px solid var(--line);border-radius:12px;padding:10px 18px;font-size:15px;color:var(--muted);z-index:40;display:none}
#help.on{display:block}
.arr{position:fixed;top:50%;width:40px;height:40px;border-radius:50%;border:1px solid var(--line);background:rgba(11,11,13,.5);color:var(--muted);font-size:22px;cursor:pointer;z-index:20;opacity:.0;transition:opacity .3s}
body:hover .arr{opacity:.6}#prev{left:18px}#next{right:18px}
.notes{display:none}

/* ?still: end state, for contact sheets */
html.still *{animation-duration:0s!important;animation-delay:0s!important;transition:none!important}
"""

JS = r"""
window.ENTER=window.ENTER||{};window.LEAVE=window.LEAVE||{};window.STEP=window.STEP||{};
const SLIDES=[...document.querySelectorAll('.deck > .slide')];
const N=SLIDES.length, TIMES=__TIMES__;
// backup slides sit after the close: reachable with the arrows, not counted in the pitch
const NM=SLIDES.filter(x=>!x.dataset.backup).length;
const STILL=/still/.test(location.search);
let cur=0, step=0;
const steps=i=>+(SLIDES[i].dataset.steps||0);
function paint(){
  SLIDES[cur].querySelectorAll('.rv').forEach(el=>el.classList.toggle('on',+el.dataset.s<=step));
  const f=STEP[cur+1];if(f)try{f(SLIDES[cur],step)}catch(e){console.error(e)}
}
/* count-ups: data-count="8.3" data-dec="1" data-prefix="$" data-suffix=" m" [data-dl=".4"] [data-dur="1.4"] */
function fmtNum(v,dec){return v.toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec})}
function countUp(el){
  const to=+el.dataset.count,dec=+(el.dataset.dec||0),pre=el.dataset.prefix||'',suf=el.dataset.suffix||'';
  const dur=(+(el.dataset.dur||1.4))*1000,dl=(+(el.dataset.dl||0))*1000,from=+(el.dataset.from||0);
  if(STILL){el.textContent=pre+fmtNum(to,dec)+suf;return;}
  el.textContent=pre+fmtNum(from,dec)+suf;
  const t0=performance.now()+dl;
  (function tick(t){const k=Math.min(1,Math.max(0,(t-t0)/dur)),e=1-Math.pow(1-k,3);
    el.textContent=pre+fmtNum(from+(to-from)*e,dec)+suf;if(k<1&&el.isConnected)el._raf=requestAnimationFrame(tick);})(performance.now());
}
function play(el){
  el.classList.remove('play');void el.offsetWidth;el.classList.add('play');
  el.querySelectorAll('.steep').forEach(g=>[...g.children].forEach((c,i)=>c.style.setProperty('--i',i)));
  el.querySelectorAll('[data-count]').forEach(c=>{if(!c.closest('.rv')||c.closest('.rv').classList.contains('on'))countUp(c)});
  el.querySelectorAll('video[data-auto]').forEach(v=>{try{v.currentTime=0;v.play()}catch(e){}});
}
function wipe(){if(STILL)return;const w=document.getElementById('wipe');w.classList.remove('go');void w.offsetWidth;w.classList.add('go');}
function goto(n,s){
  if(n<0||n>=N)return;
  const changed=n!==cur;
  if(changed){
    const old=SLIDES[cur];old.classList.remove('active');
    old.querySelectorAll('video[data-auto]').forEach(v=>{try{v.pause()}catch(e){}});
    const lf=LEAVE[cur+1];if(lf)try{lf(old)}catch(e){console.error(e)}
    wipe();
  }
  cur=n;step=Math.max(0,Math.min(s||0,steps(n)));
  const el=SLIDES[cur];el.classList.add('active');
  if(changed||!el.classList.contains('play')){play(el);const f=ENTER[cur+1];if(f)try{f(el)}catch(e){console.error(e)}}
  paint();ui();
}
function next(){ if(step<steps(cur)){step++;paint();countBuild();ui();} else goto(cur+1,0); }
function prev(){ if(step>0){step--;paint();ui();} else if(cur>0) goto(cur-1,steps(cur-1)); }
function countBuild(){SLIDES[cur].querySelectorAll('.rv[data-s="'+step+'"] [data-count], .rv[data-s="'+step+'"][data-count]').forEach(countUp);}
function ui(){
  document.getElementById('bar').style.width=(Math.min(cur+1,NM)/NM*100)+'%';
  document.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('on',i===cur));
  document.getElementById('snum').textContent=cur<NM?(cur+1)+' / '+NM+'  ·  '+TIMES[cur]:'Backup  ·  Q&A';
  document.body.className=document.body.className.replace(/\bs\d+\b/g,'').trim()+' s'+cur;
  const el=SLIDES[cur],nt=el.querySelector('.notes'),sp=el.querySelector('.spoken');
  document.getElementById('notes').innerHTML='<p class="nh">Slide '+(cur+1)+' · '+el.dataset.title+' · target '+TIMES[cur]+'</p>'
    +(sp?sp.innerHTML:'')+(nt?'<p class="nh">Sources and detail</p>'+nt.innerHTML:'');
  document.getElementById('tgt').textContent=cur<NM?'target '+TIMES[cur].split(' to ')[1]:'Q&A';
  history.replaceState(null,'','#'+(cur+1)+(step?'.'+step:''));
}
const dotsEl=document.getElementById('dots');
for(let i=0;i<NM;i++){const d=document.createElement('div');d.className='dot';d.onclick=e=>{e.stopPropagation();goto(i,0)};dotsEl.appendChild(d);}

/* presenter timer: T start/pause, Shift+T reset */
let tLeft=180,tRun=false,tLast=0;
function fmt(s){const neg=s<0;s=Math.abs(Math.round(s));return (neg?'+':'')+Math.floor(s/60)+':'+String(s%60).padStart(2,'0');}
function drawTimer(){const el=document.getElementById('tclock');el.textContent=fmt(tLeft);const t=document.getElementById('timer');t.classList.toggle('low',tLeft<=30&&tLeft>0);t.classList.toggle('over',tLeft<=0);}
function toggleTimer(reset){const t=document.getElementById('timer');t.classList.add('on');
  if(reset){tLeft=180;tRun=false;drawTimer();return;} tRun=!tRun;tLast=performance.now();drawTimer();}
(function tick(ts){if(tRun){tLeft-=(ts-tLast)/1000;tLast=ts;drawTimer();}requestAnimationFrame(tick);})(0);
window.DECK={next,prev,goto,toggleTimer,toggleNotes:()=>document.getElementById('notes').classList.toggle('on'),get cur(){return cur}};

/* keys: slide 3 hands Space, Enter and R to the live product (see deck/v2/s3.html) */
document.addEventListener('keydown',e=>{
  if(e.metaKey||e.ctrlKey||e.altKey)return;
  const k=e.key;
  if(window.DEMOKEY&&cur===2&&window.DEMOKEY(e))return;
  if(k==='ArrowRight'||k==='ArrowDown'||k===' '||k==='PageDown'||k==='Enter'){e.preventDefault();next();}
  else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev();}
  else if(k==='Home')goto(0,0);
  else if(k==='End')goto(NM-1,steps(NM-1));
  else if(k==='t'||k==='T')toggleTimer(e.shiftKey);
  else if(k==='n'||k==='N')DECK.toggleNotes();
  else if(k==='?'||k==='h'||k==='H')document.getElementById('help').classList.toggle('on');
  else if(/^[1-8]$/.test(k))goto(+k-1,0);
});
document.querySelector('.deck').addEventListener('click',e=>{if(e.target.closest('iframe,button,a,.noclick'))return;next();});

if(STILL)document.documentElement.classList.add('still');
(function(){
  const m=location.hash.match(/^#(\d+)(?:\.(\d+))?/);
  const n=m?Math.min(N,Math.max(1,+m[1]))-1:0,s=m&&m[2]?+m[2]:0;
  cur=n;SLIDES.forEach((x,i)=>{if(i!==n){x.style.transition='none';x.classList.remove('active');void x.offsetWidth;x.style.transition='';}});goto(n,s);
  if(!SLIDES[n].classList.contains('play')){play(SLIDES[n]);const f=ENTER[n+1];if(f)f(SLIDES[n]);}
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>OSME · every tea has its temperature</title>
<style>__CSS__</style>
<script>window.ENTER={};window.LEAVE={};window.STEP={};</script>
</head>
<body class="s0">
<div id="ambient"><div class="tex"></div><div class="st a"></div><div class="st b"></div><div class="st c"></div></div>
<div id="bar"></div>
<svg id="wipe" viewBox="0 0 1920 1080" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="wipeg" x1="0" x2="1"><stop offset="0" stop-color="#F2A33A"/><stop offset=".48" stop-color="#D9C46B"/><stop offset="1" stop-color="#3DBA9B"/></linearGradient></defs>
<path d="M -60 1140 A 1020 1020 0 0 1 1980 1140" pathLength="1" fill="none" stroke="url(#wipeg)" stroke-width="5" stroke-linecap="round" style="stroke-dasharray:1;stroke-dashoffset:1;filter:drop-shadow(0 0 18px rgba(242,163,58,.7))"/></svg>
<button class="arr" id="prev" onclick="DECK.prev()" aria-label="Previous">&#8249;</button>
<button class="arr" id="next" onclick="DECK.next()" aria-label="Next">&#8250;</button>
<div id="dots"></div>
<div id="snum"></div>
<img id="brandmark" src="__SYMSMALL__" alt=""/>
<div id="timer"><span id="tclock">3:00</span><small id="tgt"></small></div>
<div id="help">→ Space PageDown next · ← back · T timer · Shift+T reset · N notes · 1 to 8 jump · on slide 3: Space pours, R resets, PageDown next slide</div>
<div id="notes"></div>
<div class="deck">
__SLIDES__
</div>
<script>__JS__</script>
</body>
</html>
"""


def build():
    parts = []
    for n in range(1, len(TITLES) + 1):
        f = fragment(n)
        sp = spoken(n)
        # put the spoken script inside the slide div (before its last closing tag)
        i = f.rfind("</div>")
        f = f[:i] + sp + f[i:] if i >= 0 else f + sp
        parts.append(f"<!-- {n} · {TITLES[n - 1].upper()} -->\n" + f)
    slides = "\n".join(parts)
    # __SVG:path__ inlines an SVG file, so its SMIL runs on the page clock and can be replayed with setCurrentTime
    slides = re.sub(r"__SVG:([^_][^\s\"')]*?)__",
                    lambda mm: re.sub(r"^<\?xml[^>]*>\s*", "", (R / mm.group(1)).read_text(encoding="utf8")), slides)
    slides = re.sub(r"__ASSET:([^_][^\s\"')]*?)__", asset, slides)
    nm = nums()
    slides = re.sub(r"__NUM:(\w+)__", lambda x: nm[x.group(1)], slides)
    slides = slides.replace("__LADDER_JSON__", ladder_json())
    slides = slides.replace("__PRODUCT__", bp.html.escape((R / "product" / "index.html").read_text(encoding="utf8"), quote=True))
    if slides.count('class="slide') and slides.find('class="slide active') < 0:
        slides = slides.replace('class="slide', 'class="slide active', 1)
    css = (CSS.replace("__FONTX__", FONTX).replace("__FONT__", bp.FONT)
           .replace("__PATTERN__", bp.b64(R / "brand" / "assets" / "pattern-bubbles.svg", "image/svg+xml")))
    js = JS.replace("__TIMES__", str(TIMES).replace("'", '"'))
    small = R / "brand" / "identity" / "logo-symbol-small.svg"
    if not small.exists():
        small = R / "brand" / "identity" / "logo-symbol.svg"
    page = (PAGE.replace("__CSS__", css).replace("__SLIDES__", slides).replace("__JS__", js)
            .replace("__SYMSMALL__", bp.b64(small, "image/svg+xml")))
    return page


if __name__ == "__main__":
    page = build()
    out = D / "pitch.html"
    if "--out" in sys.argv:
        out = __import__("pathlib").Path(sys.argv[sys.argv.index("--out") + 1])
    out.write_text(page, encoding="utf8")
    print("wrote", out, len(page) // 1024, "KB")
