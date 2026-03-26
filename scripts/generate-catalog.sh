#!/usr/bin/env bash
# generate-catalog.sh — Regenerate CATALOG.md from live ASE browse data
# Usage: ./generate-catalog.sh [output_dir]
#   output_dir: directory containing the git repo (default: parent of scripts/)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PY'
import datetime as dt
import html
import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
BROWSE_BASE = "https://agentskillexchange.com/wp-json/ase-marketplace/v1/browse"
WP_CAT_URL = "https://agentskillexchange.com/wp-json/wp/v2/skill_category?per_page=100&orderby=count&order=desc"

CAT_EMOJI = {
    "CI/CD Integrations": "🔧",
    "Runbooks & Diagnostics": "📋",
    "Code Quality & Review": "✅",
    "Developer Tools": "🛠️",
    "Library & API Reference": "📚",
    "Monitoring & Alerts": "📊",
    "Data Extraction & Transformation": "🔄",
    "Security & Verification": "🔒",
    "Templates & Workflows": "📄",
    "Calendar, Email & Productivity": "📅",
    "Integrations & Connectors": "🔗",
    "Browser Automation": "🌐",
    "Image & Creative Automation": "🎨",
    "Research & Scraping": "🔍",
    "Content Writing & SEO": "✍️",
    "Media & Transcription": "🎙️",
    "WordPress & CMS": "📰",
}
VER_LABEL = {
    "listed": "Published",
    "verified_metadata": "Published",
    "security_reviewed": "Security Reviewed",
}

def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw ASE Catalog Generator"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)

def fmt_num(n):
    n = int(n or 0)
    if n >= 1_000_000:
        s = f"{n/1_000_000:.1f}".rstrip("0").rstrip(".")
        return f"{s}M"
    if n >= 1_000:
        s = f"{n/1_000:.1f}".rstrip("0").rstrip(".")
        return f"{s}k"
    return str(n) if n else "—"

def downloads_str(n):
    n = int(n or 0)
    return f"{fmt_num(n)}/wk" if n else "—"

cats, _ = fetch_json(WP_CAT_URL)
cat_rows = [{"name": html.unescape(c["name"]), "slug": c["slug"], "count": int(c["count"])} for c in cats]
items = []
page = 1
while True:
    batch, headers = fetch_json(f"{BROWSE_BASE}?per_page=100&page={page}")
    items.extend(batch)
    total_pages = int(headers.get("X-WP-TotalPages", "1"))
    if page >= total_pages:
        break
    page += 1

for item in items:
    item["categories"] = [html.unescape(x) for x in item.get("categories", [])]
    item["frameworks"] = [html.unescape(x) for x in item.get("frameworks", [])]

ver = Counter(i.get("verification", "listed") for i in items)
framework_count = len({f for i in items for f in i.get("frameworks", [])})
signal_count = sum(1 for i in items if int(i.get("github_stars") or 0) > 0 or int(i.get("npm_downloads") or 0) > 0 or (i.get("tool_license") and i.get("tool_license") != "Unknown"))

lines = [
    "# Agent Skill Exchange — Full Catalog",
    "",
    f"> **{len(items)} published skills** across **{len(cat_rows)} categories** · {ver['security_reviewed']} security reviewed · Updated {dt.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
    ">",
    "> Browse the [live marketplace](https://agentskillexchange.com/browse-skills/) for search, filtering, and one-click install.",
    "",
    "---",
    "",
    "## Skills by Category",
    "",
]

for cat in cat_rows:
    cat_name = cat['name']
    cat_slug = cat['slug']
    cat_items = [i for i in items if cat_name in i.get('categories', [])]
    cat_items.sort(key=lambda i: (-int(i.get('github_stars') or 0), -int(i.get('npm_downloads') or 0), i.get('title', '').lower()))
    emoji = CAT_EMOJI.get(cat_name, '📦')
    browse_url = 'https://agentskillexchange.com/browse-skills/?category=' + urllib.parse.quote(cat_name, safe='')
    lines += [
        f"### {emoji} {cat_name} ({cat['count']} skills)",
        "",
        f"Live views: [Browse]({browse_url}) · [Top Starred]({browse_url}&sort=stars) · [Top Downloaded]({browse_url}&sort=downloads)",
        "",
        "| Skill | Description | Tier | ⭐ Stars | 📦 Downloads |",
        "|---|---|---|---:|---:|",
    ]
    for item in cat_items:
        title = html.unescape(item.get('title', ''))
        slug = item.get('slug', '')
        tier = VER_LABEL.get(item.get('verification', 'listed'), 'Published')
        desc = html.unescape((item.get('excerpt') or '').strip())
        # Truncate long descriptions for table readability
        if len(desc) > 120:
            desc = desc[:117].rsplit(' ', 1)[0] + '…'
        # Escape pipe characters in description
        desc = desc.replace('|', '\\|')
        lines.append(f"| [{title}](skills/{slug}/) | {desc} | {tier} | {fmt_num(item.get('github_stars') or 0)} | {downloads_str(item.get('npm_downloads') or 0)} |")
    lines += ["", ""]

lines += [
    "---",
    "",
    "<div align=\"center\">",
    "",
    "**[agentskillexchange.com](https://agentskillexchange.com)** — The marketplace for trusted AI agent skills",
    "",
    "</div>",
    "",
]

(REPO_DIR / 'CATALOG.md').write_text('\n'.join(lines), encoding='utf-8')
print(f"Generated CATALOG.md for {len(items)} skills.")
PY
