# OSME business case v2 (business-lead, 27 Nov 2026, 10:50)
Status: v2, validated (judge/business-validation.md) and judged 4.5/5 (slides 5, 4, 4, 5). USD throughout (£1 = $1.27, €1 = $1.08: ASSUMPTION rates). Every number is SOURCED (URL opened 27 Nov 2026 unless dated) or labelled ASSUMPTION. Model: deck/model_business.py (run it to recompute everything below). Slides: deck/business.html.

## What changed since v1
- **Price is $1.50 a bag everywhere** (facts.md, team 10:23). v1 used $2.00 singles, so its blended $1.38 a bag and $9.0 m year 3 are stale. **Year 3 is now $8.3 m** (1.3% of the $640 m SAM), matching facts.md.
- **New: per-cup price ladder** with 9 opened prices (§2). OSME at $0.50 a cup is half a Sips By cup and under half a Tea Forte pyramid.
- **New: cost stack per bag, year 1 vs year 3** (§3): $1.27 pilot, $0.42 at scale (v1: $0.36 to $0.85 range, midpoint $0.605). Membrane material is sourced at under 1 cent a bag; the rest of the membrane line is an ASSUMPTION for coating and yield.
- **Gross margin a bag at scale: $1.08 (72%) direct, $0.33 (44%) retail** (v1 said 62%, validator 59.7%).
- **New: Ritual contribution after post and card fees: $9.78 a month; CAC payback 7.7 months; LTV:CAC 1.9x** at $1.50 (v1 said 2.8x on gross margin only, before fulfilment).
- **New: price sensitivity** $1.50 / $2.00 / $2.50 (§6). **Recommendation: $2.00 a bag** ($0.67 a cup); the team decides.
- **New: public subscriber counts** as a plausibility check (§5).

## 1. Market: TAM / SAM (unchanged from v1)
| Layer | Working | Value |
|---|---|---|
| Global tea | Fortune Business Insights 2025, via truth/customers-market.md | $18.77 bn |
| TAM: bagged tea | $18.77 bn x 38% bag share (same source) | **$7.1 bn** |
| SAM: premium bagged tea, Japan + China + UK + US | $7.1 bn x 45% (ASSUMPTION: four markets) x 20% (ASSUMPTION: premium share) | **$640 m** |

How many of them (people, not dollars):
- US: "On any given day, over 159 million Americans are drinking tea" ("more than one half of the American population"), Tea Association of the USA fact sheet 2022 via US Census Bureau, January 2024. SOURCED https://www.census.gov/newsroom/stories/hot-tea-month.html
- UK: about 100 million cups a day (UKTIA, facts.md proof point); "41% [of British adults] drink tea ... at least twice a day" (YouGov, 30 June 2025) https://yougov.com/en-gb/articles/52458-is-britain-still-a-tea-drinking-nation
- Year 3 needs about 205 k buyers: 20 k Ritual subscribers + 185 k tin and gift buyers (ASSUMPTION: one tin per buyer) = 0.13% of US daily tea drinkers alone. Japan and China counts: needs data.

## 2. Price per cup: today's tea vs OSME
| Tea | Pack price | Per cup | Source |
|---|---|---|---|
| Supermarket bag, PG Tips | £6.25 / 240 bags (Morrisons) | **$0.03** | SOURCED https://www.trolley.co.uk/product/pg-tips-240-black-tea-plant-based-biodegradable-tea-bags/ZLW941 |
| Supermarket bag, Lipton | $4.99 / 100 (Target) | $0.05 (notes only) | SOURCED https://www.target.com/p/-/A-13010225 |
| Premium bag, Twinings English Breakfast | $16.99 / 100 | **$0.17** | SOURCED https://www.twiningsusa.com/products.json |
| Premium bag, Pukka | £5.00 / 20 (Tesco) | **$0.32** | SOURCED https://www.trolley.co.uk/product/pukka-peppermint-licorice-tea-bags/MFK612 |
| Capsule, Nestlé Special.T | €0.35 a pod + €129 machine (2010 launch) | **$0.38** + machine | SOURCED https://newatlas.com/nestle-specialt-tea-machine/16883/ (dated; current stand-in: Lipton Nespresso pod €3.60/10 = $0.39, https://www.maxicoffee.com/en-eu/nespresso-original-compatible-capsules-green-marrakech-mint-lipton-p-215363.html) |
| **OSME** | **$1.50 a bag, up to 3 infusions** | **$0.50** | facts.md; 3 infusions = ASSUMPTION (lab target) |
| Loose leaf, Hibiki-an Gyokuro Premium | $37 / 100 g | **$0.62** ($1.85 a 5 g serving, 3 infusions: ASSUMPTION) | SOURCED https://www.hibiki-an.com/product_info.php/products_id/28 |
| Loose leaf, Adagio English Breakfast | $12 / 2 oz (~25 cups) | $0.48 (notes only) | SOURCED https://www.adagio.com/black/english_breakfast.html |
| Subscription, Sips By | $15 a month, ~15 cups | **$1.00** | SOURCED https://reviewed.com/cooking/features/sips-by-review-a-subscription-box-for-the-tea-lover |
| Pyramid, Tea Forte | $26 / 20 infusers | **$1.30** (one cup) | SOURCED https://teaforte.com/products.json?limit=250 |
| Cafe cup, Starbucks UK English Breakfast Grande | £2.85 | **$3.62** | SOURCED https://fastfoodsmenu.com/starbucks-menu-prices-uk/ (6 Nov 2026). Pret £3.45 on Deliveroo NOT OPENED, not used. |

