<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-1%2C280-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-1%2C271-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*1,280 published skills · 17 categories · Real ecosystem signals · Updated hourly*

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
| [Whisper Subtitle Generator](skills/whisper-subtitle-generator/) | whisper | 96.6k | Media & Transcription |
| [Playwright Multi-Tab Session Manager](skills/playwright-multi-tab-session-manager/) | playwright | 84.9k | Browser Automation |
| [Grafana OnCall Escalation Chain Manager](skills/grafana-oncall-escalation-chain-manager/) | grafana | 72.8k | Monitoring & Alerts |
| [Ansible Playbook Dry-Run Validator](skills/ansible-playbook-dryrun-validator-agent/) | ansible | 68.4k | Runbooks & Diagnostics |
| [Scrapy Spider Architect](skills/scrapy-spider-architect/) | scrapy | 60.9k | Research & Scraping |
| [Pandas DataFrame Pipeline Orchestrator](skills/pandas-dataframe-pipeline-orchestrator/) | pandas | 48.2k | Data Extraction & Transformation |
| [Terraform State Forensics Tool](skills/terraform-state-forensics-tool/) | terraform | 48.0k | Runbooks & Diagnostics |
| [Prisma Schema Migrator](skills/prisma-schema-migrator/) | prisma | 45.6k | Library & API Reference |
| [Jest Unit Test Scaffolder](skills/jest-unit-test-scaffolder/) | jest | 45.3k | Code Quality & Review |
| [Vault Transit Secrets Envelope Verifier](skills/vault-transit-secrets-envelope-verifier/) | vault | 35.3k | Security & Verification |
| [Docker Compose Service Blueprint Creator](skills/docker-compose-service-blueprint-creator/) | docker | 71.6k | Templates & Workflows |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 140 | Pipeline configs, deployment automation, build tooling |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 140 | CLI tools, scaffolders, dev environment setup |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 113 | Incident response, troubleshooting, system diagnostics |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 100 | ETL pipelines, parsing, format conversion |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 96 | Vulnerability scanning, auth setup, compliance |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 91 | SDK docs, API parsers, symbol resolvers |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 89 | Linting, code review, test generators, coverage |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 79 | Metrics, alerting rules, observability |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 61 | Scaffolders, boilerplate generators, workflow templates |
| 🔗 | [**Integrations**](categories/integrations-connectors/) | 53 | Third-party API bridges, webhooks, service connectors |
| 🎨 | [**Image & Creative**](categories/image-creative-automation/) | 52 | Image generation, asset processing, design automation |
| 📅 | [**Calendar & Productivity**](categories/calendar-email-productivity/) | 50 | Email automation, calendar management, task coordination |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 49 | Web research, content discovery, data collection |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 47 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 40 | Audio/video processing, speech-to-text |
| ✍️ | [**Content & SEO**](categories/content-writing-seo/) | 37 | SEO content, blog automation, editorial workflows |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 32 | Theme/plugin dev, WP-CLI automation, CMS management |

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

Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.

| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Published** | 1,280 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 1,271 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
