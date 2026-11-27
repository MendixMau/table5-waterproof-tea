# Table 5 · Waterproof Tea Bags

**Sell the unsellable.** Build 10:25 to 13:30 · pitches from 13:35 · done 14:30.
Everyone drives at least once.

<!-- LIVE:START -->
## Live status · 10:26 · 3 h 03 to hand-in

**Now:** Gate 1 at 10:40: you review brand, logo and market. Site, video and pitch wait for it.

| | Topic | Status | Latest preview |
|---|---|---|---|
| 🎨 | Brand & logo | 🟡 working · judge 21/25 · 10:22 | <img src="gallery/brand-v07-board.png" width="260"> |
| 🚦 | Gate 1 deck | 🟡 working · 10:23 | <img src="gallery/gate1-v01.png" width="260"> |
| 🍵 | Product demo | 🟡 working · 10:24 | <img src="gallery/product-v02.png" width="260"> |
| 🎤 | Pitch deck | ⚪ on hold · 10:18 | <img src="gallery/deck-v03.png" width="260"> |
| 🌐 | Site | ⚪ on hold · 10:20 | <img src="gallery/site-v02.png" width="260"> |
| 🎬 | Video | ⚪ on hold · 10:25 | <img src="gallery/video-v02.png" width="260"> |

**Waiting on the team:** Logo: B "Scent S"? · Price: tin $18, Ritual $24 · Ask $2.5m at $10m pre · Site: multi-page shop + real waitlist?
<!-- LIVE:END -->

## Five things to hand in by 13:30

| # | Hand-in | Definition | Lives in |
|---|---|---|---|
| 1 | Brand | Name, logo, one line | `facts.md`, `brand/identity/` |
| 2 | Customer | Who buys it, with evidence of where we found them | `truth/` |
| 3 | Product | Works today, on one laptop | `product/` |
| 4 | Site | What it does, who it is for, the price | `docs/` → GitHub Pages |
| 5 | Pitch | 3 minutes, product running, 8 slides | `deck/` |

Eight slides: 1 company · 2 problem · 3 solution · 4 customer evidence · 5 market · 6 business · 7 competition · 8 the ask.

## How we work

Lead thread → 5 topic threads → each runs **build → validate → judge** → a preview lands in `gallery/` at least every 10 minutes → the team decides at the gates.

| Topic | Output |
|---|---|
| 🎨 Brand & logo | `brand/identity/`, `brand/assets/` |
| 🍵 Product demo | `product/index.html` |
| 🎤 Presentation: Gate 1 deck, then the pitch | `deck/gate1.html`, `deck/pitch.html` |
| 🌐 Site | `docs/index.html` → GitHub Pages |
| 🎬 Video | `video/` |

**Alignment:** every thread reads `facts.md` (names, numbers), `brand/identity/tokens.css` (colours, type) and the logo files under fixed names, so one change there reaches deck, site, product and video. Every judge checks against `facts.md`.

## Rules

- **`facts.md` is the single source of truth.** Name, price, numbers: change them there first, never only on a slide.
- Every customer or market claim needs a source link in `truth/`. No source, no claim.
- Every HTML file is self-contained (images and CSS embedded) so it runs offline.
- Pull before you push. Work in your own pod's folder.

## Gates

| Time | Gate |
|---|---|
| 10:40 | **Gate 1 · brand, logo, market.** The team reviews `deck/gate1.html`. Site, video and pitch wait for it. |
| 11:00 | Build on the approved brand: product, site, video, pitch |
| 12:00 | Judge pass 1 |
| 12:45 | Judge pass 2 and full run-through |
| 13:15 | Freeze, rehearse twice |
| 13:30 | Hand in |
