<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-1%2C534-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-1%2C503-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*1,534 published skills · 17 categories · Real ecosystem signals · Updated hourly*

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
| [Excalidraw Virtual Whiteboard and Diagram SDK](skills/excalidraw-virtual-whiteboard-diagram-sdk/) | excalidraw | 119.9k | Image & Creative Automation |
| [llama.cpp Portable LLM Inference Engine in C/C++](skills/llama-cpp-portable-llm-inference/) | llama.cpp | 100.3k | Developer Tools |
| [Immich Self-Hosted Photo and Video Management Platform](skills/immich-photo-video-management-platform/) | immich | 96k | Media & Transcription |
| [Puppeteer Browser Automation Library for Chrome and Firefox](skills/puppeteer-browser-automation-library-for-chrome-and-firefox/) | puppeteer | 94k | Browser Automation |
| [MarkItDown Document-to-Markdown Converter by Microsoft](skills/markitdown-document-to-markdown-converter-microsoft/) | markitdown | 92.9k | Data Extraction & Transformation |
| [Hugo Fast Static Site Generator and CMS Framework](skills/hugo-static-site-generator-cms-framework/) | hugo | 87.4k | WordPress & CMS |
| [Playwright Cross-Browser Testing and Automation Framework](skills/playwright-cross-browser-testing-and-automation-framework/) | playwright | 85.3k | Browser Automation |
| [vLLM High-Throughput LLM Serving Engine with PagedAttention](skills/vllm-high-throughput-llm-serving/) | vllm | 74.8k | Developer Tools |
| [PaddleOCR Multilingual Document OCR and Structured Data Toolkit](skills/paddleocr-multilingual-document-ocr-toolkit/) | paddleocr | 73.7k | Data Extraction & Transformation |
| [NocoDB Self-Hosted No-Code Database Platform with REST API](skills/nocodb-self-hosted-no-code-database-rest-api/) | nocodb | 62.6k | Integrations & Connectors |
| [Rclone Cloud Storage Sync and Management CLI](skills/rclone-cloud-storage-sync-management-cli/) | rclone | 56.4k | Integrations & Connectors |
| [Typst Markup-Based Document Typesetting System](skills/typst-markup-typesetting-system/) | typst | 52.4k | Content Writing & SEO |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 178 | CLI tools, scaffolders, dev environment setup |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 142 | Pipeline configs, deployment automation, build tooling |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 115 | ETL pipelines, parsing, format conversion |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 113 | Incident response, troubleshooting, system diagnostics |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 102 | Vulnerability scanning, auth setup, compliance |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 95 | SDK docs, API parsers, symbol resolvers |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 91 | Linting, code review, test generators, coverage |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 90 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 77 | Email automation, calendar management, task coordination |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 71 | Audio/video processing, speech-to-text |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 67 | Web research, content discovery, data collection |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 67 | Scaffolders, boilerplate generators, workflow templates |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 66 | Image generation, asset processing, design automation |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 64 | Third-party API bridges, webhooks, service connectors |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 64 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 63 | Web scraping, UI testing, headless browser control |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 59 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 1,534 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 1,503 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
