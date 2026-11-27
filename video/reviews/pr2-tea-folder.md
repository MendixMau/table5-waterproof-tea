# Review: PR #2 "Add Tea folder" (Dwi1617), 11:05, video lead

What's in it:
- `Tea/Osme.png`: an AI concept board, 1536×1024. The text is baked into the image.
- `Tea/Osme_Control_20s.mp4`: 20 s, 1080p, silent. It's six Ken Burns crops of that board on a light teal slide layout.
- `Tea/make_video.py`: Pillow + imageio-ffmpeg.
- `Tea/build/`: 11 preview PNGs.
- PR #1 adds the same png and mp4 to `product/`.

Sheet: video/reviews/pr2-tea-sheet.png

## Findings
1. **It shows a different product.** "Osme Control" is a manual capsule: you lift a rod to open it and push to close. Our OSME opens and seals by itself, at its tea's temperature (facts.md: Sencha 80/70). Put it in the pitch and the jury will ask "button or temperature?"
2. **It's off brand.** It uses a light teal and navy slide look, a Georgia italic "Osme" and Segoe type. It doesn't use the Midnight Brew tokens, the Jost wordmark, the "OSME" spelling or logo v4.
3. **The picture is soft.** Each scene is a crop of about 240×180 to 350×290 px, blown up about 4× onto a 980×810 card. The baked-in text (OPEN/CLOSE, arrows) blurs.
4. **The script only runs on the author's PC.** It has Windows paths (`C:\DWI - 2026\...`) and Windows fonts. There are no BT.709 or range tags on the encode, and it fades through white.
5. **The repo gets cluttered.** A new root folder `Tea/` sits outside the topic folders, with about 7 MB of committed previews. It also duplicates #1.

## Good things to keep
- The 3-step logic (SEALED → OPEN TO BREW → CLOSE TO ISOLATE) is the same as our film's arc. That's a good sign the story reads.
- The diffusion still (orange plumes swirling from the capsule into a clear glass) is the best "tea entering water" picture we have.
- Its honesty line, "Concept only… requires testing", suits a sales jury.

## Advice for the film
- **Don't cut the PR video, or its crops, into the OSME film.** The mechanism is wrong, the brand is wrong, and the picture is too soft.
- **Do use it as a reference:**
  - (a) The diffusion still becomes the Firefly *structure reference* for a real-tea insert at the opening moment (8.6–10.6 s): a clear glass, tea plumes, re-lit in our dark amber and jade look, with no rod.
  - (b) Its 3-panel layout becomes a "SEALED · OPENS AT 80° · SEALS AT 70°" strip for the pitch or site, built in our brand.
  - (c) The "concept, needs testing" line goes on a slide, not in the film.
- **Repo:** merge one of #1 or #2, not both. A better home is `product/concepts/osme-control/`, without `build/`. Make the script paths relative. That's the lead's call.
