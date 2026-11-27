#!/usr/bin/env python3
"""Build deck/gate1.html: 6 decision slides for the team's Gate 1 review.

Same engine, CSS and JS as deck/pitch.html (imported from build_pitch.py).
Every build pulls the latest logo files from brand/identity/, brand assets from
brand/assets/ and the logo options board from gallery/brand-v04-logo-options.png.

Run: python3 deck/build_gate1.py
"""
import pathlib, subprocess, tempfile
import build_pitch as bp

R, D = bp.R, bp.D
A = R / "brand" / "assets"


def img(path):
    mime = "image/svg+xml" if path.suffix == ".svg" else "image/png"
    return bp.b64(path, mime)


def crop_option(x):
    """Cut one option card (symbol only) out of the logo options board."""
    src = R / "gallery" / "brand-v04-logo-options.png"
    out = pathlib.Path(tempfile.gettempdir()) / f"osme-opt-{x}.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                    "-vf", f"crop=540:330:{x}:180", str(out)], check=True)
    return img(out)


SYM = bp.logo("logo-symbol.svg")
LOCK = bp.LOCKUP
OPT_A, OPT_C = crop_option(52), crop_option(1207)
def crop_hero():
    """Frame the hero around the cup and its full arc for the portrait panel."""
    out = pathlib.Path(tempfile.gettempdir()) / "osme-hero-crop.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(A / "hero.png"),
                    "-vf", "crop=iw*0.55:ih:iw*0.395:0", str(out)], check=True)
    return img(out)


HERO = crop_hero()
TIN = img(A / "pack-tin.png")
BAG = img(A / "pack-single-bag.png")
SOCIAL = img(A / "social-threebubbles-1080.png")
ICONS = [img(A / f"icon-{n}.svg") for n in ("self-stopping", "three-infusions", "scent-sealed")]

FONTX = bp.b64(D / "assets-src" / "jost-latin-ext.woff2", "font/woff2")
CSS = bp.CSS + r"""
#s1 .tagline{font-size:clamp(22px,1.7vw,32px)}#s1 .cap{font-size:clamp(17px,1vw,20px)}
#s3 .kit{margin-top:2.4vh}#s2 .body{justify-content:flex-start;padding-top:4vh}#s4 .card.q{min-height:30vh;padding:3.5vh 2vw}#s4 .q .qt{font-size:clamp(24px,1.7vw,32px)}#s4 .tile{padding:2.6vh 1.6vw}#s5 .tiles{margin-top:6vh}#s5 .tile{padding:3.4vh 1.4vw;min-height:20vh}#s5 .mbar{margin-bottom:1.2vh}
.src{font-size:clamp(15px,.9vw,17px)}
@font-face{font-family:"Jost";src:url(__FONTX__) format("woff2");font-weight:300 700;unicode-range:U+0100-02BA,U+1E00-1EFF}
.g1chip{position:absolute;top:5.2vh;right:72px;font-size:17px;letter-spacing:.18em;text-transform:uppercase;padding:7px 16px;border-radius:999px;border:1px solid rgba(242,163,58,.45);color:var(--amber);background:rgba(242,163,58,.07)}
.g1chip.ok{border-color:rgba(61,186,155,.45);color:var(--jade);background:rgba(61,186,155,.07)}
.prov{display:inline-block;font-size:15px;letter-spacing:.16em;text-transform:uppercase;padding:3px 9px;border-radius:999px;border:1px dashed rgba(242,163,58,.6);color:var(--amber);vertical-align:middle;margin-left:10px}
.nm-word{font-size:clamp(90px,9vw,180px);font-weight:500;letter-spacing:.2em;line-height:1}
.logo-b{display:grid;grid-template-columns:1.25fr 1fr;gap:4vw;align-items:center}
.logo-b .hero-sym{background:#111114;border:1px solid var(--line);border-radius:20px;display:flex;align-items:center;justify-content:center;height:min(66vh,720px)}
.logo-b .hero-sym img{height:70%}
.opt{display:grid;grid-template-columns:190px 1fr;gap:24px;align-items:center;padding:2.4vh 0;border-bottom:1px solid var(--line)}
.opt:last-child{border-bottom:0}
.opt img{width:190px;border-radius:10px;background:#17171B}
.opt .sc{font-size:clamp(40px,3vw,58px);font-weight:500}
.kit{display:grid;grid-template-columns:2.2fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;height:min(72vh,800px)}
.kit .t{border-radius:16px;overflow:hidden;background:#111114;border:1px solid var(--line);position:relative;display:flex;align-items:center;justify-content:center}
.kit .t img{width:100%;height:100%;object-fit:cover}
.kit .t.fit img{object-fit:contain;padding:10px}
.kit .t .lb{position:absolute;left:12px;bottom:10px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:rgba(243,238,230,.8);background:rgba(11,11,13,.7);padding:4px 10px;border-radius:999px}
.sw{display:flex;flex-direction:column;gap:10px;padding:18px;width:100%;height:100%;justify-content:center}
.sw div{display:flex;align-items:center;gap:12px;font-size:18px;color:rgba(243,238,230,.8)}
.sw i{display:block;width:34px;height:34px;border-radius:8px;border:1px solid rgba(243,238,230,.15)}
.mbar{display:grid;grid-template-columns:17em 1fr;gap:20px;align-items:center;margin:12px 0}
.mbar .k{text-align:right;font-size:clamp(15px,1vw,19px);color:rgba(243,238,230,.8)}
.mbar .tr{height:54px;position:relative}
.mbar .fl{height:100%;border-radius:8px;min-width:6px}
.mbar .v{position:absolute;top:50%;transform:translateY(-50%);font-size:clamp(22px,1.7vw,32px);font-weight:500;padding-left:14px}
.mbar .w{font-size:clamp(18px,1.05vw,20px);color:var(--muted);margin-top:4px}
.tiles{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:4vh}
.tile{border:1px solid var(--line);border-radius:14px;padding:18px 20px;background:rgba(243,238,230,.03)}
.tile .v{font-size:clamp(28px,2.2vw,42px);font-weight:500;line-height:1.1}
.tile .k{font-size:16px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.tile .w{font-size:clamp(18px,1.05vw,20px);color:rgba(243,238,230,.65);margin-top:4px}
.dec{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.dec .card{display:flex;flex-direction:column;gap:14px;min-height:20vh;justify-content:center;padding:3.2vh 2.4vw}
.dec .q1{font-size:15px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}
.dec .rec{font-size:clamp(28px,2.1vw,40px);font-weight:500;line-height:1.25}
.dec .alt{font-size:clamp(16px,1.1vw,20px);color:rgba(243,238,230,.65)}
.ic3{display:flex;gap:26px;justify-content:center;margin-top:3vh}
.ic3 div{display:flex;flex-direction:column;align-items:center;gap:8px;font-size:14px;letter-spacing:.12em;text-transform:uppercase;color:rgba(243,238,230,.75)}
.ic3 img{height:64px}
.slide.top .body{justify-content:flex-start;padding-top:6vh}
"""

