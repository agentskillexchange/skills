#!/usr/bin/env bash
# generate-skills-json.sh — Regenerate skills.json from live ASE data
# Usage: ./generate-skills-json.sh [output_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PYEOF'
import datetime as dt
import html
import json
import sys
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
BROWSE_BASE = "https://agentskillexchange.com/wp-json/ase-marketplace/v1/browse"

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ASE Repo Generator"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)

# Fetch all skills
items = []
page = 1
while True:
    batch, headers = fetch_json(f"{BROWSE_BASE}?per_page=100&page={page}")
    items.extend(batch)
    if page >= int(headers.get("X-WP-TotalPages", "1")):
        break
    page += 1

skills = []
for item in items:
    cats = [html.unescape(x) for x in item.get("categories", [])]
    fws = [html.unescape(x) for x in item.get("frameworks", [])]
    ver = item.get("verification", "listed")
    if ver == "verified_metadata":
        ver = "listed"

    entry = {
        "slug": item.get("slug", ""),
        "name": html.unescape(item.get("title", "")),
        "description": html.unescape((item.get("excerpt") or "").strip()),
        "category": cats,
        "framework": fws,
        "verification": ver,
    }

    # Only include signals if there's real data
    signals = {}
    tool = item.get("tool_match") or ""
    if tool:
        signals["tool"] = tool
    stars = int(item.get("github_stars") or 0)
    if stars:
        signals["github_stars"] = stars
    dl = int(item.get("npm_downloads") or 0)
    if dl:
        signals["npm_weekly_downloads"] = dl
    lic = item.get("tool_license") or ""
    if lic and lic not in ("Unknown", "NOASSERTION"):
        signals["license"] = lic
    if signals:
        entry["signals"] = signals

    skills.append(entry)

output = {
    "version": "2.0",
    "total": len(skills),
    "generated": dt.datetime.utcnow().strftime("%Y-%m-%d"),
    "skills": skills,
}

(REPO_DIR / "skills.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Generated skills.json — {len(skills)} skills.")
PYEOF
