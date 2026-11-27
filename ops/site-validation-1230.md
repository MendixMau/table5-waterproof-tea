# Site validation 12:30 (fresh validator, docs/ built 12:24)

Pages: index, shop, ritual, story, keepers, handin, script and the six tea pages. Shots and logs are in /tmp/site-val-1230/.

| Check | Verdict |
|---|---|
| Self-contained (`embed-html --check`, 13/13) | PASS |
| Console errors at 1440 and 390 | PASS (0) |
| Horizontal overflow | PASS (the only wide items sit in their own scrollers, `.ex-scroll` and `.tscroll`) |
| Prices on index, shop, ritual and tea pages ($2.00, $24, $32/month, about $0.67 a cup, up to 3) | PASS |
| Prices on script.html | **FAIL** |
| Tea windows, 6 of 6 | PASS |
| Ritual: 16 bags from 3-4 origins | PASS |
| Capsule wording on index | PASS (exact text, renders cleanly at both widths) |
| Membrane figure on index | PASS at 1440, FIX at 390 |
| Banned words | PASS (none in visible copy) |
| Exclamation marks | ASK (one, inside a quote) |
| Internal links and anchors, including handin's links to brand, customer, demo, pitch and script | PASS (the `shop.html#Japan/#China/#Britain` links work through the JS filter: #China showed 3 teas) |
| Hand-in tiles | FIX |
| Cart totals | PASS: bag $2.00, tin $24, 2 tins $48, 2 tins + bag $50, Ritual $32/month |
| Pre-order waitlist (saves locally, shows success) and phone menu | PASS |

## Defects

1. **script.html, FAIL.** The page still has the old price: "One bag is a dollar fifty … fifty cents a cup", "$1.50 minus $0.42" and the Q1 note. deck/script.md was fixed at 12:29, after the 12:24 build, so the page is stale.
   Fix: rerun `docs/_src/build.py`.
2. **handin.html, FIX.** All 5 tiles show an empty 72 px strip with only a number badge, because `docs/_src/thumbs/` is empty. The "1" badge also repeats the "1 · Brand" label.
   Fix: put brand/customer/product/site/pitch `.jpg` files in `_src/thumbs/` and rebuild, or drop the `.ho-img` strip.
3. **index.html at 390, FIX.** The membrane figure is one baked image, so its gate labels, the R&D line and the sources come out at about 5 px. The "Play the explainer" button also covers the image's top-right corner.
   Fix: give phones a crop, or let the HTML caption carry the R&D line, and move the button below the figure on phones.
4. **index.html, ASK.** The forum quote "…throw them away after one steep!" breaks the no-exclamation rule. It is a verbatim quote.
   Fix: end it with a period, or keep it as verbatim.
5. **Cart, all pages, minor.** One bag reads "1 bags · up to 3 cups".
   Fix in `_src/site.js`: show "bag" when the count is 1.
6. **index.html hero at 390, minor.** The "Sencha: opens at 80 °C…" caption overlaps the saucer.
   Fix: add about 16 px top margin to the caption on phones.
