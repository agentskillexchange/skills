#!/usr/bin/env bash
# generate-categories.sh — Regenerate per-category README.md files from live ASE browse data
# Usage: ./generate-categories.sh [output_dir]
#   output_dir: directory containing the git repo (default: parent of scripts/)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PY'
import html
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
CATEGORIES_DIR = REPO_DIR / "categories"
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

CAT_DESC = {
    "CI/CD Integrations": "Pipeline configs, deployment automation, build tooling, and continuous integration/delivery skills.",
    "Runbooks & Diagnostics": "Incident response, troubleshooting guides, system diagnostics, and operational runbooks.",
    "Code Quality & Review": "Linting rules, review checklists, code standards enforcement, and quality gates.",
    "Developer Tools": "CLI helpers, dev environment setup, productivity utilities, and developer workflows.",
    "Library & API Reference": "SDK documentation, API guides, framework reference material, and library usage patterns.",
    "Monitoring & Alerts": "Metrics collection, alerting rules, observability setup, and system monitoring.",
    "Data Extraction & Transformation": "Parsing, ETL pipelines, format conversion, data wrangling, and transformation utilities.",
    "Security & Verification": "Auth setup, vulnerability scanning, compliance checks, and security automation.",
    "Templates & Workflows": "Project scaffolding, boilerplate generators, workflow templates, and starter kits.",
    "Calendar, Email & Productivity": "Email automation, calendar management, task coordination, and productivity tools.",
    "Integrations & Connectors": "Third-party API bridges, webhook handlers, service connectors, and platform integrations.",
    "Browser Automation": "Web scraping, UI testing, headless browser control, and browser-based automation.",
    "Image & Creative Automation": "Image generation, asset processing, design automation, and creative tooling.",
    "Research & Scraping": "Web research, data collection, content aggregation, and information gathering.",
    "Content Writing & SEO": "Blog posts, SEO optimization, content strategy, and writing assistance.",
    "Media & Transcription": "Audio/video processing, speech-to-text, media conversion, and transcription.",
    "WordPress & CMS": "Theme/plugin development, WP-CLI automation, CMS management, and WordPress skills.",
}

def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "OpenClaw ASE Repo Generator"})
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
cat_rows = []
for c in cats:
    cat_rows.append({
        "id": c["id"],
        "name": html.unescape(c["name"]),
        "slug": c["slug"],
        "count": int(c["count"]),
    })

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

CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)

# categories/README.md (index)
root_lines = [
    "# Skill Categories",
    "",
    f"> **{len(items)} skills** across **{len(cat_rows)} categories**",
    "",
    "| | Category | Skills | Description |",
    "|---|---|:---:|---|",
]
for cat in cat_rows:
    emoji = CAT_EMOJI.get(cat['name'], '📦')
    desc = CAT_DESC.get(cat['name'], 'Skills in this category.')
    short_desc = desc if len(desc) <= 72 else desc[:69] + '...'
    root_lines.append(f"| {emoji} | [**{cat['name']}**]({cat['slug']}/) | **{cat['count']}** | {short_desc} |")
root_lines += [
    "",
    "---",
    "",
    "[Browse all skills on agentskillexchange.com →](https://agentskillexchange.com/browse-skills/)",
    "",
]
(CATEGORIES_DIR / "README.md").write_text("\n".join(root_lines), encoding="utf-8")

# per-category README — clean format
for cat in cat_rows:
    cat_dir = CATEGORIES_DIR / cat["slug"]
    cat_dir.mkdir(parents=True, exist_ok=True)
    cat_name = cat["name"]
    emoji = CAT_EMOJI.get(cat_name, "📦")
    desc = CAT_DESC.get(cat_name, "Skills in this category.")
    cat_items = [i for i in items if cat_name in i.get("categories", [])]
    cat_items.sort(key=lambda i: (-int(i.get("github_stars") or 0), -int(i.get("npm_downloads") or 0), i.get("title", "").lower()))

    top_starred = [i for i in cat_items if int(i.get('github_stars') or 0) > 0][:10]
    top_downloaded = [i for i in cat_items if int(i.get('npm_downloads') or 0) > 0][:10]

    lines = [
        f"# {emoji} {cat_name}",
        "",
        desc,
        "",
    ]

    # Top Starred
    if top_starred:
        lines += [
            "## ⭐ Top Starred",
            "",
            "| Skill | Stars |",
            "|---|---:|",
        ]
        for item in top_starred:
            title = item.get('title', '')
            slug = item.get('slug', '')
            stars = fmt_num(item.get('github_stars') or 0)
            lines.append(f"| [{title}](../../skills/{slug}/) | ⭐ {stars} |")
        lines += ["", "---", ""]

    # Top Downloaded
    if top_downloaded:
        lines += [
            "## 📦 Top Downloaded",
            "",
            "| Skill | Downloads |",
            "|---|---:|",
        ]
        for item in top_downloaded:
            title = item.get('title', '')
            slug = item.get('slug', '')
            downloads = downloads_str(item.get('npm_downloads') or 0)
            lines.append(f"| [{title}](../../skills/{slug}/) | ⬇ {downloads} |")
        lines += ["", "---", ""]

    # Full Skill List
    lines += [
        "## Full Skill List",
        "",
        "| Skill | Stars | Downloads |",
        "|---|---:|---:|",
    ]
    for item in cat_items:
        title = item.get("title", "")
        slug = item.get("slug", "")
        stars = fmt_num(item.get("github_stars") or 0)
        downloads = downloads_str(item.get("npm_downloads") or 0)
        lines.append(f"| [{title}](../../skills/{slug}/) | {stars} | {downloads} |")

    lines += [
        "",
        "---",
        "",
        "[← Back to all categories](../)",
        "",
    ]
    (cat_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")

print(f"Generated {len(cat_rows)} category READMEs from live browse data.")
PY
