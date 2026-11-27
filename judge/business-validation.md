# Business validation v2 (business-validator-v2, fresh agent, 27 Nov 2026, 10:48)
Status: DONE. Tally: 36 PASS, 6 FIX, 2 ASK. No math error over 1%; all 17 re-opened sources say what the case says (one citation on the wrong Eightx page). Inputs: truth/business-case.md v2, deck/model_business.py (run: all outputs match the case), deck/business.html (rendered to /tmp/osme-biz-val/s1-s4.png), facts.md. Sources re-opened with WebFetch at 10:45-10:50.
Labels: SOURCED = opened page says it; ASSUMPTION = labelled as such; PASS / FIX (exact fix) / ASK.

## 1. Sources re-opened
| Number | Source quote / URL | Verdict | Fix |
|---|---|---|---|
| PG Tips £6.25 / 240 | "£6.25" / "£0.03 each", "Pg Tips Original (240)" (Morrisons). https://www.trolley.co.uk/product/pg-tips-240-black-tea-plant-based-biodegradable-tea-bags/ZLW941 | PASS | none |
| Lipton $4.99 / 100 | "$4.99 ($0.62/ounce)", "Lipton Black Tea Bags - 100ct". https://www.target.com/p/-/A-13010225 | PASS | none |
| Twinings EB $16.99 / 100 | Live JSON: "English Breakfast | 100ct | 16.99" (curl + parse 10:47; WebFetch truncated). https://www.twiningsusa.com/products.json | PASS | none |
| Pukka £5.00 / 20 | "£5.00" / "£0.25 each" (Tesco). Asda and Waitrose list £3.00. https://www.trolley.co.uk/product/pukka-peppermint-licorice-tea-bags/MFK612 | PASS | Optional: note Tesco price; at £3.00 it is $0.19 |
| Special.T €0.35 + €129 | "the EUR129 (US$180) Special.T by Nestlé machine and EUR0.35 (US$0.50) pods", dated 9 Nov 2010. https://newatlas.com/nestle-specialt-tea-machine/16883/ | PASS (dated 2010) | Slide 1 footnote: "Special.T: 2010 launch price" (case already says so; slide does not) |
| Hibiki-an Gyokuro $37 / 100 g | "US$37.00" on "Gyokuro Premium (100g/3.53oz)". https://www.hibiki-an.com/product_info.php/products_id/28 | PASS | none |
| Sips By $15, ~15 cups | "$15 a month, Sips by ships four teas per box"; "about 15 cups from each shipment" (updated 15 Nov 2022). https://reviewed.com/cooking/features/sips-by-review-a-subscription-box-for-the-tea-lover | PASS (2022) | none |
| Tea Forte $26 / 20 | "Black Tea Assortment Presentation Box | 26.00" (and Herbal, Green); description "contains 20 pyramid infusers". https://teaforte.com/products.json?limit=250 | PASS | Optional: label "presentation box" (a gift box, the cheapest per-infuser format may differ) |
| Starbucks UK EB Grande £2.85 | "English Breakfast Tea ... £2.55 (Tall) / £2.85 (Grande) / £3.05 (Venti)"; third-party guide, "prices vary by store". https://fastfoodsmenu.com/starbucks-menu-prices-uk/ | PASS (third-party) | none |
| HPC $2.70 to $91 a kg | "ranging from $2.70 USD to $91 USD per kg" (2025). https://dir.tridge.com/prices/hydroxypropyl-cellulose | PASS | none |
| Filter paper 18 gsm INR 580 to 597 a kg | Two listings, "₹ 580/Kg" (18 gsm) and "₹ 597/Kg" (18 GSM). https://m.indiamart.com/impcat/tea-bag-paper.html | PASS | Optional: "two listings, INR 580 and 597", not a range |
| Tin $1.70 (<288), $1.31 (5,000-10,000) | Visible table broken ("undefined"); schema markup: "price": 1.7 (1-287), "price": 1.31 (5000-10000). https://www.specialtybottle.com/metal-tin-containers/tea/tsq4 | PASS | none |
| Pick $0.25 | "From $0.25 per pick per order"; first four picks $0. https://revenuegeeks.com/shipbob-pricing/ | PASS | none |
| CAC $75 (F&B $53-$100) | Body: "Food & bev: $53–$100". $75 only in the page title ("Food $75"). https://eightx.co/blog/average-cac-ecommerce-vertical | PASS (cite as "midpoint of $53-$100, title says $75") | Say "$75 (midpoint of $53 to $100)" |
| Churn 4-7%, 3x ideal, scaling 1.5-2.5x | Churn page: "Healthy programs sit at 4 to 7%"; "clears the 3-to-1 LTV-to-CAC bar". "most scaling brands sit at 1.5 to 2.5x" is on the CAC page, not the churn page. | FIX (citation) | business-case.md §4 LTV:CAC row: cite https://eightx.co/blog/average-cac-ecommerce-vertical for "1.5 to 2.5x" |
| Card 2.9% + $0.30 | "eCommerce Transaction Fee / 2.9% + $0.30" (updated 18 Nov 2024). https://www.merchantmaverick.com/reviews/stripe-review/ | PASS | none |
| Migration test €165-€430 + €97 | "165–430 € per sample"; "97 € service fee per order" (excl. VAT). https://measurlabs.com/products/overall-migration-simulant-c | PASS | none |
| Tea $80/$50 a kg, coating $0.45/$0.10, packing, tag, fulfilment $6.50, retail 50%, 3 infusions, all volumes | Labelled ASSUMPTION in the case | PASS (ASSUMPTION) | Slide 2 does not say the $0.45/$0.10 membrane line and tea cost are assumptions; add "assumption" to the slide 2 footnote |

