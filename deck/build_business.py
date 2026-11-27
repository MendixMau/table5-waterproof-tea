#!/usr/bin/env python3
"""Build deck/business.html: 4 business-case slides (price ladder, cost stack, margin and price, 640 -> year 3).

Same engine, CSS and JS as deck/pitch.html (imported from build_pitch.py), like build_gate1.py.
Every number comes from deck/model_business.py; sources in truth/business-case.md.

Run: python3 deck/build_business.py
"""
import build_pitch as bp
import model_business as m

R, D = bp.R, bp.D
FONTX = bp.b64(D / "assets-src" / "jost-latin-ext.woff2", "font/woff2")
SYM = bp.logo("logo-symbol.svg")


def usd(x, d=2):
    return f"${x:,.{d}f}"


def mn(x):
    return f"${x / 1e6:.1f}\u00a0m"


CSS = bp.CSS + r"""
@font-face{font-family:"Jost";src:url(__FONTX__) format("woff2");font-weight:300 700;unicode-range:U+0100-02BA,U+1E00-1EFF}
.src{font-size:clamp(16px,1vw,19px)}
body.s0 #brandmark{opacity:.55}
.h1{font-size:clamp(26px,2.2vw,44px)}
.label{font-size:15px}
/* ladder */
.lad{display:flex;flex-direction:column;gap:1.25vh;margin-top:1vh}
.lr{display:grid;grid-template-columns:20em 1fr;align-items:center;gap:22px}
.lr .nm{font-size:clamp(17px,1.15vw,22px);color:rgba(243,238,230,.82);text-align:right}
.lr .nm small{display:block;font-size:.72em;color:var(--muted);letter-spacing:.04em}
.lr .tr{height:5.2vh;max-height:56px;position:relative}
.lr .fl{height:100%;border-radius:8px;background:rgba(243,238,230,.16);min-width:6px}
.lr .vl{position:absolute;top:50%;transform:translateY(-50%);font-size:clamp(20px,1.45vw,28px);font-weight:500;padding-left:14px;white-space:nowrap}
.lr.os .nm{color:var(--text);font-weight:500}
.lr.os .fl{background:var(--arc);box-shadow:0 0 28px rgba(242,163,58,.35)}
.lr.os .vl{color:var(--amber)}
/* cost stack */
.cs{display:grid;grid-template-columns:1.25fr 1fr;gap:4vw;align-items:end}
.stk{display:flex;gap:5vw;align-items:flex-end;justify-content:center;height:58vh}
.col{display:flex;flex-direction:column;align-items:center;gap:12px;width:15vw}
.col .tot{font-size:clamp(44px,3.6vw,72px);font-weight:500;line-height:1}
.col .yr{font-size:clamp(16px,1.05vw,20px);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.col .pile{width:100%;display:flex;flex-direction:column-reverse;border-radius:10px;overflow:hidden}
.col .pile div{display:flex;align-items:center;justify-content:center;font-size:clamp(15px,1vw,19px);font-weight:600;color:#0B0B0D}
.leg{display:flex;flex-direction:column;gap:12px}
.leg .li{display:grid;grid-template-columns:18px 1fr auto auto;gap:14px;align-items:center;font-size:clamp(17px,1.1vw,21px);color:rgba(243,238,230,.82);padding:6px 0;border-bottom:1px solid var(--line)}
.leg .li b{width:18px;height:18px;border-radius:4px;display:block}
.leg .li span{font-variant-numeric:tabular-nums;min-width:4em;text-align:right}
.leg .hd{color:var(--muted);font-size:14px;letter-spacing:.16em;text-transform:uppercase;border:0}
.oneoff{margin-top:3vh;padding-top:2vh;border-top:2px solid transparent;border-image:var(--arc) 1}
/* margin + price */
.mg{display:grid;grid-template-columns:.75fr 1.6fr;gap:4vw;align-items:center}
.mgb{display:flex;flex-direction:column;gap:2.4vh}
.mgb .big{font-size:clamp(80px,7vw,140px);color:var(--jade)}
.pt{width:100%;border-collapse:collapse;font-size:clamp(20px,1.4vw,27px)}
.pt th{font-weight:500;font-size:clamp(22px,1.6vw,32px);padding:14px 12px;text-align:right}
.pt th:first-child,.pt td:first-child{text-align:left;color:var(--muted);font-size:clamp(17px,1.15vw,22px);font-weight:400}
.pt td{white-space:nowrap;padding:1.9vh 14px;text-align:right;border-top:1px solid var(--line);font-variant-numeric:tabular-nums}
.pt .rec{background:rgba(61,186,155,.09);color:var(--text)}
.pt th.rec{color:var(--jade);border-radius:12px 12px 0 0}
.pt .now{background:rgba(242,163,58,.07)}
.pt th.now{color:var(--amber)}
.pt tr:last-child .rec{border-radius:0 0 12px 12px}
/* walk */
.wk{display:grid;grid-template-columns:1.45fr 1fr;gap:4vw;align-items:center}
.funnel{display:flex;flex-direction:column;gap:1.4vh}
.fr{display:grid;grid-template-columns:12em 1fr;gap:20px;align-items:center}
.fr .k{font-size:clamp(16px,1.05vw,20px);color:var(--muted);text-align:right;letter-spacing:.04em;line-height:1.25}
.fr .b{height:6.4vh;border-radius:10px;display:flex;align-items:center;padding:0 18px;font-size:clamp(20px,1.4vw,27px);font-weight:500;color:#0B0B0D;white-space:nowrap}
.fr .b.ghost{background:rgba(243,238,230,.07);color:var(--text);border:1px solid var(--line)}
.eq{font-size:clamp(17px,1.1vw,21px);line-height:1.5;color:rgba(243,238,230,.8)}
.eq b{color:var(--text);font-weight:500}
.bench{display:flex;flex-direction:column;gap:10px;margin-top:2.4vh}
.bench .bi{display:grid;grid-template-columns:1fr auto;font-size:clamp(16px,1.05vw,20px);color:rgba(243,238,230,.78);border-bottom:1px solid var(--line);padding:6px 0}
.bench .bi.os{color:var(--amber)}
"""


