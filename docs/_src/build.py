#!/usr/bin/env python3
"""Build the OSME shop into docs/*.html. Every page is self-contained (embed-html runs at the end).

Run: python3 docs/_src/build.py   (from anywhere). Sources: docs/_src/*, brand/identity, brand/assets, video/.
Numbers come from facts.md: prices, tea windows, proof points. Change them there first, then here.
"""
import html, os, re, subprocess, sys, urllib.parse

SRC = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(SRC)
ROOT = os.path.dirname(DOCS)
EMBED = os.path.expanduser("~/Library/CloudStorage/OneDrive-SiemensAG/AI-Presales-Workspace/personal-library/bin/embed-html")
SITE_URL = "https://mendixmau.github.io/table5-waterproof-tea/"

def rd(*p):
    with open(os.path.join(*p), encoding="utf-8") as f:
        return f.read()

# ---------------------------------------------------------------- facts (facts.md)
PRICE_BAG, PRICE_TIN, PRICE_RITUAL = 1.50, 18, 24
TEAS = [
    dict(id="gyokuro", notes="Sweet · deep · umami", name="Gyokuro", country="Japan", origin="Uji", kind="Shade-grown green", open=60, seal=50, liquor="#B8C86A",
         line="Shade-grown and sweet. Cool water, small cup, slow sip.",
         about="Gyokuro is shaded for weeks before picking, which makes it sweet and deep. Hot water ruins it, so it needs the lowest window of all: the bag waits until the water has cooled to 60 °C."),
    dict(id="sencha", notes="Bright · grassy · a little sweet", name="Sencha", country="Japan", origin="Shizuoka", kind="Everyday green", open=80, seal=70, liquor="#C9C25E",
         line="Japan's everyday green. Pour to the last drop; it carries the best of the cup.",
         about="Sencha is the cup Japan drinks every day: bright, grassy, a little sweet. Boiling water makes it bitter. The bag stays sealed until the water cools to 80 °C, brews, and seals again below 70 °C. This is the tea in our live demo."),
    dict(id="longjing", notes="Roasted chestnut · smooth · fresh", name="Longjing", country="China", origin="Hangzhou", kind="Dragon Well green", open=85, seal=75, liquor="#D6C77A",
         line="Dragon Well. Watch the flat leaves stand up and dance.",
         about="Longjing, Dragon Well, comes from the hills around Hangzhou's West Lake. Its pan-fired, flat leaves taste of roasted chestnut. It opens at 85 °C and seals again below 75 °C."),
    dict(id="tieguanyin", notes="Orchid · honey · creamy", name="Tieguanyin", country="China", origin="Fujian", kind="Oolong", open=95, seal=85, liquor="#D9A845",
         line="The Iron Goddess. Many short cups; each one opens the leaf a little more.",
         about="Tieguanyin, the Iron Goddess of Mercy, is an oolong from Fujian, made for gongfu cha: many short steeps from one leaf. It opens at 95 °C and seals again below 85 °C."),
    dict(id="puerh", notes="Earthy · deep · smooth", name="Pu-erh", country="China", origin="Yunnan", kind="Aged dark tea", open=100, seal=95, liquor="#6B2E12",
         line="Aged leaf, deep and earthy. Short, hot, again and again.",
         about="Pu-erh is aged leaf from Yunnan, deep and earthy. It wants the water at the boil and a short steep, again and again: it opens at 100 °C and seals below 95 °C."),
    dict(id="english-breakfast", notes="Malty · strong · good with milk", name="English Breakfast", country="Britain", origin="Blend", kind="Black tea", open=100, seal=90, liquor="#93441A",
         line="Britain's morning cup. Freshly boiled, a splash of milk if you like.",
         about="Britain's morning cup, strong enough for milk. It opens at the boil, so it never waits; it seals again below 90 °C, so the cup never stews."),
]
CULTURE = {
    "Japan": "Chanoyu and the everyday cup of Sencha. Ichi-go ichi-e: “each meeting should be treasured, for it can never be reproduced.”",
    "China": "Where Lu Yu wrote the Classic of Tea in the 760s, and where gongfu cha brews one leaf again and again.",
    "Britain": "Afternoon tea since about 1840, and about 100 million cups a day in the UK.",
}
QUOTES = [
    ("I spend way too much on tea to just throw them away after one steep!", "hopeofdawn", "TeaChat forum", "https://www.teachat.com/viewtopic.php?p=212298", "OSME brews again"),
    ("Some tea tastes bitter the second time around with the bag.", "leroy_the_mule", "Straight Dope forum", "https://boards.straightdope.com/t/do-you-re-use-tea-bags/85495", "OSME stops itself"),
    ("My leaves start not tasting as fresh when I reuse them from the day before.", "silversun", "TeaChat forum", "https://www.teachat.com/viewtopic.php?p=212298", "OSME keeps the scent"),
]
SOURCES = [
    ("Lu Yu’s three boils, in Okakura Kakuzō, <em>The Book of Tea</em> (1906), ch. II.", "https://en.wikisource.org/wiki/The_Book_of_Tea/Chapter_II", "wikisource.org"),
    ("The Classic of Tea, written in the 760s.", "https://en.wikipedia.org/wiki/The_Classic_of_Tea", "wikipedia.org"),
    ("Thomas Sullivan’s tea bags, about 1908.", "https://en.wikipedia.org/wiki/Tea_bag", "wikipedia.org"),
    ("96% of UK tea is brewed from a bag. QMUL, 2016.", "https://www.qmul.ac.uk/news/latest-news/2016/hss/why-britain-is-losing-its-taste-for-tea--and-how-hipsters-could-revive-it.html", "qmul.ac.uk"),
    ("About 100 million cups a day in the UK. UK Tea &amp; Infusions Association.", "https://www.tea.co.uk/tea-faqs", "tea.co.uk"),
    ("Sencha at 80 °C.", "https://en.wikipedia.org/wiki/Sencha", "wikipedia.org"),
    ("Chanoyu and ichi-go ichi-e.", "https://en.wikipedia.org/wiki/Japanese_tea_ceremony", "wikipedia.org"),
    ("Gongfu cha.", "https://en.wikipedia.org/wiki/Gongfu_tea_ceremony", "wikipedia.org"),
    ("Afternoon tea, about 1840.", "https://en.wikipedia.org/wiki/Tea_in_the_United_Kingdom", "wikipedia.org"),
    ("Temperature-gated membranes (PNIPAm) open and close with heat over repeated cycles.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC9920928/", "pmc.ncbi.nlm.nih.gov"),
    ("32% of Gen Z daily tea drinkers choose green tea. YouGov.", "https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation", "yougov.com"),
    ("7 in 10 would welcome a premium tea gift box. Mintel UK.", "https://www.mintel.com/insights/food-and-drink/flavoured-teas-could-brew-success-for-brands-this-festive-season/", "mintel.com"),
    ("Tea drinkers’ own words: TeaChat and Straight Dope.", "https://www.teachat.com/viewtopic.php?p=212298", "teachat.com"),
    ("Tea windows per tea: OSME brewing profiles (design targets), the same as the live demo.", None, None),
]

