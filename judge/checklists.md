# Judge checklists: Table 5, waterproof tea bags ("The Art of Tea")

Run these as a fresh validator. You know only this file, `facts.md`, `README.md` and the repo.
Every line is PASS or FAIL, with the evidence that proves it (a command output, a screenshot path, a URL and the quoted line).

## Ambiguity rule (read first)

If you cannot decide PASS or FAIL from evidence, do not guess. Mark it **ASK**, and write it as a question
for the humans under "Questions" in your report: the check ID, what you saw, the two readings, and what would settle it.
A `_TBD_` in `facts.md` is a FAIL for any check that needs that field, not an ASK.
Never mark PASS because something "looks fine". No evidence means FAIL or ASK.

## Report format

`judge/report-<HHMM>.md`: one table `ID | PASS/FAIL/ASK | evidence | fix`. FAILs first, then ASKs, then the Questions list.
Tally line at the end: counts of PASS, FAIL and ASK, counted from the table rows.

## Setup

```sh
R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
PL=~/Library/CloudStorage/OneDrive-SiemensAG/AI-Presales-Workspace/personal-library
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FLAGS="--headless=new --use-mock-keychain --password-store=basic --user-data-dir=/tmp/judge-chrome --disable-gpu"
OFFLINE='--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE localhost'
shot() { "$CHROME" $FLAGS ${4:+"$4"} --window-size=$2 --screenshot=$3 "$1"; }   # shot <url> 1600,900 /tmp/x.png [extra-flag]
```
Every Chrome launch carries the mock-keychain flags (a hook blocks it otherwise). Open every screenshot and look at it.

## 0. facts.md is locked (gate for everything else)

- [ ] F1 No `_TBD_` left. HOW: `grep -c _TBD_ $R/facts.md` returns 0.
- [ ] F2 Temperature table exists: one row per tea with open temperature (°C) and the close rule (temperature or "as it cools below X"). HOW: read facts.md; list the rows in the report.
- [ ] F3 Angle is the temperature trigger. HOW: facts.md Angle field says opens at the tea's ideal temperature and closes as water cools.

## 1. Research (`truth/`)

- [ ] R1 Every customer, market and competitor claim in truth/ has a URL on the same bullet or paragraph. HOW: read each file; list claims without a URL.
- [ ] R2 Each URL was opened and says the claim. HOW: open every URL (WebFetch). Quote the supporting sentence. Dead link, paywall or "not found on page" = FAIL. Search-only finds ("found by search only") = FAIL for a slide claim.
- [ ] R3 Every number shows its working: inputs, each with a source, and the arithmetic. HOW: recompute every market or price number with `python3 -c`; any difference over 1% = FAIL.
- [ ] R4 No invented quotes. HOW: every text in quote marks or attributed to a person appears verbatim at its URL (search the fetched page for an exact 6+ word substring).
- [ ] R5 Customer evidence names where the customer was found (forum thread, review, job post, survey, interview note with date). HOW: at least 3 distinct sources for the primary customer, at least 1 is people speaking for themselves, not a vendor page.
- [ ] R6 truth/ agrees with the angle. HOW: `grep -rn -i "temperature" $R/truth/`. `truth/mechanisms.md` currently says "Water temperature is never the trigger"; any such line still present and not marked superseded = FAIL.
- [ ] R7 Temperatures in facts.md have a source (tea association, vendor brewing guide). HOW: open the URL and find each tea's temperature on it.

## 2. Brand

- [ ] B1 Name clash search done and recorded in truth/ with URLs: web search `"<Name>" tea`, EUIPO eSearch, WIPO Global Brand Database (class 30), App Store, `.com` domain. HOW: re-run 2 of them yourself. An identical name on a tea or drinks product = FAIL. Similar but different class = ASK.
- [ ] B2 One-liner says what it is (contains "tea bag" or "tea" and the mechanism) in under 10 words. HOW: `echo "<one-liner>" | wc -w` < 10; and a stranger reading only it could say what the product is. If unclear, ASK.
- [ ] B3 Logo legible at 32px. HOW: `sips -Z 32 <logo>.png --out /tmp/logo32.png` (or render the SVG in an `<img width=32>` page with `shot`); open it; name or mark still readable. Then 16px for favicon: note result, not a gate.
- [ ] B4 One logo chosen. HOW: facts.md names which of `brand/logo-A|B|C`; the same file (same hash, `shasum`) or its embedded copy is used on site and deck.
- [ ] B5 Logo colours match facts.md Colours. HOW: `grep -io '#[0-9a-f]\{6\}' brand/<chosen>.svg | sort -u` vs facts.md hex values.

## 3. Product: HTML app and Mendix app (run each list for both)