def ladder():
    top = max(v for _, v, _, _ in m.LADDER)
    rows = []
    for i, (nm, v, note, _) in enumerate(m.LADDER):
        os_ = nm.startswith("OSME")
        w = max(v / top * 78, 0.6)
        sub = f"<small>{note}</small>" if note else ""
        ghost = ""
        if os_:
            g = m.PRICE / top * 78
            ghost = (f'<div style="position:absolute;left:0;top:0;bottom:0;width:{g:.1f}%;border:2px dashed rgba(242,163,58,.55);border-radius:8px"></div>'
                     f'<div class="vl" style="left:{g:.1f}%;color:rgba(243,238,230,.6);font-size:clamp(16px,1.05vw,20px)">one cup only: {usd(m.PRICE)}</div>')
        rows.append(f'<div class="lr{" os" if os_ else ""}"><div class="nm">{nm}{sub}</div>'
                    f'<div class="tr">{ghost}<div class="fl" style="width:{w:.1f}%;position:relative"></div>'
                    f'<div class="vl" style="left:{w:.1f}%">{usd(v)}</div></div></div>')
    return "\n".join(rows)


COLS = ["#6B665E", "#F2A33A", "#8A847A", "#A39C90", "#C2BAAD"]


def stack():
    y1, y3 = m.cogs(1), m.cogs(3)
    H = 46  # vh for the year-1 pile
    def pile(i):
        tot = y1 if i == 0 else y3
        segs = "".join(f'<div style="height:{v[i] / y1 * H:.2f}vh;background:{c}">{usd(v[i]) if v[i] / y1 * H > 3.2 else ""}</div>'
                       for (k, v), c in zip(m.COST.items(), COLS))
        return segs, tot
    p1, _ = pile(0)
    p3, _ = pile(1)
    leg = "".join(f'<div class="li"><b style="background:{c}"></b>{k}<span>{usd(v[0])}</span><span>{usd(v[1])}</span></div>'
                  for (k, v), c in zip(m.COST.items(), COLS))
    oo = " · ".join(f"{k} <b>${v / 1e3:,.0f} k</b>" for k, v in m.ONE_OFF.items())
    return p1, p3, y1, y3, leg, oo


