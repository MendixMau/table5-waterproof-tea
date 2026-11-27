# OSME brand film: storyboard

Preview: [gallery/video-storyboard.png](../gallery/video-storyboard.png) (8 key frames, real renders of `video/src/film.html`).

| | |
|---|---|
| Use | Pitch opener (plays before slide 1) |
| Length | 19 s, 1920×1080, 30 fps, H.264 |
| Sound | Silent by default. Optional: a soft room tone and one water pour, self-made, no music (no copyright). |
| Look | Midnight Brew tokens: matte black #0B0B0D, amber #F2A33A → gold #D9C46B → jade #3DBA9B, warm white #F3EEE6. Futura display, Avenir Next text. |
| Logo | Injected at render time from `brand/identity/logo-symbol.svg` and `logo-wordmark.svg`, so logo v4 drops in without edits. |
| Pace | Calm and patient: one new thing at a time, every beat holds at least 1 s. |

## Story in three beats
Art (Lu Yu's bubbles) → the product (the bag opens at its temperature) → the movement (OSME, the tagline).
The film says what the product does by 0:13, so the jury knows the noun before slide 1.

## Shots

| # | Time | Beat | Picture | Words on screen |
|---|---|---|---|---|
| 1 | 0:00–0:02 | Stillness | Black with a warm breath of light rising from the centre; no dead frames. | "In the eighth century, Lu Yu read water by its bubbles." |
| 2 | 0:02–0:04 | Fish eyes | First bubble rises from below, small, jade. | FISH EYES |
| 3 | 0:03–0:05 | String of pearls | Second bubble, gold, a string of tiny pearls trailing beneath it. | STRING OF PEARLS |
| 4 | 0:05–0:07 | Rolling waves | Third bubble, amber, the largest; two rings roll out. All three hold. | ROLLING WAVES |
| 5 | 0:07–0:10 | Into the bag | Caption and labels fade; the three bubbles rise one after another into the OSME tea bag, which draws itself. | none |
| 6 | 0:10–0:12 | The temperature | The amber-to-jade arc draws under the bag. A marker slides along it as the water cools: 100 °C counts down. | 100 °C … 80 °C |
| 7 | 0:12–0:14 | It opens | At 80 °C the bag breathes and a scent wisp curls up. | "Sencha opens at 80 °C. And closes as the cup cools." |
| 8 | 0:14–0:19 | OSME | Bag settles up, OSME wordmark and the arc, then the tagline. Hold, fade to black. | OSME · "Every tea has its temperature." |

## Site hero loop (`video/osme-loop.mp4`)
9 s, silent, seamless: the three bubbles drift up through the dark in turn, a scent wisp curls, the arc breathes amber → jade. No text (the site sets its own headline over it). Under 4 MB.

## Optional photoreal inserts (Kling, needs approval)
See ops/questions.md: leaves unfurling in a glass cup, steam over a cup in the dark. They would sit between shots 4 and 5 (water) or behind shot 7 (scent), 2 s each.

## Build
`node video/src/render.mjs video/src/film.html video/osme-film_vNN.mp4` (headless Chrome frame by frame → ffmpeg). Stills: `--stills 1.2,2.9,...`.