def money(v):
    return f"${v:.2f}" if isinstance(v, float) and v % 1 else f"${int(v)}"

def deg(t):
    return f"{t}&nbsp;°C"

# ---------------------------------------------------------------- logo (brand/identity, re-read every build)
def logo_symbols():
    lock = rd(ROOT, "brand/identity/logo-lockup.svg")
    sym = rd(ROOT, "brand/identity/logo-symbol.svg")
    out = []
    for name, svg, pre in (("osme-lockup", lock, "lk"), ("osme-symbol", sym, "sy")):
        vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
        inner = re.sub(r"^<svg[^>]*>|</svg>\s*$", "", svg.strip())
        ids = re.findall(r'id="([^"]+)"', inner)
        for i in ids:
            inner = inner.replace(f'id="{i}"', f'id="{pre}-{i}"').replace(f"url(#{i})", f"url(#{pre}-{i})")
        defs = re.search(r"<defs>(.*?)</defs>", inner, re.S)
        d = defs.group(1) if defs else ""
        body = inner.replace(defs.group(0), "") if defs else inner
        out.append((name, vb, d, body))
    defs = "".join(d for _, _, d, _ in out)
    syms = "".join(f'<symbol id="{n}" viewBox="{vb}">{b}</symbol>' for n, vb, _, b in out)
    vbs = {n: vb for n, vb, _, _ in out}
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{defs}{syms}</defs></svg>', vbs

def favicon():
    return "data:image/svg+xml," + urllib.parse.quote(rd(ROOT, "brand/identity/logo-favicon.svg"), safe=" =:/'")

# ---------------------------------------------------------------- tin art per tea (SVG, page font = Jost)
def tin_svg(t, w="100%"):
    tid = t["id"]
    return f'''<svg class="tin" viewBox="0 0 400 480" width="{w}" role="img" aria-label="OSME {html.escape(t['name'])} tin">
<defs><linearGradient id="tb-{tid}" x1="0" x2="1"><stop offset="0" stop-color="#08080A"/><stop offset=".3" stop-color="#25252B"/><stop offset=".45" stop-color="#1B1B20"/><stop offset="1" stop-color="#0A0A0C"/></linearGradient>
<linearGradient id="ta-{tid}" x1="0" x2="1"><stop offset="0" stop-color="#F2A33A"/><stop offset=".48" stop-color="#D9C46B"/><stop offset="1" stop-color="#3DBA9B"/></linearGradient>
<radialGradient id="tg-{tid}" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{t['liquor']}" stop-opacity=".35"/><stop offset="1" stop-color="{t['liquor']}" stop-opacity="0"/></radialGradient></defs>
<ellipse cx="200" cy="440" rx="170" ry="26" fill="url(#tg-{tid})"/>
<rect x="88" y="70" width="224" height="370" rx="18" fill="url(#tb-{tid})" stroke="#2E2E35"/>
<rect x="82" y="58" width="236" height="62" rx="14" fill="url(#tb-{tid})" stroke="#34343B"/>
<rect x="88" y="404" width="224" height="22" fill="{t['liquor']}" opacity=".85"/><rect x="82" y="112" width="236" height="3" fill="{t['liquor']}" opacity=".9"/>
<use href="#osme-symbol" x="178" y="142" width="44" height="44"/>
<text x="200" y="222" text-anchor="middle" font-family="Jost, Futura, sans-serif" font-weight="500" font-size="22" letter-spacing="7" fill="#F3EEE6">OSME</text>
<text x="200" y="272" text-anchor="middle" font-family="Jost, Futura, sans-serif" font-weight="500" font-size="{20 if len(t['name']) < 12 else 15}" letter-spacing="5" fill="{t['liquor'] if t['id'] not in ('puerh','english-breakfast') else '#E0A167'}">{html.escape(t['name'].upper())}</text>
<text x="200" y="296" text-anchor="middle" font-family="Jost, Futura, sans-serif" font-size="10.5" letter-spacing="2.6" fill="#8E8A83">{html.escape(t['country'].upper())} · OPENS AT {t['open']} °C</text>
<rect x="98" y="314" width="204" height="2.5" rx="1.2" fill="url(#ta-{tid})"/>
<text x="200" y="352" text-anchor="middle" font-family="Jost, Futura, sans-serif" font-size="9" letter-spacing="1.6" fill="#BDB7AD">12 BAGS · UP TO 3 INFUSIONS</text>
<text x="200" y="398" text-anchor="middle" font-family="Jost, Futura, sans-serif" font-size="10" fill="#6E6A64">Every tea has its temperature.</text>
</svg>'''

