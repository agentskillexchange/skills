#!/usr/bin/env bash
# generate-readme.sh — Regenerate README.md from live ASE data
# Usage: ./generate-readme.sh [output_dir]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="${1:-$(dirname "$SCRIPT_DIR")}"

python3 - "$REPO_DIR" << 'PYEOF'
import datetime
import html
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO_DIR = Path(sys.argv[1])
BROWSE_BASE = "https://agentskillexchange.com/wp-json/ase-marketplace/v1/browse"
WP_CAT_URL = "https://agentskillexchange.com/wp-json/wp/v2/skill_category?per_page=100&orderby=count&order=desc"

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
    """Format 1327 as 1,327 for badges."""
    return f"{n:,}"

def fmt_badge(n):
    """URL-encode comma for shields.io badge."""
    return f"{n:,}".replace(",", "%2C")

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

# Pick featured skills: highest-starred, one per tool, max 2 per category
# Use title-relevance tiebreaker (matches homepage PHP and top-lists generator)
from collections import defaultdict
tool_groups = defaultdict(list)
for item in items:
    if int(item.get("github_stars") or 0) <= 0:
        continue
    tool = (item.get("tool_match") or "").lower()
    if not tool:
        continue
    tool_groups[tool].append(item)

# Pick best representative per tool (title contains tool name > slug contains > alphabetical)
tool_best = []
for tool, group in tool_groups.items():
    def sort_key(item, t=tool):
        title = item.get("title", "").lower()
        slug = item.get("slug", "").lower()
        title_match = 1 if t in title else 0
        slug_match = 1 if t in slug else 0
        return (-title_match, -slug_match, item.get("title", ""))
    group.sort(key=sort_key)
    tool_best.append(group[0])

# Sort by stars descending, then apply category diversity (max 2 per cat)
tool_best.sort(key=lambda i: -int(i.get("github_stars") or 0))
featured = []
for item in tool_best:
    cats_list = item.get("categories", [])
    cat = cats_list[0] if cats_list else "Uncategorized"
    if sum(1 for f in featured if f["cat"] == cat) >= 2:
        continue
    featured.append({"title": item["title"], "slug": item["slug"], "tool": item.get("tool_match") or (item.get("tool_match") or item.get("slug", "")).lower(), "stars": int(item.get("github_stars") or 0), "cat": cat})
    if len(featured) >= 12:
        break

start_here = [
    {
        "title": "New to Agent Skills",
        "desc": "Start with a plain-English explanation, then browse a few strong examples so the idea clicks fast.",
        "link": "https://agentskillexchange.com/what-are-ai-agent-skills-plain-english-guide/",
        "cta": "Read the intro guide",
    },
    {
        "title": "Useful Right Away",
        "desc": "Jump into practical skills for research, writing, browser work, and everyday operator tasks.",
        "link": "TOP-DOWNLOADS.md",
        "cta": "See practical picks",
    },
    {
        "title": "Show Me the Heavy Hitters",
        "desc": "Browse standout skills with stronger ecosystem signal and more obvious wow factor.",
        "link": "TOP-STARS.md",
        "cta": "Browse standout skills",
    },
]

skill_of_day_pool = featured[:]
if not skill_of_day_pool:
    skill_of_day_pool = [
        {
            "title": item.get("title", "Untitled Skill"),
            "slug": item.get("slug", ""),
            "tool": item.get("tool_match") or item.get("slug", ""),
            "stars": int(item.get("github_stars") or 0),
            "cat": (item.get("categories") or ["Uncategorized"])[0],
        }
        for item in items[:12]
    ]

today_index = datetime.datetime.now(datetime.timezone.utc).timetuple().tm_yday % max(len(skill_of_day_pool), 1)
skill_of_day = skill_of_day_pool[today_index] if skill_of_day_pool else None

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
lines.append("**[What is an Agent Skill?](#what-is-an-agent-skill) · [Start Here](#start-here) · [Skill of the Day](#skill-of-the-day) · [Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md)**")
lines.append("")
lines.append(f"*{fmt_count(total)} published skills · {len(cat_rows)} categories · Real ecosystem signals · Updated hourly*")
lines.append("")
lines.append("</div>")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## What is an Agent Skill?")
lines.append("")
lines.append("An Agent Skill is a reusable capability for a specific job. It gives an agent the workflow shape, references, and boundaries needed to do the work well, without reinventing the task from scratch every time.")
lines.append("")
lines.append("In practical terms, a skill turns a vague request into something more dependable: a real workflow wrapped around a tool, API, or repeatable operating pattern.")
lines.append("")
lines.append("Read more: [What Are AI Agent Skills? A Plain-English Guide](https://agentskillexchange.com/what-are-ai-agent-skills-plain-english-guide/)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Start Here")
lines.append("")
lines.append("| Path | Why start here | Link |")
lines.append("|---|---|---|")
for row in start_here:
    lines.append(f"| **{row['title']}** | {row['desc']} | [{row['cta']}]({row['link']}) |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Skill of the Day")
lines.append("")
if skill_of_day:
    lines.append(f"[**{skill_of_day['title']}**](skills/{skill_of_day['slug']}/)")
    lines.append("")
    lines.append(f"Tool: `{skill_of_day['tool']}`  ")
    lines.append(f"Category: **{skill_of_day['cat']}**  ")
    lines.append(f"GitHub stars: **{fmt_num(skill_of_day['stars'])}**")
    lines.append("")
    lines.append("A rotating daily pick to make the repo feel alive, not frozen.")
    lines.append("")
lines.append("---")
lines.append("")
lines.append("## Quick Start")
lines.append("")
lines.append("```bash")
lines.append("# Install any skill")
lines.append("npx skills add agentskillexchange/skills --skill <slug>")
lines.append("")
lines.append("# For a specific agent")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a claude-code")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a cursor")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a codex")
lines.append("")
lines.append("# OpenClaw")
lines.append("clawhub install <slug>")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Featured Skills")
lines.append("")
lines.append("A hand-picked selection across categories. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for full rankings.")
lines.append("")
lines.append("| Skill | Tool | ⭐ Stars | Category |")
lines.append("|-------|------|--------:|----------|")
for f in featured:
    lines.append(f"| [{f['title']}](skills/{f['slug']}/) | {f['tool']} | {fmt_num(f['stars'])} | {f['cat']} |")
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
lines.append("## Programmatic Access")
lines.append("")
lines.append("### JSON Index")
lines.append("")
lines.append("[`skills.json`](skills.json) contains every skill with metadata and signals:")
lines.append("")
lines.append("```json")
lines.append('{')
lines.append('  "slug": "playwright-mcp-browser-automation",')
lines.append('  "name": "Playwright MCP Browser Automation",')
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
lines.append("### npx CLI")
lines.append("")
lines.append("```bash")
lines.append("# List all skills")
lines.append("npx skills add agentskillexchange/skills --list")
lines.append("")
lines.append("# Search")
lines.append("npx skills add agentskillexchange/skills --search kubernetes")
lines.append("")
lines.append("# Install")
lines.append("npx skills add agentskillexchange/skills --skill <slug> -a <agent>")
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
lines.append("### Option 2: Web Submission")
lines.append("")
lines.append("Submit through [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) — auto-synced to this repo hourly.")
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
lines.append("*[agentskillexchange.com](https://agentskillexchange.com/)*")
lines.append("")
lines.append("</div>")
lines.append("")

(REPO_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Generated README.md — {total} published, {sec_reviewed} security reviewed, {len(cat_rows)} categories.")
PYEOF
