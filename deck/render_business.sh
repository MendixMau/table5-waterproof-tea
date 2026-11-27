#!/bin/bash
# render_business.sh <outdir> [W,H]: screenshot the 4 business slides and tile a 2x2 contact sheet
R=/Users/maurits.visser/.bb/plugins/environment-personal-workspace/host-data/workspaces/thr_sra4smrdju
OUT=${1:-/tmp/osme-biz}; WS=${2:-1920,1080}; mkdir -p "$OUT"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for i in 1 2 3 4; do
  "$CHROME" --headless=new --use-mock-keychain --password-store=basic --user-data-dir=/tmp/osme-biz-chrome-$i \
    --disable-gpu --hide-scrollbars --window-size=$WS --virtual-time-budget=3000 \
    --screenshot="$OUT/s$i.png" "file://$R/deck/business.html?still#$i" >/dev/null 2>&1 &
done
wait
ffmpeg -y -loglevel error -start_number 1 -i "$OUT/s%d.png" -vf "scale=960:540,pad=984:564:12:12:color=0x1e1e22,tile=2x2" -frames:v 1 "$OUT/sheet.png"
