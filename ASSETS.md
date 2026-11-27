# Shared assets: one library for the deck, film, site and demo

**Rules for every thread**
1. Before you draw or animate anything, look here. Reuse the file; don't redraw it.
2. If you make something another topic could use, export it self-contained, in your own folder or in `shared/<topic>/`, and add one line to this table.
3. Keep to one storyline, one set of numbers and one look:
   - Storyline: `truth/storyline.md`, "The Art of Tea: 1,200 years of temperature".
   - Numbers: `facts.md` and `truth/business-case.md`.
   - Look: `brand/identity/tokens.css` (Midnight Brew, Jost).

| What | File | Owner | Use it for |
|---|---|---|---|
| Logo: lockup, symbol, wordmark (each also as -mono and -mono-black) | `brand/identity/logo-lockup.svg`, `logo-symbol.svg`, `logo-wordmark.svg` | brand | Everywhere. Below 40 px, use `logo-symbol-small.svg` |
| Colours and font | `brand/identity/tokens.css`, `brand/assets/fonts/` | brand | Every HTML file |
| Hero cup, static | `brand/assets/hero.svg`, `hero-titled.svg` | brand | Deck slides 3 and 8, site |
| Hero cup, alive (steam, breathing arc, loop) | `brand/motion/hero-alive.svg` | brand | Behind deck slides 3 and 8 |
| Arc sweep, the signature transition | `brand/motion/arc-sweep.svg` | brand | Every slide entry, film transitions |
| Logo reveal (the S rises out of the bag) | `brand/motion/logo-reveal.svg` | brand | Deck slides 1 and 8, film ending |
| Count-ups for big numbers | `brand/motion/count-up.js` | brand | Every big number |
| Steep-reveal entrance | `brand/motion/steep-reveal.css` | brand | Text entrances |
| Three bubbles rising (Lu Yu) | `brand/motion/three-bubbles.svg` | brand | Deck slide 1, film 0–3 s |
| All motion pieces in one page | `brand/motion/demo.html` | brand | Browse them |
| Culture motif: Britain, China, Japan | `brand/assets/culture-motif.svg` | brand | Deck slide 2, film history beats, site story |
| Icons: self-stopping, scent sealed, three infusions | `brand/assets/icon-*.svg` | brand | Deck slide 3, site |
| Tin and single bag, transparent for dark backgrounds | `brand/assets/pack-tin-transparent.svg`, `pack-single-bag-transparent.svg` | brand | Deck slide 6, site, film |
| #ThreeBubbles social tile | `brand/assets/social-threebubbles-1080.svg` | brand | Deck slide 4, social |
| Pattern | `brand/assets/pattern-bubbles*.svg` | brand | Texture |
| Brand film, silent | `video/osme-film.mp4` | video | Full-bleed on deck slide 1, site |
| Ambient loop and poster | `video/osme-loop.mp4`, `video/osme-loop-poster.jpg`; web cut at `docs/_src/loop-web.mp4` | video, site | Behind deck slide 8, site hero |
| Live demo: two cups, the 1908 bag next to OSME | `product/index.html`. F gives full screen and presenter mode; `#tea=sencha&sec=16` jumps to the rehearsal point | product | Full-screen on deck slide 3, site `demo.html` |
| Site hero cup with temperature arc | `docs/_src/hero-cup.svg`, `hero.js` | site | Deck slide 3, film |
| Site sections: the 1,200-years timeline, Sealed · Open · Sealed, the six tinted tins, the temperature slider | Coming in `shared/site/` | site | Deck slides 1–3 and 6, film |
| Business charts: price ladder, market circles | `deck/build_business.py` builds `deck/business.html` | business | Deck slides 5 and 6 |
| "What's inside" exploded view | Coming in `shared/product/` | product | Deck backup slide, site "How it works" |
| Dwi's Osme Control concept. Reference only: it is a manual capsule, not our product | `refs/dwi-osme-control/` | none | Ideas only: the plume close-up, the exploded view |
