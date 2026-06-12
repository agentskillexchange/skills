#!/usr/bin/env bash
# generate-readme.sh — Regenerate README.md from live ASE data
# Usage: ./generate-readme.sh [output_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PYEOF'
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
SITE_BASE = os.environ.get("ASE_SITE_BASE", os.environ.get("ASE_API_BASE", "https://agentskillexchange.com")).rstrip("/")
BROWSE_BASE = f"{SITE_BASE}/wp-json/ase-marketplace/v1/browse"
WP_CAT_URL = f"{SITE_BASE}/wp-json/wp/v2/skill_category?per_page=100&orderby=count&order=desc"
HOMEPAGE_PICKS_URL = f"{SITE_BASE}/wp-json/ase-marketplace/v1/homepage-picks"
INDUSTRY_MANIFEST = REPO_DIR / "scripts" / "industry-collections.json"

CAT_EMOJI = {
    "CI/CD Integrations": "🔧", "Runbooks & Diagnostics": "📋",
    "Code Quality & Review": "✅", "Developer Tools": "🛠️",
    "Library & API Reference": "📚", "Monitoring & Alerts": "📊",
    "Data Extraction & Transformation": "🔄", "Security & Verification": "🔒",
    "Templates & Workflows": "📄", "Calendar, Email & Productivity": "📅",
    "Integrations & Connectors": "🔗", "Browser Automation": "🌐",
    "Image & Creative Automation": "🎨", "Research & Scraping": "🔍",
    "Content Writing & SEO": "✍️", "Media & Transcription": "🎙️",
    "WordPress & CMS": "📰",
}
CAT_SHORT = {
    "CI/CD Integrations": "Pipeline configs, deployment automation, build tooling",
    "Runbooks & Diagnostics": "Incident response, troubleshooting, system diagnostics",
    "Code Quality & Review": "Linting, code review, test generators, coverage",
    "Developer Tools": "CLI tools, scaffolders, dev environment setup",
    "Library & API Reference": "SDK docs, API parsers, symbol resolvers",
    "Monitoring & Alerts": "Metrics, alerting rules, observability",
    "Data Extraction & Transformation": "ETL pipelines, parsing, format conversion",
    "Security & Verification": "Vulnerability scanning, auth setup, compliance",
    "Templates & Workflows": "Scaffolders, boilerplate generators, workflow templates",
    "Calendar, Email & Productivity": "Email automation, calendar management, task coordination",
    "Integrations & Connectors": "Third-party API bridges, webhooks, service connectors",
    "Browser Automation": "Web scraping, UI testing, headless browser control",
    "Image & Creative Automation": "Image generation, asset processing, design automation",
    "Research & Scraping": "Web research, content discovery, data collection",
    "Content Writing & SEO": "SEO content, blog automation, editorial workflows",
    "Media & Transcription": "Audio/video processing, speech-to-text",
    "WordPress & CMS": "Theme/plugin dev, WP-CLI automation, CMS management",
}
INDUSTRY_EMOJI = {
    "media-publishing-systems": "🎙️",
    "finance-filings": "💼",
    "ecommerce-retail-operations": "🛒",
    "legal-ops-compliance": "⚖️",
    "healthcare-documentation-intake": "🩺",
    "product-analytics-growth-ops": "📈",
    "devrel-api-documentation": "📚",
    "customer-support-success": "🎧",
    "real-estate-workflows": "🏠",
    "education-research-workflows": "🎓",
    "gtm-revops-workflows": "📣",
    "ai-agency-operations": "🧭",
    "infrastructure-sre-incident-operations": "🛠️",
    "security-operations-grc-workflows": "🛡️",
    "data-platform-analytics-engineering": "🗄️",
}
def fetch_json(url):
    separator = "&" if "?" in url else "?"
    url = f"{url}{separator}ase_repo_gen={int(time.time())}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; ASE Repo Generator/1.0)",
        "Accept": "application/json,text/plain,*/*",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    })
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8")), dict(resp.headers)

def fmt_num(n):
    n = int(n or 0)
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n) if n else "-"

def fmt_count(n):
    """Format 1327 as 1,327 for badges."""
    return f"{n:,}"

def fmt_badge(n):
    """URL-encode comma for shields.io badge."""
    return f"{n:,}".replace(",", "%2C")

def clean_text(value):
    return html.unescape(str(value or "")).strip()

def clean_table_text(value):
    return clean_text(value).replace("|", "\\|")

def display_name(item):
    return clean_text(item.get("name") or item.get("title"))