def price_table():
    cols = [m.walk(p) for p in (1.50, 2.00, 2.50)]
    cls = ["now", "rec", ""]
    head = "".join(f'<th class="{c}">{usd(w["price"])}<div class="src" style="font-weight:400;margin-top:4px">{t}</div></th>'
                   for w, c, t in zip(cols, cls, ["today", "recommended", "ceiling"]))
    rows = [
        ("Price per cup (3 cups)", lambda w: usd(w["cup"])),
        ("Gross margin a bag, direct", lambda w: f'{usd(w["gm_d2c"])} · {w["gm_d2c_pct"]:.0%}'),
        ("Gross margin a bag, retail", lambda w: f'{usd(w["gm_ret"])} · {w["gm_ret_pct"]:.0%}'),
        ("Ritual box a month", lambda w: usd(w["ritual"], 0)),
        ("Ritual contribution a month", lambda w: usd(w["contrib"])),
        ("CAC payback ($75)", lambda w: f'{w["payback"]:.1f} months'),
        ("Lifetime value : CAC", lambda w: f'{w["ltv_cac"]:.1f}x'),
    ]
    body = "".join("<tr><td>" + k + "</td>" + "".join(f'<td class="{c}">{f(w)}</td>' for w, c in zip(cols, cls)) + "</tr>"
                   for k, f in rows)
    return f'<table class="pt"><tr><th></th>{head}</tr>{body}</table>'


