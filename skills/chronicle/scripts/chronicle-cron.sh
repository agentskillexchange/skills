#!/bin/sh
# chronicle periodic maintenance.
#
#   (no args)    pull every machine's lanes and blobs into the spine, reindex
#   --narrate    additionally run the background narrator over unnarrated work
#
# Both are safe to run concurrently with live capture: lanes are append-only and blobs are
# content-addressed, so a sync that overlaps a write copies a shorter prefix and catches
# the rest next time.
#
# Narration is gated by butler, so this can never quietly drain the weekly token budget.
# Failures land in ~/.chronicle/errors.log; this script always exits 0 so a cron failure
# never turns into mail spam or a red herring during debugging.

export PATH="$HOME/.local/bin:/usr/local/bin:/opt/homebrew/bin:$PATH"
LOG="$HOME/.chronicle/cron.log"
mkdir -p "$HOME/.chronicle"

{
  echo "--- $(date -u +%Y-%m-%dT%H:%M:%SZ) $1 ---"
  chron sync 2>&1
  if [ "$1" = "--narrate" ]; then
    chron narrate 2>&1
  fi
} >> "$LOG" 2>&1

# Keep the log bounded. It is a convenience for debugging the ledger, not the ledger.
if [ -f "$LOG" ]; then
  tail -n 2000 "$LOG" > "$LOG.tmp" 2>/dev/null && mv "$LOG.tmp" "$LOG"
fi
exit 0
