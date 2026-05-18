#!/usr/bin/env bash
# generate-agent-files.sh — Update .claude-plugin, .codex, .cursor-plugin, .opencode with live counts
# Usage: ./generate-agent-files.sh [output_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PYEOF'
import json
import os
import sys
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
SITE_BASE = os.environ.get("ASE_SITE_BASE", os.environ.get("ASE_API_BASE", "https://agentskillexchange.com")).rstrip("/")

def get_total():
    req = urllib.request.Request(
        f"{SITE_BASE}/wp-json/wp/v2/skill?per_page=1",
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; ASE Repo Generator/1.0)",
            "Accept": "application/json,text/plain,*/*",
        },
        method="HEAD",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return int(resp.headers.get("X-WP-Total", 0))

total = get_total()
# Round to nearest hundred for description
rounded = f"{(total // 100) * 100:,}+"

files = {
    ".claude-plugin": f"{rounded} security-scanned agent skills — the largest open skills collection with real ecosystem signals.",
    ".codex": f"{rounded} security-scanned agent skills for Codex — the largest open skills collection with real ecosystem signals.",
    ".cursor-plugin": f"{rounded} security-scanned agent skills for Cursor — the largest open skills collection with real ecosystem signals.",
    ".opencode": f"{rounded} security-scanned agent skills — the largest open skills collection with real ecosystem signals.",
}

for filename, desc in files.items():
    data = {
        "schema_version": "1.0",
        "name": "agent-skill-exchange",
        "display_name": "Agent Skill Exchange",
        "description": desc,
        "version": "1.0.0",
        "homepage": SITE_BASE,
        "skills_directory": "skills/",
        "license": "MIT",
    }
    (REPO_DIR / filename).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

print(f"Updated agent files with {rounded} skills.")
PYEOF