def short_help(item, max_words=18):
    text_value = clean_text(item.get("description") or item.get("excerpt"))
    text_value = re.sub(r"\s+", " ", text_value)
    text_value = re.sub(r"[.\u2026]+$", "", text_value).strip()
    if not text_value:
        return "-"
    words = text_value.split()
    if len(words) > max_words:
        text_value = " ".join(words[:max_words]).rstrip(".,;:") + "..."
    return clean_table_text(text_value)

def has_parent_repo_stars(item):
    parent_stars = int(item.get("parent_repo_stars") or 0)
    if parent_stars:
        return True
    for key in ("is_monorepo_subdir", "monorepo_subdir", "uses_parent_repo_stars"):
        if item.get(key) is True:
            return True
    return False

def skill_stars(item):
    if has_parent_repo_stars(item):
        return "-"
    stars = item.get("github_stars")
    if stars is None or stars == "":
        return "-"
    return fmt_num(stars)

def first_label(item, *keys, fallback="—"):
    for key in keys:
        value = item.get(key)
        if isinstance(value, list) and value:
            return clean_text(value[0]) or fallback
        if isinstance(value, str) and value.strip():
            return clean_text(value)
    return fallback

def verification_label(value):
    if value == "security_reviewed":
        return "Security Reviewed"
    return "Published"

def parse_publish_timestamp(item):
    for key in ("published_at", "date", "date_gmt", "created_at", "modified_at"):
        value = item.get(key)
        if not value:
            continue
        text_value = str(value).strip()
        try:
            if text_value.endswith("Z"):
                text_value = text_value[:-1] + "+00:00"
            parsed = datetime.fromisoformat(text_value)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.timestamp()
        except ValueError:
            continue
    return 0

def repo_skill_exists(slug):
    return bool(slug) and (REPO_DIR / "skills" / slug / "SKILL.md").is_file()

def is_public_published(item):
    for key in ("status", "post_status"):
        value = str(item.get(key) or "").strip().lower()
        if value and value not in ("publish", "published", "public"):
            return False
    if item.get("hidden") is True or str(item.get("visibility") or "").strip().lower() == "hidden":
        return False
    return True

def recent_skill_rows(source_items, limit=10):
    seen = set()
    rows = []
    for item in sorted(source_items, key=parse_publish_timestamp, reverse=True):
        if not is_public_published(item):
            continue
        slug = str(item.get("slug") or "").strip()
        if not slug or slug in seen or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
            continue
        if not repo_skill_exists(slug):
            continue
        title = display_name(item)
        if not title:
            continue
        seen.add(slug)
        rows.append({
            "title": title,
            "slug": slug,
            "help": short_help(item),
            "stars": skill_stars(item),
            "category": first_label(item, "categories", "category"),
        })
        if len(rows) >= limit:
            break
    return rows

# Fetch live data
cats, _ = fetch_json(WP_CAT_URL)
cat_rows = [{"name": html.unescape(c["name"]), "slug": c["slug"], "count": int(c["count"])} for c in cats]

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

total = len(items)
sec_reviewed = sum(1 for i in items if i.get("verification") == "security_reviewed")
recent_skills = recent_skill_rows(items)

try:
    homepage_picks, _ = fetch_json(HOMEPAGE_PICKS_URL)
except Exception:
    homepage_picks = {}
skill_of_day = homepage_picks.get("skill_of_day") if isinstance(homepage_picks, dict) else None

try:
    industry_collections = json.loads(INDUSTRY_MANIFEST.read_text(encoding="utf-8")).get("collections", [])
except Exception:
    industry_collections = []
industry_count = len(industry_collections)

def featured_row(item):
    cats_list = [html.unescape(str(x)) for x in (item.get("categories") or [])]
    return {
        "title": display_name(item),
        "slug": item.get("slug") or "",
        "help": short_help(item),
        "stars": skill_stars(item),
        "cat": cats_list[0] if cats_list else "Uncategorized",
    }

# Canonical featured policy lives on ASE. The homepage-picks API exposes the
# recent-popular/diversified shelf used by the live homepage; the repo README
# should mirror that instead of reverting to raw all-time GitHub stars.
featured = []
if isinstance(homepage_picks, dict) and isinstance(homepage_picks.get("featured"), list):
    for item in homepage_picks.get("featured", [])[:10]:
        featured.append(featured_row(item))

