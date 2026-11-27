#!/bin/bash
# s2-frames.sh <html> <outdir>: review frames of the slide 2 timeline (frozen via ?s2t=) plus a contact strip
HTML=$1; OUT=${2:-/tmp/osme-v2-s2}; mkdir -p "$OUT"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TS="0.6 1.4 2.4 3.4 4.4 5.3 6.0 7.0 8.2 9.4"
for t in $TS; do
  "$CH" --headless=new --use-mock-keychain --password-store=basic --user-data-dir=/tmp/osme-deck/s2f-$t-$RANDOM --disable-gpu --hide-scrollbars \
    --window-size=1920,1080 --virtual-time-budget=2500 --screenshot="$OUT/s2_t$t.png" "file://$HTML?s2t=$t#2" >/dev/null 2>&1 &
done; wait
ARGS=(); for t in $TS; do ARGS+=(-i "$OUT/s2_t$t.png"); done
ffmpeg -y -loglevel error "${ARGS[@]}" -filter_complex "$(for i in 0 1 2 3 4 5 6 7 8 9; do printf "[$i]scale=640:-1[v$i];"; done)[v0][v1][v2][v3][v4][v5][v6][v7][v8][v9]xstack=inputs=10:layout=0_0|640_0|1280_0|0_360|640_360|1280_360|0_720|640_720|1280_720|0_1080:fill=0x1e1e22" "$OUT/s2_timeline.png"