def window_gauge(t):
    """Small horizontal scale 40..100 °C with the tea's window lit."""
    lo, hi = 40, 100
    x = lambda v: 10 + (v - lo) / (hi - lo) * 280
    x1, x2 = x(t["seal"]), x(t["open"])
    ticks = "".join(f'<text x="{x(v):.0f}" y="44" text-anchor="middle">{v}°</text>' for v in (40, 60, 80, 100))
    return f'''<svg class="gauge" viewBox="0 0 300 50" aria-hidden="true"><rect x="10" y="16" width="280" height="6" rx="3" fill="#2A2A30"/>
<rect x="{x1:.1f}" y="13" width="{max(x2-x1,6):.1f}" height="12" rx="6" fill="{t['liquor']}" stroke="#D9C46B" stroke-width="1"/>
<g font-family="Jost, sans-serif" font-size="10" fill="#8E8A83">{ticks}</g></svg>'''

# ---------------------------------------------------------------- shared chrome
NAV = [("shop.html", "Shop"), ("ritual.html", "Ritual"), ("story.html", "Our story"), ("keepers.html", "Keepers"), ("index.html#how", "How it works")]

def nav(active, vbs):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{n}</a></li>' for h, n in NAV)
    return f'''<nav class="top"><div class="wrap">
<a class="logo" href="index.html" aria-label="OSME home"><svg viewBox="{vbs['osme-lockup']}" role="img" aria-label="OSME"><use href="#osme-lockup"/></svg></a>
<ul class="links">{links}</ul>
<div class="nav-r"><button class="cart-btn" type="button" data-open-cart aria-label="Open cart"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M5 8h14l-1.2 11.2a2 2 0 0 1-2 1.8H8.2a2 2 0 0 1-2-1.8z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8" fill="none" stroke="currentColor" stroke-width="1.6"/></svg><span class="cart-n" data-cart-n>0</span></button>
<a class="btn primary sm" href="keepers.html#join">Join the waitlist</a>
<button class="menu-btn" type="button" aria-label="Menu" data-menu><span></span><span></span></button></div>
</div>
<div class="mobile-menu" data-mobile-menu><ul>{links}<li class="cta"><a class="btn primary" href="keepers.html#join">Join the waitlist</a></li></ul></div></nav>'''

def cart_drawer():
    return '''<div class="drawer-bg" data-close-cart></div>
<aside class="drawer" aria-label="Your cart" aria-hidden="true">
  <header><div class="eyebrow">Your cart</div><button type="button" class="x" data-close-cart aria-label="Close">×</button></header>
  <div class="drawer-items" data-cart-items></div>
  <div class="drawer-foot">
    <div class="total"><span>Total</span><b data-cart-total>$0</b></div>
    <p class="muted small" data-cart-percup></p>
    <div class="preorder" data-preorder>
      <p class="small">OSME ships after our food-safe proof. Pre-order now: we save your cart and write when your first box is ready.</p>
      <form class="wl" data-waitlist="cart" novalidate>
        <input type="email" name="email" placeholder="Your email" aria-label="Your email" autocomplete="email">
        <button class="btn primary" type="submit">Pre-order: join the waitlist</button>
      </form>
      <div class="wl-msg" role="status" aria-live="polite"></div>
    </div>
  </div>
</aside>'''

def footer(vbs, sources=True):
    src = ""
    if sources:
        items = "".join(f'<li>{t}' + (f' <a href="{u}" target="_blank" rel="noopener">{d}</a>' if u else "") + "</li>" for t, u, d in SOURCES)
        src = f'<h4>Sources</h4><ol class="sources">{items}</ol>'
    return f'''<footer class="site"><div class="wrap">
<div class="top">
  <div><svg class="flogo" viewBox="{vbs['osme-lockup']}" role="img" aria-label="OSME"><use href="#osme-lockup"/></svg>
  <p class="muted" style="margin-top:14px;max-width:340px">Every tea has its temperature. A tea bag that opens only at its perfect temperature.</p></div>
  <div class="fcols">
    <div><h4>Shop</h4><a href="shop.html">All teas</a><a href="ritual.html">The Ritual</a><a href="tea-sencha.html">Sencha</a><a href="demo.html">Live demo</a></div>
    <div><h4>OSME</h4><a href="story.html">Our story</a><a href="keepers.html">Keepers</a><a href="keepers.html#join">Waitlist</a><a href="index.html#how">How it works</a></div>
  </div>
</div>
{src}
<div class="fine"><span>OSME · said “oz-MAY” · Greek osmē, scent. A concept by Table 5, “Sell the unsellable”, 2026.</span><span>Launch prices in US dollars. Pre-orders ship after the food-safe proof.</span></div>
</div></footer>'''

def page(fname, title, desc, active, body, vbs, extra_js=""):
    css = rd(SRC, "base.css") + rd(SRC, "shop.css")
    js = rd(SRC, "site.js") + rd(SRC, "hero.js") + rd(SRC, "slider.js") + extra_js
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<link rel="icon" href="{favicon()}">
<style>
@font-face{{font-family:"Jost";src:url(../brand/assets/fonts/jost-latin.woff2) format("woff2");font-weight:300 700;font-display:swap}}
{css}
</style>
</head>
<body>
{LOGO_DEFS}
{nav(active, vbs)}
<main>
{body}
</main>
{footer(vbs)}
{cart_drawer()}
<div class="toast" role="status" aria-live="polite" data-toast></div>
<script>
(function(){{
"use strict";
var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
{js}
}})();
</script>
</body>
</html>
'''
    with open(os.path.join(DOCS, fname), "w", encoding="utf-8") as f:
        f.write(doc)
    return fname

# ---------------------------------------------------------------- building blocks
def tea_card(t):
    return f'''<article class="tea-card" data-country="{t['country']}">