# Fallback only: if the homepage API is unavailable, keep a deterministic local
# approximation so README generation does not fail outright.
if not featured:
    from collections import defaultdict
    tool_groups = defaultdict(list)
    for item in items:
        if int(item.get("github_stars") or 0) <= 0:
            continue
        tool = (item.get("tool_match") or "").lower()
        if not tool:
            continue
        tool_groups[tool].append(item)

    tool_best = []
    for tool, group in tool_groups.items():
        def sort_key(item, t=tool):
            title = display_name(item).lower()
            slug = item.get("slug", "").lower()
            title_match = 1 if t in title else 0
            slug_match = 1 if t in slug else 0
            return (-title_match, -slug_match, display_name(item))
        group.sort(key=sort_key)
        tool_best.append(group[0])

    tool_best.sort(key=lambda i: -int(i.get("github_stars") or 0))
    for item in tool_best:
        row = featured_row(item)
        if sum(1 for f in featured if f["cat"] == row["cat"]) >= 2:
            continue
        featured.append(row)
        if len(featured) >= 10:
            break

lines = []
lines.append('<div align="center">')
lines.append("")
lines.append("# Agent Skill Exchange")
lines.append("")
lines.append("### Curated and trusted AI agent skills")
lines.append("")
lines.append(f'[![Published](https://img.shields.io/badge/published-{fmt_badge(total)}-6366f1?style=for-the-badge)](CATALOG.md)')
lines.append(f'[![Industry%20Collections](https://img.shields.io/badge/industry--collections-{industry_count}-14b8a6?style=for-the-badge)](industries/README.md)')
lines.append(f'[![Categories](https://img.shields.io/badge/categories-{len(cat_rows)}-0ea5e9?style=for-the-badge)](categories/README.md)')
lines.append(f'[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-{fmt_badge(sec_reviewed)}-10b981?style=for-the-badge)](verification/)')
lines.append('[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)')
lines.append("")
lines.append("**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**")
lines.append("")
lines.append(f"*{fmt_count(total)} published skills · {industry_count} Industry Collections · {len(cat_rows)} categories · Real ecosystem signals · Updated daily*")
lines.append("")
lines.append("</div>")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## What is this?")
lines.append("")
lines.append("An open, curated catalog of trusted reusable skills for AI agents, not a generic dump. Each skill wraps a real tool, API, or workflow into a format that agents and runtimes like OpenClaw, Claude Code, Codex, Gemini, Cursor, MCP clients, LangChain, OpenAI Agents, Hermes, and custom agent workflows can install and use.")
lines.append("")
lines.append("Every skill is backed by a real upstream project — a GitHub repo, npm package, or documented API. No synthetic entries.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Quick Start")
lines.append("")
lines.append("```bash")
lines.append("# OpenClaw native install")
lines.append("clawhub install <slug>")
lines.append("")
lines.append("# Manual install for other agents")
lines.append("git clone https://github.com/agentskillexchange/skills.git")
lines.append("cp -R skills/skills/<slug> ~/.agent-skills/<slug>")
lines.append("```")
lines.append("")
lines.append("### Optional Third-Party Installer")
lines.append("")
lines.append("The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:")
lines.append("")
lines.append("```bash")
lines.append("npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill <slug>")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Skill of the Day")
lines.append("")
if skill_of_day:
    title = display_name(skill_of_day)
    slug = skill_of_day.get("slug") or ""
    description = clean_text(skill_of_day.get("description"))
    link = f"skills/{slug}/"
    lines.append(f"**[{title}]({link})** — {description}")
    lines.append("")
    lines.append("_Rotates daily across downloaded, starred, recent, verified, and industry-curated skills._")
else:
    lines.append("Daily featured skill data was unavailable during generation.")
lines.append("")
lines.append("---")
lines.append("")
if industry_collections:
    lines.append("## Industry Collections")
    lines.append("")
    lines.append("Curated skill sets organized by industry vertical:")
    lines.append("")
    lines.append("| | Collection | Description |")
    lines.append("|---|---|---|")
    for collection in industry_collections:
        slug = collection.get("slug", "")
        emoji = INDUSTRY_EMOJI.get(slug, "📦")
        title = clean_text(collection.get("title"))
        description = clean_text(collection.get("description"))
        lines.append(f"| {emoji} | [**{title}**](industries/{slug}.md) | {description} |")
    lines.append("")
    lines.append("See the full overlay index in [industries/README.md](industries/README.md).")
    lines.append("")
    lines.append("---")
    lines.append("")
lines.append("## Recently Published Skills")
lines.append("")
lines.append("| Skill | What it helps with | Stars | Category |")
lines.append("|---|---|---:|---|")
for item in recent_skills:
    lines.append(f"| [{clean_table_text(item['title'])}](skills/{item['slug']}/) | {item['help']} | {item['stars']} | {clean_table_text(item['category'])} |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Featured Skills")
lines.append("")
lines.append("Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.")
lines.append("")
lines.append("| Skill | What it helps with | Stars | Category |")
lines.append("|---|---|---:|---|")
for f in featured:
    lines.append(f"| [{clean_table_text(f['title'])}](skills/{f['slug']}/) | {f['help']} | {f['stars']} | {clean_table_text(f['cat'])} |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Categories")
