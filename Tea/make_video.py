"""Render a 20-second explainer video for the Osme Control tea capsule from Osme.png."""
import subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

SRC = r"C:\DWI - 2026\ClaudeCode\Tea\Osme.png"
OUT = r"C:\DWI - 2026\ClaudeCode\Tea\Osme_Control_20s.mp4"
W, H, FPS, DUR = 1920, 1080, 30, 20.0
XF = 0.5  # crossfade seconds

TEAL = (22, 160, 160)
TEAL_L = (210, 240, 240)
NAVY = (14, 38, 72)
GREY = (90, 100, 115)

F = r"C:\Windows\Fonts"
def font(name, size):
    try:
        return ImageFont.truetype(f"{F}\\{name}", size)
    except OSError:
        return ImageFont.truetype(f"{F}\\arial.ttf", size)

f_brand = font("segoeuib.ttf", 44)
f_brand_i = font("segoeuii.ttf", 26)
f_step = font("segoeuib.ttf", 34)
f_title = font("segoeuib.ttf", 78)
f_body = font("segoeui.ttf", 40)
f_small = font("segoeui.ttf", 24)
f_badge = font("segoeuib.ttf", 30)

src = Image.open(SRC).convert("RGB")

# (start, end, crop box, step label, title, body lines, motion arrow: None/'up'/'down')
SCENES = [
    (0, 3,  (24, 700, 262, 877),   "0–3s",   "Sealed capsule",
     ["Dry tea leaves sit inside a", "porous inner filter.", "Water-flow ports are covered."], None),
    (3, 6,  (528, 165, 812, 456),  "3–6s",   "Lower into water",
     ["The sleeve keeps the ports", "sealed – no brewing yet.", "Water stays clear."], "down"),
    (6, 9,  (543, 700, 768, 877),  "6–9s",   "Lift to OPEN",
     ["Pull the control rod up.", "The waterproof sleeve rises", "and uncovers the ports."], "up"),
    (9, 13, (838, 165, 1152, 465), "9–13s",  "Watch tea diffuse",
     ["Water flows in through the", "ports; tea flows out", "into your cup."], None),
    (13, 16, (1042, 700, 1265, 877), "13–16s", "Push to CLOSE",
     ["Press the rod down.", "The sleeve covers the ports", "again – brewing stops."], "down"),
    (16, 20, (1165, 165, 1515, 456), "16–20s", "Sip when ready",
     ["Tea stays in the cup;", "wet leaves stay trapped", "inside the capsule."], None),
]

