#!/usr/bin/env python3
"""Generate shared/product/exploded-view.svg (static) and exploded-view-animated.svg.

Usage: gen.py <repo-root>
"""
import base64, math, random, sys
from pathlib import Path

R = Path(sys.argv[1])
OUT = R / "shared/product"

BG, SURF, LINE = "#0B0B0D", "#17171B", "#2A2A30"
AMBER, JADE, MID = "#F2A33A", "#3DBA9B", "#D9C46B"
TEXT, MUTED = "#F3EEE6", "#8E8A83"
FONT = '"Jost", "Futura", "Century Gothic", "Avenir Next", sans-serif'

jost = base64.b64encode((R / "brand/assets/fonts/jost-latin.woff2").read_bytes()).decode()
logo = base64.b64encode((R / "brand/identity/logo-lockup.svg").read_bytes()).decode()

# Bag outline in local units, the logo's chamfered-shoulder shape scaled up (0,0 = top centre).
W, H = 300.0, 330.0
def bag_path(w=W, h=H, sh=0.17):
    hw = w / 2; c = w * sh; r = w * 0.09
    return (f"M{-hw:.1f} {c:.1f} L{-hw + c:.1f} 0 H{hw - c:.1f} L{hw:.1f} {c:.1f} "
            f"V{h - r:.1f} Q{hw:.1f} {h:.1f} {hw - r:.1f} {h:.1f} H{-hw + r:.1f} "
            f"Q{-hw:.1f} {h:.1f} {-hw:.1f} {h - r:.1f} Z")

# Oblique "lying flat" plane: x' = x + 0.62*y, y' = 0.36*y  (top of the bag lies to the back-left)
SK, SQ = 0.62, 0.36
def plane(cx, cy):
    # centre the plane on (cx, cy): local centre is (0, H/2)
    ox = cx - SK * H / 2; oy = cy - SQ * H / 2
    return f"matrix(1 0 {SK} {SQ} {ox:.1f} {oy:.1f})"

def P(x, y, cx, cy):
    ox = cx - SK * H / 2; oy = cy - SQ * H / 2
    return x + SK * y + ox, SQ * y + oy

