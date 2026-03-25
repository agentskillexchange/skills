<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Skills](https://img.shields.io/badge/skills-1%2C100%2B-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-1%2C100-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*1,100+ skills · 17 categories · Real ecosystem signals · Updated hourly*

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
| [Supabase MCP Server](skills/supabase-mcp-server/) | supabase | 99.5k | Developer Tools |
| [Kubernetes CrashLoop Investigator](skills/kubernetes-events-api-crashloop-investigator/) | kubernetes | 121.3k | Runbooks & Diagnostics |
| [Playwright Browser Automation](skills/playwright-mcp-browser-automation/) | playwright | 84.9k | Browser Automation |
| [Grafana OnCall Escalation Manager](skills/grafana-oncall-escalation-chain-manager/) | grafana | 72.8k | Monitoring & Alerts |
| [Podcast RSS Feed Transcriber](skills/podcast-rss-feed-transcriber/) | whisper | 96.5k | Media & Transcription |
| [OpenAPI Spec Compliance Checker](skills/openapi-spec-compliance-checker/) | fastapi | 96.5k | Library & API Reference |
| [Cypress Network Stub Generator](skills/cypress-network-stub-generator/) | cypress | 49.6k | Browser Automation |
| [SerpAPI Search Aggregator](skills/serpapi-search-aggregator/) | redis | 73.5k | Research & Scraping |
| [WordPress Content Publisher](skills/wordpress-content-publisher/) | wordpress | 21.0k | WordPress & CMS |
| [Datadog MCP Server](skills/datadog-mcp-server/) | datadog | 7.4k | Monitoring & Alerts |
| [Sentry Issue Spike Detection](skills/sentry-issue-spike-detection-agent/) | sentry | 45.9k | Monitoring & Alerts |
| [Snyk Agent Scan](skills/snyk-agent-scan/) | snyk | 4.9k | Security & Verification |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 144 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 122 | Incident response, troubleshooting, system diagnostics |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 120 | CLI helpers, scaffolders, dev environment setup |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 102 | SDK docs, API parsers, symbol resolvers |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 91 | Metrics, alerting rules, observability |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 88 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 88 | Linting, code review, test generators, coverage |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 88 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 76 | Scaffolders, boilerplate generators, workflow templates |
| 📅 | [**Calendar & Productivity**](categories/calendar-email-productivity/) | 58 | Email automation, calendar management, task coordination |
| 🎨 | [**Image & Creative**](categories/image-creative-automation/) | 53 | Image generation, asset processing, design automation |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 48 | Web research, content discovery, data collection |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 47 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 42 | Audio/video processing, speech-to-text |
| ✍️ | [**Content & SEO**](categories/content-writing-seo/) | 41 | SEO content, blog automation, editorial workflows |
| 🔗 | [**Integrations**](categories/integrations-connectors/) | 40 | Third-party API bridges, webhooks, service connectors |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 28 | Theme/plugin dev, WP-CLI automation, CMS management |

---

## Browse by Signal

| | View | What you'll find |
|---|---|---|
| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |
| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |
| 🛡️ | [**Security Reviewed**](verification/) | Skills scanned for malicious patterns |
| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, alphabetical |

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
  "framework": ["Claude Code", "Cursor", "MCP-compatible", "OpenClaw"],
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

Every skill is backed by a real tool, repo, or package. New skills require real provenance before listing.

| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Listed** | 1,164 | Published — backed by a real tool or project |
| 🛡️ **Security Reviewed** | 950 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