SLIDES = r"""
<!-- 1 · NAME -->
<div class="slide bg-mesh cover" id="s1" data-steps="0" data-title="Name">
  <div class="g1chip ok">Confirm · keep the name</div>
  <div style="display:flex;flex-direction:column;align-items:center;gap:4.2vh;margin-top:4vh" class="a">
    <div class="label" style="margin:0">Gate 1 · the name</div>
    <img src="__LOCK__" alt="OSME" style="height:clamp(170px,22vh,250px)"/>
    <div class="cover-title" style="font-size:clamp(32px,3vw,58px)">From Greek <em>osmē</em>, “scent”. Said <em>oz-MAY</em>.</div>
    <div class="arcline"></div>
    <div style="display:flex;gap:6vw;justify-content:center;text-align:center">
      <div><div class="label" style="color:var(--muted)">One line</div><div class="tagline">A tea bag that opens only at its perfect temperature.</div></div>
      <div><div class="label" style="color:var(--muted)">Tagline</div><div class="tagline">Every tea has its temperature.</div></div>
    </div>
    <div class="cap" style="max-width:56em;text-align:center">Name check 09:52: no tea or drinks brand called OSME found. A Miami perfumery uses “Osme”; an “OSMÉ PARIS” perfume trademark application is dead.</div>
  </div>
  <aside class="notes"><p>Sources: facts.md (Name, clash check 09:52), brand/strategy.md §2 (one-liner 1, tagline 1).</p></aside>
</div>

<!-- 2 · LOGO -->
<div class="slide bg-dark" id="s2" data-steps="0" data-title="Logo">
  <div class="g1chip">Decision 1 · logo B</div>
  <div class="head a"><div class="label">Gate 1 · the logo</div>
    <div class="h1">Logo B, the <em>Scent S</em>: a tea bag whose string rises as a curl of scent, amber to jade.</div></div>
  <div class="body">
    <div class="logo-b">
      <div class="hero-sym"><img src="__SYM__" alt="Logo B"/></div>
      <div>
        <div class="opt"><img src="__SYM__" alt="" style="padding:22px 40px;background:#17171B"/><div><div class="sc amber">21<span class="muted" style="font-size:.5em"> / 25</span></div><div class="sm">B · Scent S · <b class="jade" style="font-weight:500">recommended</b></div></div></div>
        <div class="opt"><img src="__OPT_A__" alt="Option A"/><div><div class="sc">18<span class="muted" style="font-size:.5em"> / 25</span></div><div class="sm">A · Three Bubbles</div></div></div>
        <div class="opt"><img src="__OPT_C__" alt="Option C"/><div><div class="sc">12<span class="muted" style="font-size:.5em"> / 25</span></div><div class="sm">C · Monoline</div></div></div>
        <div class="src" style="margin-top:1.5vh">Brief: a tea bag plus a scent wisp · scored by the brand judge, <span style="white-space:nowrap">out of 25</span></div><div style="margin-top:2vh"><img src="__LOCK__" alt="" style="height:54px"/></div>
      </div>
    </div>
  </div>
  <aside class="notes"><p>Scores: brand judge, logo v4 (ops/log.md 10:13 B 21/25; A and C as given by the lead). Files: brand/identity/logo-*.svg; options board gallery/brand-v04-logo-options.png.</p></aside>
</div>

<!-- 3 · IDENTITY IN USE -->
<div class="slide bg-night" id="s3" data-steps="0" data-title="Identity in use">
  <div class="g1chip ok">Confirm · Midnight Brew</div>
  <div class="head a"><div class="label">Gate 1 · identity in use</div>
    <div class="h1">Midnight Brew on hero, tin, bag and <em>#ThreeBubbles</em> post.</div></div>
  <div class="body">
    <div class="kit">
      <div class="t" style="grid-row:span 2;background:linear-gradient(#0d0d0f,#101013)"><img src="__HERO__" alt="" style="object-fit:contain"/><span class="lb">Hero</span></div>
      <div class="t"><img src="__TIN__" alt="" style="transform:scale(1.35)"/><span class="lb">12-bag tin</span></div>
      <div class="t"><img src="__BAG__" alt="" style="transform:scale(1.35)"/><span class="lb">Single bag</span></div>
      <div class="t fit"><img src="__SOCIAL__" alt=""/><span class="lb">#ThreeBubbles</span></div>
      <div class="t"><div class="sw">
        <div><i style="background:#0B0B0D"></i>Midnight #0B0B0D</div>
        <div><i style="background:#F2A33A"></i>Amber #F2A33A · hot</div>
        <div><i style="background:#3DBA9B"></i>Jade #3DBA9B · cool</div>
        <div><i style="background:#F3EEE6"></i>Paper #F3EEE6</div>
        <div style="font-size:22px;font-weight:500;letter-spacing:.06em;margin-top:6px">Jost · Every tea has its temperature.</div>
      </div><span class="lb">Palette and type</span></div>
    </div>
  </div>
  <aside class="notes"><p>Files: brand/assets/ (hero.png, pack-tin.png, pack-single-bag.png, social-threebubbles-1080.png), brand/identity/tokens.css. Pulled fresh at every build.</p></aside>
</div>

<!-- 4 · CUSTOMER -->
<div class="slide bg-warm" id="s4" data-steps="0" data-title="Customer">
  <div class="g1chip">Confirm · lead A</div>
  <div class="head a"><div class="label">Gate 1 · the customer</div>
    <div class="h1">First buyer: the <em>curious specialty drinker</em>, 25 to 45, who pays for good leaves; gifts and Ritual bring them in.</div></div>
  <div class="body">
    <div class="g3">
      <div class="card q"><img src="__IC0__" alt="" style="height:52px;align-self:flex-start"/><div class="qt">“I've been steeping this for 20 minutes …”</div><div class="src">weland · Hacker News</div></div>
      <div class="card q"><img src="__IC1__" alt="" style="height:52px;align-self:flex-start"/><div class="qt">“I spend way too much on tea to just throw them away after one steep!”</div><div class="src">hopeofdawn · TeaChat</div></div>
      <div class="card q"><img src="__IC2__" alt="" style="height:52px;align-self:flex-start"/><div class="qt">“…my leaves start not tasting as fresh when I reuse them from the day before.”</div><div class="src">silversun · TeaChat</div></div>
    </div>
    <div class="tiles" style="grid-template-columns:1.4fr 1fr 1fr;margin-top:4vh">
      <div class="tile" style="border-color:rgba(61,186,155,.45)"><div class="k">Route in: tea subscriptions</div><div class="v jade">$530 m <span style="font-size:.5em">+9.1% a year</span></div><div class="w">“preference for premium tea experiences” · Fact.MR 2025</div></div>
      <div class="tile"><div class="k">Segment A · lead</div><div class="v" style="font-size:clamp(20px,1.4vw,26px)">Curious specialty drinker</div><div class="w">32% of UK Gen Z daily tea drinkers choose green tea (YouGov)</div></div>
      <div class="tile"><div class="k">Segment B · or lead with</div><div class="v" style="font-size:clamp(20px,1.4vw,26px)">Gift and Ritual buyer</div><div class="w">7 in 10 would welcome a premium tea gift box (Mintel)</div></div>
    </div>
  </div>
  <aside class="notes"><p>Quotes: weland, Hacker News (trimmed) news.ycombinator.com/item?id=7725580; hopeofdawn and silversun, TeaChat teachat.com/viewtopic.php?p=212298. Sources: truth/customers-market.md §1 (quotes, URLs opened), §2 segments A and B ($530 m Fact.MR, Mintel 7 in 10, YouGov: 32% of Gen Z daily tea drinkers choose green tea; facts.md "32% of UK Gen Z drink green tea" overstates it, flagged to the lead); facts.md Customer (provisional).</p></aside>
</div>

<!-- 5 · MARKET AND MONEY -->
<div class="slide bg-grid top" id="s5" data-steps="0" data-title="Market and money">
  <div class="g1chip">Decision 2 · price · Decision 3 · ask</div>
  <div class="head a"><div class="label">Gate 1 · market, price, ask <span class="prov">provisional</span></div>
    <div class="h1">Tea bags are a <em>$7.1 billion</em> market; premium bags in four countries are $640 million; year 3 $8.3 million.</div></div>
  <div class="body">
    <div class="mbar"><div class="k">TAM · the world's tea bags</div><div><div class="tr"><div class="fl" style="width:100%;background:rgba(243,238,230,.18)"></div><div class="v" style="left:0">$7.1 bn</div></div><div class="w">$18.8 bn tea (Fortune BI 2025) × 38% sold in bags · sourced</div></div></div>
    <div class="mbar"><div class="k">SAM · premium, JP CN UK US</div><div><div class="tr"><div class="fl" style="width:9%;background:var(--jade)"></div><div class="v jade" style="left:9%">$640 m</div></div><div class="w">× 45% four markets × 20% premium · our assumptions</div></div></div>
    <div class="mbar"><div class="k">SOM · OSME year 3</div><div><div class="tr"><div class="fl" style="width:.5%;background:var(--amber);min-width:8px"></div><div class="v amber" style="left:.5%">$8.3 m</div></div><div class="w">6.5 m bags × $1.28 avg (70% direct at $1.50, 30% retail at $0.75) · assumption · validator</div></div></div>
    <div class="tiles"><span class="prov" style="position:absolute;margin:-34px 0 0 0">provisional: tin, Ritual, ask</span>
      <div class="tile" style="border-color:rgba(242,163,58,.45)"><div class="k">Every bag · locked</div><div class="v">$1.50</div><div class="w">single, tin and Ritual · team 10:23</div></div>
      <div class="tile"><div class="k">12-bag tin</div><div class="v">$18</div><div class="w">3 cups a bag (assumption) · $0.50 a cup</div></div>
      <div class="tile"><div class="k">Ritual</div><div class="v">$24<span class="muted" style="font-size:.5em"> / month</span></div><div class="w">16 bags · ~60% gross margin</div></div>
      <div class="tile" style="border-color:rgba(242,163,58,.45)"><div class="k">The ask</div><div class="v amber">$2.5 m</div><div class="w">SAFE · $10 m pre ($12.5 m post cap) · 20% dilution · 24 months runway</div></div>
    </div>
  </div>
  <aside class="notes"><p>Sources: facts.md (Price, Market, The ask, all provisional 10:05); truth/business-case.md §1 to §5. Validation: judge/business-validation.md (17 PASS, 5 FAIL, 1 ASK at 10:2x): single bag $1.50 vs $2.00; margin 59.7% at COGS midpoint $0.605; LTV $205, LTV:CAC 2.7x; year-3 average price $1.275 gives SOM $8.3 m (facts.md still says $9 m, which needs $2.00 singles; flagged to the lead); price locked at $1.50 everywhere by the team at 10:23 (facts.md Price); 20 k Keepers x $288 is an end-of-year run-rate.</p></aside>
</div>

<!-- 6 · DECISIONS -->
<div class="slide bg-mesh" id="s6" data-steps="0" data-title="Decisions">
  <div class="head a"><div class="label">Gate 1 · decide now</div>
    <div class="h1">Four decisions unlock the pitch, the site and the film: <em>logo, price, ask, Kling</em>.</div></div>
  <div class="body">
    <div class="dec"><div class="card conf" style="grid-column:span 2;min-height:0;padding:2vh 2.4vw;flex-direction:row;align-items:center;gap:2vw"><div class="q1">Confirm together</div><div class="rec" style="font-size:clamp(22px,1.6vw,30px)">Name OSME · Midnight Brew · lead customer A</div></div>
      <div class="card" style="flex-direction:row;align-items:center;gap:2vw"><img src="__SYM__" alt="" style="height:12vh"/><div style="display:flex;flex-direction:column;gap:12px"><div class="q1">1 · Logo</div><div class="rec">B, Scent S</div><div class="alt">21 / 25 · A Three Bubbles 18 · C Monoline 12</div></div></div>
      <div class="card"><div class="q1">2 · Price · locked 10:23 · confirm</div><div class="rec">$1.50 a bag everywhere</div><div class="alt" style="color:var(--text)">year 3 $8.3 m · tin $18 · Ritual $24 a month</div><div class="alt">Reopen? $2.00 singles: year 3 $9 m, tin saves 25%</div></div>
      <div class="card"><div class="q1">3 · The ask <span class="prov">provisional</span></div><div class="rec">$2.5 m SAFE at <span style="white-space:nowrap">$10 m pre-money</span></div><div class="alt">$12.5 m post cap · 20% dilution · 24 months runway · funds the food-safe membrane and the first Ritual boxes</div></div>
      <div class="card"><div class="q1">4 · Kling film credits</div><div class="rec">No for now <span class="muted" style="font-size:.6em">(user, 10:25)</span></div><div class="alt">confirm, or reopen: 3 film inserts ~150 + 3 stills ~50 = ~200 of 322 credits · nothing spent</div></div>
    </div>
  </div>
  <aside class="notes"><p>Kling: ops/log.md 10:25 video-lead "user: go, no Kling", shown as the current answer to confirm. Balance 322 credits, Standard; film inserts ~50 credits each (video, ops/questions.md 10:11), stills ~8 to 16 each, ~50 for 3 (brand, 10:11). Questions logged in ops/questions.md. Recommendations from facts.md (provisional) and brand judge scores.</p></aside>
</div>
"""