def pores_in_bag(step=24, margin=26):
    pts = []
    hw = W / 2 - margin
    y = margin + 30
    row = 0
    while y < H - margin:
        off = (step / 2) if row % 2 else 0
        x = -hw + off
        while x <= hw:
            pts.append((x, y, row))
            x += step
        y += step * 0.86
        row += 1
    return pts

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def build(animated):
    LR = 58 if animated else 70
    o = []
    A = o.append
    A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" '
      f'role="img" aria-labelledby="ttl dsc">')
    A('<title id="ttl">What is inside an OSME bag: five layers, exploded</title>')
    A('<desc id="dsc">Tag and string, seal, outer filter, temperature membrane, leaf. '
      'The membrane pores stay closed in hot water, open at 80 degrees C and close again below 70 degrees C (Sencha). '
      'The principle exists: lab membranes already open and close with temperature. Our R&amp;D makes it food-safe at 70-90 degrees C.</desc>')
    A('<defs>')
    A('<style>'
      f'@font-face{{font-family:"Jost";src:url(data:font/woff2;base64,{jost}) format("woff2");font-weight:300 700}}'
      f'text{{font-family:{FONT};fill:{TEXT}}}'
      f'.k{{font-size:18px;font-weight:500;letter-spacing:.18em;fill:{AMBER}}}'
      f'.h{{font-size:40px;font-weight:500;letter-spacing:.08em}}'
      f'.n{{font-size:20px;font-weight:500;letter-spacing:.12em;fill:{AMBER}}}'
      f'.l{{font-size:28px;font-weight:500;letter-spacing:.12em}}'
      f'.tt{{font-size:28px;font-weight:500;letter-spacing:.06em}}'
      f'.c{{font-size:22px;font-weight:400;fill:#B3AEA6}}'
      f'.t{{font-size:16px;font-weight:500;letter-spacing:.16em}}'
      f'.s{{font-size:22px;font-weight:400;fill:#B3AEA6}}'
      f'.big{{font-size:64px;font-weight:400;letter-spacing:.02em}}'
      '</style>')
    A(f'<linearGradient id="arc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{AMBER}"/>'
      f'<stop offset=".5" stop-color="{MID}"/><stop offset="1" stop-color="{JADE}"/></linearGradient>')
    A(f'<linearGradient id="strg" gradientUnits="userSpaceOnUse" x1="0" y1="330" x2="0" y2="150">'
      f'<stop offset="0" stop-color="{AMBER}"/><stop offset=".48" stop-color="{MID}"/><stop offset="1" stop-color="{JADE}"/></linearGradient>')
    A('<linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A59C8E"/>'
      '<stop offset="1" stop-color="#7C7468"/></linearGradient>')
    A('<pattern id="mesh" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
      '<path d="M0 0H9M0 0V9" stroke="#5F584E" stroke-width=".8" opacity=".6"/></pattern>')
    A(f'<linearGradient id="memb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{MID}" stop-opacity=".22"/>'
      f'<stop offset="1" stop-color="{JADE}" stop-opacity=".12"/></linearGradient>')
    A(f'<radialGradient id="liq"><stop offset="0" stop-color="{MID}"/><stop offset=".7" stop-color="#C8D468" stop-opacity=".55"/>'
      f'<stop offset="1" stop-color="#C8D468" stop-opacity="0"/></radialGradient>')
    A('<filter id="drop" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="10" flood-color="#000" flood-opacity=".7"/></filter>'
      '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5"/></filter>')
    A('<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="14"/></filter>')
    A(f'<clipPath id="lens"><circle r="{LR}"/></clipPath>')
    A('</defs>')
    A(f'<rect width="1600" height="1000" fill="{BG}"/>')
    # soft warm pool behind the stack
    A(f'<ellipse cx="420" cy="560" rx="360" ry="300" fill="{AMBER}" opacity=".05" filter="url(#soft)"/>')

    # ---------- title
    A('<text x="80" y="92" class="k">WHAT&#8217;S INSIDE · THE OSME BAG</text>')
    A('<text x="80" y="144" class="h">FIVE LAYERS. ONE OF THEM READS THE WATER.</text>')
    A(f'<image href="data:image/svg+xml;base64,{logo}" x="1380" y="62" width="140" height="64"/>')

    # ---------- exploded stack
    CX = 360
    LY = {"tag": 236, "seal": 340, "filter": 455, "memb": 590, "leaf": 728}
    K, T0, T1 = 1.12, 178, 172
    def S(x, y): return CX + (x - CX) * K, T1 + (y - T0) * K
    A(f'<g transform="translate({CX*(1-K):.2f} {T1 - T0*K:.2f}) scale({K})">')
    bp = bag_path()
    # assembly axis
    ax_top = P(0, H / 2, CX, LY["seal"]); ax_bot = P(0, H / 2, CX, LY["leaf"])
    A(f'<path d="M{CX} {LY["tag"] + 20} V{LY["leaf"] + 90}" stroke="{LINE}" stroke-width="1.5" stroke-dasharray="3 7"/>')

    # leaf layer (bottom): a flat plane with sencha needles scattered
    rnd = random.Random(7)
    A('<g opacity=".75">')
    A(f'<g transform="{plane(CX, LY["leaf"])}">')
    A(f'<path d="{bp}" fill="#C8D468" fill-opacity=".05" stroke="{LINE}" stroke-width="2" stroke-dasharray="6 8"/>')
    A('</g>')
    for i in range(110):
        x = rnd.uniform(-W / 2 + 30, W / 2 - 30); y = rnd.uniform(50, H - 30)
        px, py = P(x, y, CX, LY["leaf"]); py -= rnd.uniform(0, 8)
        ln = rnd.uniform(22, 40); wd = rnd.uniform(3.5, 6); a = rnd.uniform(-35, 35) + 18
        col = rnd.choice(["#6F8A35", "#86A13F", "#A9BE55", "#C8D468", "#5E7A2C", "#7E9A3A"])
        A(f'<path transform="translate({px:.1f} {py:.1f}) rotate({a:.0f})" d="M{-ln/2:.1f} 0 Q0 {-wd:.1f} {ln/2:.1f} 0 Q0 {wd*0.7:.1f} {-ln/2:.1f} 0Z" fill="{col}"/>')
    A('</g>')

    # membrane layer
    pores = pores_in_bag()
    A(f'<g filter="url(#drop)"><g transform="translate(0 7)"><path transform="{plane(CX, LY["memb"])}" d="{bp}" fill="#3A3520"/></g>')
    A(f'<path transform="{plane(CX, LY["memb"])}" d="{bp}" fill="#101013"/></g>')
    A(f'<g transform="{plane(CX, LY["memb"])}">')
    A(f'<path d="{bp}" fill="url(#memb)" stroke="{MID}" stroke-width="2"/>')
    if animated:
        # closed slits (always drawn) with colour shifting hot -> cool
        A('<g id="slits">')
        for x, y, row in pores:
            A(f'<path d="M{x-6:.1f} {y:.1f}h12" stroke-width="3" stroke-linecap="round"/>')
        A('</g>')
        rows = max(p[2] for p in pores) + 1
        for r in range(rows):
            d = r * 0.025
            A(f'<g opacity="0">{anim_open(d)}')
            for x, y, row in pores:
                if row == r:
                    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="url(#liq)"/>'
                      f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="none" stroke="{MID}" stroke-width="1.2"/>')
            A('</g>')
    else:
        for x, y, row in pores:
            A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7.5" fill="url(#liq)"/>'
              f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="none" stroke="{MID}" stroke-width="1.2"/>')
    A('</g>')
    # magnifier ring on membrane, leader to the inset
    mx, my = P(70, 150, CX, LY["memb"])
    A(f'<ellipse cx="{mx:.1f}" cy="{my:.1f}" rx="44" ry="26" fill="none" stroke="{MID}" stroke-width="2.4"/>')

    # outer filter layer
    A(f'<g opacity=".6" filter="url(#drop)"><path transform="translate(0 6) {plane(CX, LY["filter"])}" d="{bp}" fill="#4E483F"/></g>')
    A(f'<g opacity=".6" transform="{plane(CX, LY["filter"])}">')
    A(f'<path d="{bp}" fill="url(#paper)"/>')
    A(f'<path d="{bp}" fill="url(#mesh)"/>')
    A(f'<path d="{bp}" fill="none" stroke="#C9C1B4" stroke-opacity=".7" stroke-width="1.5"/>')
    A('</g>')

    # seal: a narrow crimped strip, zigzag front edge, lying flat
    A(f'<g opacity=".6" transform="{plane(CX, LY["seal"])}">')
    hw = W / 2; n = 30; tw = W / n
    zz = " ".join(f"L{hw - (i + .5) * tw:.1f} 58 L{hw - (i + 1) * tw:.1f} 46" for i in range(n))
    A(f'<path d="M{-hw:.1f} 104 H{hw:.1f} V184 {zz.replace(" 58", " 196").replace(" 46", " 184")} Z" fill="#8F877A"/>')
    for i in range(n):
        x = -hw + (i + .5) * tw
        A(f'<path d="M{x:.1f} 112V178" stroke="#5F584E" stroke-width="2" stroke-linecap="round"/>')
    A('</g>')
    # tag + S string, upright, rising from the seal centre
    sx, sy = P(0, 106, CX, LY["seal"])  # string root on the seal's top edge
    tx, ty = sx + 64, LY["tag"] - 22
    A(f'<g opacity=".6" transform="translate({sx:.1f} {sy:.1f})">')
    # S-curve going up, ending at the tag
    dx, dy = tx - sx, ty - sy
    A(f'<path d="M0 0 C0 {dy*0.18:.1f} {dx*1.1:.1f} {dy*0.22:.1f} {dx*1.0:.1f} {dy*0.45:.1f} '
      f'C{dx*0.9:.1f} {dy*0.68:.1f} {-dx*0.5:.1f} {dy*0.62:.1f} {-dx*0.4:.1f} {dy*0.86:.1f} '
      f'C{-dx*0.32:.1f} {dy*1.0:.1f} {dx*0.4:.1f} {dy*1.0:.1f} {dx-16:.1f} {dy:.1f}" '
      f'fill="none" stroke="url(#strgA)" stroke-width="4" stroke-linecap="round"/>')
    A('</g>')
    # gradient for string in absolute coords
    o.insert(o.index('</defs>'),
             f'<linearGradient id="strgA" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="{dy:.1f}">'
             f'<stop offset="0" stop-color="{AMBER}"/><stop offset=".48" stop-color="{MID}"/><stop offset="1" stop-color="{JADE}"/></linearGradient>')
    A(f'<g opacity=".6" transform="translate({tx - 16:.1f} {ty - 36:.1f})">'
      f'<rect width="62" height="76" rx="10" fill="{JADE}"/>'
      f'<circle cx="16" cy="36" r="5" fill="{BG}"/>'
      f'<path d="M30 26 h20 M30 38 h16 M30 50 h20" stroke="{BG}" stroke-opacity=".35" stroke-width="3" stroke-linecap="round"/></g>')

    A('</g>')
    # ---------- labels with leaders
    LX = 700
    labels = [
        ("tag", "01", "TAG AND STRING", "Hot amber to cool jade.", (tx + 46, ty)),
        ("seal", "02", "SEAL", "Crimped shut at the top.", P(W/2, 140, CX, LY["seal"])),
        ("filter", "03", "OUTER FILTER", "Paper mesh, like any bag.", P(W/2, H*0.45, CX, LY["filter"])),
        ("memb", "04", "TEMPERATURE MEMBRANE", "Pores react to water temperature.", P(W/2, H*0.45, CX, LY["memb"])),
        ("leaf", "05", "LEAF", "Sencha, waiting for its moment.", P(W/2, H*0.45, CX, LY["leaf"])),
    ]
    for key, num, name, cap, (px, py) in labels:
        y = S(0, LY[key] - 6 if key != "tag" else ty)[1]
        px, py = S(px, py)
        col = MID if key == "memb" else MUTED
        A(f'<path d="M{px+10:.1f} {py:.1f} L{LX-30} {y - 4:.1f} H{LX-14}" fill="none" stroke="{col}" stroke-width="1.2"/>'
          f'<circle cx="{px+10:.1f}" cy="{py:.1f}" r="3.5" fill="{col}"/>')
        A(f'<text x="{LX}" y="{y + 4:.1f}" class="n" style="fill:{AMBER}">{num}</text>'
          + (f'<text x="{LX + 44}" y="{y + 6:.1f}" class="l" style="fill:{MID}">TEMPERATURE</text>'
             f'<text x="{LX + 44}" y="{y + 40:.1f}" class="l" style="fill:{MID}">MEMBRANE</text>'
             if key == "memb" else f'<text x="{LX + 44}" y="{y + 6:.1f}" class="l">{name}</text>'))

    # ---------- inset: the membrane up close
    IX, IY, IW, IH = 1110, 190, 420, 670
    A(f'<rect x="{IX}" y="{IY}" width="{IW}" height="{IH}" rx="22" fill="{SURF}" stroke="{LINE}" stroke-width="1.5"/>')
    A(f'<text x="{IX + 32}" y="{IY + 48}" class="k">SENCHA, UP CLOSE</text>')
    if not animated:
        A(f'<text x="{IX + 32}" y="{IY + 84}" class="t" style="fill:{MUTED}">WATER COOLS FROM THE BOIL ↓</text>')
    # leader from magnifier to inset
    smx, smy = S(mx + 44, my)
    A(f'<path d="M{smx:.1f} {smy:.1f} C{smx + 160:.1f} {smy:.1f} {IX - 160} {IY + 300} {IX} {IY + 300}" fill="none" stroke="{MID}" stroke-width="2"/>')

    states = [
        ("hot", "SEALED", "Above 80 °C", "Leaf waits.", AMBER),
        ("open", "OPEN", "80 to 70 °C", "Tea steeps.", MID),
        ("cool", "SEALED", "Below 70 °C", "Stops over-steeping.", JADE),
    ]
    for i, (key, word, temp, cap, col) in enumerate(states):
        cy = IY + (250 if animated else 186) + i * (158 if animated else 172)
        cx = IX + 92
        A(f'<g transform="translate({cx} {cy})">')
        if animated:
            A(f'<circle r="{LR + 9}" fill="none" stroke="{col}" stroke-width="2.5" opacity="0">{anim_active(key)}</circle>')
        A(f'<circle r="{LR}" fill="#101013"/>')
        A('<g clip-path="url(#lens)">')
        # membrane fibre texture
        for k in range(-80, 81, 14):
            A(f'<path d="M-80 {k} Q0 {k + 6} 80 {k}" stroke="{col}" stroke-opacity=".18" stroke-width="5" fill="none"/>')
        for gy in range(-56, 57, 28):
            for gx in range(-56, 57, 28):
                ox = 14 if (gy // 28) % 2 else 0
                x = gx + ox
                if key == "open":
                    A(f'<circle cx="{x}" cy="{gy}" r="10" fill="url(#liq)" opacity=".9"/>'
                      f'<circle cx="{x}" cy="{gy}" r="7" fill="#0B0B0D" opacity=".35"/>'
                      f'<circle cx="{x}" cy="{gy}" r="7" fill="none" stroke="{MID}" stroke-width="1.6"/>')
                else:
                    A(f'<path d="M{x-7} {gy}h14" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
        A('</g>')
        A(f'<circle r="{LR}" fill="none" stroke="{col}" stroke-width="2"/>')
        A('</g>')
        A(f'<text x="{IX + 180}" y="{cy - 24}" class="t" style="fill:{col}">{word}</text>'
          f'<text x="{IX + 180}" y="{cy + 10}" class="tt">{temp}</text>'
          f'<text x="{IX + 180}" y="{cy + 42}" class="s">{esc(cap)}</text>')
        if i < 2:
            g = (158 if animated else 172) - 2 * LR
            nc = states[i + 1][4]
            A(f'<path d="M{cx} {cy + LR + 5} v{g - 16} m-6 -6 l6 6 l6 -6" fill="none" stroke="{nc}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    # cooling arrow along the lenses

    # ---------- animated readout
    if animated:
        A(f'<g transform="translate({IX + 32} {IY + 96})">')
        A(f'<text x="0" y="0" class="k" fill="{MUTED}" style="fill:{MUTED}">WATER</text>')
        temps = timeline()
        for (t0, t1, val) in temps:
            A(f'<text x="0" y="62" class="big" opacity="0">{val}<tspan font-size="30" dx="6">°C</tspan>{anim_window(t0, t1)}</text>')
        A(f'<text x="196" y="52" class="t" style="fill:{AMBER}" opacity="0">SEALED · TOO HOT{anim_window(0, T_OPEN)}</text>')
        A(f'<text x="196" y="52" class="t" style="fill:{MID}" opacity="0">OPEN · STEEPING{anim_window(T_OPEN, T_CLOSE)}</text>')
        A(f'<text x="196" y="52" class="t" style="fill:{JADE}" opacity="0">SEALED · DONE{anim_window(T_CLOSE, DUR)}</text>')
        A('</g>')

    # ---------- honest line + logo
    A(f'<rect x="80" y="884" width="1440" height="84" rx="14" fill="{JADE}" fill-opacity=".13"/>'
      f'<rect x="80" y="884" width="7" height="84" rx="3" fill="{JADE}"/>')
    A(f'<text x="112" y="934" class="t" style="fill:{JADE};font-size:18px">THE PRINCIPLE EXISTS:</text>')
    A(f'<text x="384" y="935" style="font-size:24px;font-weight:400">'
      f'lab membranes already open and close with temperature. Our R&amp;D makes it food-safe at 70-90 °C.</text>')

    if animated:
        o.insert(o.index('</defs>'), slit_style())
    A('</svg>')
    return "\n".join(o)

# ---------- animation timeline (seconds); one shared 12 s loop, all SMIL so it runs inside <img> too
DUR = 12.0
C_OPEN, C_CLOSE = 3.5, 8.5
def temp_at(t):
    if t < C_OPEN: return 100 - 20 * t / C_OPEN
    if t < C_CLOSE: return 80 - 10 * (t - C_OPEN) / (C_CLOSE - C_OPEN) - 0.001
    return max(64, 70 - 0.001 - 6 * (t - C_CLOSE) / 2.0)

def timeline():
    out = []; t = 0.0; step = 0.05; cur = None; start = 0.0
    while t < DUR + 1e-9:
        v = math.ceil(temp_at(t)) if t < C_CLOSE else math.floor(temp_at(t))
        if t < C_OPEN: v = math.ceil(temp_at(t))
        if v != cur:
            if cur is not None: out.append((start, t, cur))
            cur, start = v, t
        t += step
    out.append((start, DUR, cur))
    return out

_TL = timeline()
T_OPEN = next(t0 for t0, t1, v in _TL if v <= 80)
T_CLOSE = next(t0 for t0, t1, v in _TL if v < 70)

def kt(x): return f"{max(0.0, min(1.0, x / DUR)):.4f}"

def anim_window(t0, t1):
    # discrete opacity 0 -> 1 at t0, back to 0 at t1
    if t0 <= 0:
        return (f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
                f'values="1;0" keyTimes="0;{kt(t1)}"/>')
    if t1 >= DUR:
        return (f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
                f'values="0;1" keyTimes="0;{kt(t0)}"/>')
    return (f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" calcMode="discrete" '
            f'values="0;1;0" keyTimes="0;{kt(t0)};{kt(t1)}"/>')

def anim_open(d):
    a, b = T_OPEN + d, T_OPEN + d + 0.2
    c, e = T_CLOSE + d, T_CLOSE + d + 0.2
    return (f'<animate attributeName="opacity" dur="{DUR}s" repeatCount="indefinite" '
            f'values="0;0;1;1;0;0" keyTimes="0;{kt(a)};{kt(b)};{kt(c)};{kt(e)};1"/>')

def anim_active(key):
    w = {"hot": (0, T_OPEN), "open": (T_OPEN, T_CLOSE), "cool": (T_CLOSE, DUR)}[key]
    return anim_window(*w)

def slit_style():
    # slit colour: amber while hot, jade after the close
    return (f'<style>#slits path{{stroke:{AMBER};animation:slit {DUR}s linear infinite}}'
            f'@keyframes slit{{0%{{stroke:{AMBER};opacity:1}}{T_OPEN/DUR*100:.2f}%{{stroke:{AMBER};opacity:1}}'
            f'{(T_OPEN+.25)/DUR*100:.2f}%{{opacity:0}}{T_CLOSE/DUR*100:.2f}%{{opacity:0;stroke:{JADE}}}'
            f'{(T_CLOSE+.25)/DUR*100:.2f}%{{opacity:1;stroke:{JADE}}}100%{{opacity:1;stroke:{JADE}}}}}</style>')

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "exploded-view.svg").write_text(build(False))
(OUT / "exploded-view-animated.svg").write_text(build(True))
print("ok", [(p.name, p.stat().st_size) for p in OUT.glob("exploded*.svg")])
