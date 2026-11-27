# Pitch v2 validator brief (fresh agent, never the builder)
Repo R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
Read: ops/agents/_common.md, facts.md, truth/business-case.md, truth/history-cultures.md, truth/customers-market.md, deck/model_business.py (run it), judge/checklists.md §5 and §6.
Target: the frozen build named in your prompt (HTML file + render folder with sN.png end states, sN_strip.png frames at 0 / 0.5 / 1.5 s, sheet.png). Source fragments: deck/v2/s1..s8.html; engine deck/build_pitch_v2.py. Do NOT edit any file.
Checks, each PASS / FAIL / ASK with evidence:
- V1 numbers: every number on every slide matches model_business.py at PRICE 1.50 or facts.md / truth (year 3 $8.3 m never $9 m; margin $1.08, 72%, labelled "at year-3 scale"; $0.50 a cup; TAM $7.1 bn, SAM $640 m, 1.3%; ask $2.5 m SAFE at $10 m pre; use of funds; competitor prices; 96% wording vs its source; 16% vs its source; dates 760, 1500s, c. 1840, 1908).
- V2 every slide's `<aside class="notes">` gives a source for every number on that slide.
- V3 no em or en dashes in visible deck copy and in the fragments (`grep -c '[–—]'`); the product iframe srcdoc belongs to another topic: report separately.
- V4 English only; tone positive (art, scent, ritual, love), not anti-screen or anti-AI; "tea-tech disruptor" absent.
- V5 1920x1080: open every sN.png: nothing clipped, overlapping or cut off; body text at least 28 px (labels and source captions may be smaller), at most 2 data elements per slide, no tables on stage. Also render at 1600x900 (`deck/render_v2.sh <html> /tmp/osme-val-1600 ...` uses 1920; copy its Chrome line with --window-size=1600,900 and ?still) and look.
- V6 presenter: N notes, T timer with target time, each slide shows its target (bottom-right), slide 3 keys (Space or Enter pour, R reset, PageDown next, PageUp back, also with focus inside the iframe): verify by reading the JS in the engine and deck/v2/s3.html; drive it in headless Chrome if you can.
- V7 `~/Library/CloudStorage/OneDrive-SiemensAG/AI-Presales-Workspace/personal-library/bin/embed-html --check <html>` reports self-contained.
- V8 bland test: every slide has at least one brand visual AND one motion moment (see the strips; slide 2 also has a timeline sheet, its motion runs ~9 s; slide 1 is the film, headless video stalls after ~1 s).
Chrome launches MUST carry --use-mock-keychain --password-store=basic and an own --user-data-dir.
Output: judge/report-deck-v2-<HHMM>.md (ID | PASS/FAIL/ASK | evidence | exact fix: slide, element, new text), FAILs first, tally line. Report back under 200 words: the FAILs and ASKs with fixes, and the tally "PASS/FAIL (k)".
