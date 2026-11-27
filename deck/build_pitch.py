#!/usr/bin/env python3
"""Build deck/pitch.html: the OSME 8-slide pitch.

Engine forked from ~/Mendix/KT-POC-1146version/design/presentation.html (copy in
deck/_engine-kt-presentation.html; the original is never touched). Restyled to the
Midnight Brew tokens. Every build re-reads the latest logos from brand/identity/,
the live product from product/index.html and the spoken lines from deck/script.md.

Run: python3 deck/build_pitch.py
"""
import base64, html, pathlib, re

R = pathlib.Path(__file__).resolve().parent.parent
D = R / "deck"


def b64(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def logo(name):
    """Latest logo file from brand/identity (logo v4 lands there)."""
    p = R / "brand" / "identity" / name
    return b64(p, "image/svg+xml")


FONT = b64(D / "assets-src" / "jost-latin.woff2", "font/woff2")
LOCKUP = logo("logo-lockup.svg")
SYMBOL = logo("logo-symbol.svg")
PRODUCT = html.escape((R / "product" / "index.html").read_text(encoding="utf8"), quote=True)


def script_lines():
    """Spoken lines per slide from deck/script.md (blocks headed '... · Slide N ...')."""
    p = D / "script.md"
    out = {}
    if not p.exists():
        return out
    txt = p.read_text(encoding="utf8")
    body = txt.split("## Numbers and sources")[0]
    blocks = re.split(r"\n(?=\*\*[^\n]*Slide)", body)
    for b in blocks:
        m = re.match(r"\*\*([^\n]*?)Slides? ([\d](?:\s*(?:and|,|&)\s*\d)*)[^\n]*\*\*", b)
        if not m:
            continue
        nums = [int(x) for x in re.findall(r"\d", m.group(2))]
        head = re.sub(r"\*\*", "", b.split("\n", 1)[0]).strip()
        lines = b.split("\n", 1)[1].strip() if "\n" in b else ""
        lines = re.sub(r"\*\*|\*|_", "", lines)
        chunk = f"<p class='nh'>{html.escape(head)}</p>" + "".join(
            f"<p>{html.escape(l.strip())}</p>" for l in lines.split("\n") if l.strip())
        for n in nums:
            out[n] = out.get(n, "") + chunk
    return out


SPOKEN = script_lines()

# Sources per slide: every number on a slide, where it comes from.
SOURCES = {
    1: ["Name and one-liner: facts.md (Name), brand/strategy.md §2 one-liner 1, tagline 1.",
        "Lu Yu, Classic of Tea, written 760 to 762 CE: truth/history-cultures.md §2 (Wikipedia, The Classic of Tea).",
        "Three boils 'fish eyes, string of pearls, rolling waves': facts.md (Lu Yu's stages), our rendering of Okakura, The Book of Tea (1906), ch. II."],
    2: ["760: Lu Yu's Classic of Tea, truth/history-cultures.md §2.",
        "1500s: Sen no Rikyū (1522 to 1591), chanoyu, history-cultures.md §1 and §7.",
        "c. 1840: afternoon tea, Anna Maria, Duchess of Bedford, history-cultures.md §1.",
        "About 1908: Thomas Sullivan's silk tea bags, history-cultures.md §4 (Wikipedia, Tea bag).",
        "96%: 'Over 96 per cent of tea in Britain is now made with teabags', QMUL 2016, history-cultures.md §4.",
        "Bitter green tea: The Tea Spot side-by-side test, boiling version 'noticeably more bitter', truth/customers-market.md §1."],
    3: ["Sencha: opens at 80 °C, seals again below 70 °C: facts.md (Demo tea). Sencha 80 °C, 1 min: history-cultures.md §1.",
        "Up to 3 infusions per bag: facts.md (Price).",
        "Principle: PNIPAm-grafted membranes open and close with temperature, 5 clean cycles (PMC9920928), history-cultures.md §6. Plain PNIPAm switches at 32 °C; making it food-safe at 70 to 90 °C is our R&D (facts.md R&D framing).",
        "Demo keys: D full screen demo, Space pours, R resets, arrows change tea, Esc back to the deck."],
    4: ["Quotes verbatim (HN edited for language): truth/customers-market.md §1. weland, Hacker News https://news.ycombinator.com/item?id=7725580 ; hopeofdawn and silversun, TeaChat https://www.teachat.com/viewtopic.php?p=212298",
        "16% of UK tea drinkers brew black tea loose leaf (UKTIA 2024): customers-market.md §2 https://www.teaandcoffee.net/?p=34292",
        "Segment: curious specialty drinkers, 25 to 45, loose leaf, matcha, origin teas: facts.md (Customer) and customers-market.md §2 A."],
    5: ["TAM $7.1 bn = $18.77 bn global tea (Fortune BI 2025) x 38% bag share: truth/business-case.md §1, facts.md (Market).",
        "SAM $640 m = $7.1 bn x 45% (four first markets, ASSUMPTION) x 20% (premium share, ASSUMPTION): business-case.md §1.",
        "SOM $9 m in year 3 = 6.5 m bags x $1.38 average net price: business-case.md §1 and §4. Shown as 20 k Ritual subscribers at end of year 3 (business-case.md §4) x $24 x 12 = $5.76 m, the rest from tins and retail.",
        "Do not mix in the $39 bn specialty figure (different scope): facts.md."],
    6: ["$18 tin of 12, $24 a month Ritual, up to 3 infusions so about $0.50 a cup: facts.md (Price).",
        "62% gross margin direct: COGS midpoint $0.57 vs $1.50 a bag, business-case.md §3 (ASSUMPTION ranges). $11 margin a tin = $18 x 62%.",
        "Sips By about $1 a cup: customers-market.md §5. Tea Forte $1.30 per infuser (20 for $26), one cup: customers-market.md §5.",
        "Retail ~30% of year-3 sales: business-case.md §4."],
    7: ["Tea Forte pyramid infusers: customers-market.md §4 and §5.",
        "Nestlé Special.T: machine €129, pods €0.35: customers-market.md §4 (New Atlas).",
        "Loose leaf and gongfu: needs timer, thermometer, skill: customers-market.md §4.",
        "Teforia ($649 to $1,000 smart infuser) shut down in 2017: the lesson that hardware which needs explaining dies (customers-market.md §4)."],
    8: ["$2.5 m on a SAFE at a $10 m pre-money valuation: facts.md (The ask), business-case.md §5.",
        "Use of funds 35 / 15 / 30 / 15 / 5%: business-case.md §5.",
        "Milestones Q2 2027 lab prototype at 80 °C, Q2 2028 food-contact certification, Q3 2028 D2C launch UK and US: business-case.md §4.",
        "Close: brand/strategy.md §2 tagline and §4 call to action.",
        "Proven / not yet: PNIPAm-grafted membranes gate at 32 °C over 5 cycles, PMC9920928 (truth/history-cultures.md §6); food-safe 70 to 90 °C is R&D (facts.md R&D framing)."],
}


def notes(n):
    spoken = SPOKEN.get(n, "<p class='nh'>Script</p><p>(deck/script.md not parsed yet)</p>")
    src = "".join(f"<li>{html.escape(s)}</li>" for s in SOURCES[n])
    return f"<aside class='notes'>{spoken}<p class='nh'>Sources</p><ul>{src}</ul></aside>"


CSS = r"""
@font-face{font-family:"Jost";src:url(__FONT__) format("woff2");font-weight:300 700;font-display:block}
:root {
  /* Midnight Brew (brand/identity/tokens.css) */
  --bg:#0B0B0D; --surface:#17171B; --line:#2A2A30;
  --amber:#F2A33A; --mid:#D9C46B; --jade:#3DBA9B;
  --text:#F3EEE6; --muted:#8E8A83;
  --arc:linear-gradient(90deg,#F2A33A 0%,#D9C46B 48%,#3DBA9B 100%);
  --font:"Jost","Futura","Century Gothic","Avenir Next",sans-serif;
  --dur:300ms; --ease:cubic-bezier(.2,.7,.3,1);
  --col:min(1240px,70vw);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;font-family:var(--font);background:var(--bg);color:var(--text)}

/* engine (KT presentation.html) */
.deck{width:100vw;height:100vh;position:relative}
.slide{position:absolute;inset:0;opacity:0;pointer-events:none;display:flex;flex-direction:column;align-items:center;
  padding:5.2vh 72px 6vh;overflow:hidden;transition:opacity var(--dur) var(--ease),transform var(--dur) var(--ease);transform:translateY(20px)}
.slide.active{opacity:1;pointer-events:auto;transform:translateY(0)}
.slide.out{opacity:0;transform:translateY(-20px)}
.slide.cover{justify-content:center}
.head{width:var(--col);flex:0 0 auto}
.body{width:var(--col);flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:3vh;min-height:0}

/* chrome */
#bar{position:fixed;top:0;left:0;height:3px;background:var(--arc);width:0%;transition:width .4s var(--ease);z-index:100}
#dots{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:8px;z-index:100}
.dot{width:6px;height:6px;border-radius:50%;background:rgba(243,238,230,.2);cursor:pointer;transition:background .2s,transform .2s}
.dot.on{background:var(--amber);transform:scale(1.4)}
.arr{position:fixed;top:50%;transform:translateY(-50%);background:rgba(243,238,230,.04);border:1px solid rgba(243,238,230,.1);color:rgba(243,238,230,.45);font-size:18px;width:40px;height:40px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:100;backdrop-filter:blur(6px);font-family:var(--font)}
.arr:hover{background:rgba(243,238,230,.12);color:var(--text)}
#prev{left:18px}#next{right:18px}
#snum{position:fixed;bottom:20px;right:24px;font-size:12px;color:rgba(243,238,230,.3);z-index:100;letter-spacing:.08em}
#brandmark{position:fixed;bottom:16px;left:24px;height:22px;opacity:.55;z-index:100}
body.s0 #brandmark{opacity:0}

/* backgrounds, rotated per slide */
.bg-dark{background:var(--bg)}
.bg-night{background:#08080A}
.bg-mesh{background:#070708;background-image:radial-gradient(ellipse 55% 50% at 20% 38%,rgba(242,163,58,.13) 0%,transparent 70%),radial-gradient(ellipse 50% 55% at 82% 64%,rgba(61,186,155,.10) 0%,transparent 70%)}
.bg-grid{background:#09090B;background-image:linear-gradient(rgba(243,238,230,.028) 1px,transparent 1px),linear-gradient(90deg,rgba(243,238,230,.028) 1px,transparent 1px);background-size:40px 40px}
.bg-warm{background:linear-gradient(135deg,#16100A 0%,#0B0B0D 62%)}

/* type */
.label{font-size:13px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--amber);margin-bottom:12px}
.label .tt{color:var(--muted);letter-spacing:.18em}
.h1{font-size:clamp(22px,2.05vw,40px);font-weight:500;line-height:1.22;letter-spacing:-.005em;max-width:30em}
.cap{font-size:clamp(14px,.95vw,18px);line-height:1.5;color:var(--muted)}
.sm{font-size:clamp(15px,1vw,19px);line-height:1.55;color:rgba(243,238,230,.72)}
em{font-style:normal;color:var(--amber)}
.jade{color:var(--jade)} .amber{color:var(--amber)} .muted{color:var(--muted)}
.row{display:flex;align-items:center}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:22px}
.card{background:rgba(243,238,230,.04);border:1px solid rgba(243,238,230,.09);border-radius:16px;padding:26px 28px;backdrop-filter:blur(4px)}
.chip{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;padding:6px 14px;border-radius:999px;border:1px solid rgba(243,238,230,.14);color:rgba(243,238,230,.75)}
.chip.a{border-color:rgba(242,163,58,.45);color:var(--amber);background:rgba(242,163,58,.07)}
.chip.j{border-color:rgba(61,186,155,.45);color:var(--jade);background:rgba(61,186,155,.07)}
.chip.g{border-color:rgba(217,196,107,.45);color:var(--mid);background:rgba(217,196,107,.07)}
.big{font-weight:500;line-height:.95;letter-spacing:-.02em}
.src{font-size:13px;color:rgba(142,138,131,.85);letter-spacing:.02em}

/* builds: data-steps on the slide, .rv[data-s=k] appears at step k */
.rv{opacity:0;transform:translateY(12px);transition:opacity .45s var(--ease),transform .45s var(--ease)}
.rv.on{opacity:1;transform:none}
.rv.nofly{transform:none}
html.still *,html.still *::before,html.still *::after{animation-duration:0s!important;animation-delay:0s!important;transition:none!important}

/* staggered entrance */
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.slide.active .a{animation:fadeUp .5s var(--ease) both}
.slide.active .a2{animation:fadeUp .5s .12s var(--ease) both}

/* speaker notes (N) and timer (T) */
.notes{display:none}
#notes{position:fixed;left:0;right:0;bottom:0;max-height:42vh;overflow:auto;background:rgba(11,11,13,.96);border-top:1px solid var(--line);
  padding:18px 72px 28px;z-index:300;font-size:16px;line-height:1.55;color:rgba(243,238,230,.85);display:none}
#notes.on{display:block}
#notes .nh{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--amber);margin:12px 0 6px}
#notes p{margin-bottom:6px}#notes ul{padding-left:18px;color:var(--muted);font-size:14px}
#timer{position:fixed;top:16px;right:24px;z-index:300;font-size:22px;font-weight:500;letter-spacing:.06em;padding:6px 16px;border-radius:999px;
  border:1px solid rgba(242,163,58,.4);color:var(--amber);background:rgba(11,11,13,.85);display:none;font-variant-numeric:tabular-nums}
#timer.on{display:block}#timer.low{color:#F3EEE6;border-color:#F3EEE6}#timer.over{color:#0B0B0D;background:var(--amber)}
#help{position:fixed;top:16px;left:24px;z-index:300;font-size:13px;color:var(--muted);display:none;letter-spacing:.04em}
#help.on{display:block}

/* slide 1: cover */
.lockup{height:clamp(90px,10vh,130px);display:block}
.cover-title{font-size:clamp(30px,3.2vw,62px);font-weight:500;line-height:1.15;letter-spacing:-.01em;text-align:center;max-width:22em}
.bubbles{display:flex;align-items:flex-end;justify-content:center;gap:clamp(40px,5vw,96px)}
.bub{display:flex;flex-direction:column;align-items:center;gap:14px}
.bub i{display:block;border-radius:50%}
.bub span{font-size:clamp(15px,1.05vw,20px);letter-spacing:.14em;text-transform:uppercase;color:rgba(243,238,230,.8)}
.arcline{height:4px;width:min(720px,40vw);border-radius:4px;background:var(--arc);box-shadow:0 0 24px rgba(242,163,58,.35),0 0 48px rgba(61,186,155,.18);margin:0 auto}
.tagline{font-size:clamp(20px,1.6vw,30px);letter-spacing:.06em;color:var(--text);text-align:center}

/* slide 2: timeline */
.tl{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:2vh}
.tl::before{content:"";position:absolute;left:12.5%;right:12.5%;top:44px;height:3px;background:linear-gradient(90deg,#F2A33A,#D9C46B 45%,#3DBA9B 70%,#4a4a50 78%,#4a4a50);border-radius:3px}
.tn{display:flex;flex-direction:column;align-items:center;text-align:center;gap:12px;position:relative}
.tn .node{width:90px;height:90px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;background:#111114;border:3px solid var(--amber)}
.tn.c2 .node{border-color:var(--mid)} .tn.c3 .node{border-color:var(--jade)}
.tn.grey .node{border-color:#55555c;filter:grayscale(1);background:#141416}
.tn .yr{font-size:clamp(24px,1.9vw,38px);font-weight:500}
.tn.grey .yr{color:#9a978f}
.tn .what{font-size:clamp(15px,1vw,19px);color:rgba(243,238,230,.7);max-width:15em;line-height:1.45}
.stat{display:flex;align-items:center;gap:36px;justify-content:center}
.stat .big{font-size:clamp(84px,8vw,160px);color:var(--text)}

/* slide 3: demo */
.demo-wrap{position:relative;flex:1;min-height:0;border-radius:18px;border:1px solid rgba(242,163,58,.28);box-shadow:0 0 0 1px rgba(61,186,155,.08),0 24px 80px rgba(0,0,0,.6),0 0 60px rgba(242,163,58,.08);overflow:hidden;background:#0B0B0D}
.demo-wrap iframe{position:absolute;left:0;top:0;border:0;transform-origin:0 0;background:#0B0B0D}
.demo-bar{display:flex;gap:12px;align-items:center;justify-content:center;margin-top:14px;flex-wrap:wrap}
body.demo .slide#s3{padding:0}
body.demo .slide#s3 .head,body.demo .slide#s3 .demo-bar{display:none}
body.demo .slide#s3 .body{width:100vw;padding:0}
body.demo .slide#s3 .demo-wrap{border-radius:0;border:0}
body.demo #dots,body.demo .arr,body.demo #snum,body.demo #brandmark{display:none}
#s3 .body{justify-content:flex-start;padding-bottom:1vh}

/* slide 4: quotes */
.q{display:flex;flex-direction:column;gap:16px;height:100%}
.q .qt{font-size:clamp(19px,1.35vw,26px);line-height:1.4;color:var(--text);flex:1}
.q .ic{display:flex;gap:8px;height:22px;align-items:center}.bd{display:block;width:18px;height:18px;border-radius:50%;box-shadow:0 0 14px currentColor}
.ev{display:flex;align-items:center;justify-content:center;gap:34px;margin-top:4.5vh}
.ev .big{font-size:clamp(72px,6.4vw,124px);color:var(--jade)}

/* slide 5: market rings */
.mk{display:grid;grid-template-columns:auto 1fr;gap:5vw;align-items:center}
.mk svg{height:min(56vh,600px);width:auto;display:block}
.mrow{display:flex;flex-direction:column;gap:4px;padding:16px 0;border-bottom:1px solid var(--line)}
.mrow:last-child{border-bottom:0}
.mrow .k{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.mrow .v{font-size:clamp(40px,3.4vw,66px);font-weight:500;line-height:1.05}
.mrow .w{font-size:clamp(15px,1vw,19px);color:rgba(243,238,230,.7)}

/* slide 6: business */
.biz{display:grid;grid-template-columns:0.9fr 1.1fr;gap:5vw;align-items:center}
.tin{position:relative;width:min(400px,22vw);aspect-ratio:1/1.12;margin:0 auto;border-radius:28px;background:linear-gradient(160deg,#1d1d22,#101013);border:1px solid #33333a;
  box-shadow:inset 0 2px 0 rgba(255,255,255,.06),0 30px 80px rgba(0,0,0,.6),0 0 50px rgba(242,163,58,.08);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px}
.tin::before{content:"";position:absolute;left:0;right:0;top:15%;height:2px;background:var(--arc);opacity:.8}
.tin img{width:62%}
.tin .tl1{font-size:15px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.tin .pr{font-size:clamp(44px,3.6vw,72px);font-weight:500;color:var(--amber);line-height:1}
.bars{display:flex;flex-direction:column;gap:16px}
.bar{display:grid;grid-template-columns:12em 1fr;align-items:center;gap:18px}
.bar .nm{font-size:clamp(15px,1vw,19px);color:rgba(243,238,230,.8);text-align:right}
.bar .tr{height:42px;border-radius:8px;background:rgba(243,238,230,.05);position:relative}
.bar .fl{height:100%;border-radius:8px;display:flex;align-items:center;justify-content:flex-end;padding-right:14px;font-size:clamp(17px,1.15vw,22px);font-weight:500;color:#0B0B0D}
.route{display:flex;align-items:flex-start;margin-top:5vh}
.rs{flex:1;display:flex;flex-direction:column;align-items:center;position:relative;text-align:center;gap:8px}
.rs+.rs::before{content:"";position:absolute;top:30px;left:-50%;width:100%;height:2px;background:rgba(243,238,230,.14)}
.rn{width:62px;height:62px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:26px;border:2px solid var(--amber);background:#141012;position:relative;z-index:1}
.rs:nth-child(2) .rn{border-color:var(--mid)} .rs:nth-child(3) .rn{border-color:var(--jade)}
.rl{font-size:clamp(16px,1.1vw,21px);font-weight:500}.rsub{font-size:clamp(14px,.95vw,18px);color:var(--muted)}

/* slide 7: 2x2 */
.mx svg{width:100%;height:min(62vh,680px);display:block}

/* slide 8: ask */
.ask{display:grid;grid-template-columns:auto 1fr;gap:5vw;align-items:center}
.ask .big{font-size:clamp(100px,8.6vw,172px);color:var(--amber)}
.fund{display:flex;height:56px;border-radius:10px;overflow:hidden;margin:10px 0 12px}
.fund div{display:flex;align-items:center;justify-content:center;font-size:clamp(15px,1vw,19px);font-weight:600;color:#0B0B0D}
.flg{display:flex;flex-wrap:wrap;gap:8px 26px;white-space:nowrap;font-size:clamp(14px,.92vw,17px);color:rgba(243,238,230,.75)}
.flg b{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:8px;vertical-align:-1px}
.ms{display:flex;gap:0;margin-top:3.5vh}
.pv{display:flex;flex-direction:column;gap:10px;margin-top:3.5vh;font-size:clamp(15px,1vw,19px);color:rgba(243,238,230,.8)}
.pv .chip{margin-right:10px;font-size:12px;padding:4px 12px}
.rn{font-size:24px;font-weight:500;color:var(--text)}
.closer{display:flex;align-items:center;justify-content:center;gap:28px;margin-top:6vh;padding-top:4vh;border-top:2px solid transparent;border-image:var(--arc) 1}
.closer img{height:clamp(64px,7vh,90px)}
"""

SLIDES = r"""
<!-- 1 · COMPANY -->
<div class="slide bg-mesh cover" id="s1" data-steps="2" data-title="Company">
  <div class="col a" style="display:flex;flex-direction:column;align-items:center;gap:3.2vh">
    <div class="label" style="margin:0">osmē <span class="tt">· Greek for scent · said oz-MAY</span></div>
    <img class="lockup" src="__LOCKUP__" alt="OSME"/>
    <div class="cover-title"><b style="font-weight:500">OSME</b> makes a tea bag that opens only at <em>its perfect temperature</em>.</div>
    <div class="sm" style="text-align:center;margin-top:-1vh">For curious specialty tea drinkers, sold direct and by subscription.</div>
    <div class="rv" data-s="1" style="margin-top:2.4vh">
      <div class="bubbles">
        <div class="bub"><i style="width:26px;height:26px;background:var(--jade);box-shadow:0 0 18px rgba(61,186,155,.6)"></i><span>Fish eyes</span></div>
        <div class="bub"><i style="width:40px;height:40px;background:var(--mid);box-shadow:0 0 22px rgba(217,196,107,.55)"></i><span>String of pearls</span></div>
        <div class="bub"><i style="width:56px;height:56px;background:var(--amber);box-shadow:0 0 28px rgba(242,163,58,.6)"></i><span>Rolling waves</span></div>
      </div>
    </div>
    <div class="rv" data-s="2" style="display:flex;flex-direction:column;align-items:center;gap:18px;margin-top:1vh">
      <div class="arcline"></div>
      <div class="tagline">Every tea has its temperature.</div>
    </div>
  </div>
  __NOTES1__
</div>

<!-- 2 · PROBLEM -->
<div class="slide bg-warm" id="s2" data-steps="3" data-title="Problem">
  <div class="head a"><div class="label">The problem</div>
    <div class="h1">For 1,200 years tea was an art of heat and time; the tea bag of about 1908 traded it for <em>convenience</em>.</div></div>
  <div class="body">
    <div class="tl">
      <div class="tn rv" data-s="1"><div class="node"><i class="bd" style="background:var(--amber);width:22px;height:22px"></i></div><div class="yr">760</div><div class="what">China: Lu Yu reads water by its bubbles</div></div>
      <div class="tn c2 rv" data-s="1"><div class="node"><i class="bd" style="background:var(--mid);width:22px;height:22px"></i></div><div class="yr">1500s</div><div class="what">Japan: Rikyū's tea ceremony</div></div>
      <div class="tn c3 rv" data-s="1"><div class="node"><i class="bd" style="background:var(--jade);width:22px;height:22px"></i></div><div class="yr">c. 1840</div><div class="what">Britain: afternoon tea</div></div>
      <div class="tn grey rv" data-s="2"><div class="node"><i style="display:block;width:22px;height:28px;border-radius:3px;background:#77746d"></i></div><div class="yr">~1908</div><div class="what">The tea bag: one temperature, no timer, one cup</div></div>
    </div>
    <div class="stat rv" data-s="3" style="margin-top:7vh">
      <div class="big">96%</div>
      <div style="max-width:30em"><div class="sm" style="font-size:clamp(19px,1.35vw,26px);color:var(--text)">of tea in Britain is now made with a bag.</div>
        <div class="cap" style="margin-top:10px">Boiling water on green tea: “noticeably more bitter” in a side-by-side test.</div>
        <div class="src" style="margin-top:8px">QMUL 2016 · The Tea Spot</div></div>
    </div>
  </div>
  __NOTES2__
</div>

<!-- 3 · SOLUTION (LIVE DEMO) -->
<div class="slide bg-dark" id="s3" data-steps="0" data-title="Solution">
  <div class="head a"><div class="label">The solution · live</div>
    <div class="h1">The OSME bag stays sealed in boiling water, opens at <em>80 °C</em> for Sencha and seals again below 70 °C.</div></div>
  <div class="body" style="margin-top:2vh">
    <div class="demo-wrap" id="demoWrap"><iframe id="demo" title="OSME live product" srcdoc="__PRODUCT__"></iframe></div>
    <div class="demo-bar">
      <span class="chip j">Proven in labs</span><span class="sm">PNIPAm membranes open and close with heat, 5 clean cycles</span>
      <span class="chip a" style="margin-left:18px">Our R&amp;D</span><span class="sm">the same switch, food-safe, at 70 to 90 °C</span>
    </div>
  </div>
  __NOTES3__
</div>

<!-- 4 · CUSTOMER EVIDENCE -->
<div class="slide bg-night" id="s4" data-steps="4" data-title="Customer evidence">
  <div class="head a"><div class="label">Customer evidence</div>
    <div class="h1">Curious specialty drinkers say it in their own words: they forget the bag, bin good leaves and <em>lose the scent</em>.</div></div>
  <div class="body">
    <div class="g3">
      <div class="card q rv" data-s="1"><div class="ic"><i class="bd" style="background:var(--amber)"></i></div><div class="qt">“I've been steeping this for 20 minutes …”</div>
        <div><span class="chip a">OSME stops itself</span></div><div class="src">weland · Hacker News, trimmed<br/>news.ycombinator.com/item?id=7725580</div></div>
      <div class="card q rv" data-s="2"><div class="ic"><i class="bd" style="background:var(--mid)"></i><i class="bd" style="background:var(--mid)"></i></div><div class="qt">“I spend way too much on tea to just throw them away after one steep!”</div>
        <div><span class="chip g">OSME brews again</span></div><div class="src">hopeofdawn · TeaChat<br/>teachat.com/viewtopic.php?p=212298</div></div>
      <div class="card q rv" data-s="3"><div class="ic"><i class="bd" style="background:var(--jade)"></i><i class="bd" style="background:var(--jade)"></i><i class="bd" style="background:var(--jade)"></i></div><div class="qt">“My leaves start not tasting as fresh when I reuse them from the day before.”</div>
        <div><span class="chip j">OSME keeps the scent</span></div><div class="src">silversun · TeaChat<br/>same thread</div></div>
    </div>
    <div class="ev rv" data-s="4">
      <div class="big">16%</div>
      <div><div class="sm" style="font-size:clamp(19px,1.35vw,26px);color:var(--text)">of British tea drinkers already brew their black tea loose leaf.</div>
        <div class="cap" style="margin-top:8px">Our first buyer: the curious specialty drinker, 25 to 45, who pays for good leaves.</div>
        <div class="src" style="margin-top:6px">UKTIA 2024</div></div>
    </div>
  </div>
  __NOTES4__
</div>

<!-- 5 · MARKET -->
<div class="slide bg-grid" id="s5" data-steps="3" data-title="Market">
  <div class="head a"><div class="label">Market <span class="tt">· tea-tech disruptor</span></div>
    <div class="h1">OSME starts in a <em>$7.1 billion</em> tea bag market and aims for $9 million in sales in year 3.</div></div>
  <div class="body">
    <div class="mk">
      <svg viewBox="0 0 600 600" aria-hidden="true">
        <defs><radialGradient id="mkg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#F2A33A" stop-opacity=".9"/><stop offset="1" stop-color="#F2A33A" stop-opacity=".55"/></radialGradient></defs>
        <g class="rv nofly" data-s="1"><circle cx="300" cy="300" r="290" fill="rgba(243,238,230,.035)" stroke="rgba(243,238,230,.28)" stroke-width="2"/>
          <text x="300" y="70" text-anchor="middle" fill="#8E8A83" font-size="22" letter-spacing="4" font-family="Jost">TEA BAGS</text></g>
        <g class="rv nofly" data-s="2"><circle cx="300" cy="380" r="200" fill="rgba(61,186,155,.07)" stroke="#3DBA9B" stroke-width="2"/>
          <text x="300" y="232" text-anchor="middle" fill="#3DBA9B" font-size="22" letter-spacing="4" font-family="Jost">PREMIUM · 4 MARKETS</text></g>
        <g class="rv nofly" data-s="3"><circle cx="300" cy="490" r="84" fill="url(#mkg)" style="filter:drop-shadow(0 0 24px rgba(242,163,58,.5))"/>
          <text x="300" y="498" text-anchor="middle" fill="#0B0B0D" font-size="26" font-weight="600" letter-spacing="3" font-family="Jost">YEAR 3</text></g>
      </svg>
      <div>
        <div class="mrow rv" data-s="1"><div class="k">The world's tea bags</div><div class="v">$7.1 bn</div><div class="w">$18.8 bn tea market × 38% sold in bags</div></div>
        <div class="mrow rv" data-s="2"><div class="k">Premium bags · Japan, China, UK, US</div><div class="v jade">$640 m</div><div class="w">× 45% four first markets × 20% premium (our assumptions)</div></div>
        <div class="mrow rv" data-s="3"><div class="k">OSME sales, year 3</div><div class="v amber">$9 m</div><div class="w">20 k Ritual Keepers × $288 a year = $5.8 m, plus tins and retail</div></div>
      </div>
    </div>
  </div>
  __NOTES5__
</div>

<!-- 6 · BUSINESS -->
<div class="slide bg-warm" id="s6" data-steps="3" data-title="Business">
  <div class="head a"><div class="label">Business <span class="tt">· direct to consumers</span></div>
    <div class="h1">OSME sells an $18 tin and a $24 Ritual subscription direct: about <em>$0.50 a cup</em> at 62% gross margin.</div></div>
  <div class="body">
    <div class="biz">
      <div class="tin rv" data-s="1"><div class="tl1">12 bags · Sencha</div><img src="__LOCKUP__" alt="OSME"/><div class="pr">$18</div><div class="tl1">Up to 3 cups a bag</div><div class="tl1" style="color:var(--jade)">$11 margin a tin</div></div>
      <div>
        <div class="bars rv" data-s="2">
          <div class="cap" style="margin-left:calc(12em + 18px);letter-spacing:.16em;text-transform:uppercase;font-size:13px">Price per cup</div>
          <div class="bar"><div class="nm">OSME bag</div><div class="tr"><div class="fl" style="width:38%;background:var(--arc)">$0.50</div></div></div>
          <div class="bar"><div class="nm">Tea subscription box</div><div class="tr"><div class="fl" style="width:77%;background:#5a5a60;color:var(--text)">~$1.00</div></div></div>
          <div class="bar"><div class="nm">Pyramid infuser</div><div class="tr"><div class="fl" style="width:100%;background:#5a5a60;color:var(--text)">$1.30</div></div></div>
          <div class="cap" style="margin-left:calc(12em + 18px)"><span class="amber">62% gross margin</span> direct · Sips By and Tea Forte prices</div>
        </div>
        <div class="route rv" data-s="3">
          <div class="rs"><div class="rn">1</div><div class="rl">Web shop</div><div class="rsub">tins and gifts</div></div>
          <div class="rs"><div class="rn">2</div><div class="rl">Ritual · $24/mo</div><div class="rsub">members are Keepers</div></div>
          <div class="rs"><div class="rn">3</div><div class="rl">Premium retail</div><div class="rsub">from year 3</div></div>
        </div>
      </div>
    </div>
  </div>
  __NOTES6__
</div>

<!-- 7 · COMPETITION -->
<div class="slide bg-grid" id="s7" data-steps="2" data-title="Competition">
  <div class="head a"><div class="label">Competition</div>
    <div class="h1">Loose leaf keeps the art, bags and capsules keep the ease; only the <em>OSME bag</em> controls the steep itself.</div></div>
  <div class="body mx">
    <svg viewBox="0 0 1240 640" aria-hidden="true" font-family="Jost">
      <line x1="120" y1="590" x2="1200" y2="590" stroke="rgba(243,238,230,.25)" stroke-width="2"/>
      <line x1="120" y1="590" x2="120" y2="30" stroke="rgba(243,238,230,.25)" stroke-width="2"/>
      <line x1="660" y1="40" x2="660" y2="580" stroke="rgba(243,238,230,.07)" stroke-width="2" stroke-dasharray="6 8"/>
      <line x1="130" y1="310" x2="1200" y2="310" stroke="rgba(243,238,230,.07)" stroke-width="2" stroke-dasharray="6 8"/>
      <text x="1200" y="626" text-anchor="end" fill="#8E8A83" font-size="20" letter-spacing="4">EASE →</text>
      <text x="96" y="40" text-anchor="end" fill="#8E8A83" font-size="20" letter-spacing="4" transform="rotate(-90 96 40)">ART OF TEA →</text>
      <g class="rv nofly" data-s="1">
        <circle cx="200" cy="150" r="16" fill="#8E8A83"/><text x="230" y="144" fill="#F3EEE6" font-size="27">Loose leaf and gongfu</text><text x="230" y="176" fill="#8E8A83" font-size="21">needs a timer, thermometer and skill</text>
        <circle cx="700" cy="330" r="16" fill="#8E8A83"/><text x="730" y="324" fill="#F3EEE6" font-size="27">Tea Forte pyramid bags</text><text x="730" y="356" fill="#8E8A83" font-size="21">whole leaf, still over-steeps, one cup</text>
        <circle cx="860" cy="440" r="16" fill="#8E8A83"/><text x="890" y="434" fill="#F3EEE6" font-size="27">Nestlé Special.T capsules</text><text x="890" y="466" fill="#8E8A83" font-size="21">a €129 machine and pods</text>
        <circle cx="960" cy="540" r="16" fill="#55555c"/><text x="740" y="534" fill="#bdb9b1" font-size="23" text-anchor="end">Supermarket bags</text><text x="740" y="562" fill="#8E8A83" font-size="19" text-anchor="end">one temperature, keeps steeping</text>
      </g>
      <g class="rv nofly" data-s="2">
        <circle cx="1080" cy="110" r="46" fill="none" stroke="#F2A33A" stroke-width="3" opacity=".45"><animate attributeName="r" values="34;56;34" dur="3s" repeatCount="indefinite"/></circle>
        <circle cx="1080" cy="110" r="26" fill="#F2A33A" style="filter:drop-shadow(0 0 22px rgba(242,163,58,.8))"/>
        <text x="1140" y="206" text-anchor="end" fill="#F2A33A" font-size="34" font-weight="500">OSME</text>
        <text x="1140" y="240" text-anchor="end" fill="#F3EEE6" font-size="21">opens at its temperature, stops itself</text>
        <text x="1140" y="268" text-anchor="end" fill="#8E8A83" font-size="19">brews 3 times · any kettle, no machine</text>
      </g>
    </svg>
  </div>
  __NOTES7__
</div>

<!-- 8 · THE ASK -->
<div class="slide bg-mesh" id="s8" data-steps="3" data-title="The ask">
  <div class="head a"><div class="label">The ask <span class="tt">· tea-tech disruptor</span></div>
    <div class="h1">We ask <em>$2.5 million</em> to prove the food-safe OSME bag and ship the first Ritual boxes.</div></div>
  <div class="body">
    <div class="ask">
      <div><div class="big">$2.5 m</div><div class="sm" style="margin-top:14px;font-size:clamp(18px,1.25vw,24px)">SAFE · $10 m pre-money</div></div>
      <div class="rv" data-s="1">
        <div class="cap" style="letter-spacing:.16em;text-transform:uppercase;font-size:13px">Use of funds</div>
        <div class="fund"><div style="width:35%;background:#F2A33A">35%</div><div style="width:15%;background:#E6B552">15%</div><div style="width:30%;background:#D9C46B">30%</div><div style="width:15%;background:#8DBF84">15%</div><div style="width:5%;background:#3DBA9B"></div></div>
        <div class="flg"><span><b style="background:#F2A33A"></b>Membrane R&amp;D</span><span><b style="background:#E6B552"></b>Food safety</span><span><b style="background:#D9C46B"></b>Brand and launch</span><span><b style="background:#8DBF84"></b>Tea origins</span><span><b style="background:#3DBA9B"></b>Ops 5%</span></div>
        <div class="pv"><div><span class="chip j">Proven</span> lab membranes (PNIPAm) open and close with heat</div>
          <div><span class="chip a">Not yet</span> food-safe at 70 to 90 °C: this round pays for it</div></div>
        <div class="ms">
          <div class="rs"><div class="rn">1</div><div class="rl">Q2 2027</div><div class="rsub">lab bag opens at 80 °C</div></div>
          <div class="rs"><div class="rn">2</div><div class="rl">Q2 2028</div><div class="rsub">food-contact approval</div></div>
          <div class="rs"><div class="rn">3</div><div class="rl">Q3 2028</div><div class="rsub">first Ritual boxes, UK and US</div></div>
        </div>
      </div>
    </div>
    <div class="closer rv" data-s="3">
      <img src="__SYMBOL__" alt=""/>
      <div><div class="tagline" style="text-align:left">Every tea has its temperature.</div>
        <div class="sm" style="margin-top:6px">Take back one cup a day. <span class="amber">Become a Keeper.</span></div></div>
    </div>
  </div>
  __NOTES8__
</div>
"""

JS = r"""
const SLIDES=[...document.querySelectorAll('.slide')];
const N=SLIDES.length;
let cur=0, step=0;
const steps=i=>+(SLIDES[i].dataset.steps||0);
function paint(){
  SLIDES[cur].querySelectorAll('.rv').forEach(el=>el.classList.toggle('on',+el.dataset.s<=step));
}
function goto(n,s){
  if(n<0||n>=N)return;
  if(n!==cur){
    SLIDES[cur].classList.remove('active');SLIDES[cur].classList.add('out');
    const p=cur;setTimeout(()=>SLIDES[p].classList.remove('out'),380);
  }
  cur=n;step=Math.max(0,Math.min(s||0,steps(n)));
  SLIDES[cur].classList.add('active');paint();ui();
  if(cur!==2)document.body.classList.remove('demo');
  if(cur===2)fitDemo();
}
function next(){ if(step<steps(cur)){step++;paint();ui();} else goto(cur+1,0); }
function prev(){ if(step>0){step--;paint();ui();} else if(cur>0) goto(cur-1,steps(cur-1)); }
function ui(){
  document.getElementById('bar').style.width=((cur+1)/N*100)+'%';
  document.querySelectorAll('.dot').forEach((d,i)=>d.classList.toggle('on',i===cur));
  document.getElementById('snum').textContent=(cur+1)+' / '+N;
  document.getElementById('prev').style.opacity=cur===0&&step===0?.25:1;
  document.getElementById('next').style.opacity=cur===N-1&&step===steps(cur)?.25:1;
  document.body.className=document.body.className.replace(/\bs\d+\b/g,'').trim()+' s'+cur;
  const nt=SLIDES[cur].querySelector('.notes');
  document.getElementById('notes').innerHTML='<p class="nh">Slide '+(cur+1)+' · '+SLIDES[cur].dataset.title+'</p>'+(nt?nt.innerHTML:'');
  history.replaceState(null,'','#'+(cur+1)+(step?'.'+step:''));
}
const dotsEl=document.getElementById('dots');
for(let i=0;i<N;i++){const d=document.createElement('div');d.className='dot';d.onclick=e=>{e.stopPropagation();goto(i,0)};dotsEl.appendChild(d);}

/* live demo: iframe scaled to fit, D toggles full screen, keys inside go to the app */
const DW=1600, DH=900;
function fitDemo(){
  const w=document.getElementById('demoWrap'), f=document.getElementById('demo');
  if(!w||!f)return;
  const r=w.getBoundingClientRect(), k=Math.min(r.width/DW,r.height/DH);
  const iw=r.width/k, ih=r.height/k;
  f.style.width=iw+'px';f.style.height=ih+'px';f.style.transform='scale('+k+')';
}
function demo(on){
  document.body.classList.toggle('demo',on);
  requestAnimationFrame(()=>{fitDemo();if(on){const f=document.getElementById('demo');f.focus();try{f.contentWindow.focus()}catch(e){}}});
}
window.addEventListener('resize',fitDemo);
document.getElementById('demo').addEventListener('load',()=>{
  const f=document.getElementById('demo');fitDemo();
  try{
    const w=f.contentWindow;
    if(w.osme&&w.osme.choose)w.osme.choose('sencha');
    w.document.addEventListener('keydown',e=>{
      if(e.key==='Escape'){demo(false);window.focus();}
      else if(e.key==='d'||e.key==='D'){demo(!document.body.classList.contains('demo'));}
      else if(e.key==='PageDown'){demo(false);window.focus();next();}
      else if(e.key==='PageUp'){demo(false);window.focus();prev();}
      else if(e.key==='t'||e.key==='T'){toggleTimer(e.shiftKey);}
    });
  }catch(e){}
});

/* presenter timer: T start/pause, Shift+T reset */
let tLeft=180, tRun=false, tLast=0, tShown=false;
function fmt(s){const neg=s<0;s=Math.abs(Math.round(s));return (neg?'+':'')+Math.floor(s/60)+':'+String(s%60).padStart(2,'0');}
function drawTimer(){const el=document.getElementById('timer');el.textContent=fmt(tLeft);el.classList.toggle('low',tLeft<=30&&tLeft>0);el.classList.toggle('over',tLeft<=0);}
function toggleTimer(reset){
  const el=document.getElementById('timer');
  if(reset){tLeft=180;tRun=false;tShown=true;el.classList.add('on');drawTimer();return;}
  if(!tShown){tShown=true;el.classList.add('on');}
  tRun=!tRun;tLast=performance.now();drawTimer();
}
(function tick(ts){if(tRun){tLeft-=(ts-tLast)/1000;tLast=ts;drawTimer();}requestAnimationFrame(tick);})(0);

document.addEventListener('keydown',e=>{
  const k=e.key;
  if(k==='ArrowRight'||k==='ArrowDown'||k===' '||k==='PageDown'||k==='Enter'){e.preventDefault();next();}
  else if(k==='ArrowLeft'||k==='ArrowUp'||k==='PageUp'||k==='Backspace'){e.preventDefault();prev();}
  else if(k==='Home')goto(0,0);
  else if(k==='End')goto(N-1,steps(N-1));
  else if(k==='t'||k==='T')toggleTimer(e.shiftKey);
  else if(k==='n'||k==='N')document.getElementById('notes').classList.toggle('on');
  else if(k==='d'||k==='D'){if(cur!==2)goto(2,0);demo(!document.body.classList.contains('demo'));}
  else if(k==='Escape')demo(false);
  else if(k==='?'||k==='h'||k==='H')document.getElementById('help').classList.toggle('on');
  else if(/^[1-8]$/.test(k))goto(+k-1,0);
});
document.querySelector('.deck').addEventListener('click',e=>{
  if(e.target.closest('iframe,.demo-wrap,button,a'))return;
  next();
});
let tx=0;
document.addEventListener('touchstart',e=>{tx=e.touches[0].clientX},{passive:true});
document.addEventListener('touchend',e=>{const dx=e.changedTouches[0].clientX-tx;if(Math.abs(dx)>50)(dx<0?next:prev)();},{passive:true});

/* ?still: no animation, for screenshots */
if(/still/.test(location.search))document.documentElement.classList.add('still');
/* start from the hash: #N or #N.S */
(function(){
  const m=location.hash.match(/^#(\d+)(?:\.(\d+))?/);
  const n=m?Math.min(N,Math.max(1,+m[1]))-1:0, s=m&&m[2]?+m[2]:0;
  cur=n;SLIDES[n].classList.add('active');step=Math.min(s,steps(n));paint();ui();
  if(n===2)setTimeout(fitDemo,50);
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>OSME · a tea bag that opens only at its perfect temperature</title>
<style>__CSS__</style>
</head>
<body class="s0">
<div id="bar"></div>
<button class="arr" id="prev" onclick="prev()" aria-label="Previous">&#8249;</button>
<button class="arr" id="next" onclick="next()" aria-label="Next">&#8250;</button>
<div id="dots"></div>
<div id="snum"></div>
<img id="brandmark" src="__LOCKUP__" alt=""/>
<div id="timer">3:00</div>
<div id="help">D live demo full screen · Space pours · →  next · ← back · T timer · Shift+T reset · N notes · D live demo · Esc leave demo · 1 to 8 jump</div>
<div id="notes"></div>
<div class="deck">
__SLIDES__
</div>
<script>__JS__</script>
</body>
</html>
"""

if __name__ == "__main__":
    slides = SLIDES
    for n in range(1, 9):
        slides = slides.replace(f"__NOTES{n}__", notes(n))
    out = (PAGE.replace("__CSS__", CSS).replace("__SLIDES__", slides).replace("__JS__", JS)
           .replace("__FONT__", FONT).replace("__LOCKUP__", LOCKUP).replace("__SYMBOL__", SYMBOL)
           .replace("__PRODUCT__", PRODUCT))
    (D / "pitch.html").write_text(out, encoding="utf8")
    print("wrote", D / "pitch.html", len(out) // 1024, "KB; script blocks parsed:", sorted(SPOKEN))
