# OSME film: experiment "fv2" (history of tea with people, Firefly and a Kokoro voice)

You are a second Claude Code session helping the video lead of Table 5's OSME pitch. Read this file fully before acting.

## Where you are
- **Repo (open your session here):** `/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju`
- **Your folders, the only places you write:** `video/firefly-v2/` and `video/vo-in/`. Put the final cut in `video/renders/osme-film-fv2_vNN.mp4`.
- **Don't touch** `video/osme-film.mp4` (the main film, v03), `video/src/`, `facts.md`, or other teams' folders. **Never `git commit`**; the lead commits.
- When you finish a step, add one line to `ops/log.md`: `HH:MM | video-fv2 | PREVIEW | video/firefly-v2/<file> | what changed`. Questions go to `ops/questions.md` as `HH:MM | video-fv2 | question | what you chose meanwhile`. Don't wait for answers.
- Deadline: final by 13:00, freeze 13:15.

## What OSME is
A tea bag that stays sealed until the water reaches its tea's ideal temperature, opens to brew, and closes again as the water cools. Sencha opens at 80 °C and seals below 70 °C. Name: OSME, said "oz-MAY". The jury is presales and sales people.
Tone: calm, premium, patient. Life, art, scent, love. Never anti-screen, anti-AI or snobbish. The 1908 tea bag is shown with respect: it made tea easy for everyone.
Facts you may use are only in `facts.md` and `truth/history-cultures.md`. Don't add dates or claims beyond those.

## The current film (what you build on)
- `video/renders/osme-film_v03.mp4`: 18.4 s, 1920×1080, 30 fps, silent. All animated HTML/SVG, no people.
- Timeline: 0–3.4 Lu Yu's bubbles · 3.4–6.3 the 1908 bag at a boil · 6.0–8.6 the OSME bag in a glass, Sencha 100, SEALED · 8.6–10.6 opens at 80 · 10.6–11.9 seals at 70 · 11.9–13.8 the one-liner · 13.5–18.4 the lockup "OSME · Every tea has its temperature."
- Reference stills: `video/firefly-v2/ref/osme-v03-*.png`. Logo: `video/firefly-v2/ref/logo-symbol.svg`. Brand hero: `brand/assets/hero.png`.
- Brand colours: background #0B0B0D, amber #F2A33A, gold #D9C46B, jade #3DBA9B, cream #F3EEE6.

## The experiment: tea through history, in people, about 26 s
Firefly makes the people shots. The product moment stays as the existing HTML animation, cut from v03, because Firefly can't show the bag opening exactly.

| # | Time | Shot | Source | Voice line |
|---|---|---|---|---|
| 1 | 0.0–3.0 | **The master, Tang China (Cha Jing, 760 CE):** a scholar seen from behind or the side, hands over a clay brazier, small bubbles in a shallow kettle | Firefly | vo-01 |
| 2 | 3.0–5.5 | **Japan, chanoyu (Rikyū, 16th c.):** hands whisk matcha with a bamboo chasen, steam from an iron kettle | Firefly | vo-02 |
| 3 | 5.5–8.0 | **Britain, afternoon tea (c. 1840):** a porcelain pot pours for two friends at a lamp-lit table | Firefly | vo-03 |
| 4 | 8.0–10.5 | **The tea bag (c. 1908 → today):** a hand drops a tea bag into a mug; a kettle pours boiling water | Firefly | vo-04 |
| 5 | 10.5–17.5 | **OSME:** cut from v03, 6.0–13.0 (the bag waits at 100, opens at 80, seals at 70) | v03 | vo-05, vo-06 |
| 6 | 17.5–21.0 | **Today, love:** one person hands a glass of green tea across a table; the other smells it and smiles | Firefly | vo-07 |
| 7 | 21.0–26.0 | **Lockup:** cut from v03, 13.5–18.4 | v03 | vo-08 |

