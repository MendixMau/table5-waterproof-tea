#!/bin/bash
# render_v2.sh <html> <outdir> [slides]: still frame per slide (sN.png), motion frames at 0, 0.5 and 1.5 s
# (sN_m0/1/2.png), a strip per slide (sN_strip.png), and sheet.png (stills, 2x4) when all 8 are rendered.
HTML=$1; OUT=${2:-/tmp/osme-v2}; SL=${3:-"1 2 3 4 5 6 7 8"}; mkdir -p "$OUT"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
shot(){ # slide query budget file
  "$CHROME" --headless=new --use-mock-keychain --password-store=basic --user-data-dir=/tmp/osme-deck/v2chrome-$RANDOM$RANDOM \
    --disable-gpu --hide-scrollbars --autoplay-policy=no-user-gesture-required --window-size=1920,1080 --virtual-time-budget=$3 \
    --screenshot="$4" "file://$HTML$2#$1" >/dev/null 2>&1; }
for i in $SL; do
  shot $i "?still" 4000 "$OUT/s$i.png" &
  shot $i "" 60 "$OUT/s${i}_m0.png" &
  shot $i "" 500 "$OUT/s${i}_m1.png" &
  shot $i "" 1500 "$OUT/s${i}_m2.png" &
  wait
  ffmpeg -y -loglevel error -i "$OUT/s${i}_m0.png" -i "$OUT/s${i}_m1.png" -i "$OUT/s${i}_m2.png" \
    -filter_complex "[0]scale=640:-1[a];[1]scale=640:-1[b];[2]scale=640:-1[c];[a][b][c]hstack=3" "$OUT/s${i}_strip.png"
done
if [ "$SL" = "1 2 3 4 5 6 7 8" ]; then
  ffmpeg -y -loglevel error -start_number 1 -i "$OUT/s%d.png" -vf "scale=960:540,pad=984:564:12:12:color=0x1e1e22,tile=2x4" -frames:v 1 "$OUT/sheet.png"
  ffmpeg -y -loglevel error -start_number 1 -i "$OUT/s%d_strip.png" -vf "pad=iw+16:ih+16:8:8:color=0x1e1e22,tile=1x8" -frames:v 1 "$OUT/strips.png"
fi
