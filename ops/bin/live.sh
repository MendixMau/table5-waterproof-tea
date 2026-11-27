#!/bin/zsh
# Rebuilds the live board every 30 s; commits and pushes the shareable files every 5 min.
setopt nullglob
cd "${0:A:h}/../.."
i=0
while true; do
  python3 ops/bin/board.py 2>>/tmp/t5-live.err
  if (( i % 10 == 0 )); then
    git add README.md facts.md gallery ops truth judge brand deck product docs video/*.md 2>>/tmp/t5-live.err
    git commit -qm "Live progress $(date +%H:%M)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" >/dev/null 2>&1 && git push -q 2>>/tmp/t5-live.err
  fi
  i=$((i + 1))
  sleep 30
done
