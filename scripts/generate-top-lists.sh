#!/usr/bin/env bash
# generate-top-lists.sh — Regenerate TOP-STARS.md and TOP-DOWNLOADS.md from live ASE data
# Usage: ./generate-top-lists.sh [output_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PYEOF'
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

def fmt_num(n):
    n = int(n or 0)
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}".rstrip("0").rstrip(".") + "M"
    if n >= 1_000:
        return f"{n/1_000:.1f}".rstrip("0").rstrip(".") + "k"
    return str(n) if n else "—"

# Fetch all skills
items = []
page = 1
while True:
    batch, headers = fetch_json(f"{BROWSE_BASE}?per_page=100&page={page}")
    items.extend(batch)
    if page >= int(headers.get("X-WP-TotalPages", "1")):
        break
    page += 1

for item in items:
    item["categories"] = [html.unescape(x) for x in item.get("categories", [])]

# --- TOP-STARS.md ---
# Deduplicate by tool name, keep highest-starred representative
starred = [i for i in items if int(i.get("github_stars") or 0) > 0]
starred.sort(key=lambda i: -int(i.get("github_stars") or 0))
seen_tools = set()
top_stars = []
for item in starred:
    tool = (item.get("tool_match") or "").lower()
    if not tool or tool in seen_tools:
        continue
    seen_tools.add(tool)
    top_stars.append(item)
    if len(top_stars) >= 50:
        break

lines = [
    "# ⭐ Top Starred Skills",
    "",
    "Skills backed by the most-starred GitHub repositories, deduplicated by upstream tool.",
    "",
    f"*{len(top_stars)} unique tools with GitHub star data*",
    "",
    "| # | Skill | Stars | Tool | Category |",
    "|--:|-------|------:|------|----------|",
]
for i, item in enumerate(top_stars, 1):
    title = item.get("title", "")
    slug = item.get("slug", "")
    tool = item.get("tool_match") or ""
    cat = item["categories"][0] if item["categories"] else ""
    stars = fmt_num(item.get("github_stars") or 0)
    lines.append(f"| {i} | [{title}](skills/{slug}/) | {stars} | {tool} | {cat} |")
lines += ["", "---", "", "[← Back to README](README.md)", ""]
(REPO_DIR / "TOP-STARS.md").write_text("\n".join(lines), encoding="utf-8")

# --- TOP-DOWNLOADS.md ---
downloaded = [i for i in items if int(i.get("npm_downloads") or 0) > 0]
downloaded.sort(key=lambda i: -int(i.get("npm_downloads") or 0))
seen_tools = set()
top_downloads = []
for item in downloaded:
    tool = (item.get("tool_match") or "").lower()
    if not tool or tool in seen_tools:
        continue
    seen_tools.add(tool)
    top_downloads.append(item)
    if len(top_downloads) >= 50:
        break

lines = [
    "# 🔥 Top Downloaded Skills",
    "",
    "Skills backed by the most-downloaded npm packages, deduplicated by upstream tool.",
    "",
    f"*{len(top_downloads)} unique tools with npm download data*",
    "",
    "| # | Skill | Weekly Downloads | Tool | Category |",
    "|--:|-------|----------------:|------|----------|",
]
for i, item in enumerate(top_downloads, 1):
    title = item.get("title", "")
    slug = item.get("slug", "")
    tool = item.get("tool_match") or ""
    cat = item["categories"][0] if item["categories"] else ""
    dl = fmt_num(item.get("npm_downloads") or 0)
    lines.append(f"| {i} | [{title}](skills/{slug}/) | {dl}/wk | {tool} | {cat} |")
lines += ["", "---", "", "[← Back to README](README.md)", ""]
(REPO_DIR / "TOP-DOWNLOADS.md").write_text("\n".join(lines), encoding="utf-8")

print(f"Generated TOP-STARS.md ({len(top_stars)} tools) and TOP-DOWNLOADS.md ({len(top_downloads)} tools).")
PYEOF
