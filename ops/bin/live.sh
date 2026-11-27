#!/bin/zsh
setopt nullglob
cd "${0:A:h}/../.."
# Everything colleagues need on GitHub. Missing paths are skipped (a missing pathspec would abort git add).
PATHS=(README.md ASSETS.md facts.md gallery ops truth judge brand deck product docs shared refs
       video/*.md video/*.mp4 video/*.jpg video/src video/reviews video/firefly-v2 video/vo-in)
i=0
while true; do
  python3 ops/bin/board.py 2>>/tmp/t5-live.err
  if (( i % 10 == 0 )); then
    L=(); for p in $PATHS; do [[ -e $p ]] && L+=($p); done
    git add -- $L 2>>/tmp/t5-live.err
    git commit -qm "Live progress $(date +%H:%M)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" >/dev/null 2>&1
    git push -q 2>>/tmp/t5-live.err || { git pull -q --rebase=merges 2>>/tmp/t5-live.err && git push -q 2>>/tmp/t5-live.err; }
  fi
  i=$((i + 1)); sleep 30
done