<a class="tc-img" href="tea-{t['id']}.html" aria-label="{t['name']}">{tin_svg(t)}</a>
<div class="tc-body">
  <div class="eyebrow">{t['country']} · {t['origin']}</div>
  <h3><a href="tea-{t['id']}.html">{t['name']}</a></h3>
  <div class="tc-window"><i class="liquor" style="background:{t['liquor']}"></i>Opens at {deg(t['open'])} · seals below {deg(t['seal'])}</div>
  <div class="tc-buy">
    <button class="btn sm primary" type="button" data-add="{t['id']}:tin">Tin {money(PRICE_TIN)}</button>
    <button class="btn sm" type="button" data-add="{t['id']}:bag">Bag {money(PRICE_BAG)}</button>
  </div>
</div></article>'''

def quotes_block():
    q = "".join(f'''<figure class="quote"><q>{html.escape(a)}</q><div><div class="fix">{f}</div><cite>{b}, <a href="{u}" target="_blank" rel="noopener">{c}</a></cite></div></figure>''' for a, b, c, u, f in QUOTES)
    return f'<div class="quotes">{q}</div>'

def waitlist_block(heading='Take back one cup a day.<br><span class="arc-text">Become a Keeper.</span>', sub="The first Ritual boxes go to the waitlist first."):
    return f'''<div class="join" id="join">
  <div><div class="eyebrow">Join the waitlist</div><h2>{heading}</h2><p class="muted">{sub}</p>
  <div class="kcount" data-keeper-count hidden></div></div>
  <div><form class="wl" data-waitlist="page" novalidate>
    <input type="email" name="email" placeholder="Your email" aria-label="Your email" autocomplete="email">
    <button class="btn primary" type="submit">Join the waitlist</button></form>
  <div class="wl-msg" role="status" aria-live="polite"></div>
  <div class="wl-note" data-wl-note></div></div>
</div>'''

def three_steps():
    return f'''<div class="steps">
  <article class="step hot"><div class="num">01</div>
    <svg class="mini" viewBox="0 0 200 120" aria-hidden="true"><rect x="70" y="18" width="60" height="84" rx="10" fill="#1E1E23" stroke="#F2A33A" stroke-width="2.4"/><path d="M80 44h40M80 62h40M80 80h40" stroke="#F2A33A" stroke-width="1.4" opacity=".6"/><path d="M40 30q-8 -12 0 -24M160 30q8 -12 0 -24" stroke="#F2A33A" stroke-width="2" fill="none" opacity=".5" stroke-linecap="round"/></svg>
    <div class="temp">&gt;80<small>°C</small></div><div class="state">Sealed · too hot</div>
    <p>Pour straight from the kettle. The bag stays shut, so the leaf never scorches.</p></article>
  <article class="step open"><div class="num">02</div>
    <svg class="mini" viewBox="0 0 200 120" aria-hidden="true"><circle cx="100" cy="60" r="56" fill="#D9C46B" opacity=".10"/><rect x="70" y="18" width="60" height="84" rx="10" fill="#1E1E23" stroke="#D9C46B" stroke-width="2.4" stroke-dasharray="6 5"/><path d="M80 44h40M80 62h40M80 80h40" stroke="#D9C46B" stroke-width="1.4" stroke-dasharray="3 4"/><circle cx="52" cy="70" r="5" fill="#C9C25E" opacity=".7"/><circle cx="148" cy="52" r="6" fill="#C9C25E" opacity=".6"/><circle cx="40" cy="44" r="3" fill="#C9C25E" opacity=".5"/><circle cx="160" cy="84" r="4" fill="#C9C25E" opacity=".55"/></svg>
    <div class="temp">80–70<small>°C</small></div><div class="state">Open · its window</div>
    <p>At {deg(80)} the bag opens and the Sencha brews in the water it was made for.</p></article>
  <article class="step cool"><div class="num">03</div>
    <svg class="mini" viewBox="0 0 200 120" aria-hidden="true"><rect x="70" y="18" width="60" height="84" rx="10" fill="#1E1E23" stroke="#3DBA9B" stroke-width="2.4"/><path d="M80 44h40M80 62h40M80 80h40" stroke="#3DBA9B" stroke-width="1.4" opacity=".6"/><circle cx="100" cy="60" r="10" fill="#3DBA9B" opacity=".25"/><circle cx="100" cy="60" r="4" fill="#3DBA9B"/></svg>
    <div class="temp">&lt;70<small>°C</small></div><div class="state">Sealed · scent kept</div>
    <p>Below {deg(70)} it closes. The steep stops itself, never bitter, and the leaf keeps its scent for the next cup.</p></article>