# ---------- static background ----------
def make_bg():
    bg = Image.new("RGB", (W, H))
    px = bg.load()
    for y in range(H):
        for x in range(0, W):
            t = (x / W) * 0.6 + (y / H) * 0.4
            px[x, y] = (int(246 - 20 * t), int(252 - 8 * t), int(252 - 6 * t))
    d = ImageDraw.Draw(bg)
    # decorative teal swoosh top-right
    d.ellipse((W - 420, -380, W + 380, 260), fill=(200, 236, 236))
    d.ellipse((-300, H - 160, 500, H + 500), fill=(214, 240, 240))
    # header
    d.text((80, 42), "Osme", font=font("georgiabi.ttf", 64), fill=NAVY)
    d.rounded_rectangle((268, 52, 520, 112), 12, fill=NAVY)
    d.text((394, 82), "CONTROL", font=f_brand, fill="white", anchor="mm")
    d.text((548, 82), "How it works", font=font("segoeuib.ttf", 44), fill=NAVY, anchor="lm")
    # footer disclaimer
    d.text((W // 2, H - 34), "Concept illustration only · Seal performance, hot-water food safety and "
           "brewing control require testing.", font=f_small, fill=GREY, anchor="mm")
    return bg

BG = make_bg()

CARD = (80, 150, 1060, 960)  # x0,y0,x1,y1 for the image card
CW, CH = CARD[2] - CARD[0], CARD[3] - CARD[1]

def prep_image(box):
    """Crop + upscale to cover the card (slightly oversized for Ken Burns)."""
    im = src.crop(box)
    s = max(CW / im.width, CH / im.height) * 1.12
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    return im

IMGS = [prep_image(s[2]) for s in SCENES]

# rounded mask + shadow for card
mask = Image.new("L", (CW, CH), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, CW - 1, CH - 1), 36, fill=255)
shadow = Image.new("RGBA", (CW + 80, CH + 80), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rounded_rectangle((40, 50, CW + 40, CH + 50), 36, fill=(10, 50, 60, 70))
shadow = shadow.filter(ImageFilter.GaussianBlur(18))

def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def arrow(d, cx, cy, direction, a):
    """Animated arrow showing the rod moving up or down."""
    col = (*TEAL, int(255 * a))
    L = 110
    if direction == "up":
        d.rectangle((cx - 14, cy - L // 2 + 40, cx + 14, cy + L // 2), fill=col)
        d.polygon([(cx - 44, cy - L // 2 + 44), (cx + 44, cy - L // 2 + 44), (cx, cy - L // 2 - 16)], fill=col)
    else:
        d.rectangle((cx - 14, cy - L // 2, cx + 14, cy + L // 2 - 40), fill=col)
        d.polygon([(cx - 44, cy + L // 2 - 44), (cx + 44, cy + L // 2 - 44), (cx, cy + L // 2 + 16)], fill=col)

def render_scene(i, t):
    """Render scene i at absolute time t."""
    start, end, _, label, title, body, mot = SCENES[i]
    local = t - start
    dur = end - start
    p = local / dur
    frame = BG.copy()
    d = ImageDraw.Draw(frame, "RGBA")

    # card with Ken Burns zoom/pan
    im = IMGS[i]
    z = 1.0 + 0.10 * ease(p) if i % 2 == 0 else 1.10 - 0.10 * ease(p)
    sw, sh = int(im.width * z / 1.12), int(im.height * z / 1.12)
    sw, sh = max(sw, CW), max(sh, CH)
    zim = im.resize((sw, sh), Image.BILINEAR)
    ox = int((sw - CW) * (0.5 + 0.15 * math.sin(p * math.pi - math.pi / 2) * (1 if i % 2 else -1)))
    oy = int((sh - CH) * 0.5)
    ox = max(0, min(sw - CW, ox))
    view = zim.crop((ox, oy, ox + CW, oy + CH))
    frame.paste(shadow, (CARD[0] - 40, CARD[1] - 40), shadow)
    frame.paste(view, (CARD[0], CARD[1]), mask)
    d.rounded_rectangle(CARD, 36, outline=(255, 255, 255), width=6)

    # motion arrow on the card
    if mot:
        bob = math.sin(local * 5) * 14
        a = ease(local / 0.4) * ease((dur - local) / 0.3)
        arrow(d, CARD[2] - 110, CARD[1] + 200 + bob, mot, a)

    # time badge on card
    d.rounded_rectangle((CARD[0] + 26, CARD[1] + 26, CARD[0] + 200, CARD[1] + 82), 18, fill=(*TEAL, 235))
    d.text((CARD[0] + 113, CARD[1] + 54), label, font=f_badge, fill="white", anchor="mm")

    # right-hand text with slide-in
    tx = 1140
    a1 = ease(local / 0.5)
    a2 = ease((local - 0.25) / 0.5)
    off1 = int((1 - a1) * 60)
    off2 = int((1 - a2) * 60)
    d.rounded_rectangle((tx + off1, 300, tx + 240 + off1, 352), 26, fill=(*NAVY, int(255 * a1)))
    d.text((tx + 120 + off1, 326), f"STEP {i + 1} OF 6", font=f_step, fill=(255, 255, 255, int(255 * a1)), anchor="mm")
    d.text((tx + off1, 380), title, font=f_title, fill=(*NAVY, int(255 * a1)))
    d.rectangle((tx + off1, 488, tx + 120 + off1, 496), fill=(*TEAL, int(255 * a1)))
    y = 530
    for line in body:
        d.text((tx + off2, y), line, font=f_body, fill=(*GREY, int(255 * a2)))
        y += 58

    # progress bar with step dots
    px0, px1, py = tx, W - 100, 860
    d.rounded_rectangle((px0, py - 5, px1, py + 5), 5, fill=(200, 222, 226))
    d.rounded_rectangle((px0, py - 5, px0 + int((px1 - px0) * t / DUR), py + 5), 5, fill=TEAL)
    for k, s in enumerate(SCENES):
        cx = px0 + int((px1 - px0) * s[0] / DUR)
        on = t >= s[0]
        d.ellipse((cx - 14, py - 14, cx + 14, py + 14), fill=TEAL if on else (200, 222, 226),
                  outline="white", width=4)
    d.text((px1, py + 40), f"{t:4.1f}s / 20s", font=f_small, fill=GREY, anchor="rm")

    # finale tag in last scene
    if i == len(SCENES) - 1:
        fa = ease((local - 2.2) / 0.6)
        if fa > 0:
            d.rounded_rectangle((tx, 930 - 50, W - 100, 930 + 10), 20, fill=(*TEAL_L, int(255 * fa)))
            d.text(((tx + W - 100) // 2, 900), "After use: open, empty, wash and dry.",
                   font=font("segoeuib.ttf", 30), fill=(*NAVY, int(255 * fa)), anchor="mm")
    return frame

def frame_at(t):
    # find current scene; crossfade into the next one near the boundary
    for i, s in enumerate(SCENES):
        if s[0] <= t < s[1] or i == len(SCENES) - 1:
            cur = i
            break
    img = render_scene(cur, t)
    if cur + 1 < len(SCENES) and t > SCENES[cur][1] - XF:
        nxt = render_scene(cur + 1, SCENES[cur + 1][0] + (t - (SCENES[cur][1] - XF)) * 0.0)
        img = Image.blend(img, nxt, ease((t - (SCENES[cur][1] - XF)) / XF))
    # global fade in / out
    if t < 0.4 or t > DUR - 0.5:
        k = ease(t / 0.4) if t < 0.4 else ease((DUR - t) / 0.5)
        img = Image.blend(Image.new("RGB", (W, H), "white"), img, k)
    return img

def main():
    exe = imageio_ffmpeg.get_ffmpeg_exe()
    cmd = [exe, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(DUR * FPS)
    for f in range(n):
        p.stdin.write(frame_at(f / FPS).tobytes())
        if f % 60 == 0:
            print(f"frame {f}/{n}", flush=True)
            if len(sys.argv) > 1:  # preview mode: dump stills
                frame_at(f / FPS).save(f"preview_{f:03d}.png")
    p.stdin.close()
    p.wait()
    print("done", OUT, "exit", p.returncode)

if __name__ == "__main__":
    main()
