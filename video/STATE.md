# Video build state

- Source: `video/src/film.html` (v03; v01/v02 kept as `film_v01.html`, `film_v02.html`), `video/src/loop.html` (SVG timelines driven by `window.setT(t)`), `video/src/render.mjs` (headless Chrome → ffmpeg, injects the current brand/identity logos), `video/src/shot.mjs`.
- Renders: `video/renders/osme-film_vNN.mp4`, `video/renders/osme-loop_vNN.mp4`. Finals are copied to `video/osme-film.mp4` and `video/osme-loop.mp4`.
- Loop: **final v03** (P = 9 s, seamless, crf 10, 1.9 MB), poster `video/osme-loop-poster.jpg`.
- Film v03 scene starts (18.4 s):
  - S1=0: Lu Yu's three bubbles
  - S2=3.4: 1908 bag at a boil
  - S3=6.0: the bubbles become the OSME bag, Sencha at 100
  - S4=8.6: the push-in; it opens at 80 and the tea plumes
  - S5=10.6: seals at 70; jade ring
  - S6=11.9: one-liner
  - S7=13.5: the bag flies into the lockup and tagline
  - The fade ends at 18.4.
- Evidence: `python3.14 -I personal-library/bin/film-frames.py <mp4> --scenes "..." --step 1 --out /tmp/osme-video/critic-film-vNN`
- Reviews: `video/reviews/` (judge and critic per round). Ledger: `video/critic-ledger.md`.
- Open: the critic and judge rounds on v03, then the creative-director pass. Also open: whether the film pre-empts the live demo (ops/questions.md, 10:52).
