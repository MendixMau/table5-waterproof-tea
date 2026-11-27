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
| Steep-reveal entrance | `brand/motion/steep-reveal.css` | brand | Text entrances (decks: `data-steep="wait"` on every slide) |
| Three bubbles rising (Lu Yu) | `brand/motion/three-bubbles.svg` | brand | Deck slide 1, film 0–3 s |
| Title card "1,200 years of temperature": Lu Yu's bubbles, the arc, Britain · China · Japan (animated, all in by 3.5 s, then holds; static SVG + PNG) | `brand/motion/title-1200-years.svg`, `brand/assets/title-1200-years-static.svg` (+ `.png`) | brand | Deck slide 1, film 0–3 s (beats 1–2) |
| Play and pause all motion in a slide: `osmePlay(slide)`, `osmePause(slide)` | `brand/motion/osme-play.js` | brand | Deck slide changes |
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
| Site hero cup + temperature arc, animated (Sencha cooling loop), with or without headline | `shared/site/hero-cup.html`, `hero-cup-solo.html` (+ `.png` still) | site | Deck slide 3, film "Now" beat |
| 1,200-years timeline: 760s · 1908 · Now | `shared/site/timeline.html` (+ `.png`) | site | Deck slides 1–2, film history beats |
| Sealed · Open · Sealed cards (Sencha >80 / 80–70 / <70 °C) | `shared/site/sealed-open-sealed.html` (+ `.png`) | site | Deck slide 3 |
| Six tins, tinted per tea, with opening temperatures | `shared/site/six-tins.html` (+ `.png`) | site | Deck slide 6, film product beat |
| Temperature slider, interactive; `?auto` sweeps 100→60→100 °C for recording | `shared/site/slider.html` (+ `.png`) | site | Deck slide 3 live, film |
| Lu Yu's three bubbles row: fish eyes, string of pearls, rolling waves | `shared/site/bubbles-row.html` (+ `.png`) | site | Deck slide 1, film 0–3 s |
| Deck versions of all seven site pieces: every HTML text ≥ 28 px at 1920, ranges as "80 to 70 °C" (no dash). SVG art keeps its own type | `shared/site/<piece>-deck.html` (+ `-deck.png`) | site | Deck slides: use these, not the web versions |
| Membrane explainer, on the site | `docs/membrane.html` (copy of product's `shared/product/membrane-how.html`), still on `docs/index.html#how` | site | Live since 12:23 |
| Hand-in page: the brief's five things, five tiles | `docs/handin.html`, linked from every site footer | site | Hand-in URL …/handin.html |
| How to use the shared/site slides: 1920x1080, scale to any window or iframe; rebuild with `python3 docs/_src/shared.py` (same components as the site) | `docs/_src/shared.py` | site | Rebuild after a logo or number change |
| Business charts: price ladder, market circles | `deck/build_business.py` builds `deck/business.html` | business | Deck slides 5 and 6 |
| "What's inside" exploded view: 5 layers (tag, seal, filter, membrane, leaf) + Sencha membrane inset (sealed / open / sealed), 1600×1000, Jost embedded | `shared/product/exploded-view.svg` (static), `shared/product/exploded-view-animated.svg` (12 s loop: 100 → 80 °C opens → below 70 °C seals; works as `<img>`) | product | Deck backup slide, site "How it works" (live on docs/index.html#how since 11:33). Regenerate: `python3 shared/product/_src/gen-exploded.py .` |
| Dwi's Osme Control concept. Reference only: it is a manual capsule, not our product | `refs/dwi-osme-control/` | none | Ideas only: the plume close-up, the exploded view |
