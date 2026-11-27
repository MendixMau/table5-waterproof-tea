#!/usr/bin/env python3
"""OSME business model v2: one place for every number on deck/business.html and truth/business-case.md.

Each input carries a label: S = SOURCED (URL opened, see truth/business-case.md), A = ASSUMPTION.
Run: python3 deck/model_business.py   (prints the working the validator recomputes)
"""

# ---------- 1. price ladder: USD per cup (one serving) ----------
# (name, per cup, note, label)
LADDER = [
    ("Supermarket bag · PG Tips", 0.03, "240 bags £6.25", "S"),
    ("Premium bag · Twinings", 0.17, "100 bags $16.99", "S"),
    ("Premium bag · Pukka", 0.32, "20 bags £5.00", "S"),
    ("Capsule · Special.T", 0.38, "+ €129 machine", "S"),
    ("OSME · 3 cups a bag", 0.50, "$1.50 a bag", "A"),
    ("Loose leaf · Hibiki-an gyokuro", 0.62, "100 g $37, 3 infusions", "S"),
    ("Subscription · Sips By", 1.00, "$15 a month, ~15 cups", "S"),
    ("Pyramid · Tea Forte", 1.30, "20 infusers $26, one cup", "S"),
    ("Cafe cup · Starbucks UK", 3.62, "Grande £2.85", "S"),
]

INFUSIONS = 3            # A: up to 3 infusions a bag (facts.md, provisional)
PRICE = 1.50             # facts.md: $1.50 a bag everywhere
TIN_BAGS, TIN_PRICE = 12, 18.0
RITUAL_BAGS, RITUAL_PRICE = 16, 24.0
WHOLESALE = 0.50         # A: retailer pays 50% of shelf price

# ---------- 2. cost stack per bag (USD) ----------
# component: (year 1 pilot, year 3 scale, label)
COST = {
    "Tea, 3 g single origin": (0.24, 0.15, "A"),
    "Thermo membrane bag":    (0.45, 0.10, "A"),
    "Tag and string":         (0.03, 0.01, "A"),
    "Packing (hand / co-pack)": (0.30, 0.05, "A"),
    "Tin or box, per bag":    (0.25, 0.10, "A"),
}
ONE_OFF = {  # USD, inside the $2.5 m ask
    "Membrane R&D and IP (18 months)": 875_000,
    "Food-contact certification EU, US, Japan": 375_000,
    "Pilot coating line and tooling": 200_000,
}

# ---------- 3. Ritual subscriber per month ----------
FULFIL = 6.50            # A: pick, pack and post one box a month (3PL), free shipping
PAY_PCT, PAY_FIX = 0.029, 0.30   # card fee per charge
CAC = 75.0               # S: Eightx food & beverage DTC CAC
CHURN = 0.07             # S range 4-7% healthy (Eightx); plan 7%

# ---------- 4. year-3 walk ----------
SAM = 640e6
RITUAL_AVG = 13_000      # A: average Ritual subscribers in year 3 (6 k start, 20 k end)
TINS = 180_000           # A: 12-bag tins and gift tins sold D2C in year 3
RETAIL_BAGS = 2_000_000  # A: bags sold through premium retail


def cogs(year):
    return sum(v[0 if year == 1 else 1] for v in COST.values())


def econ(price):
    c3 = cogs(3)
    ritual = price * RITUAL_BAGS
    box_cogs = RITUAL_BAGS * c3
    fee = ritual * PAY_PCT + PAY_FIX
    contrib = ritual - box_cogs - FULFIL - fee
    return dict(
        price=price, cup=price / INFUSIONS,
        gm_d2c=price - c3, gm_d2c_pct=(price - c3) / price,
        gm_ret=price * WHOLESALE - c3, gm_ret_pct=(price * WHOLESALE - c3) / (price * WHOLESALE),
        ritual=ritual, box_cogs=box_cogs, fee=fee, contrib=contrib,
        payback=CAC / contrib, ltv=contrib / CHURN, ltv_cac=contrib / CHURN / CAC,
        rev_ritual=RITUAL_AVG * ritual * 12, rev_tins=TINS * TIN_BAGS * price,
        rev_retail=RETAIL_BAGS * price * WHOLESALE,
    )


def walk(price):
    e = econ(price)
    total = e["rev_ritual"] + e["rev_tins"] + e["rev_retail"]
    bags = RITUAL_AVG * RITUAL_BAGS * 12 + TINS * TIN_BAGS + RETAIL_BAGS
    return dict(total=total, bags=bags, share=total / SAM, **e)


if __name__ == "__main__":
    print(f"COGS y1 {cogs(1):.2f}  y3 {cogs(3):.2f}")
    for p in (1.50, 2.00, 2.50):
        w = walk(p)
        print(f"\n${p:.2f}/bag  cup {w['cup']:.3f}")
        print(f"  GM D2C {w['gm_d2c']:.2f} ({w['gm_d2c_pct']:.1%})  retail {w['gm_ret']:.2f} ({w['gm_ret_pct']:.1%})")
        print(f"  Ritual {w['ritual']:.2f} - cogs {w['box_cogs']:.2f} - fulfil {FULFIL:.2f} - fee {w['fee']:.2f} = {w['contrib']:.2f}/month"
              f"  payback {w['payback']:.1f} mo  LTV {w['ltv']:.0f}  LTV:CAC {w['ltv_cac']:.2f}")
        print(f"  Y3 ritual {w['rev_ritual']/1e6:.2f}m + tins {w['rev_tins']/1e6:.2f}m + retail {w['rev_retail']/1e6:.2f}m"
              f" = {w['total']/1e6:.2f}m  bags {w['bags']/1e6:.2f}m  share of SAM {w['share']:.2%}")
    print(f"\nY1 pilot GM at $1.50: {(1.5-cogs(1)):.2f} ({(1.5-cogs(1))/1.5:.1%})")
