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

VER_LABEL = {
    "listed": "Listed",
    "verified_metadata": "Verified Metadata",
    "security_reviewed": "Security Reviewed",
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

# categories/README.md
root_lines = [
    "# Skill Categories",
    "",
    "Categories are the **top-level map** of the catalog. For live sorting by stars, downloads, and verification, jump into ASE Browse from any category.",
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
    browse_url = "https://agentskillexchange.com/browse-skills/?category=" + urllib.parse.quote(cat['name'], safe='')
    root_lines.append(f"| {emoji} | [**{cat['name']}**]({cat['slug']}/) | **{cat['count']}** | {short_desc} |")
root_lines += [
    "",
    "---",
    "",
    "<div align=\"center\">",
    "",
    "**[Browse all skills on agentskillexchange.com →](https://agentskillexchange.com/browse-skills/)**",
    "",
    "</div>",
    "",
]
(CATEGORIES_DIR / "README.md").write_text("\n".join(root_lines), encoding="utf-8")

# per-category README
for idx, cat in enumerate(cat_rows):
    cat_dir = CATEGORIES_DIR / cat["slug"]
    cat_dir.mkdir(parents=True, exist_ok=True)
    cat_name = cat["name"]
    cat_slug = cat["slug"]
    emoji = CAT_EMOJI.get(cat_name, "📦")
    desc = CAT_DESC.get(cat_name, "Skills in this category.")
    cat_items = [i for i in items if cat_name in i.get("categories", [])]
    cat_items.sort(key=lambda i: (-int(i.get("github_stars") or 0), -int(i.get("npm_downloads") or 0), i.get("title", "").lower()))

    related = [c for c in cat_rows if c["slug"] != cat_slug][:4]
    browse_base = "https://agentskillexchange.com/browse-skills/?category=" + urllib.parse.quote(cat_name, safe='')
    top_starred = [i for i in cat_items if int(i.get('github_stars') or 0) > 0][:6]
    top_downloaded = [i for i in cat_items if int(i.get('npm_downloads') or 0) > 0][:6]
    top_security = [i for i in cat_items if i.get('verification') == 'security_reviewed'][:6]

    def add_section(title, section_items, stat_kind):
        if not section_items:
            return []
        out = [f"## {title}", "", "| Skill | Tier | Signal | Install |", "|---|---|---:|---|"]
        for item in section_items:
            skill_title = item.get('title', '')
            slug = item.get('slug', '')
            tier = VER_LABEL.get(item.get('verification', 'listed'), 'Listed')
            if stat_kind == 'stars':
                signal = '⭐ ' + fmt_num(item.get('github_stars') or 0)
            elif stat_kind == 'downloads':
                signal = '⬇ ' + downloads_str(item.get('npm_downloads') or 0)
            else:
                signal = '🛡️ ' + tier
            out.append(f"| [{skill_title}](../../skills/{slug}/) | {tier} | {signal} | `clawhub install {slug}` |")
        out += ["", "---", ""]
        return out

    lines = [
        f"# {emoji} {cat_name}",
        "",
        f"> **{cat['count']} skills** · [Browse on agentskillexchange.com →]({browse_base})",
        "",
        desc,
        "",
        f"**Live views:** [Top Starred]({browse_base}&sort=stars) · [Top Downloaded]({browse_base}&sort=downloads) · [Security Reviewed]({browse_base}&verification=security_reviewed)",
        "",
        "## At a Glance",
        "",
        f"- **Top Starred:** {len(top_starred)} visible with GitHub signal data",
        f"- **Top Downloaded:** {len(top_downloaded)} visible with npm signal data",
        f"- **Security Reviewed:** {sum(1 for i in cat_items if i.get('verification') == 'security_reviewed')} skills",
        "",
        "---",
        "",
    ]

    lines += add_section('⭐ Top Starred', top_starred, 'stars')
    lines += add_section('🔥 Top Downloaded', top_downloaded, 'downloads')
    lines += add_section('🛡️ Security Reviewed', top_security, 'security')
    lines += [
        "## Full Skill List",
        "",
        "| Skill | Tier | GitHub Stars | npm Downloads | Install |",
        "|---|---|---:|---:|---|",
    ]

    for item in cat_items:
        title = item.get("title", "")
        slug = item.get("slug", "")
        tier = VER_LABEL.get(item.get("verification", "listed"), "Listed")
        stars = fmt_num(item.get("github_stars") or 0)
        downloads = downloads_str(item.get("npm_downloads") or 0)
        lines.append(f"| [{title}](../../skills/{slug}/) | {tier} | {stars} | {downloads} | `clawhub install {slug}` |")

    lines += [
        "",
        "---",
        "",
        "## Quick Install",
        "",
        "```bash",
        "# Install any skill from this category",
        "clawhub install <slug>",
        "",
        "# Or using npx",
        "npx skills add agentskillexchange/skills --skill <slug>",
        "",
        "# For a specific agent",
        "npx skills add agentskillexchange/skills --skill <slug> -a claude-code",
        "npx skills add agentskillexchange/skills --skill <slug> -a cursor",
        "npx skills add agentskillexchange/skills --skill <slug> -a codex",
        "```",
        "",
        "---",
        "",
        "## Related Categories",
        "",
    ]
    for rel in related:
        rel_emoji = CAT_EMOJI.get(rel['name'], '📦')
        lines.append(f"- {rel_emoji} [{rel['name']}](../{rel['slug']}/) ({rel['count']} skills)")
    lines += ["", "---", "", "[← Back to all categories](../)", ""]
    (cat_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")

print(f"Generated {len(cat_rows)} category READMEs from live browse data.")
PY