Paths: HTML in `product/` (find with `ls $R/product`); Mendix app location must be written in `product/README.md`. Missing location = FAIL.
- [ ] P1 Starts with one documented command. HOW: product/README.md gives it; run it exactly as written.
- [ ] P2 Full demo flow runs without errors: pick a tea, heat water, bag opens at the right temperature, colour/strength rises, water cools, bag closes, steeping stops, second infusion works. HOW: screenshot each step; for HTML, `--enable-logging=stderr --v=0` and grep stderr for `Uncaught|Error`; for Mendix, no error popup and no ERROR in the runtime console.
- [ ] P3 Temperature logic matches facts.md for every tea in F2. HOW: set the water 1 °C below, at, and 1 °C above each open temperature: closed, open, open. Then cool below the close value: closed. Record a table. Source values: grep the code (`grep -rn "80\|85\|95" product/`) and compare to facts.md.
- [ ] P4 Same tea list and same temperatures in HTML and Mendix. HOW: compare the two P3 tables cell by cell.
- [ ] P5 Runs offline. HOW: HTML: `$PL/bin/embed-html --check <file>` reports no local refs, `grep -c 'https\?://' <file>` lists only non-loaded text links, and `shot file://<file> 1600,900 /tmp/p-off.png "$OFFLINE"` renders fully. Mendix: run on localhost with Wi-Fi off (ask a human to toggle it) or with OFFLINE flags; flow P2 still completes.
- [ ] P6 Showable in under 60 seconds. HOW: from app already open to bag closed, count clicks (at most 6) and time one run by stopwatch or a scripted run; record seconds. Over 60 = FAIL.
- [ ] P7 Built for the demo laptop. HOW: product/README.md names the laptop and both apps were run on it at a timed rehearsal (who, when). Not written = ASK.

## 4. Site (`docs/index.html`)

- [ ] S1 Says what it does, in the first screen. HOW: `shot file://$R/docs/index.html 1440,900 /tmp/s-desk.png`; the mechanism is visible without scrolling.
- [ ] S2 Says who it is for: the primary customer from facts.md, same words. HOW: grep the exact facts.md Primary customer phrase.
- [ ] S3 Shows the price, identical to facts.md (amount, currency, unit, e.g. per box of N). HOW: `grep -o '€[0-9.,]*[^<]*' docs/index.html` vs facts.md Price.
- [ ] S4 Self-contained. HOW: `$PL/bin/embed-html --check $R/docs/index.html` reports no local refs; exit code 0.
- [ ] S5 Renders on a phone. HOW: `shot file://$R/docs/index.html 390,844 /tmp/s-phone.png`; no horizontal scroll, no cut-off text, price visible. Also `--window-size=390,2400` for the full page.
- [ ] S6 Not the placeholder. HOW: `grep -c "Coming soon" docs/index.html` returns 0.
- [ ] S7 Published. HOW: open the GitHub Pages URL (from README or facts.md) and confirm it serves the same file (`curl -s <url> | shasum` vs local). No URL recorded = ASK.

## 5. Deck and script (`deck/`)

- [ ] D1 Exactly 8 slides. HOW: count slide elements (`grep -c '<section' deck/*.html` or the deck's slide class); confirm by rendering `#1`..`#9` (9 must not exist).
- [ ] D2 Order is company, problem, solution, customer evidence, market, business, competition, the ask. HOW: list the 8 titles in the report; map each to its slot.
- [ ] D3 One message per slide. HOW: write each slide's claim in one clause; a slide needing "and" for two unrelated claims = FAIL.
- [ ] D4 Titles are plain sentences that name the subject (deck-content-rules section 4). HOW: for each title, would it fit another product's deck unchanged? Yes = FAIL.
- [ ] D5 Every number on a slide is in facts.md with a source in truth/. HOW: `grep -oE '[€$]?[0-9][0-9.,]*%?' ` over the deck; each one found in facts.md and traced to a truth/ URL.
- [ ] D6 Script fits 3:00. HOW: `wc -w deck/script.md`; 360 to 440 words = PASS. Timed read-aloud by a human, if done, overrides: at most 3:00.
- [ ] D7 Demo moment is in the script: a marked cue (e.g. `[DEMO]`) saying what is clicked and what the jury sees, on the solution slide. HOW: grep the cue; demo text at most 140 words.
- [ ] D8 Slide 8 asks for one concrete thing (amount, pilot, intro), matching facts.md The ask. HOW: string compare.
- [ ] D9 Competition slide names the 3 facts.md competitors and states the real difference, not three cards of one line (deck-critical-review section 1).
- [ ] D10 No repetition: build the table `# | title | claim | named things` from deck-critical-review section 1; two slides sharing most named things = FAIL.
- [ ] D11 Renders clean. HOW: `shot "file://<deck>#N" 1600,900 /tmp/d-N.png` for N=1..8; no overflow, clipping or empty slide; last build step shown.
- [ ] D12 Deck self-contained: `$PL/bin/embed-html --check <deck>` passes.
- [ ] D13 No em or en dashes in copy. HOW: `grep -c '[–—]' deck/*` returns 0.

## 6. Cross-item consistency

For each field, grep the exact facts.md value in every artefact and fill a table: field x (facts, site, deck, script, HTML app, Mendix app).
- [ ] X1 Name: same spelling and capitals everywhere. HOW: `grep -rn "<Name>" $R/docs $R/deck $R/product`; also grep for the old names (SteepLock, DryDesk, other logo options) which must return 0.
- [ ] X2 Price identical (amount, currency, unit) on site, deck slide 6, script.
- [ ] X3 Primary customer identical on site, deck slide 4, script.
- [ ] X4 Every number in deck, site and script exists in facts.md with the same value and unit.
- [ ] X5 Temperatures identical in facts.md, HTML app, Mendix app, site and deck (if shown).
- [ ] X6 One-liner identical on site, deck slide 1 and in the apps' header (if shown).
- [ ] X7 Colours and font match facts.md: grep hex codes and `font-family` in site, deck and HTML app.
- [ ] X8 Mendix app shows the same brand: open it, screenshot header; logo and name match.

Any difference in X1 to X6 is a FAIL even if both versions look right. Fix it in facts.md first, then everywhere.
