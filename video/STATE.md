# Video build state

- Source: `video/src/film.html`, `video/src/loop.html` (SVG timelines driven by `window.setT(t)`), `video/src/render.mjs` (headless Chrome → ffmpeg, injects the current brand/identity logos), `video/src/shot.mjs`.
- Renders: `video/renders/osme-film_vNN.mp4`, `video/renders/osme-loop_vNN.mp4`. Finals copied to `video/osme-film.mp4`, `video/osme-loop.mp4`.
- Film scene starts: S1=0 (Lu Yu, fish eyes) S2=3.2 (pearls) S3=4.8 (rolling waves) S4=7.5 (into the bag) S5=9.6 (temperature) S6=12.0 (opens, wisp) S7=14.2 (OSME, tagline), end 19.0.
- Evidence: `python3.14 -I personal-library/bin/film-frames.py <mp4> --scenes "..." --step 1 --out /tmp/osme-video/critic-film-vNN`
- Critic ledger: `video/critic-ledger.md`.
- Loop: P = 9 s, source frames are seamless (frame 9.0 == 0.0); the encoded seam shows a keyframe jump at crf 20.
