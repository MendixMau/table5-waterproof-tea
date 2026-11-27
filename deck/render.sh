#!/bin/bash
# render.sh <outdir> [W,H]: screenshot every slide at its last build step, plus a contact sheet
R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
OUT=${1:-/tmp/osme-deck/shots}; WS=${2:-1920,1080}; mkdir -p "$OUT"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
STEPS=(2 3 0 4 3 3 2 3)
for i in 1 2 3 4 5 6 7 8; do
  s=${STEPS[$((i-1))]}
  "$CHROME" --headless=new --use-mock-keychain --password-store=basic --user-data-dir=/tmp/osme-deck/chrome-$i \
    --disable-gpu --hide-scrollbars --window-size=$WS --virtual-time-budget=4000 \
    --screenshot="$OUT/s$i.png" "file://$R/deck/pitch.html?still#$i.$s" >/dev/null 2>&1 &
done
wait
ls "$OUT"
