# Common rules for every agent (read first)

Repo root: /Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
Exercise: presales training "Sell the unsellable", Table 5. Hand-ins by 13:30: brand, customer, product, site, pitch (3 min, 8 slides: company, problem, solution, customer evidence, market, business, competition, the ask). Jury: presales and sales professionals. Branding and storytelling are the top goal.

## Locked (facts.md is the source of truth; read it)
- Name OSME (Greek osmē, "scent"). A global B2C tea brand and tea-tech disruptor: a MOVEMENT, not an app or a tea lounge.
- Belief: in a world of AI and craziness, we go back to what life is about: art, love, scent.
- Product: a waterproof tea bag that stays sealed until the water reaches its tea's ideal temperature, opens to brew, and closes as the water cools. Self-stopping steep, reusable for several infusions, scent sealed in between cups.
- Story: tea across cultures (Japan, China, Britain first). Lu Yu's 8th-century Classic of Tea read water by its bubbles. The tea bag (~1908) traded the art for convenience. Technology brings the art back. Values: patience, ritual, harmony.
- B2C only: D2C web shop, "Ritual" subscription, premium retail. No hotels, offices or B2B.
- Look "Midnight Brew": dark matte black, a glowing temperature arc from amber (hot) to jade (cool), Lu Yu's three bubble stages as a 3-dot motif, geometric sans display, calm, premium. Never a default app or SaaS look.

## Tone decisions (09:58)
- Positive story: life, art, scent, love. Do NOT frame Osme as anti-screen, anti-phone or anti-AI; no "screen-free" or "phone-down" rituals.
- Everyone can be a tea person: inclusive, welcoming, never snobbish.
- "Tea-tech disruptor" appears only on jury slides (market, business, the ask), never in consumer copy.
- Name written OSME; said "oz-MAY".

## Never lose work
1. Before starting, check whether your output file already exists. If it does, RESUME from it; don't start over.
2. Save to your output file early (a skeleton within 3 minutes) and after every meaningful step.
3. Append one line to ops/log.md at start, at each milestone and at the end:
   `HH:MM | <agent> | <status: START/PROGRESS/DONE/BLOCKED> | <one line>`
   (use `date +%H:%M`; append with `>>`, never rewrite the file).
4. Do not git commit; the lead commits.

## Validate before reporting
- Sources: only cite URLs you opened, and re-check that they say what you claim.
- Visuals: render with headless Chrome. Every Chrome launch MUST include `--use-mock-keychain --password-store=basic` and its own `--user-data-dir`. Look at the screenshots critically and iterate at least once.
- HTML: run `~/Library/CloudStorage/OneDrive-SiemensAG/AI-Presales-Workspace/personal-library/bin/embed-html <file>` then `embed-html --check <file>` until it passes.
- Ambiguities that change the outcome go under "Questions for the team" in your output and report; don't guess silently.
