#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"
python3 - "$REPO_DIR" << 'PYEOF'
import datetime as dt
import html
import json
import math
import sys
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
BROWSE_BASE = "https://agentskillexchange.com/wp-json/ase-marketplace/v1/browse"
HOMEPAGE_PICKS_URL = "https://agentskillexchange.com/wp-json/ase-marketplace/v1/homepage-picks"
WP_CAT_URL = "https://agentskillexchange.com/wp-json/wp/v2/skill_category?per_page=100&orderby=count&order=desc"
INDUSTRY_MANIFEST = REPO_DIR / "scripts" / "industry-collections.json"
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
}
INDUSTRY_STAGE = {
    "wave-1": "Wave 1",
    "wave-2": "Wave 2",
    "wave-3": "Wave 3",
    "wave-4": "Wave 4",
    "pilot": "Pilot",
    "planned": "Planned",
}
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

def fmt_count(n):
    return f"{n:,}"

def fmt_badge(n):
    return f"{n:,}".replace(",", "%2C")

cats, _ = fetch_json(WP_CAT_URL)
cat_rows = [{"name": html.unescape(c["name"]), "slug": c["slug"], "count": int(c["count"])} for c in cats]
industry_manifest = json.loads(INDUSTRY_MANIFEST.read_text(encoding="utf-8"))
industry_rows = industry_manifest.get("collections") or []
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

def parse_dt(value):
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(str(value).replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except Exception:
        return None


def recent_popular_components(item):
    now = dt.datetime.now(dt.timezone.utc)
    published_at = parse_dt(item.get("date")) or now
    days_old = max(0, (now - published_at).days)
    recency_score = max(0, 45 - min(days_old, 45)) * 120
    weekly_views = int(item.get("views_weekly") or 0)
    stars = int(item.get("github_stars") or 0)
    downloads = int(item.get("npm_downloads") or item.get("npm_weekly_downloads") or 0)
    trust_score = 900 if item.get("verification") == "security_reviewed" else 350 if item.get("verification") == "verified_metadata" else 0
    view_score = min(2400, weekly_views * 80)
    star_score = min(1800, int(math.log(stars + 1) * 180)) if stars > 0 else 0
    download_score = min(1600, int(math.log(downloads + 1) * 160)) if downloads > 0 else 0
    return {
        "score": recency_score + view_score + star_score + download_score + trust_score,
        "days_old": days_old,
        "views_weekly": weekly_views,
        "stars": stars,
        "downloads": downloads,
    }


def recent_popular_sort_key(item):
    rp = item["_recent_popular"]
    return (-rp["score"], -rp["views_weekly"], rp["days_old"], -rp["stars"], -rp["downloads"], item.get("title", "").lower())


def build_recent_popular_picks(items, limit=12, max_per_category=2):
    picks = []
    seen_tools = set()
    cat_counts = {}
    ranked = sorted(items, key=recent_popular_sort_key)
    for item in ranked:
        tool = (item.get("tool_match") or item.get("slug") or "").strip().lower()
        if not tool or tool in seen_tools:
            continue
        cat = (item.get("categories") or ["Uncategorized"])[0]
        if cat_counts.get(cat, 0) >= max_per_category:
            continue
        seen_tools.add(tool)
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
        picks.append(item)
        if len(picks) >= limit:
            return picks
    if len(picks) < limit:
        for item in ranked:
            tool = (item.get("tool_match") or item.get("slug") or "").strip().lower()
            if not tool or tool in seen_tools:
                continue
            seen_tools.add(tool)
            picks.append(item)
            if len(picks) >= limit:
                break
    return picks


for item in items:
    item["_recent_popular"] = recent_popular_components(item)

pool = build_recent_popular_picks(items, limit=60)
if not pool:
    pool = sorted(items, key=lambda i: i.get("title", "").lower())
day_index = dt.datetime.now(dt.timezone.utc).timetuple().tm_yday - 1
skill = pool[day_index % len(pool)] if pool else None
featured = build_recent_popular_picks(items, limit=12)

# Prefer the live site's canonical homepage picks when available so README never drifts
# from ASE's rendered Skill of the Day. The local algorithm above is the fallback.
try:
    homepage_picks, _ = fetch_json(HOMEPAGE_PICKS_URL)
    if homepage_picks.get("skill_of_day"):
        skill = homepage_picks["skill_of_day"]
    if homepage_picks.get("featured"):
        featured = homepage_picks["featured"]
except Exception:
    pass

lines = []
lines.append('<div align="center">')
lines.append("")
lines.append("# Agent Skill Exchange")
lines.append("")
lines.append("### The open catalog of AI agent skills")
lines.append("")
lines.append(f'[![Published](https://img.shields.io/badge/published-{fmt_badge(total)}-6366f1?style=for-the-badge)](skills/)')
lines.append(f'[![Categories](https://img.shields.io/badge/categories-{len(cat_rows)}-0ea5e9?style=for-the-badge)](categories/)')
lines.append(f'[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-{fmt_badge(sec_reviewed)}-10b981?style=for-the-badge)](verification/)')
lines.append('[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)')
lines.append("")
lines.append("**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**")
lines.append("")
lines.append(f"*{fmt_count(total)} published skills · {len(cat_rows)} categories · Real ecosystem signals · Updated hourly*")
lines.append("")
lines.append("</div>")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## What is an Agent Skill")
lines.append("")
lines.append("An agent skill is a reusable capability package for AI coding agents. Each entry here wraps a real tool, API, or workflow into a format agents like Claude Code, Cursor, Codex, and OpenClaw can install and use.")
lines.append("")
lines.append("Every published skill is backed by a real upstream project or documented integration. No synthetic filler, no fake repo stars, no proxy download theater.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Start Here")
lines.append("")
lines.append("```bash")
lines.append("# Install any skill")
lines.append("npx skills add agentskillexchange/skills --skill <slug>")
lines.append("")
lines.append("# Target a specific agent")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a claude-code")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a cursor")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a codex")
lines.append("")
lines.append("# OpenClaw")
lines.append("clawhub install <slug>")
lines.append("```")
lines.append("")
lines.append("- Browse by category in [categories/](categories/)")
lines.append("- See strong signals in [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md)")
lines.append("- Use [CATALOG.md](CATALOG.md) for the full human-readable index")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Skill of the Day")
lines.append("")
if skill:
    cats_list = skill.get("categories") or ["Uncategorized"]
    frameworks = skill.get("frameworks") or []
    tool = skill.get("tool_match") or skill.get("slug") or "tool"
    lines.append(f"### [{skill['title']}](skills/{skill['slug']}/)")
    lines.append("")
    lines.append(skill.get("description") or "")
    lines.append("")
    lines.append(f"- Tool: `{tool}`")
    lines.append(f"- Category: {cats_list[0]}")
    if frameworks:
        lines.append(f"- Frameworks: {', '.join(frameworks[:6])}")
    if int(skill.get("github_stars") or 0) > 0:
        lines.append(f"- GitHub stars: {fmt_count(int(skill.get('github_stars') or 0))}")
    if int(skill.get("npm_weekly_downloads") or 0) > 0:
        lines.append(f"- npm weekly downloads: {fmt_count(int(skill.get('npm_weekly_downloads') or 0))}")
    lines.append(f"- Listing: https://agentskillexchange.com/skills/{skill['slug']}/")
