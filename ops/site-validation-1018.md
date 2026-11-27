# Site validation 10:18 (docs/index.html, sha ca1f5d76)

Evidence: /tmp/site-val/v1-{desk,phone}-{first,s0..s7}.png (snap.js). desk scrollWidth 1440/1440, phone 390/390. Console: no errors. embed-html --check: self-contained, exit 0.

| ID | Verdict | Evidence | Fix |
|---|---|---|---|
| S7 Published | FIX | https://mendixmau.github.io/table5-waterproof-tea/ serves the old "Table 5" placeholder (sha 6721d250, local ca1f5d76). .../demo.html returns 404, so the hero's "Try the live demo" link is dead. docs/demo.html is untracked. | Lead: `git add docs/index.html docs/demo.html`, commit, push; re-curl both URLs and compare shasums. |
| X6 One-liner | FIX (facts.md) | facts.md One-liner = `_TBD_` (by the checklist rule, that's a FAIL). Site and deck both use "A tea bag that opens only at its perfect temperature." | facts.md: `\| One-liner \| _TBD_ \|` -> `\| One-liner \| A tea bag that opens only at its perfect temperature. \|` |
| X7 Colours/font | FIX (facts.md + 1 line) | facts.md Colours/Font = `_TBD_`. All 10 site hex tokens match brand/identity/tokens.css exactly. Site `--font-display` starts with "Futura","Jost"; tokens.css starts with "Jost","Futura". No font is embedded. | facts.md Colours -> "tokens.css: bg #0B0B0D, surface #17171B, primary #F2A33A, mid #D9C46B, accent #3DBA9B, text #F3EEE6"; Font -> "Display Futura/Jost, body Avenir Next". Then put the two display stacks in the same order (the site builder or tokens.css). |
| X4 Numbers | FIX (facts.md) | Site numbers not in facts.md: 32% Gen Z green tea (YouGov), 7 in 10 gift (Mintel), 96% bags (QMUL), 100 million cups (tea.co.uk), 760, 1908, c.1840, 1,200 years, and five tea temperatures besides Sencha. I opened every source and each one says the claim. | Add a facts.md row "Site proof points" listing these values and their URLs (as in the site footer). |
| Footer src 2 | FIX (minor) | Wikipedia says "written by Lu Yu in the 760s CE", not 760–762. | docs/index.html l.596: `The Classic of Tea, 760–762 CE.` -> `The Classic of Tea, 760s CE.` |
| S1 First screen | PASS | Desk and phone first screens show "A tea bag that opens only at its perfect temperature" + "stays sealed while too hot, opens, closes as it cools" + the 82° SEALED arc. |  |
| S2 Who | PASS | Exact facts phrase: "OSME is for people worldwide who love tea and its rituals." Hero chip: "anyone who loves a good cup, and anyone who would love to". |  |
| S3 Price | PASS | $1.50 single bag, $18 tin of 12, $24/month Ritual, about $0.50 a cup: these match facts.md. Phone first screen shows $1.50. |  |
| S4 Self-contained | PASS | embed-html --check exit 0. |  |
| S5 Phone | PASS | 390 = 390, no overflow; I looked at all 8 slices and no text is cut off. |  |
| S6 No placeholder | PASS | "Coming soon": 0. |  |
| X1 Name | PASS | Only "OSME". 0 hits for Osme, Osmé or old names. |  |
| X2 Price | PASS | Site matches facts.md. Deck has $1.50 a bag, the $18 tin of 12 and $24/mo. |  |
| X5 Temps | PASS | Site = product/demo profiles: Sencha 80/70, Gyokuro 60/50, Longjing 85/75, Tieguanyin 95/85, Pu-erh 100/95, English Breakfast 100/90. Footer marks the non-Sencha temperatures "design targets". |  |
| Brief sections | PASS | Hero (logo, tagline, arc visual, one-liner). Sealed/Open/Sealed with 80/70 and a demo link. Japan/China/Britain with temperatures. Segments + 3 quotes. Price. Manifesto, Keepers, #ThreeBubbles, waitlist button ("nothing is sent"). Footer with 12 sources. |  |
| Banned words | PASS | 0 hits: app, smart, disrupt, users, consumers, instant, AI, hack, game-changer, revolutionary, screen, phone, emoji. The only "!" is inside hopeofdawn's quote (customer quotes are excepted). |  |
| Quotes | PASS | All 3 are verbatim at their URLs with the right author: hopeofdawn and silversun at teachat p=212298, leroy_the_mule at straightdope /85495. Lu Yu's line is on Wikisource ch. II. Ichi-go ichi-e is on Wikipedia. |  |

Tally: PASS 12, FIX 5 (1 blocking: S7 publish; 3 facts.md fills; 1 minor copy), ASK 0.
