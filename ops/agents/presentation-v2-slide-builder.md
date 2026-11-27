# Pitch v2 slide builder brief (presentation topic)

Repo R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju

## Why this rebuild
The team and Maurits said the deck is "way too bland, only using basics". The bar now is a premium brand launch, like a product keynote, not a consulting deck. Maurits in his own words: animations matter for telling the story, and the story of the art of tea and scent (China, Japan, Britain, then the 1908 bag, then OSME) must recur across the deck in animation quality, not as "three bullet points from 760 to today".
**The bland test:** every slide has at least one brand visual AND one motion moment. No slide may be only text, cards and tables. Projector first: body text at least 28 px at 1920 wide, numbers huge, at most 2 data elements per slide, no tables on stage (detail goes in the notes).

## The engine (do NOT edit it; ask in your report if you need a feature)
deck/build_pitch_v2.py stitches deck/v2/s1.html ... s8.html into deck/pitch.html. Read its docstring and CSS/JS first: it defines the fragment contract and the motion language you must use.
- `.draw` on SVG paths with `pathLength="1"`: the path draws itself on slide entry (`--d` duration, `--dl` delay). The amber-to-jade ARC sweep is the signature: use it on your slides.
- Scent rise: the logo's S string drawn upward with `.draw` (see brand/identity/logo-symbol.svg for the path).
- `.steep` container: its children reveal blur to sharp with a warm bleed and a 130 ms stagger.
- `data-count="8.3" data-dec="1" data-prefix="$" data-suffix=" m"`: count-up on entry (or when its `.rv` build step shows).
- `.rv data-s="k"` + `data-steps="k"` on the slide: click builds. Use only where the speaker needs them.
- Hooks for richer motion: `window.ENTER[n]=el=>{...}` runs on every entry (restart your JS/SVG animation there), `LEAVE[n]`, `STEP[n]=(el,step)=>{...}`. Use `if(document.documentElement.classList.contains('still'))` to jump to the end state for screenshots.
- Global ambient steam and bubble texture already sit behind every slide; slides are transparent.
- Assets: `__ASSET:brand/assets/hero.png__` (path from the repo root) becomes a data URI. Numbers: `__NUM:y3__` etc. (see the docstring) and `__LADDER_JSON__`. Never type a business number by hand; use the tokens.
- Tokens: Midnight Brew (bg #0B0B0D, amber #F2A33A hot/opens, mid #D9C46B, jade #3DBA9B cool/seals, text #F3EEE6, muted #8E8A83), Jost. Use `logo-symbol-small.svg` for marks under 40 px.
- Scope all your CSS with `#sN`. Put your own `@keyframes` names with an `sN-` prefix.

## Assets to reuse (look at them first)
brand/assets/: hero.png/svg (glass cup, OSME bag, arc), hero-titled, culture-motif.svg/png (Britain, China, Japan), pattern-bubbles*, pack-tin, pack-single-bag, social-threebubbles-1080, icon-self-stopping / icon-three-infusions / icon-scent-sealed (.svg). brand/identity/logo-*.svg (final route 1). product/index.html: its inline SVG cup, liquid and bag animation (copy the SVG parts you need into your fragment; do not iframe it). docs/_src/: the site generator, with per-tea tinted tins (build.py, hero-cup.svg). video/: osme-film.mp4, osme-loop.mp4 (+ osme-loop-poster.jpg). gallery/*.png shows what the other threads built.

## Facts
Only from facts.md, truth/ (history-cultures.md, customers-market.md, business-case.md v2) and deck/model_business.py. Year 3 is $8.3 m (never $9 m). Price $1.50 a bag (token). Margin $1.08 a bag, 72%, always labelled "at year-3 scale". English only, no em or en dashes anywhere. Tone positive (art, scent, ritual, love), not anti-screen or anti-AI. Each fragment ends with an `<aside class="notes">` listing the source of every number on it.

## Your loop
1. Build: `cd $R/deck && python3 build_pitch_v2.py --out /tmp/osme-v2-<you>.html`
2. Render: `$R/deck/render_v2.sh /tmp/osme-v2-<you>.html /tmp/osme-v2-<you> "<your slide numbers>"` gives sN.png (end state), sN_m0/m1/m2.png (0, 0.5, 1.5 s) and sN_strip.png. Open them. Check: no clipping at 1920x1080, text at least 28 px, the motion actually shows in the strip, the bland test passes.
3. Iterate. First complete version by 11:18, polished by 11:32. Write only your own fragment files in deck/v2/ (and helper files deck/v2/sN-*.{svg,js} if needed). Do not edit any other file. Every Chrome launch needs --use-mock-keychain --password-store=basic and its own --user-data-dir (the render script does this).
4. Report under 150 words: what each slide shows, the motion moments, which assets, anything you could not do.
