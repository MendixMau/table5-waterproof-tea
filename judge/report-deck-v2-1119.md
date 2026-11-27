# Deck v2 validation, frozen build /tmp/osme-v04.html (renders /tmp/osme-v04/, 1600x900 at /tmp/osme-val-1600/)
Script checks and spoken-notes text skipped (v1, being rewritten).

| ID | Result | Evidence | Exact fix |
|---|---|---|---|
| V5 | ASK | s3.png at 1920 and 1600: the "Lab-proven: membranes open and close with heat..." pill sits on the bottom edge of the OSME and 1908 panels and touches the "1st infusion · the same bag" line. Everything else clean at both sizes; no tables; max 2 data elements per slide. | Slide 3, `.s3-proof` pill: move it down about 24 px (or lift the iframe panels) so it clears the panel border. |
| V1 | ASK | Slide 2 says "OSME seals at 70 °C"; facts.md and slide 3 say "seals below 70 °C". | Slide 2, cup caption: "OSME seals below 70 °C". |
| V8 | ASK | Count-ups in the strips show passing values ($5.8 bn on slide 5 at 0 s, $1.9 m on slide 8). Probably a headless timing artifact; a jury member may read a wrong figure mid-count. | Optional: slides 5 and 8, start the counters from 0 and count up in under 1 s. |
| V1 | PASS | Built HTML: no __NUM left. $7.1 bn, $640 m, $8.3 m, 1.3%; $1.50, 3 infusions, $0.50 a cup; 72%, $1.08 "at year-3 scale"; Sips By $1.00, Tea Forte $1.30, PG Tips $0.03, Starbucks $3.62; $2.5 m SAFE at $10 m pre; funds 35/15/30/20 (=15+5); 20 k subs; 96% (QMUL 2016); 16% (UKTIA 2024, black tea); 760, 1500s, c. 1840, 1908. All match model_business.py at 1.50 and truth/. | none |
| V2 | PASS | Every on-screen number has a source in its slide's aside, including tin of 12 (s6) and the 5:40 timer (marked illustration, s2). | none |
| V3 | PASS | 0 en/em dashes in fragments, build, visible copy and the iframe srcdoc. | none |
| V4 | PASS | English only; positive tone; "tea-tech disruptor" not in slide copy (only in v1 spoken note of slide 8, a jury slide). | none |
| V6 | PASS (code read, not driven) | Engine: N notes, T/Shift+T timer 3:00, `tgt` shows target bottom-right per slide. s3.html: DEMOKEY hands Space/Enter pour, R reset to the demo; iframe listener gives PageDown/PageUp/N/T to the deck. | none |
| V7 | PASS | embed-html --check: "osme-v04.html: self-contained". | none |
| V8 | PASS | Every slide has a brand visual and motion: s1 film, s2 9 s timeline (China, Japan, Britain, 1908, cups, 96%), s3 arc intro then live demo, s4 typed quotes, s5 rings and counters, s6 bars and tins, s7 axes then dots, s8 arc and count-up. | none |

Not checked (out of scope): spoken notes still v1 ("nine million dollars" s5, "sixty-two percent" s6), to be replaced by the script rewrite.

Tally: PASS 7 / FAIL 0 / ASK 3
