# Tea Master (Mendix) — build plan for "The Art of Tea"

Scoped 27 Nov 2026, 09:40 local. Build window ends 13:30. Nothing has been created or run yet.

## Feasibility: YES (with a small risk)

mxcli alone covers the whole path: `mxcli new` → MDL scripts (`mxcli exec`) → `mxcli run --local`.
No Studio Pro, no template and no licence step. Checked on this Mac:
- mxcli nightly-20261105. MxBuild and runtime **11.16.1 are already cached** (`~/.mxcli/mxbuild`, `~/.mxcli/runtime`), so there is no 800 MB download.
- JDK 25 (Temurin) is installed, which 11.14+ needs. Postgres is listening on 127.0.0.1:5432. Docker is not needed.
- Proof from earlier: `~/Mendix/poc-lab/DeskBooking` took about 2 minutes from `new` to `init`, then it served at :8097.
- The runtime is unlicensed (trial): at most 6 sessions, and it **stops at a random time 2 to 4 h after start**. Restart it right before the demo.

Method: the light-mode POC path (`~/Mendix/personal-toolkit/skills/workshop-poc-path.md`), cut down. No pipeline, no toolkit wiring, stock Atlas.

## Time estimate (about 2 h 15 min, finished by about 12:15 if we start 10:00)

| Step | Time |
|---|---|
| Create the app and do a first run (login 200) | 10 min |
| Domain model, enums, security, demo user | 20 min |
| Seed microflow (8 teas, 3 bags, a few past sessions) | 20 min |
| Pages: tea catalogue, tea detail, bag list | 25 min |
| Brew session page with Waiting/Open/Sealed steps (microflow buttons) | 35 min |
| Dashboard (counters) and navigation | 20 min |
| Screenshot check, fixes, demo-script run | 15 min |

That leaves a 1 h 15 min buffer before 13:30.

## App

**Customer frame:** a premium hotel tea lounge, "Tea Master".

**Entities (module TeaMaster)**
- **Tea:** Name, Culture (enum: China, Japan, India, Morocco, England, SouthAfrica, Taiwan), OpenTempC (int), CloseTempC (int), SteepSeconds, MaxInfusions, Ritual (long text)
- **Bag:** BatchCode (for example `AOT-2611-0042`), InfusionsUsed (int), Status (Sealed / Brewing / Spent). Bag belongs to one Tea.
- **BrewSession:** StartTempC, CurrentTempC, State (Waiting / Open / Sealed), OpenedAt, SealedAt, InfusionNo. BrewSession belongs to one Bag.

**Microflows (3 plus seed)**
- `ACT_StartBrew`: creates a session in Waiting at the water temperature.
- `ACT_StepTemp`: changes the water temperature in steps (+5 °C / −5 °C). When it reaches OpenTempC the session goes to Open and records OpenedAt. When it drops below CloseTempC it goes to Sealed, records SealedAt and adds 1 to Bag.InfusionsUsed.
- `ACT_NextInfusion`: starts a new session on the same bag.
- `ASU_Seed` (runs after startup and returns Boolean): fills the data.

**Pages**
1. Tea catalogue: a list of cards grouped by culture, with each tea's open and close temperature.
2. Tea detail: the ritual text and that tea's bags.
3. Brew session: a large state badge (Waiting, Open or Sealed), the current temperature next to the target, and buttons for +5 °C, −5 °C and next infusion.
4. Dashboard: total brews, average infusions per bag, and "bags saved", meaning extra infusions compared with one bag per cup.

**Seed teas:** Gyokuro (JP, 60/50), Sencha (JP, 75/60), Long Jing (CN, 80/65), Tieguanyin oolong (TW, 90/75), Darjeeling first flush (IN, 90/80), Moroccan mint (MA, 95/80), English Breakfast (UK, 98/85), Rooibos (ZA, 98/85).

**Demo user:** `teamaster` / a password of 12 or more characters. Security is set to Production level.

**Demo flow (60 s):** catalogue, then Gyokuro, then start a brew at 40 °C. Press +5 until 60 °C: the bag opens (Open). Press −5 until below 50 °C: the bag seals (Sealed). Start the next infusion, then show the dashboard.

## Exact commands

```bash
mkdir -p ~/Mendix/tea-master && cd ~/Mendix/tea-master
mxcli new TeaMaster --version 11.16.1 --output-dir ./app
cd app && mv mxcli mxcli.linux && cp "$(which mxcli)" mxcli   # macOS: swap in the native binary
git init && git add -A && git commit -qm "blank TeaMaster"
mxcli run --local --watch --detach --db-type hsqldb --app-port 8110 --admin-port 8111 -p TeaMaster.mpr
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8110/login.html   # expect 200
# build loop, one script per step:
mxcli check mdl/01-domain.mdl -p TeaMaster.mpr && mxcli exec mdl/01-domain.mdl -p TeaMaster.mpr && mxcli run wait -p TeaMaster.mpr
#   02-security-seed.mdl, 03-catalogue.mdl, 04-brew.mdl, 05-dashboard-nav.mdl
mxcli run restart -p TeaMaster.mpr          # right before the demo, for a fresh 2-4 h window
```

HSQLDB means there is no database to create. If HSQLDB gives trouble, switch to Postgres: `createdb -U mendix teamaster`.

## Risks

1. Trial runtime stop at 2 to 4 h. Mitigation: restart just before 13:30 and before the demo.
2. MDL limits on page layout: no live animation and no real sensor. The "temperature" is driven by buttons. Fine for a demo, but say it out loud.
3. The runtime has to restart after entity changes. Freeze the domain model early, then do the page work with hot reload.
4. Ports or session clashes with other apps on this Mac. Fixed with dedicated ports 8110/8111. Log out after each test run (6-seat cap).

## Questions for the team before I build

1. Which customer frame: hotel tea lounge, a premium tea brand (B2B batch tracking) or a home "tea ritual" consumer app?
2. Are these the right teas and temperatures? They must match the HTML demo, so please share one list.
3. App name and wording: "Tea Master" or "The Art of Tea"? Any brand colours, or stock Atlas?
4. Does the Mendix app show the same brew moment as the HTML demo, or a different angle (ops/traceability: bags, batches, waste saved)?
5. Who presents the app, on which laptop and at what time? (I'll restart the runtime 10 minutes before.)
