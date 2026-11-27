# Deck v2 validation: /tmp/osme-v03.html (fresh validator)
Renders: /tmp/osme-v03/ (1920x1080), /tmp/osme-val-1600/ (1600x900, ?still). Script checks skipped (deck/script.md still v1).

| ID | Result | Evidence | Exact fix |
|---|---|---|---|
| V5a | FAIL | s3: footer "3 / 8 · 0:45 to 1:25" (#snum) sits on the lower edge of the iframe's FULL SCREEN button, at 1920 and 1600 | s3: hide #snum on slide 3 (`body.s2 #snum{display:none}`) or lift it above the product control bar |
| V5b | FAIL | s8 end state: the glowing ground arc under the cup starts under "Origin, stock and ops" and runs through the 20% label | s8: start the ground arc right of the label (x > 1150 px at 1920) or move the 20% label up/left |
| V5c | FAIL | s2 end state: the dimmed timeline (CHINA/JAPAN/BRITAIN/TEA BAG, years, icons) stays behind the two cups; the OSME bag string crosses "JAPAN", "1908" sits under "More than" | s2: fade the timeline row to opacity 0 (or move it up out of the cup zone) once the cups enter |
| V2 | FAIL | s3 shows "3 infusions, one bag" with no source in its notes; s6 tin label "OPENS AT 80 °C" not sourced in s6 notes | s3 notes add: "3 infusions: up to 3 a bag, facts.md Price (ASSUMPTION, lab target)". s6 notes add: "Sencha opens at 80 °C (facts.md, tea windows)" |
| V1a | ASK | facts.md says "Up to 3 infusions"; s3 chip "3 infusions, one bag", s6 title "brews 3 cups", label "3 cups a bag" | s3 chip: "Up to 3 infusions, one bag"; s6 title: "One $1.50 bag brews up to 3 cups: $0.50 a cup, ..." |
| V1b | ASK | s2 "More than 96% of Britain's tea now comes from a bag" (QMUL 2016) vs s4 "16% ... brew their black tea loose leaf" (UKTIA 2024: 84% bag). A juror can add 96 + 16. Also source says 16% of black tea brewing, slide says "of UK tea drinkers" | Team pick: keep both but s4 text "16% of British black tea is already brewed loose leaf"; or drop 96% and use UKTIA 84% on s2 |
| V6 | PASS (note) | Engine: N notes, T timer 3:00 (Shift+T reset), #tgt "target <end>", bottom-right "N / 8 · from to" on every slide. s3: deck focus Space/Enter forwarded to product, R reset, PageDown/PageUp navigate; iframe-focus capture handler: PageDown next, PageUp/Left back, product handles Space/Enter/R. Not driven headless (time). Mismatch: notes say "PageDown or Right next slide", but focus is put inside the iframe after 300 ms and the product maps ArrowRight to pour | s3.html line 62: `if(k==='PageDown'||k==='ArrowRight')DECK.next();` or change note to "PageDown next slide" |
| V1 | PASS | $8.3 m (no $9 m on stage), 1.3%, $1.08 / 72% "at year-3 scale", $0.50 a cup, TAM $7.1 bn, SAM $640 m, $2.5 m SAFE at $10 m pre, 35/15/30/20 (15+5), Tea Forte $1.30, Sips By ~$1, Special.T €0.35 + €129, PG Tips $0.03, Starbucks $3.62, 760 / 1500s / c. 1840 / 1908 all match model_business.py at 1.50 and truth/. 96% wording = truth safe line | - |
| V3 | PASS | `grep -c '[–—]'` = 0 for s1..s8.html and build_pitch_v2.py; built HTML 0 outside srcdoc, 0 entities. Product srcdoc (separate): 0 dashes | - |
| V4 | PASS | English only; positive tone; "tea-tech disruptor" absent from stage copy. (Spoken panel from script v1 has it on s8: script topic) | - |
| V7 | PASS | embed-html --check: "osme-v03.html: self-contained" | - |
| V8 | PASS | Each slide: brand visual (bag/S string, arc, tins) + motion (s1 film, s2 9 s timeline, s3 live demo, s4 wisp, s5 rings + count, s6 bars + count, s7 plot reveal, s8 arc + count) | - |

Separate, product iframe (other topic): s3 still "The bag is still / in. 8:02 steeped." wraps mid-phrase; make it "Still in: 8:02 steeped."
Separate, script v1 text in the spoken panel: s5 "nine million dollars", s6 "sixty-two percent", s8 "As a tea-tech disruptor", s3 "press D" (product uses F). Fix in script v2.
Render artefact (not a deck bug): strip frames for s2/s6/s7 show slide 1 fading out because each shot deep-links from load; s8 count-up m2 frame reads "$0.0 m" (ASK: check live that the count does not restart).

Tally: PASS 6 / FAIL 2 (V5 x3 items, V2), ASK 2 (V1a, V1b)
