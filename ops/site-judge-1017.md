# Site judge, 10:17 (docs/index.html)

Renders: /tmp/site-judge/j1-* (desk 1440, phone 390). No console errors, no horizontal scroll, embed-html --check: self-contained.

## 1. 10-second test (first screen only)

| | Desktop | Phone |
|---|---|---|
| What | YES. "A tea bag that opens only at its perfect temperature." | YES, same line, readable without scrolling |
| Who | WEAK. "Anyone who loves a good cup, and anyone who would love to" = "everyone"; a stranger says "tea drinkers, I guess" | WEAK, same chip |
| Price | YES. "$1.50 a bag, about $0.50 a cup" (Ritual $24/month not visible) | YES, chip is above the fold |

## 2. Scores (1-5)

| Criterion | Score | Why |
|---|---|---|
| Clarity | 5 | One-liner names a tea bag in 9 words, and the hero dial shows sealed/open live. |
| Customer evidence | 4 | 3 human segments, 3 verbatim linked quotes (TeaChat x2, Straight Dope), YouGov/Mintel/QMUL numbers. Gap: the hero says "everyone", and no count of how many curious specialty drinkers exist. |
| Credibility of product | 4 | "Honest" note, PNIPAm source, 80/70 °C used the same everywhere, $0.50 a cup. Gap: no unit cost and no "what is not proven yet" line next to price. |
| Story | 4 | 760, 1908, Now is clean and sourced. But it sits third, after the mechanism, so the "why" comes late. |
| Visual design | 4 | Midnight Brew is right: matte black, amber-to-jade arc, Futura display, restraint. Pulled down by five three-card grids in a row and a SaaS pricing table ("Become a Keeper" badge on the middle tier). |
| Phone | 4 | Text is clean and stacks well. The first screen is all text plus 2 stacked full-width buttons; the dial, the best visual, starts below the fold. 12,400 px tall. |

## 3. Senior designer critique

- Hierarchy: the hero is strong. "Every tea has its temperature." with the gradient word carries the brand. The one-liner in amber is the second read, which is right.
- Rhythm: How it works, Cultures, Who, Quotes and Price are all three equal cards. By the Who section the eye skims. Nothing is full-bleed and nothing breaks the 1140 px column until the manifesto.
- Imagery: no photograph or film anywhere. Only flat vector icons and one illustrated mug. video/renders/osme-loop_v01.mp4 (542 KB) exists and is not used. A stranger never sees a real bag in a real cup.
- Typography: good. Futura display, light body, wide-tracked labels. The body copy on desktop cards (about 13 px, grey) is on the edge of readable.
- Generic or empty: the pricing tiers look like a SaaS plan picker. The 96% card has no quote under it, so it reads unfinished. The empty band under the hero on desktop is wasted.
- Scroll-past risk: the cultures tea lists (6 rows of temperatures) and the source list. Fine as reference; nobody reads them on a first visit.

## 4. Top 3 changes

1. **Make "who" concrete in the hero (Clarity, Evidence, 10-second test).** Replace the FOR chip text with a named person. For example: "FOR people who pay for good leaf and hate a bitter second cup, and the friends who gift them". This matches the curious cup and the giver. Keep "Everyone can be a tea person." as the Who headline lower down.
2. **Use the film and break the card rhythm (Visual, Story).** Embed osme-loop_v01.mp4 (muted, autoplay, loop, playsinline, poster frame, as a data URI) as a full-bleed band between the hero and "Sealed. Open. Sealed.", with one caption line: "Sencha. Opens at 80 °C. Seals below 70 °C." Then turn the pricing tiers into one horizontal "Ritual" hero card with the bag and the tin as two small lines beside it, so the page loses one three-card grid.
3. **Get the dial into the phone's first screen (Phone).** At widths under 600 px: hide the 4-line body paragraph (the one-liner already says it), put the 2 CTAs side by side or drop "See how it opens", and move the dial (about 260 px tall) directly under the one-liner. Then a phone stranger sees the product working before they scroll.
