# Business v2 validator (fresh agent, never the builder)
Read ops/agents/_common.md, facts.md, judge/checklists.md (business + D5/X2/X4 rows), ops/threads/business.md.
Inputs: truth/business-case.md (v2), deck/model_business.py (all numbers; run it), deck/business.html (render: deck/render_business.sh /tmp/osme-biz-val; read the PNGs), /tmp/t5-business/*.md (research notes with URLs).
Checks, verdict per row PASS / FIX (exact fix) / ASK:
1. Every number on the 4 slides and in business-case.md v2 is either SOURCED (open the URL now; quote the line) or labelled ASSUMPTION. Re-open at least the 8 ladder sources and the 6 most important cost sources.
2. Recompute all math: per-cup ladder, COGS sums Y1/Y3, gross margin $ and % D2C and retail, Ritual contribution, CAC payback, LTV, year-3 walk, share of SAM, the $1.50/$2.00/$2.50 table. >1% off = FIX.
3. Consistency with facts.md (price $1.50, tin $18, Ritual $24/16 bags, TAM $7.1 bn, SAM $640 m, competitors' prices, the ask $2.5 m). Any number that changes a facts.md value must be listed as a proposed facts.md change (ops/questions.md), not silently used.
4. Slides: no em or en dashes (grep), embed-html --check passes, no clipped or overflowing text in the PNGs.
Write judge/business-validation.md (overwrite: v2 header with time; keep it a table). Final reply: tally + the FIX list, under 200 words.
