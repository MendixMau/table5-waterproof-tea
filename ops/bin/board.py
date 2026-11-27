#!/usr/bin/env python3
"""Live board for Table 5.

Writes ops/board.html (one self-contained page that reloads itself every 30 s)
and the live block in README.md. ops/bin/live.sh runs it every 30 s.
The lead sets the headline, the current gate and the holds in ops/board-status.txt.
"""
import base64, datetime as dt, html, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
GAL = ROOT / "gallery"
CACHE = pathlib.Path("/tmp/t5-board-cache")
CACHE.mkdir(exist_ok=True)

# key, label, icon, log-agent prefix, gallery prefix, which log lines count
TOPICS = [
    ("brand", "Brand & logo", "🎨", "brand", "brand-", None),
    ("gate1", "Gate 1 deck", "🚦", "presentation", "gate1-", lambda s: "gate1" in s.lower()),
    ("product", "Product demo", "🍵", "product", "product-", None),
    ("deck", "Pitch deck", "🎤", "presentation", "deck-", lambda s: "gate1" not in s.lower()),
    ("site", "Site", "🌐", "site", "site-", None),
    ("video", "Video", "🎬", "video", "video-", None),
]
GATES = [("Brief + facts", "09:30"), ("Gate 1 · brand, logo, market", "10:40"),
         ("Build on the brand", "11:00"), ("Judge passes", "12:00 · 12:45"),
         ("Freeze + rehearse", "13:15"), ("Hand in", "13:30")]
STATE = {"working": ("#F2A33A", "🟡", "working"), "hold": ("#8A8F98", "⚪", "on hold"),
         "done": ("#3DBA9B", "🟢", "done"), "blocked": ("#E5484D", "🔴", "blocked"),
         "waiting": ("#8A8F98", "⚪", "not started")}
HAND_IN = dt.datetime.combine(dt.date.today(), dt.time(13, 30))

CSS = """
:root{--bg:#0B0B0D;--card:#16161A;--line:#2A2A31;--text:#F3EFE6;--muted:#8A8F98;--amber:#F2A33A;--jade:#3DBA9B}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:15px/1.4 Jost,-apple-system,"Helvetica Neue",Arial,sans-serif;padding:24px 32px 40px}
header{display:flex;align-items:baseline;gap:20px;flex-wrap:wrap}
h1{font-size:20px;letter-spacing:.24em;margin:0;font-weight:600}
.clock{color:var(--amber);font-weight:600}
.legend{margin-left:auto;color:var(--muted);font-size:12px}
.legend i{display:inline-block;width:9px;height:9px;border-radius:50%;margin:0 4px 0 10px}
.now{font-size:26px;font-weight:500;margin:14px 0 16px;max-width:1100px}
.track{display:flex;gap:6px;margin-bottom:18px}
.gate{flex:1;border-top:5px solid #3A3A42;padding-top:6px;color:var(--muted);font-size:12px}
.gate b{display:block;color:var(--muted);font-size:13px;font-weight:600}
.gate.done{border-color:var(--jade)}.gate.done b{color:var(--text)}
.gate.now{border-color:var(--amber)}.gate.now b{color:var(--amber)}
.decide{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:22px}
.lbl{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin-right:4px}
.chip{border:1px solid var(--amber);color:var(--amber);border-radius:999px;padding:3px 12px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(600px,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.card img{display:block;width:100%;max-height:520px;object-fit:contain;background:#000}
.card.hold img{opacity:.45}
.empty{aspect-ratio:16/9;display:grid;place-items:center;color:var(--muted)}
.meta{display:flex;gap:10px;align-items:center;padding:10px 14px 2px}
.t{font-weight:600;font-size:16px}
.st{border-radius:999px;padding:1px 9px;font-size:12px;color:#0B0B0D;font-weight:600}
.j{color:var(--jade);font-size:13px;font-weight:600}
.when{margin-left:auto;color:var(--muted);font-size:13px}
.note{padding:2px 14px 12px;color:var(--muted);font-size:13px}
details{margin-top:20px;color:var(--muted);font-size:13px}
summary{cursor:pointer;color:var(--text)}
pre{white-space:pre-wrap;font-size:12px}
"""


def cfg():
    out, p = {}, ROOT / "ops/board-status.txt"
    for line in p.read_text().splitlines() if p.exists() else []:
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def log():
    rows = []
    for line in (ROOT / "ops/log.md").read_text().splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) >= 4 and re.fullmatch(r"\d\d:\d\d", parts[0]):
            rows.append(parts)
    return rows


def short(text, n=12):
    words = re.sub(r"[`*]", "", text).split()
    return " ".join(words[:n]) + (" …" if len(words) > n else "")


def data_uri(path, width=1400):
    """Downscaled JPEG as a data URI, cached by mtime so the 30 s rebuild stays cheap."""
    out = CACHE / f"{path.stem}-{int(path.stat().st_mtime)}.jpg"
    if not out.exists():
        dims = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
                              capture_output=True, text=True).stdout
        size = max([int(x) for x in re.findall(r":\s*(\d+)", dims)] or [0])
        cmd = ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "78"]
        if size > width:
            cmd += ["-Z", str(width)]
        subprocess.run(cmd + [str(path), "--out", str(out)], capture_output=True)
    if out.exists():
        return "data:image/jpeg;base64," + base64.b64encode(out.read_bytes()).decode()
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