lines.append("")
lines.append("| | Category | Skills | What's inside |")
lines.append("|---|---|---:|---|")
for cat in cat_rows:
    emoji = CAT_EMOJI.get(cat["name"], "📦")
    short = CAT_SHORT.get(cat["name"], "Skills in this category")
    lines.append(f'| {emoji} | [**{cat["name"]}**](categories/{cat["slug"]}/) | {cat["count"]} | {short} |')
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Browse The Catalog")
lines.append("")
lines.append("| | View | What you'll find |")
lines.append("|---|---|---|")
lines.append("| 🧭 | [**Live Browse**](https://agentskillexchange.com/browse-skills/) | Search, filters, skill detail panels, and install links on agentskillexchange.com |")
lines.append("| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |")
lines.append("| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |")
lines.append("| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, sorted by category and stars |")
lines.append("| 🔌 | [**JSON Index**](skills.json) | Machine-readable catalog for programmatic access |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Programmatic Access")
lines.append("")
lines.append("### JSON Index")
lines.append("")
lines.append("[`skills.json`](skills.json) contains every skill with metadata and signals:")
lines.append("")
lines.append("```json")
lines.append('{')
lines.append('  "name": "Playwright MCP Browser Automation",')
lines.append('  "slug": "playwright-mcp-browser-automation",')
lines.append('  "title": "Playwright MCP Browser Automation",')
lines.append('  "description": "Official Playwright-powered browser control for agent workflows.",')
lines.append('  "category": ["Browser Automation"],')
lines.append('  "framework": ["Claude Code", "Cursor", "MCP", "OpenClaw"],')
lines.append('  "verification": "security_reviewed",')
lines.append('  "signals": {')
lines.append('    "tool": "playwright",')
lines.append('    "github_stars": 84874,')
lines.append('    "npm_weekly_downloads": 39806814,')
lines.append('    "license": "Apache-2.0"')
lines.append('  }')
lines.append('}')
lines.append("```")
lines.append("")
lines.append("### Optional Third-Party Installer")
lines.append("")
lines.append("The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:")
lines.append("")
lines.append("```bash")
lines.append("# List all skills")
lines.append("npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --list")
lines.append("")
lines.append("# Search")
lines.append("npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --search kubernetes")
lines.append("")
lines.append("# Install")
lines.append("npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill <slug> -a <agent>")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Trust & Safety")
lines.append("")
lines.append("Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.")
lines.append("")
lines.append("| Tier | Count | Meaning |")
lines.append("|------|------:|---|")
lines.append(f'| 📋 **Published** | {fmt_count(total)} | In the catalog — every skill is backed by a real tool, repo, or package |')
lines.append(f'| 🛡️ **Security Reviewed** | {fmt_count(sec_reviewed)} | Scanned for malicious patterns, prompt injection, and unsafe instructions |')
lines.append("")
lines.append("More: [verification/](verification/)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Submit a Skill")
lines.append("")
lines.append("Two ways to add a skill:")
lines.append("")
lines.append("### Option 1: Pull Request")
lines.append("")
lines.append("1. Fork this repo")
lines.append("2. Copy `template/SKILL.md` to `skills/your-skill-slug/SKILL.md`")
lines.append("3. Fill in the frontmatter and content (see [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md))")
lines.append("4. Open a PR")
lines.append("")
lines.append("Requirements:")
lines.append("- Skill must wrap a real, existing tool (GitHub repo, npm package, documented API)")
lines.append("- Content must be 100+ words with real technical detail")
lines.append("- Must fit an existing category and framework")
lines.append("")
lines.append("### Option 2: Create Skill Wizard")
lines.append("")
lines.append(f"Use [agentskillexchange.com/create-skill]({SITE_BASE}/create-skill/) to generate a repo-ready `SKILL.md`, then open a pull request with the generated file.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Skill Format")
lines.append("")
lines.append("Each skill is a directory with a `SKILL.md`:")
lines.append("")
lines.append("```")
lines.append("skills/")
lines.append("  playwright-mcp-browser-automation/")
lines.append("    SKILL.md")
lines.append("```")
lines.append("")
lines.append("See the [full spec](spec/SKILL_SPEC.md) and [template](template/SKILL.md).")
lines.append("")
lines.append("---")
lines.append("")
lines.append('<div align="center">')
lines.append("")
lines.append(f"*[agentskillexchange.com]({SITE_BASE}/)*")
lines.append("")
lines.append("</div>")
lines.append("")

(REPO_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Generated README.md — {total} published, {sec_reviewed} security reviewed, {len(cat_rows)} categories.")
PYEOF
