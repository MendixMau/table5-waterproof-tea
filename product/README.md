# product

## HTML demo (the one shown in the pitch)

Start: `open product/index.html`. It is one self-contained file that works offline and loads nothing at runtime. Press **F** for full screen; that also turns on presenter mode, which hides the captions and fades the footer.

| Key | Does |
|---|---|
| Space, Enter, PageDown, → | The one action: pour, resume a paused rehearsal, or brew again once the bag has sealed (2nd, 3rd infusion). A presentation clicker works. |
| R | Reset |
| 1 / 2 / 4 | Time-lapse speed |
| F | Full screen + presenter mode |
| P | Presenter mode on/off |
| ↑ ↓ | Change tea (only before the pour or after a finished run) |
| ← / PageUp | Nothing, on purpose |

The demo tea is **Sencha**, selected on load. The bag opens when the water cools to 80 °C and seals again below 70 °C (facts.md). The ordinary 1908 bag sits beside it. English Breakfast is backup only: it opens at the boil, so it never shows "Waiting".

Timings at 1x for Sencha: it opens at about 8 s (with a short slow-motion moment), seals at about 25 s and is done at about 29 s. Press Space again for the 2nd infusion.

Rehearsal: `index.html#tea=sencha&sec=16` jumps to 16 demo seconds after the pour and pauses there; Space resumes from there. Add `&present=1` for presenter mode. The tea ids are gyokuro, sencha, longjing, tieguanyin, puerh and eb.

## Mendix app

Not built yet. The plan is in `mendix-plan.md`; no app location exists so far.

## Explainer video

`product/Osme_Control_20s.mp4` is a 20-second 1080p explainer (no audio) of the Osme Control concept: sealed capsule, lower into water, lift to open, tea diffuses, push to close, sip. It is built from the concept storyboard image, so it is a stills-and-motion slideshow rather than real product footage.
