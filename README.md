<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-1%2C724-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-1%2C669-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*1,724 published skills · 17 categories · Real ecosystem signals · Updated hourly*

</div>

---

## What is this?

An open, machine-readable catalog of reusable skills for AI coding agents. Each skill wraps a real tool, API, or workflow into a format that agents like Claude Code, Cursor, Codex, and OpenClaw can install and use.

Every skill is backed by a real upstream project — a GitHub repo, npm package, or documented API. No synthetic entries.

---

## Quick Start

```bash
# Install any skill
npx skills add agentskillexchange/skills --skill <slug>

# For a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code
npx skills add agentskillexchange/skills --skill <slug> -a cursor
npx skills add agentskillexchange/skills --skill <slug> -a codex

# OpenClaw
clawhub install <slug>
```

---

## Featured Skills

A hand-picked selection across categories. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for full rankings.

| Skill | Tool | ⭐ Stars | Category |
|-------|------|--------:|----------|
| [yt-dlp Feature-Rich Audio and Video Downloader CLI](skills/yt-dlp-feature-rich-audio-video-downloader-cli/) | yt-dlp | 154.3k | Media & Transcription |
| [Kubernetes Events API CrashLoop Investigator](skills/kubernetes-events-api-crashloop-investigator/) | kubernetes | 121.4k | Runbooks & Diagnostics |
| [Excalidraw Virtual Whiteboard and Diagram SDK](skills/excalidraw-virtual-whiteboard-diagram-sdk/) | excalidraw | 119.9k | Image & Creative Automation |
| [llama.cpp Portable LLM Inference Engine in C/C++](skills/llama-cpp-portable-llm-inference/) | llama.cpp | 100.9k | Developer Tools |
| [Podcast RSS Feed Transcriber](skills/podcast-rss-feed-transcriber/) | whisper | 97.1k | Media & Transcription |
| [Puppeteer Browser Automation Library for Chrome and Firefox](skills/puppeteer-browser-automation-library-for-chrome-and-firefox/) | puppeteer | 94k | Browser Automation |
| [MarkItDown Document-to-Markdown Converter by Microsoft](skills/markitdown-document-to-markdown-converter-microsoft/) | markitdown | 93.2k | Data Extraction & Transformation |
| [Hugo Fast Static Site Generator and CMS Framework](skills/hugo-static-site-generator-cms-framework/) | hugo | 87.4k | WordPress & CMS |
| [Playwright Cross-Browser Testing and Automation Framework](skills/playwright-cross-browser-testing-and-automation-framework/) | playwright | 85.5k | Browser Automation |
| [PostgreSQL MCP Server](skills/postgresql-mcp-server/) | servers | 82.7k | Data Extraction & Transformation |
| [uv Ultra-Fast Python Package and Project Manager](skills/uv-ultra-fast-python-package-project-manager/) | uv | 82.4k | Developer Tools |
| [ElasticSearch Cluster Vitals Agent](skills/elasticsearch-cluster-vitals-agent/) | elasticsearch | 76.4k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 240 | CLI tools, scaffolders, dev environment setup |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 146 | Pipeline configs, deployment automation, build tooling |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 126 | ETL pipelines, parsing, format conversion |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 117 | Vulnerability scanning, auth setup, compliance |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 114 | Incident response, troubleshooting, system diagnostics |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 103 | SDK docs, API parsers, symbol resolvers |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 102 | Metrics, alerting rules, observability |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 96 | Linting, code review, test generators, coverage |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 94 | Email automation, calendar management, task coordination |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 82 | Third-party API bridges, webhooks, service connectors |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 76 | Image generation, asset processing, design automation |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 76 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 75 | Audio/video processing, speech-to-text |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 74 | Scaffolders, boilerplate generators, workflow templates |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 72 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 70 | Web scraping, UI testing, headless browser control |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 62 | SEO content, blog automation, editorial workflows |

---

## Browse

| | View | What you'll find |
|---|---|---|
| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |
| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |
| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, sorted by category and stars |
| 🔌 | [**JSON Index**](skills.json) | Machine-readable catalog for programmatic access |

---

## Programmatic Access

### JSON Index

[`skills.json`](skills.json) contains every skill with metadata and signals:

```json
{
  "slug": "playwright-mcp-browser-automation",
  "name": "Playwright MCP Browser Automation",
  "description": "Official Playwright-powered browser control for agent workflows.",
  "category": ["Browser Automation"],
  "framework": ["Claude Code", "Cursor", "MCP", "OpenClaw"],
  "verification": "security_reviewed",
  "signals": {
    "tool": "playwright",
    "github_stars": 84874,
    "npm_weekly_downloads": 39806814,
    "license": "Apache-2.0"
  }
}
```

### npx CLI

```bash
# List all skills
npx skills add agentskillexchange/skills --list

# Search
npx skills add agentskillexchange/skills --search kubernetes

# Install
npx skills add agentskillexchange/skills --skill <slug> -a <agent>
```

---

## Trust & Safety

Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.

| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Published** | 1,724 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 1,669 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

More: [verification/](verification/)

---

## Submit a Skill

Two ways to add a skill:

### Option 1: Pull Request

1. Fork this repo
2. Copy `template/SKILL.md` to `skills/your-skill-slug/SKILL.md`
3. Fill in the frontmatter and content (see [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md))
4. Open a PR

Requirements:
- Skill must wrap a real, existing tool (GitHub repo, npm package, documented API)
- Content must be 100+ words with real technical detail
- Must fit an existing category and framework

### Option 2: Web Submission

Submit through [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) — auto-synced to this repo hourly.

---

## Skill Format

Each skill is a directory with a `SKILL.md`:

```
skills/
  playwright-mcp-browser-automation/
    SKILL.md
```

See the [full spec](spec/SKILL_SPEC.md) and [template](template/SKILL.md).

---

<div align="center">

*[agentskillexchange.com](https://agentskillexchange.com/)*

</div>