def build():
    e = m.econ(m.PRICE)
    w = m.walk(m.PRICE)
    p1, p3, y1, y3, leg, oo = stack()
    rit, tins, ret = w["rev_ritual"], w["rev_tins"], w["rev_retail"]
    mx = m.SAM
    slides = f"""
<!-- 1 · PRICE LADDER -->
<div class="slide bg-grid" id="s1" data-steps="0" data-title="Price per cup">
  <div class="head a"><div class="label">Business · price per cup</div>
    <div class="h1">At $1.50 a bag and three cups, an OSME cup costs <em>50 cents</em>: half a Sips By cup, under half a Tea Forte pyramid.</div></div>
  <div class="body"><div class="lad a2">{ladder()}</div>
    <div class="src" style="margin-top:2.4vh">USD per cup. Prices opened 27 Nov 2026 on retailer and brand pages; £1 = $1.27, €1 = $1.08. OSME assumes 3 infusions a bag (lab target).</div></div>
  <aside class="notes"><p>Ladder sources in truth/business-case.md §2.</p></aside>
</div>

<!-- 2 · COST STACK -->
<div class="slide bg-dark" id="s2" data-steps="0" data-title="Cost per bag">
  <div class="head a"><div class="label">Business · cost per bag</div>
    <div class="h1">One bag costs <em>{usd(y1)}</em> to make in the pilot and <span class="jade">{usd(y3)}</span> at year-3 scale. The membrane is the line we fund.</div></div>
  <div class="body"><div class="cs a2">
    <div class="stk">
      <div class="col"><div class="tot amber">{usd(y1)}</div><div class="pile" style="height:46vh">{p1}</div><div class="yr">Year 1 · pilot</div></div>
      <div class="col"><div class="tot jade">{usd(y3)}</div><div class="pile">{p3}</div><div class="yr">Year 3 · scale</div></div>
    </div>
    <div><div class="leg"><div class="li hd"><i></i>Per bag<span>Year 1</span><span>Year 3</span></div>{leg}</div>
      <div class="sm" style="margin-top:2.2vh"><b class="amber">Membrane:</b> the polymer is under 1 cent a bag (food-grade cellulose, $2.70 to $91 a kg, 2 g a m² on 84 cm²). The 10 cents is coating, curing and lost yield.</div>
      <div class="src" style="margin-top:1vh">Sourced: tin, polymer and filter paper prices. Assumptions: tea, membrane process, tag, packing.</div>
      <div class="sm" style="margin-top:1.2vh">Year 1 is hand-made in small lots: {1-y1/1.5:.0%} margin, a pilot, not a business.</div>
      <div class="oneoff sm">One-off, funded by the ask: {oo}</div></div>
  </div></div>
  <aside class="notes"><p>Cost lines and labels in truth/business-case.md §3.</p></aside>
</div>

<!-- 3 · MARGIN AND PRICE -->
<div class="slide bg-mesh" id="s3" data-steps="0" data-title="Margin and price">
  <div class="head a"><div class="label">Business · margin per bag · price recommendation, the team decides</div>
    <div class="h1">Every price earns over 70% a bag at scale; only <span class="jade">$2.00</span> repays a subscriber's acquisition in <em>{m.econ(2.0)['payback']:.0f} months</em> instead of {e['payback']:.0f}.</div></div>
  <div class="body"><div class="mg a2">
    <div class="mgb"><div class="cap" style="letter-spacing:.16em;text-transform:uppercase">Months to repay a $75 subscriber</div>
      <div class="row" style="gap:22px;align-items:baseline"><div class="big" style="font-size:clamp(76px,6.4vw,128px);color:var(--amber)">{e['payback']:.1f}</div><div class="sm">at $1.50 · LTV:CAC {e['ltv_cac']:.1f}x</div></div>
      <div class="row" style="gap:22px;align-items:baseline"><div class="big" style="font-size:clamp(76px,6.4vw,128px);color:var(--jade)">{m.econ(2.0)['payback']:.1f}</div><div class="sm">at $2.00 · LTV:CAC {m.econ(2.0)['ltv_cac']:.1f}x</div></div>
      <div class="sm">Investors expect 3x. A Ritual box at $1.50: $24 minus bags {usd(e['box_cogs'])}, post {usd(m.FULFIL)}, card fee {usd(e['fee'])} = {usd(e['contrib'])} a month.</div></div>
    {price_table()}
  </div></div>
  <aside class="notes"><p>Working in truth/business-case.md §4 and §6.</p></aside>
</div>

<!-- 4 · 640 TO YEAR 3 -->
<div class="slide bg-warm" id="s4" data-steps="0" data-title="Year 3">
  <div class="head a"><div class="label">Business · from market to year 3</div>
    <div class="h1">Year 3 at $1.50: {m.RITUAL_AVG/1e3:.0f} k subscribers on average, {m.TINS/1e3:.0f} k tins and {m.RETAIL_BAGS/1e6:.0f} m retail bags make <em>{mn(w['total'])}</em>, {w['share']:.1%} of our market.</div></div>
  <div class="body"><div class="wk a2">
    <div class="funnel">
      <div class="fr"><div class="k">TAM · tea bags</div><div class="b ghost" style="width:100%">$7.1 bn a year</div></div>
      <div class="fr"><div class="k">SAM · premium bags, 4 first markets</div><div style="display:flex;align-items:center;gap:16px"><div class="b ghost" style="width:9%;min-width:9%;position:relative;padding:0"><i style="position:absolute;right:0;top:0;bottom:0;width:6px;background:var(--amber);border-radius:0 10px 10px 0;box-shadow:0 0 14px rgba(242,163,58,.6)"></i></div><span style="font-size:clamp(20px,1.4vw,27px);font-weight:500">$640 m</span><span class="sm">9% of TAM, to scale</span></div></div>
      <div class="fr"><div class="k" style="color:var(--text)">OSME year 3<br/><span style="font-size:.8em;color:var(--muted)">1.3% of SAM, zoomed in</span></div><div class="b" style="width:100%;padding:0;overflow:hidden;gap:0">
        <div style="width:{rit/w['total']*100:.1f}%;height:100%;background:#F2A33A;display:flex;align-items:center;padding-left:12px;white-space:nowrap;overflow:hidden">{mn(rit)}</div>
        <div style="width:{tins/w['total']*100:.1f}%;height:100%;background:#D9C46B;display:flex;align-items:center;padding-left:12px;white-space:nowrap;overflow:hidden">{mn(tins)}</div>
        <div style="width:{ret/w['total']*100:.1f}%;height:100%;background:#3DBA9B;display:flex;align-items:center;padding-left:8px;white-space:nowrap;overflow:hidden;font-size:.85em">{mn(ret)}</div></div></div>
      <div class="fr"><div class="k"></div><div class="flg" style="gap:8px 22px;flex-wrap:nowrap"><span><b style="background:#F2A33A"></b>Ritual subscription</span><span><b style="background:#D9C46B"></b>Tins and gifts (web shop)</span><span><b style="background:#3DBA9B"></b>Premium retail</span></div></div>
      <div class="fr"><div class="k"></div><div class="big" style="font-size:clamp(64px,5.4vw,104px);color:var(--amber);white-space:nowrap">{mn(w['total'])}<span class="sm" style="font-size:clamp(18px,1.2vw,23px);margin-left:18px;letter-spacing:0">= {w['share']:.1%} of SAM</span></div></div>
      <div class="fr"><div class="k"></div><div class="sm">Tins sell as gifts: 7 in 10 would welcome a premium tea gift box (Mintel). The $2.5 m funds the food-safe membrane and the first Ritual boxes; growth to 20 k subscribers is paid from margin and a Series A.</div></div>
    </div>
    <div><div class="eq"><b>Bottom-up</b><br/>{m.RITUAL_AVG:,} subscribers × $24 × 12 = {mn(rit)}<br/>{m.TINS:,} tins and gifts × $18 = {mn(tins)}<br/>{m.RETAIL_BAGS/1e6:.0f} m retail bags × $0.75 = {mn(ret)}<br/><br/><b>Top-down</b><br/>{mn(w['total'])} ÷ $640 m = {w['share']:.1%} of SAM</div>
      <div class="bench"><div class="src" style="letter-spacing:.16em;text-transform:uppercase">Plausibility: public subscription counts</div>__BENCH__</div></div>
  </div></div>
  <aside class="notes"><p>Walk and benchmarks in truth/business-case.md §5.</p></aside>
</div>
"""
    return slides