else:
    lines.append("No featured skill was available for today's rotation.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Featured Skills")
lines.append("")
lines.append("A strong cross-section of high-signal skills across the catalog.")
lines.append("")
lines.append("| Skill | Tool | ⭐ Stars | Category |")
lines.append("|-------|------|--------:|----------|")
for f in featured:
    cat = (f.get("categories") or ["Uncategorized"])[0]
    tool = f.get("tool_match") or f.get("slug") or "tool"
    lines.append(f"| [{f['title']}](skills/{f['slug']}/) | {tool} | {fmt_num(int(f.get('github_stars') or 0))} | {cat} |")
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
lines.append("## Industry Collections")
lines.append("")
lines.append("Curated editorial overlays for teams that want repo navigation by real workflow clusters without replacing the core category taxonomy.")
lines.append("")
lines.append("| | Collection | Stage | What you'll find |")
lines.append("|---|---|---|---|")
for collection in industry_rows:
    emoji = INDUSTRY_EMOJI.get(collection["slug"], "📦")
    stage = INDUSTRY_STAGE.get((collection.get("launch_stage") or "planned").lower(), (collection.get("launch_stage") or "planned").replace("-", " ").title())
    summary = collection.get("description", "").strip().rstrip(".")
    lines.append(f'| {emoji} | [**{collection["title"]}**](industries/{collection["slug"]}.md) | {stage} | {summary} |')
lines.append("")
lines.append("See the full overlay index in [industries/README.md](industries/README.md).")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Browse")
lines.append("")
lines.append("| | View | What you'll find |")
lines.append("|---|---|---|")
lines.append("| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |")
lines.append("| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |")
lines.append("| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, sorted by category and stars |")
lines.append("| 🔌 | [**JSON Index**](skills.json) | Machine-readable catalog for programmatic access |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Trust & Safety")
lines.append("")
lines.append("Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.")
lines.append("")
lines.append("| Tier | Count | Meaning |")
lines.append("|------|------:|---|")
lines.append(f'| 📋 **Published** | {fmt_count(total)} | In the catalog, every skill is backed by a real tool, repo, or package |')
lines.append(f'| 🛡️ **Security Reviewed** | {fmt_count(sec_reviewed)} | Scanned for malicious patterns, prompt injection, and unsafe instructions |')
lines.append("")
lines.append("More: [verification/](verification/)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Submit a Skill")
lines.append("")
lines.append("1. Fork this repo and add a `skills/<slug>/SKILL.md` entry, or")
lines.append("2. Submit through [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) for hourly sync")
lines.append("")
lines.append("---")
lines.append("")
lines.append("<div align=\"center\">")
lines.append("")
lines.append("*[agentskillexchange.com](https://agentskillexchange.com/)*")
lines.append("")
lines.append("</div>")
(REPO_DIR / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
PYEOF