</div>'''

def honest():
    return '<p class="honest"><span class="tag">Honest</span><span><b>The principle exists:</b> lab membranes already open and close with temperature. Our R&amp;D makes it food-safe at 70–90&nbsp;°C. Up to 3 infusions per bag.</span></p>'

FAQ = [
    ("How does the bag know the temperature?", "The principle exists: lab membranes already open and close with temperature. Our R&amp;D makes it food-safe at 70–90&nbsp;°C. Each tea’s bag is tuned to its own window."),
    ("Do I need a special kettle or mug?", "No. Pour from any kettle into any mug. The bag waits for its window, brews, and seals again as the water cools. No thermometer, no timer."),
    ("How many cups from one bag?", "Up to 3 infusions, about $0.50 a cup. Between cups the bag stays sealed, so the leaf keeps its scent."),
    ("When does it ship?", "Pre-orders ship after our food-safe proof. Joining the waitlist costs nothing today; we write before your first box is ready. The Ritual ships free, and you can skip or pause any month."),
]

def faq():
    items = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
    return f'<div class="faq"><div><div class="eyebrow">Questions</div><h2>Good to know.</h2></div><div class="faq-list">{items}</div></div>'

def benefits():
    icons = [("icon-self-stopping.svg", "Stops itself", "Opens in its window, closes as the water cools. Never stewed, never bitter."),
             ("icon-scent-sealed.svg", "Scent kept", "Sealed between cups, so the leaf keeps its scent for the next infusion."),
             ("icon-three-infusions.svg", "Up to 3 cups", "One bag brews up to 3 times: about $0.50 a cup.")]
    return '<div class="benefits">' + "".join(f'<div class="ben"><img src="../brand/assets/{i}" alt="" width="56" height="56"><div><b>{h}</b><p>{p}</p></div></div>' for i, h, p in icons) + "</div>"

# ---------------------------------------------------------------- pages
def home(vbs):
    hero_cup = rd(SRC, "hero-cup.svg")
    teas = "".join(tea_card(t) for t in TEAS[:3])
    body = f'''
<header class="hero" id="top"><div class="wrap">
  <div class="hero-text">
    <div class="eyebrow"><b>OSME</b> &nbsp;·&nbsp; Greek for scent<span class="say"> &nbsp;·&nbsp; said “oz-MAY”</span></div>
    <h1><span>Every tea has</span><span class="arc-text">its temperature.</span></h1>
    <p class="oneliner">A tea bag that <em>opens only at its perfect temperature.</em></p>
    <p class="sub">It stays sealed while the water is too hot, opens to brew, and closes again as the water cools. The steep stops itself, the scent stays in, and the same bag brews again.</p>
    <div class="facts-row">
      <span class="chip"><span class="k">For</span> curious tea drinkers who pay for good leaf and hate a bitter cup</span>
      <span class="chip"><span class="k">Price</span> <b>$1.50</b> a bag · about <b>$0.50</b> a cup · Ritual <b>$24</b>/month</span>
    </div>
    <div class="cta-row"><a class="btn primary" href="shop.html">Shop the teas</a><a class="btn" href="#how">See how it opens</a></div>
  </div>
  <div class="hero-visual" aria-label="Animation: a Sencha bag in a cup stays sealed above 80 °C, opens between 80 and 70 °C, and seals again below 70 °C">
    {hero_cup}
    <div class="hv-caption">Sencha: opens at 80&nbsp;°C, seals below 70&nbsp;°C · cooling sped up</div>
  </div>
</div></header>

<section class="band" aria-label="Lu Yu's three bubbles">
  <video autoplay muted loop playsinline preload="auto" src="_src/loop-web.mp4"></video>
  <div class="wrap band-in">
    <div class="eyebrow">Since the eighth century</div>
    <p class="band-h">Lu Yu read water by its bubbles.<br><span class="arc-text">OSME reads it for you.</span></p>
    <div class="band-steps"><span><i style="background:#3DBA9B;width:9px;height:9px"></i>Fish eyes</span><span><i style="background:#D9C46B;width:12px;height:12px"></i>String of pearls</span><span><i style="background:#F2A33A;width:15px;height:15px"></i>Rolling waves</span></div>
  </div>
</section>

<section id="how"><div class="wrap">
  <div class="eyebrow">How it works · <b>Sencha</b>, Japan</div>
  <h2>Sealed. Open. Sealed.</h2>
  <p class="lead">Boiling water scorches a green tea. An ordinary bag brews at any heat and never stops. An OSME bag waits for its tea’s window, brews inside it, and closes when it is done.</p>
  {three_steps()}
  <div class="tryit">
    <div class="panel">
      <div class="eyebrow">Try it · drag the water temperature</div>
      <input id="tSlider" type="range" min="60" max="100" step="1" value="68" aria-label="Water temperature in degrees Celsius">
      <div class="range-labels"><span>100&nbsp;°C</span><span>60&nbsp;°C</span></div>
      <div class="slider-row" style="margin-top:22px">
        <div class="readout" id="tRead">92<small>°C</small></div>
        <div><div class="sstate" id="tState" style="color:#F2A33A">Sealed · too hot</div>
        <div class="sdesc" id="tDesc">The bag waits. Nothing brews until the water cools to 80&nbsp;°C.</div></div>
      </div>
    </div>
    <div class="panel demo">
      <div><div class="eyebrow">The live demo</div><h3 style="margin:12px 0 10px">Watch two cups side by side.</h3>
      <p>An OSME Sencha bag next to an ordinary 1908 bag, cooling sped up. Six teas, three cultures.</p></div>
      <a class="btn primary" href="demo.html">Try the live demo</a>
    </div>
  </div>
  <figure class="exploded"><div class="ex-scroll"><img src="../shared/product/exploded-view-animated.svg" alt="What is inside an OSME bag: tag and string, seal, outer filter, the temperature membrane and the leaf. The Sencha membrane is sealed above 80 °C, open from 80 to 70 °C, sealed below 70 °C." width="1600" height="1000"></div>
  <figcaption class="muted small">What is inside: five layers, one of them reads the water. <span class="swipe">Swipe to see all of it.</span></figcaption></figure>
  <div class="phone-only">{honest()}</div>
</div></section>

<section id="teas"><div class="wrap">
  <div class="sec-head"><div><div class="eyebrow">The teas</div><h2>Six teas. Six temperatures.</h2>
  <p class="lead">From Japan, China and Britain, each bag tuned to its own window.</p></div>
  <a class="btn" href="shop.html">Shop all six</a></div>
  <div class="tea-grid">{teas}</div>
