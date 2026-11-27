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
- Film v05 (storyline cut, `src/film_v05.html`, made by `/tmp/osme-video/tools/make_v05.py` from v04; v04 wraps v03 shifted by 8.0 s), 26.4 s:
  - S1=0: title "1,200 years of temperature"
  - S2=1.9: 760s China, Lu Yu's bubbles (they grow)
  - S3=4.8: 1500s Japan, chanoyu iron kettle's pine wind
  - S4=8.0: 1840s Britain, afternoon tea, 100 million cups
  - S5=11.4: 1908 tea bag, art for ease, 96%
  - S6=14.3: Now, OSME sealed at 100, opens at 80 (16.7), seals at 70 (18.7)
  - S7=19.9: value line; S8=21.5: lockup; fade 25.6 to 26.4
- Voice version: `/tmp/osme-video/tools/mix.sh` places Kokoro lines (video/vo-in) with adelay, loudnorm -16 LUFS.
- Open: the critic and judge rounds on v03, then the creative-director pass. Also open: whether the film pre-empts the live demo (ops/questions.md, 10:52).

## 12:12 state (film v11)
- Build chain: `src/film_v05.html` ... `src/film_v11.html`, each made from the previous by `tools/make_vNN.py <in> <out>` (string patches; copies of /tmp/osme-video/tools). Render: `node src/render.mjs src/film_vNN.html renders/osme-film_vNN.mp4` (~5 min).
- `tools/post.sh NN`: voice mix (cues in `vo-in/cues-v11.txt`), evidence pack, `gallery/video-vNN.png`, loudness. `tools/fv2b.sh NN VV`: people version (Firefly Japan/Britain/share with film captions over them).
- Scene starts v11 (26.4 s): S1=0 title card (1.3-2.3 s: "Since 1908: every tea at 100 °C.", temps flip to 100), S2=3.0 China, S3=4.8 Japan kettle, S4=8.0 Britain, S5=11.4 1908, S6=14.3 OSME (opens 80 at 16.8, seals 69 at 18.75), S7=19.9 value line, S8=21.5 lockup.
- Slide-1 files: `osme-film-v04.mp4` (silent) and `osme-film-v04-vo.mp4` = v11. `osme-film.mp4` is still v03 until critic + judge pass.
- Critic r5 on v10: PASS (7.8). Judge r5 on v10: HOOK 3, rest 4 -> v11 hook fix. Judge r6 + critic r6 (S1-S2) on v11 running.
- People version: `renders/osme-film-fv2_v05.mp4` (27.1 s, on v11). Maurits' call; not for slide 1.
