#!/usr/bin/env bash
# sync-from-api.sh — Reproduce generated repo artifacts from the public ASE API.
# Usage: ASE_API_BASE=https://agentskillexchange.com ./scripts/sync-from-api.sh [repo_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}" 
export ASE_API_BASE="${ASE_API_BASE:-https://agentskillexchange.com}"
export ASE_SITE_BASE="${ASE_SITE_BASE:-$ASE_API_BASE}"

case "$ASE_API_BASE" in
  http://*|https://*) ;;
  *) echo "ASE_API_BASE must be an http(s) URL, got: $ASE_API_BASE" >&2; exit 2 ;;
esac

echo "Syncing generated ASE repo artifacts from $ASE_API_BASE"
bash "$SCRIPT_DIR/generate-all.sh" "$REPO_DIR"
