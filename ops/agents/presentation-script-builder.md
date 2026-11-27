# Presentation: script builder brief

Repo: /Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
Read first: ops/agents/_common.md, facts.md, deck/story.md (draft 2, its "3-minute script" section is your base).
Output: deck/script.md (if it exists, RESUME from it). Save a skeleton within 3 minutes. Log to ops/log.md as `presentation-script`.

## Task
Write the final 3-minute pitch script, 400 to 420 words of spoken text (count with `wc -w` on the spoken lines only, and report both counts), from story.md's script. Keep its arc and voice; fill every placeholder with these locked numbers:

| Slide | Numbers to say (and their source, list them at the bottom of script.md) |
|---|---|
| 1 Company | Lu Yu's Classic of Tea, written 760 to 762 CE ("twelve hundred years ago" is fine); three boils "fish eyes, string of pearls, rolling waves" (facts.md; Okakura 1906 in truth/history-cultures.md §2). OSME said "oz-MAY", Greek osmē = scent. |
| 2 Problem | Tea bag about 1908 (truth/history-cultures.md §4). "More than 96 in every 100 cups of tea in Britain are made with a bag" (QMUL 2016, history-cultures.md §4). Do NOT say 97. |
| 3 Solution DEMO | Sencha (Japan): boiling water 100 °C, the OSME bag opens when the water cools to 80 °C and seals again below 70 °C (facts.md Demo tea). Up to 3 infusions per bag (facts.md Price). Ordinary 1908 bag side by side, keeps steeping. |
| 4 Customer | Curious specialty drinkers: anyone who loves a good cup, and anyone who would love to (facts.md). Three quotes paraphrased: forgot the bag for 20 minutes (Hacker News), throwing leaves away after one steep (TeaChat), leaves not fresh the next day (TeaChat). Number: 16% of British tea drinkers already brew loose leaf (UKTIA 2024, customers-market.md §2). |
| 5 Market | The world spends $7 billion a year on tea bags (TAM $7.1 bn = $18.8 bn × 38%). First markets Japan, China, Britain and the US: $640 million (SAM). Year 3: $9 million in sales (SOM). |
| 6 Business | D2C web shop, "Ritual" subscription $24 a month, then premium retail. 12-bag tin $18. Up to 3 infusions, so about 50 cents a cup. 62% gross margin direct (truth/business-case.md §3). Ritual members are Keepers. |
| 7 Competition | Loose leaf and gongfu keep the art but ask time and skill; Tea Forte pyramid bags look premium but still over-steep and give one cup; Nestlé Special.T capsules need a €129 machine. Only OSME: art and ease, in one bag, no machine. |
| 8 The ask | $2.5 million on a SAFE at a $10 million pre-money valuation, to prove the food-safe membrane and ship the first Ritual boxes (facts.md). Honesty line: "The principle exists: lab membranes already open and close with temperature. Our R&D makes it food-safe at 70 to 90 degrees." Close: "Every tea has its temperature. Take back one cup a day, and become a Keeper. OSME." |

## Rules
- Format: one block per slide: `**0:00 to 0:20 · Slide 1 · Company**` then the spoken lines. Timing at about 140 words a minute, ending 3:00.
- Slide 3 must carry a marked cue line `[DEMO] ...` saying what the presenter clicks (press D or the slide shows the live app; click "Pour 100 °C") and what the jury sees. Demo spoken text at most 140 words.
- Tone (facts.md, _common.md): positive (life, art, scent, love), everyone can be a tea person, never anti-screen, anti-phone or anti-AI. "Tea-tech disruptor" only on slides 5, 6 or 8, at most once.
- No em dashes or en dashes anywhere in the file (`grep -c '[–—]' deck/script.md` must be 0). No numbers other than those above.
- English only. Spoken style: short sentences, numbers written as they are said.
- Under the script: a "Numbers and sources" table (number, slide, source file and section) and a "Questions for the team" list if any.
- Do not edit any other file. Do not git commit.