</div></section>

<section class="ritual-teaser"><div class="wrap">
  <div class="rt">
    <div class="rt-img"><img src="../brand/assets/pack-tin.svg" alt="The OSME Sencha tin"></div>
    <div>
      <span class="badge">Become a Keeper</span>
      <div class="eyebrow" style="color:var(--brand-primary)">The Ritual subscription</div>
      <div class="amt-xl">$24<small> / month</small></div>
      <p class="lead">16 bags from 3-4 origins at your door every month. Free shipping, skip or pause any month. Ritual members are Keepers.</p>
      <div class="cta-row" style="margin-top:22px"><button class="btn primary" type="button" data-add="ritual:ritual">Add the Ritual</button><a class="btn" href="ritual.html">What’s in the box</a></div>
    </div>
  </div>
</div></section>

<section id="who"><div class="wrap">
  <div class="eyebrow">Who it’s for</div>
  <h2>Everyone can be a tea person.</h2>
  <p class="lead">First for the curious cup: people who love tea and its rituals, pay for good leaf and hate a bitter cup. And for anyone who would love to be one, without a thermometer, a timer or a lesson.</p>
  <div class="who-grid">
    <article class="who"><h3>The curious cup</h3><p>You love a good cup and you are exploring: Sencha, oolong, matcha. You pay for good leaf and hate scorching it or throwing it away after one steep.</p><div class="stat"><b>32%</b>of Gen Z daily tea drinkers choose green tea (YouGov)</div></article>
    <article class="who"><h3>The giver</h3><p>You want a present that shows itself: a tin of twelve, the bag opening in the cup. Then the Ritual box every month.</p><div class="stat"><b>7 in 10</b>would welcome a premium tea gift box (Mintel)</div></article>
    <article class="who"><h3>The everyday cup</h3><p>A mug in the morning, no ceremony. You just want it right every time, even when you forget the bag in the cup.</p><div class="stat"><b>96%</b>of UK tea is brewed from a bag (QMUL)</div></article>
  </div>
  {quotes_block()}
</div></section>

<section class="movement"><div class="wrap">{waitlist_block()}</div></section>
'''
    return page("index.html", "OSME · Every tea has its temperature.", "OSME is a tea bag that opens only at its perfect temperature, closes as the water cools, keeps the scent and brews again.", "index.html", body, vbs)

def shop(vbs):
    cards = "".join(tea_card(t) for t in TEAS)
    body = f'''
<header class="page-head"><div class="wrap">
  <div class="eyebrow">Shop</div>
  <h1 class="h1">Every tea has its temperature.</h1>
  <p class="lead">Six teas from Japan, China and Britain. A tin holds 12 bags of one tea, one origin, for {money(PRICE_TIN)}; a single bag is {money(PRICE_BAG)}. Each bag brews up to 3 times, about $0.50 a cup.</p>
  <div class="filters" role="group" aria-label="Filter by culture"><button class="chip-btn on" data-filter="all">All</button><button class="chip-btn" data-filter="Japan">Japan</button><button class="chip-btn" data-filter="China">China</button><button class="chip-btn" data-filter="Britain">Britain</button></div>
</div></header>
<section class="tight"><div class="wrap">
  <a class="ritual-strip" href="ritual.html"><span class="badge">Become a Keeper</span><b>The Ritual · $24/month</b><span>16 bags from 3-4 origins every month · free shipping · skip or pause any month</span><span class="go">→</span></a>
  <div class="tea-grid six" data-tea-grid>{cards}</div>
  {benefits()}
</div></section>
'''
    return page("shop.html", "Shop · OSME", "Six OSME teas from Japan, China and Britain. Tin of 12 $18, single bag $1.50, Ritual $24/month.", "shop.html", body, vbs)

def tea_page(t, vbs):
    others = "".join(tea_card(o) for o in TEAS if o["id"] != t["id"])[:]
    # the single-bag art is labelled Sencha, so only the Sencha page gets the second view
    bag_img = '<img class="p-bag" src="../brand/assets/pack-single-bag.svg" alt="A single OSME Sencha bag">' if t["id"] == "sencha" else ""
    thumbs = '<div class="thumbs" role="group" aria-label="Views"><button type="button" class="on" data-view-btn="tin">The tin</button><button type="button" data-view-btn="bag">The bag</button></div>' if t["id"] == "sencha" else ""
    sencha_note = '<a class="btn" href="demo.html">See Sencha open in the live demo</a>' if t["id"] == "sencha" else ""
    body = f'''
<section class="product"><div class="wrap">
  <div class="crumbs"><a href="shop.html">Shop</a> / <a href="shop.html#{t['country']}">{t['country']}</a> / {t['name']}</div>
  <div class="pgrid">
    <div class="p-gal">
      <div class="p-art" data-view="tin">{tin_svg(t)}{bag_img}</div>
      {thumbs}
    </div>
    <div class="p-info">
      <div class="eyebrow">{t['country']} · {t['origin']} · {t['kind']}</div>
      <h1 class="h1">{t['name']}</h1>
      <p class="p-line">{html.escape(t['line'])}</p>
      <div class="notes"><span class="k">Tasting notes</span>{t['notes']}</div>
      <div class="p-window"><div><span class="k">Opens at</span><b>{deg(t['open'])}</b></div><div><span class="k">Seals below</span><b>{deg(t['seal'])}</b></div><div><span class="k">Infusions</span><b>up to 3</b></div></div>
      {window_gauge(t)}
      <div class="options" role="radiogroup" aria-label="Choose">
        <label class="opt"><input type="radio" name="opt" value="tin" checked><span><b>The tin</b><small>12 bags · made to be given</small></span><em>{money(PRICE_TIN)}</em></label>
        <label class="opt"><input type="radio" name="opt" value="bag"><span><b>Single bag</b><small>up to 3 infusions</small></span><em>{money(PRICE_BAG)}</em></label>
        <label class="opt"><input type="radio" name="opt" value="ritual"><span><b>In the Ritual box</b><small>16 bags from 3-4 origins a month</small></span><em>$24/mo</em></label>
      </div>
      <div class="buy-row"><div class="qty"><button type="button" data-q="-1" aria-label="Less">−</button><span data-qv>1</span><button type="button" data-q="1" aria-label="More">+</button></div>
      <button class="btn primary grow" type="button" data-add-opt="{t['id']}">Add to cart</button></div>
      <p class="muted small">Pre-order. Ships after our food-safe proof. About $0.50 a cup.</p>
      {sencha_note}
    </div>
  </div>
