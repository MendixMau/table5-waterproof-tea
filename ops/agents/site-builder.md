# Site builder brief (site orchestrator builds this itself)
Output: docs/index.html (one self-contained page; embed-html then --check). Resume from the file if it exists.
Sections: nav · hero (logo, "Every tea has its temperature.", one-liner, who, price chip, animated cup loop) · how it works (3 states, Sencha 80/70 °C, slider, link to docs/demo.html = copy of product/index.html) · story timeline (760 Lu Yu, 1908 bag, now) · teas by culture (temps from product/index.html) · who it's for (segments, 3 quotes) · price (facts.md) · movement (manifesto, Keepers, #ThreeBubbles, waitlist form, no backend) · footer sources.
Copy rules: brand/strategy.md §5 (no app, smart, disrupt, users, emoji, exclamation marks). Numbers from facts.md; others from truth/*.md with source.
Previews: gallery/site-vNN.png (desktop 1440 + phone 390 side by side).

## State at HOLD (10:20)
docs/index.html = v02 (logo v4, embedded, --check passes, 390/1440 no overflow, no console errors). docs/demo.html = copy of product/index.html.
Judge v02 (ops/site-judge-1017.md): 25/30, nothing below 4. Validator (ops/site-validation-1018.md): 12 PASS, 5 FIX (publish, 3 facts.md fills, footer "760s CE").
Tools: /tmp/site-shots/snap.js (playwright shots + console errors), /tmp/site-shots/sheet.js (gallery contact sheet).

## Next 3 steps (after resume)
1. Hero "who": chip -> "For curious tea drinkers who pay for good leaf and hate a bitter cup. And anyone who would love to be one." Phone (<600px): display:contents reorder so the bag dial sits right under the one-liner, hide the 4-line paragraph, buttons side by side.
2. Break the card rhythm: full-width band between hero and How with video/renders/osme-loop_v01.mp4 (muted, autoplay, loop, playsinline, poster; embedded by embed-html), text "Lu Yu read water by its bubbles. OSME reads it for you." Price block -> one wide Ritual card ($24/month) + single bag and tin as two small cards beside it.
3. Small fixes: footer "760s CE", font stacks in tokens.css order (Jost first), who-card stats pinned to the bottom, small grey text >= 14px; then refresh demo.html copy, embed + check, gallery/site-v03.png, fresh validator + judge.