def topic_rows(lines, c):
    rows = []
    for key, label, icon, agent, prefix, keep in TOPICS:
        mine = [l for l in lines if l[1].startswith(agent) and (keep is None or keep(" ".join(l)))]
        last = mine[-1] if mine else None
        state = c.get(key) or ("waiting" if not last else
                               {"HOLD": "hold", "DONE": "done", "BLOCKED": "blocked"}.get(last[2].upper(), "working"))
        judge = ""
        for l in reversed(mine):
            m = re.search(r"judge\s*(\d+(?:\.\d)?)\s*/\s*(\d+)", " ".join(l[3:]), re.I)
            if m:
                judge = f"judge {m.group(1)}/{m.group(2)}"
                break
        note = next((l[-1] for l in reversed(mine) if l[2].upper() == "PREVIEW"), last[-1] if last else "")
        imgs = sorted(GAL.glob(prefix + "*.png"), key=lambda p: p.stat().st_mtime)
        rows.append(dict(key=key, label=label, icon=icon, state=state, judge=judge,
                         when=last[0] if last else "", note=short(note), img=imgs[-1] if imgs else None))
    return rows


def questions():
    out = []
    for line in (ROOT / "ops/questions.md").read_text().splitlines():
        parts = [x.strip() for x in line.split("|")]
        if len(parts) >= 3 and re.fullmatch(r"\d\d:\d\d", parts[0]) \
                and not re.search(r"\b(ANSWERED|RESOLVED|DECIDED)\b", line):
            out.append(f"{parts[0]} · {parts[1]} · {short(parts[2], 14)}")
    return out[-8:]


def left(now):
    mins = max(0, int((HAND_IN - now).total_seconds() // 60))
    return f"{mins // 60} h {mins % 60:02d}"


def page(rows, c, now):
    gate = int(c.get("gate", 1))
    track = "".join(
        f'<div class="gate {"done" if i < gate else "now" if i == gate else ""}"><b>{html.escape(n)}</b>{t}</div>'
        for i, (n, t) in enumerate(GATES))
    decide = "".join(f'<span class="chip">{html.escape(d.strip())}</span>'
                     for d in c.get("decide", "").split(" · ") if d.strip())
    cards = []
    for r in rows:
        colour, _, word = STATE[r["state"]]
        img = (f'<img src="{data_uri(r["img"])}" alt="{html.escape(r["label"])}">' if r["img"]
               else '<div class="empty">first preview soon</div>')
        cards.append(
            f'<div class="card {r["state"]}">{img}<div class="meta">'
            f'<span class="t">{r["icon"]} {html.escape(r["label"])}</span>'
            f'<span class="st" style="background:{colour}">{word}</span><span class="j">{r["judge"]}</span>'
            f'<span class="when">{r["when"]}</span></div><div class="note">{html.escape(r["note"])}</div></div>')
    qs = questions()
    recent = html.escape("\n".join(" | ".join(l) for l in log()[-20:]))
    legend = "".join(f'<i style="background:{STATE[k][0]}"></i>{STATE[k][2]}'
                     for k in ("working", "done", "hold", "blocked"))
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="30"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OSME · live board</title><style>{CSS}</style></head><body>
<header><h1>OSME · TABLE 5</h1><span class="clock">{now:%H:%M} · {left(now)} to hand-in</span>
<span class="legend">{legend}</span></header>
<div class="now">{html.escape(c.get("now", ""))}</div>
<div class="track">{track}</div>
<div class="decide"><span class="lbl">Your call</span>{decide}</div>
<div class="grid">{"".join(cards)}</div>
<details><summary>Questions from the threads ({len(qs)})</summary><ul>{"".join(f"<li>{html.escape(q)}</li>" for q in qs)}</ul></details>
<details><summary>Log, last 20 lines</summary><pre>{recent}</pre></details>
</body></html>"""


def readme(rows, c, now):
    out = ["<!-- LIVE:START -->", f"## Live status · {now:%H:%M} · {left(now)} to hand-in", "",
           f"**Now:** {c.get('now', '')}", "", "| | Topic | Status | Latest preview |", "|---|---|---|---|"]
    for r in rows:
        _, dot, word = STATE[r["state"]]
        img = f'<img src="gallery/{r["img"].name}" width="260">' if r["img"] else "soon"
        judge = f" · {r['judge']}" if r["judge"] else ""
        out.append(f"| {r['icon']} | {r['label']} | {dot} {word}{judge} · {r['when']} | {img} |")
    out += ["", "**Waiting on the team:** " + c.get("decide", ""), "<!-- LIVE:END -->"]
    block, p = "\n".join(out), ROOT / "README.md"
    text = p.read_text()
    if "<!-- LIVE:START -->" in text:
        text = re.sub(r"(?s)<!-- LIVE:START -->.*?<!-- LIVE:END -->", lambda _: block, text)
    else:
        text = text.replace("Everyone drives at least once.\n", "Everyone drives at least once.\n\n" + block + "\n", 1)
    p.write_text(text)


if __name__ == "__main__":
    now, c = dt.datetime.now(), cfg()
    rows = topic_rows(log(), c)
    tmp = ROOT / "ops/.board.tmp.html"
    tmp.write_text(page(rows, c, now))
    tmp.replace(ROOT / "ops/board.html")  # atomic, so a reload never shows half a page
    readme(rows, c, now)