Per-cup basis: OSME counts 3 infusions a bag (lab target); Tea Forte, Sips By and bags count one cup each as sold. Worst case, OSME brews one cup: $1.50, shown as a dashed bar on slide 1.
Read: at $1.50 a bag, the first cup costs as much as a Tea Forte pyramid; by the third cup it is $0.50, the price of good loose leaf, with no machine, timer or thermometer.

## 3. Manufacturing cost per bag
| Line | Year 1 pilot | Year 3 scale | Label and working |
|---|---|---|---|
| Tea, 3 g single origin | $0.24 | $0.15 | ASSUMPTION: $80/kg pilot lots, $50/kg at scale. Check: a sencha wholesale listing shows ~$39/kg (Faire, NOT OPENED, 403) |
| Thermo membrane bag | $0.45 | $0.10 | Material SOURCED under 1 cent: food-grade hydroxypropyl cellulose $2.70 to $91 a kg (https://dir.tridge.com/prices/hydroxypropyl-cellulose) x 2 g/m² (ASSUMPTION) x 84 cm² bag (2 faces 6 x 7 cm, ASSUMPTION) = 0.017 g, under $0.002; filter paper 18 gsm INR 580 to 597 a kg (~$7, ASSUMPTION $1 = INR 85) = ~$0.12 a m², ~$0.001 a bag (listing, SOURCED https://m.indiamart.com/impcat/tea-bag-paper.html). Coating, curing and lost yield: ASSUMPTION ($0.45 hand-coated pilot, $0.10 at scale). Lab PNIPAM would cost ~$1+ a bag (Sigma list price, NOT OPENED), which is why the route is food-grade cellulose. |
| Tag and string | $0.03 | $0.01 | ASSUMPTION (empty bags with tag ~$0.005 on IndiaMART, NOT OPENED) |
| Packing (hand / co-pack) | $0.30 | $0.05 | ASSUMPTION; co-packers publish MOQs (3,000 to 10,000 bags a blend), not prices (https://m.indiamart.com/impcat/tea-packaging-services.html) |
| Tin or box, per bag | $0.25 | $0.11 | SOURCED tin $1.70 each under 288, $1.31 at 5,000 to 10,000 (https://www.specialtybottle.com/metal-tin-containers/tea/tsq4); $1.31 / 12 = $0.11. Year 1 adds sleeve and gift card (ASSUMPTION) |
| **Total** | **$1.27** | **$0.42** | 0.24+0.45+0.03+0.30+0.25 = 1.27; 0.15+0.10+0.01+0.05+0.11 = 0.42 |

Fulfilment per Ritual box (not in COGS, in §4): $6.50 = pick and pack ~$0.25 a pick (ShipBob, https://revenuegeeks.com/shipbob-pricing/) + mailer + postage (ASSUMPTION ~$6). Card fee 2.9% + $0.30 (Stripe US, via https://www.merchantmaverick.com/reviews/stripe-review/ and https://checkoutpage.com/blog/stripe-processing-fees; stripe.com served Thai prices).

One-off costs (inside the $2.5 m ask):
| Item | USD | Label |
|---|---|---|
| Membrane R&D and IP, 18 months | $875 k | ASSUMPTION (35% of the ask, v1 use of funds) |
| Food-contact certification EU, US, Japan | $375 k | ASSUMPTION (15% of the ask). Lab tests are cheap: EU overall migration test €165 to €430 a sample + €97 an order (https://measurlabs.com/products/overall-migration-simulant-c); the budget is for toxicology, dossiers and repeat cycles |
| Pilot coating line and tooling | $200 k | ASSUMPTION (inside "first inventory", v1 use of funds) |

## 4. Margin per bag and the Ritual subscriber (at $1.50)
| | Working | Result |
|---|---|---|
| Gross margin a bag, direct, year 3 | $1.50 − $0.42 | **$1.08 (72%)** |
| Gross margin a bag, retail, year 3 | retailer pays 50% of shelf (ASSUMPTION; keystone pricing, Faire snippet NOT OPENED): $0.75 − $0.42 | **$0.33 (44%)** |
| Gross margin a bag, year 1 pilot | $1.50 − $1.27 | $0.23 (15%) |
| Ritual box a month | 16 bags x $1.50 | $24.00 |
| − bags | 16 x $0.42 | − $6.72 |
| − fulfilment | ASSUMPTION | − $6.50 |
| − card fee | 2.9% x $24 + $0.30 | − $1.00 |
| **Contribution a subscriber a month** | | **$9.78 (41%)** |
| CAC | Eightx food and beverage DTC $53 to $100, headline $75 (https://eightx.co/blog/average-cac-ecommerce-vertical) | $75 |
| CAC payback | $75 / $9.78 | **7.7 months** |
| Lifetime contribution | $9.78 / 7% monthly churn (Eightx: healthy 4 to 7%, https://eightx.co/blog/coffee-subscription-churn-rate-benchmark) | $140 |
| LTV : CAC | $140 / $75 | **1.9x** (Eightx CAC page: "the ideal LTV to CAC ratio is 3 to 1", "most scaling brands sit at 1.5 to 2.5x", https://eightx.co/blog/average-cac-ecommerce-vertical) |

## 5. From $640 m to year 3 (at $1.50)
Bottom-up (all volumes ASSUMPTION):
| Stream | Working | Revenue |
|---|---|---|
| Ritual subscription | 12,000 average subscribers (4 k end of year 2, 20 k end of year 3, linear) x $24 x 12 | $3.46 m |
| Tins and gifts, D2C | 185,000 tins x $18 (12 bags) | $3.33 m |
| Premium retail | 2,000,000 bags x $0.75 (50% of $1.50 shelf) | $1.50 m |
| **Year 3** | 6.52 m bags | **$8.29 m ≈ $8.3 m** |
Top-down check: $8.29 m / $640 m SAM = **1.3%** (v1: 1.4%).
Funding check (ASSUMPTION): Ritual grows from 4 k subscribers (end of year 2) to 20 k (end of year 3). Gross adds in year 3 = 16 k net + churn 7% x 12 k average x 12 = ~10.1 k, so ~26.1 k adds x $75 = **~$2.0 m CAC in year 3**. Year-3 contribution before marketing covers it: Ritual 12 k x 12 x $9.78 = $1.41 m + tins 185 k x ($18 − 12 x $0.42) = $2.40 m (before post) + retail 2 m x $0.33 = $0.66 m = ~$4.5 m. The $2.5 m ask funds R&D, certification, pilot line and launch, not year-3 acquisition; the Series A trigger (20 k subscribers) covers the rest.

Plausibility, public subscription counts:
| Company | Count | Source |
|---|---|---|
| Sips By (tea) | 350,000 "members", 2020 (not stated as paying) | SOURCED https://www.worldteanews.com/Insights/tea-subscription-service-boosts-specialty-tea-growth |
| Trade Coffee (US) | ~75,000 subscribers, 2020 | SOURCED https://www.geekwire.com/2020/madrona-leads-9m-investment-coffee-startup-trade-connects-home-brewers-roasters/ |
| Pact Coffee (UK) | ~60,000, 2021 | SOURCED https://techround.co.uk/startups/pact-coffee-changing-morning-fix/ |
| **OSME, end of year 3** | **20,000** | ASSUMPTION: a third of Trade or Pact after 4-5 years |
Churn reality check: tea subscriptions range from 5-month lives (Simple Loose Leaf) to 30 months (Plum Deluxe) (https://freshcup.com/coffee-subscriptions/); our 7% a month = ~14 months.

## 6. Price sensitivity: $1.50 vs $2.00 vs $2.50 a bag (year-3 cost $0.42)
| | $1.50 (today) | **$2.00 (recommended)** | $2.50 |
|---|---|---|---|
| Per cup (3 infusions) | $0.50 | **$0.67** | $0.83 |
| Gross margin a bag, direct | $1.08 · 72% | **$1.58 · 79%** | $2.08 · 83% |
| Gross margin a bag, retail | $0.33 · 44% | **$0.58 · 58%** | $0.83 · 66% |
| Ritual box (16 bags) | $24 | **$32** | $40 |
| Contribution a month | $9.78 | **$17.55** | $25.32 |
| CAC payback | 7.7 months | **4.3 months** | 3.0 months |
| LTV : CAC | 1.9x | **3.3x** | 4.8x |
| Year 3 at the same volumes (ASSUMPTION) | $8.3 m | $11.0 m | $13.8 m |
Ladder check: $0.67 a cup is still below Sips By ($1.00) and half of Tea Forte ($1.30); $0.83 a cup nears Sips By and the Ritual box hits $40 a month, above Sips By's $15.
**Recommendation: $2.00 a bag** (tin $24, Ritual $32 a month). It clears the 3x LTV:CAC investors expect, halves payback, and keeps the cup under every premium rival on the ladder. At $2.00 the same $8.3 m year 3 needs 25% fewer bags. At $1.50, 3x LTV:CAC needs CAC near $47 ($140 / 3): gifting and the waitlist must do the work. The team decides; until then every slide says $1.50.

## 7. The raise
$2.5 m on a SAFE at a $10 m pre-money valuation ($12.5 m post-money cap, 20% dilution, 24 months runway). Use of funds: membrane R&D and IP 35%, certification 15%, brand and launch 30%, origin partnerships and first inventory 15%, ops 5%. Series A trigger: 20 k subscribers or $5 m revenue run-rate.
Valuation check: "The median pre-money valuation on new primary seed rounds on Carta rose to a new high of $16 million in Q3, an increase of 14% from the same period last year." (Crowdfund Insider on Carta's Q3 2025 report, 2 Dec 2025, opened 27 Nov 2026) https://www.crowdfundinsider.com/2025/12/256059-early-stage-valuations-keep-rising-down-rounds-growing-less-frequent-carta-private-markets-insights/ . The carta.com report URL returns 403 to our fetcher, so it is replaced by this one. A pre-revenue consumer brand with material R&D risk prices below that median: $10 m pre (ASSUMPTION).

## How v2 settles the v1 validation FAILs (judge/business-validation.md v1, 10:24)
| v1 FAIL | v1 fix | v2 answer |
|---|---|---|
| Single bag $1.50 vs $2.00 | lock one | $1.50 everywhere (facts.md); $2.00 kept only as a recommendation in §6 |
| Year-3 average price $1.38, SOM $9 m | $1.275, $8.3 m | v2 bottom-up by stream: **$8.3 m** (§5) |
| Gross margin 62% (COGS midpoint $0.57 vs $0.605) | about 60% | v2 replaces the v1 range with a line-by-line stack: year-3 COGS **$0.42**, gross margin **$1.08 a bag, 72%** direct (§3, §4). "About 60%" was the v1 range midpoint and is retired |
| LTV $213 | $205 | v2 counts post and card fees: contribution $9.78 a month / 7% = **$140** (on v1's gross-margin basis it would be $24 / 7% x 72% = $247) |
| LTV:CAC 2.8x | 2.7x | **1.9x** on contribution at $1.50 (3.3x at $2.00, §6) |
| Carta citation 403 | other source | Crowdfund Insider, same figure (above) |

## Questions for the team (also in ops/questions.md)
1. Price: stay at $1.50 or move to $2.00 a bag (§6)? Everything shows $1.50 until the team decides.
2. facts.md Market: year-3 SOM $9 m (gate1.html shows $8.3 m, validator v1 mix) → **$8.3 m** at $1.50 (locked by the lead, 10:49; v2 bottom-up gives $8.29 m).
3. Is 3 infusions a bag the locked claim? The per-cup ladder depends on it.