BENCH = [("Sips By tea members, 2020", "350 k"), ("Trade Coffee subscribers, 2020", "75 k"),
         ("Pact Coffee UK subscribers, 2021", "60 k"), ("OSME Ritual, end of year 3", "20 k")]

if __name__ == "__main__":
    slides = build().replace("__BENCH__", "".join(
        f'<div class="bi{" os" if k.startswith("OSME") else ""}"><span>{k}</span><span>{v}</span></div>' for k, v in BENCH))
    JS = (bp.JS.replace("document.getElementById('demo').addEventListener", "document.getElementById('demo')&&document.getElementById('demo').addEventListener")
          .replace("else if(k==='d'||k==='D'){if(cur!==2)goto(2,0);demo(!document.body.classList.contains('demo'));}", "")
          .replace("if(cur===2)fitDemo();", "").replace("if(n===2)setTimeout(fitDemo,50);", "")
          .replace("/^[1-8]$/", "/^[1-4]$/"))
    page = (bp.PAGE.replace("__CSS__", CSS).replace("__SLIDES__", slides).replace("__JS__", JS)
            .replace("<title>OSME · a tea bag that opens only at its perfect temperature</title>", "<title>OSME · business case</title>")
            .replace(" · D live demo full screen · Space pours", "").replace(" · D live demo", "").replace(" · Esc leave demo", "")
            .replace("1 to 8 jump", "1 to 4 jump")
            .replace("__FONTX__", FONTX).replace("__FONT__", bp.FONT).replace("__LOCKUP__", bp.LOCKUP).replace("__SYM__", SYM))
    (D / "business.html").write_text(page, encoding="utf8")
    print("wrote", D / "business.html", len(page) // 1024, "KB")