## 2. Math recomputed (python, model run + by hand)
| Item | Recomputed | Verdict | Fix |
|---|---|---|---|
| Ladder per cup | PG Tips 6.25/240 x 1.27 = 0.033; Twinings 16.99/100 = 0.17; Pukka 5/20 x 1.27 = 0.3175; Special.T 0.35 x 1.08 = 0.378; Lipton pod 0.36 x 1.08 = 0.389; Hibiki-an 37 x 5/100 / 3 = 0.617; Sips By 15/15 = 1.00; Tea Forte 26/20 = 1.30; Starbucks 2.85 x 1.27 = 3.62; OSME 1.50/3 = 0.50 | PASS | none |
| COGS Y1 / Y3 | 0.24+0.45+0.03+0.30+0.25 = 1.27; 0.15+0.10+0.01+0.05+0.11 = 0.42; tin 1.31/12 = 0.109 | PASS | none |
| Membrane material | 2 g/m² x 0.0084 m² = 0.0168 g; at $91/kg = $0.0015; paper 18 g/m² x ~$7/kg = $0.126/m², x 0.0084 = $0.001 | PASS | none |
| GM a bag | D2C 1.08 / 1.50 = 72.0%; retail 0.33 / 0.75 = 44.0%; pilot 0.23 / 1.50 = 15.3% | PASS | none |
| Ritual contribution | 24 - 6.72 - 6.50 - (0.029 x 24 + 0.30 = 0.996) = 9.78 (40.8%) | PASS | none |
| CAC payback, LTV, LTV:CAC | 75 / 9.78 = 7.67 mo; 9.78 / 0.07 = 139.7; 139.7 / 75 = 1.86x; life 1/0.07 = 14.3 mo | PASS | none |
| $2.00 / $2.50 table | cup 0.667 / 0.833; GM 1.58 (79.0%) / 2.08 (83.2%); retail 0.58 (58.0%) / 0.83 (66.4%); contribution 17.55 / 25.32; payback 4.27 / 2.96; LTV:CAC 3.34 / 4.82; Y3 11.31 m / 14.14 m; "25% fewer bags" 8.48/11.31 = 0.75 | PASS | none |
| Year-3 walk | 13,000 x 24 x 12 = 3.744 m; 180,000 x 18 = 3.24 m; 2 m x 0.75 = 1.50 m; total 8.484 m; bags 2.496 + 2.16 + 2.0 = 6.656 m; 13 k = (6 k + 20 k)/2 | PASS | none |
| Share of SAM | 8.484 / 640 = 1.33%; SAM/TAM 640 / 7,100 = 9.0% | PASS | none |
| TAM / SAM | 18.77 x 0.38 = 7.13 bn; 7.1 x 0.45 x 0.20 = 0.639 bn | PASS (SAM = ASSUMPTION) | none |
| Raise | 2.5 / 12.5 = 20%; use of funds 35+15+30+15+5 = 100%; one-offs 875 k = 35%, 375 k = 15% of 2.5 m | PASS | none |
| Slide 3 title "4 months instead of 8" | 4.27 and 7.67 rounded to whole months | PASS (rounding) | Optional: "4.3 months instead of 7.7" to match the table |
| Funding check, CAC spend | Case: "4 k to 20 k subscribers (16 k x $75 = $1.2 m)". At 7% monthly churn and 13 k average, year 3 alone loses ~11 k subscribers (13,000 x 0.07 x 12), which must be re-bought: ~$0.8 m more CAC in year 3. Also "4 k" start conflicts with "6 k start of year 3" unless 4 k is end of year 1 (not stated). | FIX | business-case.md §5 funding check: count gross adds, (20 k - 4 k) + churn replacement, ~27 k x $75 = ~$2.0 m CAC by end of year 3, and say when the 4 k is |
| Per-cup basis | OSME and Hibiki-an get 3 infusions; Tea Forte gets "one cup" though its infusers are also re-steeped | ASK | Team: state the basis on slide 1 ("Tea Forte counted as one cup") or give Tea Forte 2 cups ($0.65); OSME still under it |

