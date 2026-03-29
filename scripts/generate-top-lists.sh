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

# --- Shared: pick best representative per tool ---
def best_per_tool(items_list, signal_key, limit):
    """Deduplicate by tool_match, picking the best representative per tool.
    Tiebreaker: prefer skill whose title/slug contains the tool name, then alphabetical title.
    This matches the homepage PHP logic for consistency."""
    valid = [i for i in items_list if int(i.get(signal_key) or 0) > 0]
    # Group by tool
    from collections import defaultdict
    tool_groups = defaultdict(list)
    for item in valid:
        tool = (item.get("tool_match") or "").lower()
        if not tool:
            continue
        tool_groups[tool].append(item)
    # Pick best per tool
    tool_best = []
    for tool, group in tool_groups.items():
        def sort_key(item):
            title = item.get("title", "").lower()
            slug = item.get("slug", "").lower()
            title_match = 1 if tool in title else 0
            slug_match = 1 if tool in slug else 0
            return (-title_match, -slug_match, item.get("title", ""))
        group.sort(key=sort_key)
        best = group[0]
        tool_best.append(best)
    # Sort by signal descending
    tool_best.sort(key=lambda i: -int(i.get(signal_key) or 0))
    return tool_best[:limit]

# --- TOP-STARS.md ---
top_stars = best_per_tool(items, "github_stars", 50)

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
top_downloads = best_per_tool(items, "npm_downloads", 50)

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
