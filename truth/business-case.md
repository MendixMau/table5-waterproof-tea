# OSME business case (business agent)
Status: DONE (draft for business-validator). USD throughout. Every number is SOURCED (URL opened) or labelled ASSUMPTION.
Market inputs reused from truth/customers-market.md (truth-customers).

## 1. Market: TAM / SAM / SOM
| Layer | Working | Value |
|---|---|---|
| Global tea | Fortune Business Insights, 2025 (via customers-market.md) | $18.77 bn |
| TAM: bagged tea worldwide | $18.77 bn x 38% bag share of packaging (same source) | **$7.1 bn** |
| SAM: premium and specialty bagged tea, Japan + China + UK + US | $7.1 bn x 45% (ASSUMPTION: four first markets' share of bagged-tea value) x 20% (ASSUMPTION: premium/specialty share) | **$640 m** |
| SOM: year-3 share | $640 m x 1.4% (ASSUMPTION, realistic for a year-3 D2C brand) | **$9 m** = year-3 revenue below |

Context lines for the jury (sourced via customers-market.md): UK drinks ~100 m cups a day, 97.5% from a bag (UKTIA); tea market grows 6.1% a year to $32 bn by 2034.
Caveat: APAC is 45% of global tea revenue (Fortune), but that is region, not our four countries. The 45% is an ASSUMPTION, not that figure.

## 2. B2C price
| Offer | Price | Per bag | Per cup (3 infusions, ASSUMPTION) |
|---|---|---|---|
| Single bag (gift, tasting) | $2.00 | $2.00 | $0.67 |
| 12-bag tin (one tea, one origin) | $18 | $1.50 | **$0.50** |
| "Ritual" subscription: 16 bags/month, 3-4 origins, free shipping, skip or pause any month | $24/month | $1.50 | $0.50 |

Anchors (all from customers-market.md, URLs opened there):
- Sips By tea subscription: $13.75-16/month, about $1 per cup.
- Nestle Special.T capsules: EUR 0.35 per pod plus a EUR 129 machine.
- Search-reported, page NOT opened (403): Harney & Sons tin of 20 sachets $14 (=$0.70/cup, one cup each); Tea Forte pyramid infusers about $1.75-2.10 each. Validator: confirm or drop.

Why premium holds: one OSME bag gives about three cups (ASSUMPTION, to be proven in the lab), so $1.50 a bag is $0.50 a cup. That is below a Sips By cup and in the range of premium sachets, while the shelf price signals craft. No machine to buy (unlike Special.T). The tin is the art object; the cup price is the rational close.

## 3. Production and unit economics
### The membrane (be honest: this is the R&D)
- Science that exists: thermo-responsive polymers change state reversibly at a set temperature. PNIPAM switches from hydrated (swollen) to dehydrated (collapsed) at about 32 C, and the switch point shifts 5-10 C or more with molar mass, concentration and end groups (Wikipedia, Poly(N-isopropylacrylamide), opened): https://en.wikipedia.org/wiki/Poly(N-isopropylacrylamide)
- Grafted onto a porous film, collapsed chains open the pores above the switch temperature and swollen chains close them below it ("thermo-gated membranes"; search-reported in several papers, PMC/RSC pages blocked our fetch, validator to confirm).
- What is R&D, not fact: (1) moving the switch to 70-90 C per tea, (2) a food-contact-approved polymer (PNIPAM is not a food material; route = food-grade cellulose or wax based alternatives), (3) many open/close cycles without leaching. Budget: 12-18 months lab work, ASSUMPTION.
- Certification: food-contact approval in the EU, US and Japan before launch (ASSUMPTION: 6-9 months, $150-300k).

### COGS per bag (ASSUMPTION ranges, year-3 scale)
| Item | Low | High |
|---|---|---|
| Tea, 3 g premium single origin | $0.06 | $0.15 |
| Thermo-membrane bag | $0.15 | $0.40 |
| Co-packing (contract packer) | $0.05 | $0.10 |
| Tin and packaging, per bag | $0.10 | $0.20 |
| **Total** | **$0.36** | **$0.85** |
Midpoint $0.57 vs $1.50 price = **62% gross margin** D2C. Retail at 50% of shelf ($0.75/bag) = 24%, so retail is for reach, D2C for margin. Year 1 hand-made pilot bags: ASSUMPTION $1.20 COGS.

### D2C metrics (benchmarks opened)
- CAC: food and beverage DTC $53-100, headline $75 (Eightx, 2026) https://eightx.co/blog/average-cac-ecommerce-vertical . Plan: $75.
- Retention: coffee subscriptions lose 5-10% a month, healthy 4-7%; pause/skip lifts retention ~22% (Eightx, 2026) https://eightx.co/blog/coffee-subscription-churn-rate-benchmark . Plan: 7%/month.
- AOV: food and beverage one-time $60-100, subscription $70-120 (Eightx, 2026) https://eightx.co/blog/average-ecommerce-aov-subscription-vs-onetime-2026 . Plan: one-time AOV $40 (two tins plus a single), ASSUMPTION, below benchmark because we are one product.
- LTV (Eightx formula ARPU / churn): $24 / 7% = $343 revenue, x 62% = **$213 gross-margin LTV**. LTV:CAC = 2.8x (Eightx: 3x ideal, scaling brands 1.5-2.5x).

## 4. 3-year plan (year 1 = 2027)
| | Year 1: lab | Year 2: launch | Year 3: grow |
|---|---|---|---|
| Bags sold | 60 k (pilot, pre-orders) | 1.2 m | 6.5 m |
| Avg net price / bag | $1.60 | $1.42 | $1.38 (30% retail) |
| Revenue | $0.1 m | $1.7 m | **$9.0 m** |
| Gross margin | 20% | 50% | 62% D2C, ~51% blended (0.7x62% + 0.3x24%) |
| Ritual subscribers (end) | 1 k waitlist | 4 k | 20 k |
Milestones: Q2 Y1 lab prototype opens/closes at 80 C; Q4 Y1 first tea-origin partnerships (Uji sencha Japan, Fujian China, Assam/Darjeeling for the British blend); Q2 Y2 food-contact certification; Q3 Y2 D2C launch UK + US (pre-order list from the film and #ThreeBubbles community); Q1 Y3 Japan via partner, China via cross-border e-commerce, first premium retail shelf. Check: 6.5 m x $1.38 = $9.0 m; 1.2 m x $1.42 = $1.7 m.

## 5. The raise (YC style)
- One-liner: OSME is the tea bag that knows its tea's temperature: it opens to brew, closes as the water cools, and brews again.
- Problem: the tea bag (~1908) traded the art for convenience: over-steeped, bitter, one cup, and the scent is gone (complaints in customers-market.md).
- Why now: thermo-responsive materials are lab-proven; premium D2C subscriptions are a known playbook; tea grows 6% a year.
- Insight: the art of tea is temperature and time. Put both in the bag and everyone can be a tea person.
- Traction plan: waitlist + pre-orders in Y1, 4 k subscribers by end Y2, 20 k by end Y3.
- **The ask: $2.5 m seed on a post-money SAFE at a $12.5 m post-money cap ($10 m pre-money), 20% dilution, 24 months runway.**
- Use of funds: membrane R&D and IP 35%; food-safety certification 15%; brand, film and launch 30%; origin partnerships and first inventory 15%; ops 5%.
- Valuation reasoning: Carta median seed pre-money was $16 m in Q3 2025 (opened) https://carta.com/data/state-of-private-markets-q3-2025-full-report , skewed to software and AI. A pre-revenue consumer brand with material R&D risk prices below the median: $10 m pre. YC's standard deal values the first $125k at 7% (=$1.79 m post-money) plus $375k on an uncapped MFN SAFE (opened) https://www.ycombinator.com/deal ; we would sit between that entry point and the Carta median.
- Series A trigger: 20 k subscribers or $5 m revenue run-rate.

## 6. The 4 numbers the pitch says out loud
1. **$7 billion**: what the world spends on tea bags every year.
2. **3 cups, 1 bag**: one OSME bag brews about three times.
3. **50 cents a cup**: premium tea at half the price of a subscription cup (Sips By ~$1); 62% D2C gross margin.
4. **$2.5 million** at a $10 million pre-money valuation, to take the bag from lab to launch.

## Questions for the team
1. Is "about 3 infusions per bag" the locked product claim? Price per cup and margin depend on it (product agent).
2. Keep the $10 m pre-money, or show the jury the cleaner "YC entry + $2.5 m" framing only?
3. Do we name retail (30% of Y3) on the business slide, or keep the slide pure D2C + Ritual?
4. Price comparables Harney and Tea Forte could not be opened (403); use only Sips By and Special.T on the slide unless validator confirms.
5. Is the SAM split (45% four markets, 20% premium) acceptable as stated assumptions, or does truth-customers have a specialty-tea figure to replace it?