### One look for every Firefly shot
Add this style text to every prompt, and upload `ref/osme-v03-9.6.png` as the **style reference**:
> warm painterly 2D animation, hand-drawn ink and gouache texture, near-black background (#0B0B0D), one warm amber key light, gold highlights, a hint of jade in the shadows, cream skin highlights, calm and still, premium, cinematic 16:9, no text, no logos, no watermark

Rules for people:
- Respectful and never a caricature.
- Faces turned away, in profile or soft-focus; hands carry the story. There is no known portrait of Lu Yu, so never show a definite face for him.
- In shot 6, the two people are of different ages and backgrounds, natural and warm, not glamour.

### Firefly prompts (image first, then image-to-video from that frame)
1. **fv2-01-master:** "A Tang dynasty Chinese tea master in simple robes, seen from behind over his shoulder, kneels by a small clay brazier with a shallow kettle; tiny bubbles like fish eyes rise in the water; his hand rests near a bamboo scoop" + style. Video motion: "the bubbles rise slowly, steam drifts, his hand lifts slightly, slow camera push-in".
2. **fv2-02-japan:** "Close-up of hands whisking bright green matcha in a dark ceramic bowl with a bamboo whisk, an iron kettle steams softly behind, tatami and shoji in shadow" + style. Motion: "the whisk moves in a gentle rhythm, foam forms, steam curls".
3. **fv2-03-britain:** "A Victorian afternoon tea at dusk: a porcelain teapot pours amber tea into a fine cup, two friends' hands and sleeves at a lamp-lit table, a cake stand soft in the background" + style. Motion: "the tea pours in a slow stream, a hand lifts the cup".
4. **fv2-04-teabag:** "A modern kitchen at night: a hand drops a paper tea bag into a white mug while a kettle pours boiling water, steam rises fast" + style. Motion: "the water pours, the tea darkens quickly in the mug, steam".
6. **fv2-06-share:** "Two people at a wooden table in warm evening light; one hands a clear glass of pale green tea to the other, who lifts it to their nose and smiles with eyes closed" + style. Motion: "the hand-over, a slow breath in, a gentle smile, steam rises".

Settings: 16:9, 1920×1080, 5 s, no audio. Save as `video/firefly-v2/in/fv2-0N-<name>.png` (keyframe) and `.mp4` (clip).
**Credits:** Maurits approves Adobe credits. Check the balance first and log it. Make **one image** (prompt 1) as the test and show it to him before you make the rest.

## Voice (Kokoro, open source, Apache 2.0)
- Set up Kokoro from github.com/hexgrad/kokoro, in its own venv under `video/vo-in/.venv` (or reuse an existing install).
- Voice `af_heart` (fallback `bf_emma`), speed 0.9, calm and warm. One WAV per line, 24 kHz mono, in `video/vo-in/`.
- Spell OSME as "Oz-may" in the input.
- Write `video/vo-in/README.txt` with the exact command.

| File | Line |
|---|---|
| vo-01 | Twelve centuries ago, a tea master read water by its bubbles. |
| vo-02 | Japan made each bowl a ceremony. |
| vo-03 | Britain made it an afternoon with friends. |
| vo-04 | Then the tea bag made tea easy, and every tea got boiling water. |
| vo-05 | Oz-may waits. At its temperature, it opens. |
| vo-06 | As the water cools, it closes, and keeps the scent. |
| vo-07 | So every cup is the one you meant to make. |
| vo-08 | Oz-may. Every tea has its temperature. |

## Assembly (ffmpeg)
1. Cut each Firefly clip to its slot length (table above). Trim from the calmest part, with a 0.3 s crossfade between shots.
2. Cut the v03 parts with `-ss/-t` from `video/renders/osme-film_v03.mp4`.
3. Grade the Firefly clips so the blacks sit at #0B0B0D (`eq` or `curves`), and check one frame against `ref/osme-v03-9.6.png`.
4. Place each voice line at its slot start plus 0.2 s (`adelay`), then mix. Final loudness: `loudnorm=I=-16:TP=-1.5:LRA=11`.
5. Encode, following the screen-recording-colour-range rule (browser frames are full range):
   `-vf "...,scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p" -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -color_range tv -colorspace bt709 -color_primaries bt709 -color_trc bt709 -r 30 -c:a aac -b:a 192k -movflags +faststart`
   Firefly mp4s are limited range already: use `in_range=tv` for those.
6. Output `video/renders/osme-film-fv2_v01.mp4`. Never overwrite a render; bump the version.
7. Make a contact sheet (8 frames) at `video/firefly-v2/fv2-sheet-v01.png` and log the PREVIEW.
8. Hand back to the video lead (log line), who runs the critic and judge on it.

## Hard no
- No Kling.
- No music.
- No real brand logos in the generated images.
- No text baked into the images.