JS = (bp.JS.replace("document.getElementById('demo').addEventListener", "document.getElementById('demo')&&document.getElementById('demo').addEventListener")
      .replace("else if(k==='d'||k==='D'){if(cur!==2)goto(2,0);demo(!document.body.classList.contains('demo'));}", "")
      .replace("if(cur===2)fitDemo();", "").replace("if(n===2)setTimeout(fitDemo,50);", "")
      .replace("/^[1-8]$/", "/^[1-6]$/"))

page = (bp.PAGE.replace("__CSS__", CSS).replace("__SLIDES__", SLIDES).replace("__JS__", JS)
        .replace("<title>OSME · a tea bag that opens only at its perfect temperature</title>", "<title>OSME · Gate 1 decisions</title>")
        .replace(" · D live demo full screen · Space pours", "").replace(" · D live demo", "").replace(" · Esc leave demo", "")
        .replace("1 to 8 jump", "1 to 6 jump")
        .replace("__FONTX__", FONTX).replace("__FONT__", bp.FONT).replace("__LOCKUP__", LOCK).replace("__LOCK__", LOCK).replace("__SYM__", SYM)
        .replace("__OPT_A__", OPT_A).replace("__OPT_C__", OPT_C).replace("__HERO__", HERO).replace("__TIN__", TIN)
        .replace("__BAG__", BAG).replace("__SOCIAL__", SOCIAL)
        .replace("__IC0__", ICONS[0]).replace("__IC1__", ICONS[1]).replace("__IC2__", ICONS[2]))
(D / "gate1.html").write_text(page, encoding="utf8")
print("wrote", D / "gate1.html", len(page) // 1024, "KB")
