# Site judge brief v2 (multi-page shop; fresh agent)
Repo R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
Target: OSME's multi-page shop in $R/docs/ (index, shop, tea-<id> x6, ritual, story, keepers; demo.html is the product team's live demo). Hand-in line: "A real multi-page shop on GitHub Pages with a working waitlist." Read $R/judge/rubric.md, $R/brand/strategy.md, $R/facts.md.
Render: `cd /tmp/site-shots && node multi.js $R/docs /tmp/site-judge2 index.html shop.html tea-sencha.html ritual.html story.html keepers.html` (1440 + 390, first screen + full page per page) and `node cart.js $R/docs /tmp/site-judge2` (cart drawer + pre-order + phone menu). Look at the PNGs; for tall full-page shots, crop slices yourself with Playwright clip or sips if needed.
Be a hard jury of presales and sales professionals and a senior brand/web/e-commerce designer.
1. 10-second test on the Home first screen (desktop and phone): what it is, who it's for, the price. Yes/no each, with what a stranger would say.
2. Score 1-5: Clarity, Customer evidence, Credibility of the product, Story, Visual design (premium "Midnight Brew", never a default SaaS or template look), Phone experience, and Shop credibility (does it feel like a real shop someone would pre-order from: product pages, cart, Ritual). One line of reasoning each.
3. Senior designer critique across pages: hierarchy, rhythm, typography, imagery, what feels generic, empty or repetitive.
4. The 3 changes that would raise the scores most, concrete enough to implement (page, what, how).
Write it to $R/ops/site-judge-<HHMM>.md and return a summary under 250 words. Edit nothing else.
