# Site judge v2 (fresh eyes): 10:51

Target: `docs/` multi-page shop (index, shop, tea-sencha, ritual, story, keepers + cart). Renders in `/tmp/site-judge2/` (first screen + full page, 1440 and 390) and ordered slices in `/tmp/site-judge2/sl/`. Cart script: badge 3, total $37.50, pre-order saved, no console errors.

Hand-in line: "A real multi-page shop on GitHub Pages with a working waitlist." **Verdict: the shop is real; the waitlist is not.** `WAITLIST = { kind: "" }` in every page, so emails go to localStorage, and every form prints "Pre-launch: your email is saved on this device until our waitlist service is connected." A juror who types their email reads that the site did not save it.

## 1. 10-second test, Home first screen

| | Desktop 1440 | Phone 390 | What a stranger says |
|---|---|---|---|
| What it is | Yes | Yes | "A tea bag that only opens at the right temperature. The cup shows it." The H1 is a tagline, but the subline gives the product noun in the first glance and the animated cup proves it. |
| Who it's for | Weak yes | Weak yes | "Tea people... and anyone?" The FOR pill says "curious tea drinkers who pay for good leaf and hate a bitter cup, and anyone who would love to be one". The second half cancels the first, and the pill is the smallest text on the screen. |
| Price | Yes | Yes | "$1.50 a bag, 50 cents a cup, $24 a month." It shows on the phone first screen too, above the CTAs. |

The first screen passes. The FOR/PRICE capsules look like input fields or chips, not like a premium statement.

## 2. Scores (1-5)

| Criterion | Score | Why |
|---|---|---|
| Clarity | 4 | Product, price and mechanism are clear in 10 s on both devices. One gap: "who it's for" is diluted to "everyone" (home section H2 "Everyone can be a tea person."). |
| Customer evidence | 3 | Three verbatim forum quotes with handles and links (TeaChat, Straight Dope) are good. But there is no single named customer, no count of how many exist, and the 32% stat is misquoted: the site says "32% of UK Gen Z drink green tea", while facts.md says "32% of Gen Z daily tea drinkers choose green tea". |
| Credibility of the product | 3 | The "HONEST" note (PNIPAm source, "Pre-orders ship after the food-safe proof") is strong. Undercut by: the bag never appears as a real object (only a line drawing), there is no ship date or timeline, and a waitlist that admits it is not connected. |
| Story | 4 | 760s → 1908 → Now timeline plus the manifesto on Keepers is clean and sourced. Lu Yu / three bubbles repeat on Home, Story, Keepers and Ritual, so the fourth time it reads as filler. |
| Visual design | 4 | This really is Midnight Brew: matte black, amber→jade arc text, temperature-coded numbers, a hero cup animation that does the job. It drops to template in the card grid (3-up rounded cards on every page), six identical black tins, and the same benefits row and waitlist panel cloned on every page. |
| Phone experience | 3 | Layout holds, no overflow, the menu works. But: the "added" toast sits on top of the PRE-ORDER button in the phone cart drawer (`cart-phone.png`), and after submit the success message is hidden below it (`cart-phone-done.png`). The shop's phone first screen shows no product, only H1, filters and the Ritual banner. Home is 9,780 px of stacked cards. |
| Shop credibility | 3 | Cart, quantity, totals, cost per cup, tin/bag/Ritual options and breadcrumbs all work and feel real. Missing: a working email capture, any ship date, shipping/returns/FAQ, more than one image per product (no leaf, no bag, no brewed cup), and tasting notes beyond one line. Six tins differ only in a 9 px label. |

## 3. Senior designer critique

- **Hierarchy.** Home hero is right: a big tagline, an amber product line, then proof. On inner pages the H1 repeats the tagline (Shop: "Every tea has its temperature." again), which wastes the most valuable line on the page. The Ritual hero ("One box a month. One cup a day, made with love.") is the best inner-page H1.
- **Rhythm.** Every page ends with the same sequence: benefits row (Stops itself / Scent kept / Up to 3 cups), then about 180 px of empty gradient band, then the waitlist panel, then a 14-line sources footer. The empty band above the waitlist (`.movement` section padding) reads as a broken load on Home, Ritual and Keepers. Sources on every footer are good for the jury but heavy for a shopper.
- **Typography.** Jost is used consistently and the tracked small caps eyebrows are elegant. Problems: the waitlist H2 breaks as "Take back one cup a / day." (an orphan); the "ē" in "Greek osmē" falls back to another font and looks broken in every footer; the FOR/PRICE pill text is about 12 px, too small for the most important facts.
- **Imagery.** This is the biggest gap. No photography anywhere: no leaf, no water, no hands, no cup with real tea. Six product tiles are the same rendered black tin, and the tin label is unreadable at card size. The Story culture icons (spiral, pot, whisk) are nice and should be used more. The one strong visual, the hero cup opening, is not reused on the product page, where it would sell hardest.
- **Generic / repetitive.** The 3-up card grid is used for steps, teas, personas, quotes, cultures and the Ritual steps. Lu Yu's three bubbles appears on 4 pages. The "HONEST" note is duplicated verbatim on Home and Story. Keepers mentions a Keeper count (`data-keeper-count`) that is hidden, so the "movement" page has no proof of movement.
- **What works.** The hero cup animation; the drag-the-temperature slider; the Sencha product page layout (temperature tiles, window bar, tin/bag/Ritual radios, "See Sencha open in the live demo"); the cart's "25 bags · up to 75 cups · about $0.50 a cup" line; the example Ritual box grid coloured by tea.

## 4. The 3 changes that raise the scores most

1. **All pages (shared JS): make the waitlist real and say so.** Set `WAITLIST = { kind: "formspree", endpoint: "https://formspree.io/f/<id>" }` (or the Google Form option already coded) in the shared script block of every page, and rebuild. Delete the "Pre-launch: saved on this device" note, and show "You are Keeper #N" from `countUrl` so the hidden `data-keeper-count` turns on (Home and Keepers). Test one real submission from the GitHub Pages URL. Raises Shop credibility, Credibility and the hand-in line itself.
2. **tea-*.html and shop.html: give the product a body.** On each tea page, replace the single tin image with a 3-frame gallery: tin; the hero cup animation embedded at that tea's own open/seal values (reuse the index hero component with `data-open=80 data-seal=70`); a dry-leaf/brewed-cup colour card. Add a short block with tasting notes (3 words), "Ships: after food-safe proof, target <month>" and a 4-question FAQ (Is it safe? When does it ship? Can I cancel the Ritual? Is the bag plastic-free?). In shop.html, enlarge the tin label (tea name 2x) or tint each tin's lid in its tea colour so six products stop looking like one. Raises Shop credibility and Visual design.
3. **Phone cart + Home "Who it's for": fix the toast and name one customer.** (a) In the shared CSS/JS, hide the toast while the cart drawer is open, or put it at the top on screens under 600 px, so PRE-ORDER and the success message are visible (`cart-phone.png`). (b) On index.html, change the H2 "Everyone can be a tea person." to one named customer ("For the curious cup: people who pay for good leaf and hate a bitter cup") and correct the stat to the facts.md wording: "32% of Gen Z daily tea drinkers choose green tea (YouGov)". Add a size number from truth/business-case.md under it. Shorten the hero FOR pill to the first clause only. Raises Phone experience, Customer evidence and Clarity.

Smaller: cut the empty band above the waitlist (reduce `.movement` padding-top); use `text-wrap: balance` on the waitlist H2; on Shop, put the first product row above the fold on phone (move the filter chips into one scrollable row and the Ritual banner below the grid); render "osmē" with a font that has the glyph, or write "osme".