</div></section>
<section class="tight"><div class="wrap">
  <div class="p-cols">
    <div><div class="eyebrow">The tea</div><p class="lead" style="margin-top:12px">{t['about']}</p></div>
    <div><div class="eyebrow">Its culture · {t['country']}</div><p class="lead" style="margin-top:12px">{CULTURE[t['country']]}</p></div>
  </div>
  {benefits()}
</div></section>
<section class="tight"><div class="wrap">{faq()}</div></section>
<section class="tight"><div class="wrap"><div class="sec-head"><div><div class="eyebrow">More teas</div><h2>Each with its own window.</h2></div><a class="btn" href="shop.html">All teas</a></div>
<div class="tea-grid scroll">{others}</div></div></section>
'''
    return page(f"tea-{t['id']}.html", f"{t['name']} · OSME", f"OSME {t['name']}: opens at {t['open']} °C, seals below {t['seal']} °C. Tin of 12 $18, single bag $1.50.", "shop.html", body, vbs)

def ritual(vbs):
    # 16 bags from 3-4 origins: example box this month
    box = [TEAS[1]] * 6 + [TEAS[2]] * 4 + [TEAS[3]] * 3 + [TEAS[5]] * 3
    bags = "".join(f'<i title="{b["name"]}" style="--c:{b["liquor"]}"></i>' for b in box)
    legend = "".join(f'<span><i style="background:{t["liquor"]}"></i>{t["name"]} × {n}</span>' for t, n in ((TEAS[1], 6), (TEAS[2], 4), (TEAS[3], 3), (TEAS[5], 3)))
    body = f'''
<header class="page-head ritual-head"><div class="wrap rgrid">
  <div>
    <span class="badge">Become a Keeper</span>
    <div class="eyebrow" style="color:var(--brand-primary);margin-top:12px">The Ritual subscription</div>
    <h1 class="h1">One box a month.<br><span class="arc-text">One cup a day, made with love.</span></h1>
    <div class="amt-xl">$24<small> / month</small></div>
    <ul class="ticks"><li>16 bags from 3-4 origins</li><li>Up to 3 infusions per bag: about $0.50 a cup</li><li>Free shipping, skip or pause any month</li><li>Ritual members are Keepers</li></ul>
    <div class="cta-row" style="margin-top:26px"><button class="btn primary" type="button" data-add="ritual:ritual">Add the Ritual · $24/month</button></div>
  </div>
  <div class="box-vis">
    <div class="eyebrow">An example box</div>
    <div class="bag-grid">{bags}</div>
    <div class="legend">{legend}</div>
  </div>
</div></header>
<section class="tight"><div class="wrap">
  <div class="eyebrow">How the Ritual works</div>
  <div class="r-steps">
    <div><span class="n">1</span><b>A box at your door</b><p>Every month, 16 bags from 3-4 origins across Japan, China and Britain.</p></div>
    <div><span class="n">2</span><b>Any kettle, any mug</b><p>Pour from the kettle. Each bag waits for its own temperature, brews, and stops itself.</p></div>
    <div><span class="n">3</span><b>Three Bubbles a day</b><p>One cup made with love. Watch the water, take three breaths, share ten seconds with #ThreeBubbles.</p></div>
    <div><span class="n">4</span><b>You are a Keeper</b><p>Keepers of the scent, keepers of the ritual. Skip or pause any month.</p></div>
  </div>
  {benefits()}
</div></section>
<section class="tight"><div class="wrap">{faq()}</div></section>
<section class="movement"><div class="wrap">{waitlist_block('The first boxes go to<br><span class="arc-text">the waitlist first.</span>', 'Join now and we write when your first Ritual box is ready.')}</div></section>
'''
    return page("ritual.html", "The Ritual · OSME", "The OSME Ritual: $24 a month for 16 bags from 3-4 origins, free shipping, skip or pause any month.", "ritual.html", body, vbs)

def story(vbs):
    cult = ""
    for c in ("Britain", "China", "Japan"):  # hot to cool, same order as the culture motif and the deck
        rows = "".join(f'<a class="tea-row" href="tea-{t["id"]}.html"><i class="liquor" style="background:{t["liquor"]}"></i><div><b>{t["name"]}</b><span>{t["origin"]} · {t["kind"].lower()}</span></div><div class="window">{deg(t["open"])}<small>seals below {deg(t["seal"])}</small></div></a>' for t in TEAS if t["country"] == c)
        cult += f'<article class="culture"><header><div class="country">{c}</div><div class="ritual">{CULTURE[c]}</div></header>{rows}</article>'
    body = f'''
<header class="page-head story-head"><div class="wrap">
  <div class="eyebrow">Our story</div>
  <h1 class="h1">1,200 years of temperature.</h1>
  <p class="lead">Every great tea culture learned to read its water. The tea bag made tea easy and forgot the art. OSME brings the art back, inside the bag.</p>