## 3. Consistency with facts.md
| Item | Case / slides | facts.md | Verdict | Fix |
|---|---|---|---|---|
| Price $1.50, tin $18, Ritual $24/16 bags | same | same | PASS | none |
| TAM $7.1 bn, SAM $640 m, ask $2.5 m, $10 m pre | same | same | PASS | none |
| Competitors Tea Forte $1.30, Sips By ~$1, Special.T €0.35 + €129 | same | same | PASS | none |
| Year-3 SOM | **$8.5 m** (business-case v2, business.html slide 4) | **$8.3 m** ("business thread is re-running the walk"); deck/gate1.html also shows $8.3 m | FIX | ops/questions.md #31 says "$9 m -> $8.5 m" but facts.md already reads $8.3 m. Correct the question to "$8.3 m -> $8.5 m"; until the lead locks it, gate1.html and business.html disagree on stage |
| GM $1.08 / 72%, ladder, COGS $1.27/$0.42, $9.78, 7.7 mo, 1.9x, 20 k | on slides | not in facts.md | ASK | Already proposed in ops/questions.md #32; D5/X4 stay open until the lead adds them |
| $2.00 recommendation on slide 3 | shown as an option, slides keep $1.50 | $1.50 | PASS | none (question #30 open) |

## 4. Slides (deck/business.html)
| Check | Result | Verdict | Fix |
|---|---|---|---|
| En/em dashes | grep for U+2013/U+2014 in deck/business.html: 0 | PASS | none |
| embed-html --check | "business.html: self-contained" | PASS | none |
| Slide 4 retail bar | "$1.5 m" label in the teal segment is clipped at the right edge (/tmp/osme-biz-val/s4.png) | FIX | build_business.py: let the retail label sit outside/after the bar, or set the segment min-width so "$1.5 m" fits |
| Slide 4 bottom-up text | "= $3.7 m" wraps, leaving "m" alone on a line | FIX | Use a non-breaking space in "$3.7 m" (and all "$x m") or shorten to "6-20 k" |
| Slides 1-3 | No clipping or overflow seen | PASS | none |
| Slide 2 labels | Tea cost and membrane line $0.45/$0.10 are assumptions but the slide does not say so | FIX | Add "Tea, coating and packing: assumptions" to the slide 2 note |

## Addendum 10:49 (business-lead, after validation)
Judge r3 found 6 k start vs 4 k end of year 2. Settled on 4 k -> 20 k, average 12 k: Ritual $3.46 m, year 3 $8.20 m (1.28% of SAM), CAC in year 3 ~$2.0 m. Recomputed with deck/model_business.py; all other rows unchanged.
