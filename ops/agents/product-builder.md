# product · builder (the product lead builds in-thread)
Output: product/index.html, a single self-contained file. v1 (10:02) is backed up at /tmp/t5-product/index.v1.html.
Tools (in /tmp/t5-product/):
- inline-logo.py re-inlines brand/identity/logo-symbol.svg and logo-lockup.svg as <symbol>s between <!--LOGO--> markers. Run it before every preview.
- shot.mjs <file> <prefix> [w,h] [tea] [secs] shoots states through the #tea=<id>&sec=<demo seconds> hook (Playwright headless shell, mock keychain flags).
- contact.mjs <out.png> <title> <imgs...> builds a gallery contact sheet.
Engine: Newton cooling K=0.075, room 22 °C. Bag opens when t <= hi and seals when t < lo; Sencha hi 80, lo 70 (facts.md).
Time-lapse per tea: waiting is about 8 s or less, brewing about 16 s, then a 4 s hold and the phase is "done". Sencha takes about 28 s from pour to done at 1x.
JS API: window.osme {state, teas, pour, again, reset, choose, speed, advance(sec), lapses}.
