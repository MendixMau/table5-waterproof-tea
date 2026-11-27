# Brand builder 1: pattern, benefit icons, culture motif (asset kit part 1)

Read first: ops/agents/_common.md, facts.md, brand/strategy.md, brand/identity/tokens.css, truth/history-cultures.md (sections 1, 2, 3).
Resume rule: if files below already exist, improve them; don't start over.

Brand look "Midnight Brew": matte black #0B0B0D, surface #17171B, line #2A2A30, paper white #F3EEE6, muted #8E8A83,
amber #F2A33A (hot) -> gold #D9C46B -> jade #3DBA9B (cool) temperature arc. Lu Yu's three bubble stages
(fish eyes, string of pearls, rolling waves; Okakura: "eye of fishes, crystal beads, billows") as a small-to-large 3-dot motif.
Calm, premium, geometric, flat. Never clip-art, never a default app look. No emoji, no exclamation marks.
New logo v4 (being finalised) is a tea bag with a scent wisp; draft options: /tmp/osme-brand/opt/sheet.png. Match its style: flat solid shapes, round caps, ~2-4 px strokes on a 64 grid.

Deliver to brand/assets/ (each as SVG plus a PNG render):
1. pattern-bubbles.svg / .png: a seamless tile (SVG <pattern> or a tile that repeats) of the three bubble stages and arc fragments, quiet on #0B0B0D (low contrast, for backgrounds). Also a 1600x900 PNG swatch of it repeated: pattern-bubbles-swatch.png. Optional light variant on #F3EEE6.
2. Icons, 64x64 viewBox, one consistent family, colour version plus a mono (#F3EEE6) version:
   icon-self-stopping.svg (self-stopping steep: bag opens and closes; e.g. bag with an open/closed seam and a falling temperature arc),
   icon-three-infusions.svg (up to 3 infusions: three cups or three bubbles in a row with the bag),
   icon-scent-sealed.svg (scent sealed in: a wisp held inside a closed bag / a seal).
   Plus icons-sheet.png showing all three at 128, 64 and 32 px with captions "Self-stopping steep", "Up to 3 infusions", "Scent sealed in".
3. culture-motif.svg / .png (1600x600): Japan, China, Britain as three abstract marks in one row, linked by the arc, WITHOUT clichés (no pagodas, dragons, geishas, Big Ben, Union Jack, cherry blossom, chopsticks). Use the tea itself: Japan = sencha / the chasen whisk's fine lines, or matsukaze (the kettle's pine-wind) as ripples, 80 °C; China = gongfu, the gaiwan's lid and many short infusions as stacked arcs; Britain = the milk swirl into black tea at the boil, 100 °C. Each with a small label (JAPAN · 80 °C, CHINA · gongfu, BRITAIN · 100 °C) in Jost. Check the temperatures against truth/history-cultures.md.

Tools: write SVG by hand or with a Python script kept in /tmp/osme-brand/builder1/. Text inside SVGs: either convert to paths with /tmp/osme-brand/textpath.py (run with /tmp/osme-brand/venv/bin/python; text_path(text, size, wght, tracking) returns (d, width, cap_height, lsb)), or embed Jost via @font-face pointing to a base64 data URI of /tmp/osme-brand/font/jost-latin.woff2 (variable font, weights 100-900).
Render PNGs with /tmp/osme-brand/shot.sh <abs html path> <W,H> <out.png> (headless Chrome with the required --use-mock-keychain --password-store=basic and its own --user-data-dir; set DSF=2 env for 2x). Look at every PNG you make, critique it like a senior designer, and iterate at least once.
Log to ops/log.md as `HH:MM | brand-builder-1 | STATUS | line`. Do not edit other files. Don't git commit.
Return: list of files, and 2 lines on what you are least sure of.
