# Judge, film fv2 v08 (osme-film-v04-vo.mp4, 26.5 s, photos + drawn), round 7

| Criterion | Score | Fix asked |
|---|---|---|
| HOOK | 4 | none. The title card reads in silence (0-2.4 s): headline, then "Since 1908, the tea bag: every tea at 100 °C.", with the temperatures struck to 100. Last round's fact fix and voice clash are both gone. Note: the film has no music bed (the gaps between voice lines measure silent), so the room hears 2.4 s of total silence at the start. That works only if Maurits says nothing and does not look at the laptop. |
| CLARITY | 4 | none. The steps read Sealed 100° -> 94° SEALED "too hot for Sencha" -> 80° OPEN -> 69° SEALED "scent kept inside", and the voice says the same thing in plain words. |
| STORY | 4 | none. The real people carry the history (China, Japan, Britain) and the sharing beat. The drawn parts carry the idea (1908 problem, product, logo). The mix makes sense: the past is photographed and the invention is drawn. The couple beat (20.5-22.3 s) moves the ending from mechanism to people, which matches the "life, love" tone. |
| CRAFT | 3 | The couple shot is the film's only warm human close-up, and both of its transitions spoil it. **In:** 20.1-20.4 s, the caption "It opens at its tea's temperature…" and the 69° readout fade across the couple's faces. **Out:** 22.4-22.7 s, the flying OSME bag icon lands on the woman's face, like a sticker, before the logo resolves. Fix (ffmpeg only): change both crossfades with the couple photo from a dissolve to `xfade=transition=fadeblack` (0.3 s), or trim the logo clip's head by about 0.35 s so the bag's flight happens on dark ground, not over her face. The couple gets about 2 s of clean screen either way. |
| BRAND | 4 | optional (carried over from v11): 13.5-14.5 s, "NOW · OSME" is still tiny. The voice says "Oz-may" at 14.3 s and again at 23.2 s, so the pronunciation lands twice, and the logo holds for about 4 s. |

**Weakest moment:** 22.3-22.7 s. The bag icon lands on the woman's face and "OSME" ghosts across the couple. It is the hand-off from people to brand, and the eye sees a collision instead of a reveal. Runner-up: 2.4-2.7 s, where "In China…" starts about 0.3 s before China appears on screen (the voice is over the title card's struck "100 °C"). It is small, but it is the first word the room hears.

**Facts:** no new errors. Lu Yu c. 760 judging water by its bubbles ("by eye") is right. Chanoyu in the 1500s is right. Afternoon tea in the 1840s and about 100 million cups a day match history-cultures.md. "96% of UK tea is brewed from a bag" matches the QMUL figure. Sencha opens at 80 and is SEALED at 69, which fits "seals below 70". The title card puts "100 °C" under JAPAN and CHINA, but the subline "the tea bag" makes it a claim about the bag, so it holds. Still soft: "pine wind" rests on a garden blog. Risk, not an error: the China tea master and the couple are AI-generated but look like photos, and the China one is labelled "LU YU". A presales jury may ask "is that real?" If asked, say "AI-generated reconstruction". Optionally add a 1-line credit in the end card's corner (caption change only).

**Voice vs picture:** in sync, measured from the mix:
- China starts at 2.40 s, about 0.3 s before the photo (the cut is at 2.7 s).
- Japan (5.05 s) and Britain (8.25 s) sit inside their scenes.
- vo-04 (10.75 s) starts on the 1908 bag.
- "It opens" ends at about 16.7 s; OPEN shows at 16.75 s.
- "It closes" lands in 17.0-19.7 s, around the SEALED readout at 18.75 s.
- vo-07 (20.5-21.9 s) plays on the couple.
- "Oz-may" (23.2 s) lands with the formed logo and tagline.

There are no text-versus-voice clashes, apart from the caption ghosting into the couple shot (CRAFT fix). Optional: on the couple, add the caption "Everyone can be a tea person." at 20.5-22.2 s, so the beat also reads with the sound off.

**On the mix:** it works and it is better than the all-drawn cut for this jury. Real faces at 2.7-10.7 s give the history weight, and the couple gives the ending a reason. The drawn product scenes stay the clearest part of the film. The one cost is the two seams into and out of the couple, and that one ffmpeg change fixes both.
