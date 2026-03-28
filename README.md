<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-1%2C418-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-1%2C382-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*1,418 published skills · 17 categories · Real ecosystem signals · Updated hourly*

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
| [Decap CMS Git-Based Content Management for Static Sites](skills/decap-cms-git-based-content-management-static-sites/) | react | 244.2k | WordPress & CMS |
| [Trafilatura Web Text Extraction and Crawling Toolkit](skills/trafilatura-web-text-extraction-crawling/) | huggingface | 158.5k | Research & Scraping |
| [K9s Kubernetes Terminal Dashboard](skills/k9s-kubernetes-terminal-dashboard/) | kubernetes | 121.4k | Developer Tools |
| [commitlint Conventional Commit Message Linter](skills/commitlint-conventional-commit-message-linter/) | angular | 100.1k | Code Quality & Review |
| [Supabase MCP Server for Database and Project Management](skills/supabase-mcp-server-database-project-management/) | supabase | 99.7k | Integrations & Connectors |
| [Coqui TTS Deep Learning Text-to-Speech Toolkit](skills/coqui-tts-deep-learning-text-to-speech-toolkit/) | pytorch | 98.6k | Media & Transcription |
| [WhisperX Speech Recognition with Word-Level Timestamps and Diarization](skills/whisperx-speech-recognition-timestamps-diarization/) | whisper | 96.7k | Media & Transcription |
| [FastMCP Python MCP Server and Client Framework](skills/fastmcp-python-mcp-server-client-framework/) | fastapi | 96.6k | Developer Tools |
| [Browser Session Replay Analyzer](skills/browser-session-replay-analyzer/) | puppeteer | 93.9k | Browser Automation |
| [Figma Design Token Extractor](skills/figma-design-token-extractor-3/) | storybook | 89.6k | Image & Creative Automation |
| [Lightpanda Headless Browser for AI Automation](skills/lightpanda-headless-browser-ai-automation/) | playwright | 85.1k | Browser Automation |
| [Elastic APM Transaction Anomaly Spotter](skills/elastic-apm-transaction-anomaly-spotter/) | elasticsearch | 76.4k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 153 | CLI tools, scaffolders, dev environment setup |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 140 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 113 | Incident response, troubleshooting, system diagnostics |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 104 | ETL pipelines, parsing, format conversion |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 99 | Vulnerability scanning, auth setup, compliance |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 94 | SDK docs, API parsers, symbol resolvers |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 89 | Linting, code review, test generators, coverage |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 85 | Metrics, alerting rules, observability |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 66 | Scaffolders, boilerplate generators, workflow templates |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 64 | Email automation, calendar management, task coordination |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 62 | Audio/video processing, speech-to-text |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 61 | Web research, content discovery, data collection |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 60 | Third-party API bridges, webhooks, service connectors |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 60 | Image generation, asset processing, design automation |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 57 | Web scraping, UI testing, headless browser control |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 55 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 52 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 1,418 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 1,382 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
