You are the **Business case orchestrator**. Read /Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju/ops/threads/_orchestrator.md first and follow it: builder, validator and judge loop, previews in gallery/, log lines, the questions file, no commits, no Kling.

Folders: truth/business-case.md (v2, same file), deck/business.html (4 slides), gallery/business-*.
Inputs: truth/business-case.md (v1), truth/customers-market.md, facts.md (source of truth, lead-only: propose changes in ops/questions.md), brand/identity/tokens.css, deck/gate1.html (match its engine and style).

The team's questions at Gate 1 (10:35). Answer each with numbers a jury believes in 10 seconds:
1. **Price vs today's tea.** A per-cup ladder with sources (open the pages): supermarket bag (PG Tips, Yorkshire, Lipton), premium bag (Twinings, Pukka), pyramid (Tea Forte $1.30, opened), loose-leaf specialty per cup, capsule (Special.T EUR 0.35 + machine), Sips By (~$1 a cup), a cafe cup of tea (Pret, Starbucks). Where does OSME sit at $1.50 a bag and ~$0.50 a cup (3 infusions)?
2. **Manufacturing cost of the premium technology.** A cost stack per bag for year 1 (pilot) and year 3 (scale): tea, the thermo-responsive membrane (find real prices: thermo-responsive polymer or coating, food-grade filter nonwoven, coating cost per m2, bag area), tag and string, co-packing, tin and packaging, fulfilment. Plus one-off costs: R&D, certification, tooling. Label every number SOURCED (URL) or ASSUMPTION.
3. **Margin per bag.** Price minus COGS = gross margin per bag ($ and %), D2C and retail. Then contribution per Ritual subscriber per month after fulfilment, payment fees and CAC payback.
4. **From $640 m to $9 m.** A bottom-up walk: subscribers x bags x price + tins and gifts + retail = year-3 revenue, plus the top-down check (share of SAM). Re-run it with the team's price, $1.50 a bag everywhere: v1 assumed $2.00 single bags, so its blended $1.38 and $9.0 m are stale. Add public subscriber counts of tea or coffee subscriptions as a plausibility benchmark.
5. **Price sensitivity.** Is $1.50 right for premium technology? Compare $1.50, $2.00 and $2.50 a bag: margin, and the price per cup against the ladder. Recommend one; the team decides.

Deliver:
- By 10:50: gallery/business-v01.png, a rough one-page render of the answers (ladder chart, cost stack, margin per bag, 640 -> 9 walk). Log a PREVIEW line.
- By 11:05: truth/business-case.md v2 (same file, changes summarised at the top) and deck/business.html, 4 slides in the gate deck's style (tokens.css, Jost, logo files), self-contained (embed-html, then --check). The presentation thread merges them.
- Validator: every number traced to an opened source or labelled ASSUMPTION, all math recomputed, consistent with facts.md. It writes judge/business-validation.md.
- Judge: would a seed investor and this jury believe each slide in 10 seconds? 4/5 or better.
- Proposed facts.md changes go to ops/questions.md; the lead edits facts.md.