</div></header>
<section class="tight"><div class="wrap">
  <div class="timeline">
    <div class="tl"><div class="yr">760s</div><h3>Lu Yu reads the water</h3><p>China’s <em>Classic of Tea</em> judges water by its bubbles: three stages, three moments.</p><blockquote>“The first boil is when the little bubbles like the eye of fishes swim on the surface.”</blockquote></div>
    <div class="tl"><div class="yr">1908</div><h3>The tea bag trades art for ease</h3><p>Thomas Sullivan’s silk bags make tea fast. One temperature, no stop, one cup. Today 96% of UK tea is brewed from a bag.</p></div>
    <div class="tl"><div class="yr arc-text">Now</div><h3>The art, back in the bag</h3><p>A bag that knows its tea: it opens at the right heat, closes when done, and keeps the scent. Any kettle, any mug.</p></div>
  </div>
</div></section>
<section class="tight"><div class="wrap">
  <img class="motif" src="../brand/assets/culture-motif.svg" alt="Britain, China and Japan: three tea cultures">
  <div class="cultures">{cult}</div>
</div></section>
<section class="tight"><div class="wrap">
  <div class="eyebrow">The name</div>
  <h2>OSME. Greek for scent.</h2>
  <p class="lead">The right temperature opens a tea’s scent; the wrong one changes it. We named the brand after what we protect: the scent of every tea, kept.</p>
  {honest()}
</div></section>
'''
    return page("story.html", "Our story · OSME", "From Lu Yu's three bubbles to the 1908 tea bag to OSME: the art of tea, back in the bag.", "story.html", body, vbs)

def keepers(vbs):
    body = f'''
<header class="page-head"><div class="wrap mv">
  <div>
    <div class="eyebrow">Keepers · the movement</div>
    <div class="manifesto" style="margin-top:22px">
      <p>The world got fast. We forgot to taste it.</p><p>So we go back.</p><div class="gap"></div>
      <p>To <span class="arc-text">art</span>: water read by its bubbles, as Lu Yu did in the eighth century.</p>
      <p>To <span class="arc-text">love</span>: a cup made for someone, at its own temperature.</p>
      <p>To <span class="arc-text">scent</span>: the leaf kept whole between infusions.</p><div class="gap"></div>
      <p class="muted">Technology serves the ritual, never replaces it.</p><p>Breathe in.</p>
      <div class="sig">This is OSME</div>
    </div>
  </div>
  <div class="ritual-card">
    <div class="eyebrow">The daily ritual</div>
    <div class="hashtag arc-text">#ThreeBubbles</div>
    <p class="muted" style="font-size:15px;margin-top:8px">Once a day, one cup made with love. Watch the water through Lu Yu’s three stages and take one breath at each.</p>
    <div class="bubbles">
      <div class="bubble"><div class="b"><i style="width:12px;height:12px;background:#3DBA9B"></i></div><div><b>Fish eyes</b><span>the first small bubbles · breathe in</span></div></div>
      <div class="bubble"><div class="b"><i style="width:18px;height:18px;background:#D9C46B"></i></div><div><b>String of pearls</b><span>beads rising from the bottom · breathe out</span></div></div>
      <div class="bubble"><div class="b"><i style="width:26px;height:26px;background:#F2A33A"></i></div><div><b>Rolling waves</b><span>the full boil · pour</span></div></div>
    </div>
  </div>
</div></header>
<section class="tight"><div class="wrap">
  <div class="k-grid">
    <img src="../brand/assets/social-threebubbles-1080.svg" alt="#ThreeBubbles social post">
    <div>
      <div class="eyebrow">Who are the Keepers</div>
      <h2>Keepers of the scent.<br>Keepers of the ritual.</h2>
      <p class="lead">Every Ritual member is a Keeper. The welcome box says it: “You are now a Keeper.” Share ten seconds of your bag opening in the cup: no faces, no talking, just water and scent.</p>
      <ul class="ticks"><li>First access to new teas and origins</li><li>#ThreeBubbles: one cup a day, together</li><li>Every bag brews up to 3 times: less waste, more cups</li></ul>
    </div>
  </div>
</div></section>
<section class="movement"><div class="wrap">{waitlist_block()}</div></section>
'''
    return page("keepers.html", "Keepers · OSME", "Join the OSME movement: art, love, scent. #ThreeBubbles, one cup a day. Become a Keeper.", "keepers.html", body, vbs)

# ---------------------------------------------------------------- main
def web_loop():
    """Light copy of the film loop for the page band, made fresh from video/osme-loop.mp4 every build."""
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(ROOT, "video/osme-loop.mp4"), "-an", "-vf", "scale=1280:-2",
                    "-c:v", "libx264", "-crf", "30", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                    os.path.join(SRC, "loop-web.mp4")], check=True)

if __name__ == "__main__":
    web_loop()
    LOGO_DEFS, VBS = logo_symbols()
    out = [home(VBS), shop(VBS), ritual(VBS), story(VBS), keepers(VBS)] + [tea_page(t, VBS) for t in TEAS]
    # live demo: the product thread's page, copied as is
    with open(os.path.join(ROOT, "product/index.html"), encoding="utf-8") as f:
        demo = f.read()
    with open(os.path.join(DOCS, "demo.html"), "w", encoding="utf-8") as f:
        f.write(demo)
    out.append("demo.html")
    bad = 0
    for fn in out:
        p = os.path.join(DOCS, fn)
        subprocess.run([EMBED, p], check=True, capture_output=True)
        r = subprocess.run([EMBED, "--check", p], capture_output=True, text=True)
        ok = r.returncode == 0
        bad += not ok
        print(("OK  " if ok else "FAIL"), fn, os.path.getsize(p) // 1024, "KB", "" if ok else r.stdout + r.stderr)
    sys.exit(1 if bad else 0)
