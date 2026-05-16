<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C468-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-2%2C463-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*2,468 published skills · 17 categories · Real ecosystem signals · Updated hourly*

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

## Skill of the Day

**[Run repeatable Google Ads and SEO audits inside Claude Code with Toprank](https://agentskillexchange.com/skills/run-repeatable-google-ads-and-seo-audits-inside-claude-code-with-toprank/)** — Use Toprank when an agent needs a repeatable Claude Code workflow for Google Ads and SEO audits, with concrete slash commands, account-backed analysis, and optional repo edits instead…

_Rotates daily by UTC date from the Security Reviewed pool._

---

## Industry Collections

Curated skill sets organized by industry vertical:

| | Collection | Description |
|---|---|---|
| 🎙️ | [**Media & Publishing Systems**](industries/media-publishing-systems.md) | Transcription, subtitles, podcast workflows, chaptering, localization, loudness cleanup, and final-mile publishing prep. _(Wave 1)_ |
| 💼 | [**Finance & Filings**](industries/finance-filings.md) | Filings research, invoice intake, billing operations, reconciliation, and finance-adjacent reporting. _(Wave 1)_ |
| 🛒 | [**Ecommerce & Retail Operations**](industries/ecommerce-retail-operations.md) | Catalog management, storefront automation, orders, inventory sync, marketplace support, and review-driven merchandising. _(Wave 1)_ |
| ⚖️ | [**Legal Ops & Compliance**](industries/legal-ops-compliance.md) | Contract workflows, forms, document review, archive search, and evidence-oriented legal and compliance support. _(Wave 1)_ |
| 🩺 | [**Healthcare Documentation & Intake**](industries/healthcare-documentation-intake.md) | Documentation intake, OCR, transcription, structured extraction, and biomedical literature support for paperwork-heavy workflows. _(Wave 2)_ |
| 📈 | [**Product Analytics & Growth Ops**](industries/product-analytics-growth-ops.md) | Product analytics, feature flags, rollout checks, session replay, privacy-friendly web analytics, and experiment/evaluation workflows. _(Wave 3)_ |
| 📚 | [**DevRel & API Documentation**](industries/devrel-api-documentation.md) | API docs, OpenAPI references, SDK generation, docs-site publishing, prose linting, and developer enablement workflows. _(Wave 3)_ |
| 🎧 | [**Customer Support & Success**](industries/customer-support-success.md) | Helpdesk queues, ticket triage, conversation lookup, knowledge-base workflows, customer context, CRM sync, and reply-drafting support. _(Wave 4)_ |
| 🏠 | [**Real Estate Workflows**](industries/real-estate-workflows.md) | Property research support, transaction paperwork, signature routing, document intake, CRM context, and listing follow-up workflows for real-estate operations. _(Wave 4)_ |

See the full overlay index in [industries/README.md](industries/README.md).

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | Tool | ⭐ Stars | Category |
|-------|------|--------:|----------|
| [Route Claude Code requests across models and providers with Claude Code Router](skills/route-claude-code-requests-across-models-and-providers-with-claude-code-router/) | route-claude-code-requests-across-models-and-providers-with-claude-code-router | 33.9k | Developer Tools |
| [Preserve coding-agent context by sandboxing bulky tool output and retrieving only relevant session state with Context Mode](skills/preserve-coding-agent-context-by-sandboxing-bulky-tool-output-and-retrieving-only-relevant-session-state-with-context-mode/) | preserve-coding-agent-context-by-sandboxing-bulky-tool-output-and-retrieving-only-relevant-session-state-with-context-mode | 10k | Developer Tools |
| [Run long-horizon spec-driven coding agent workflows with GSD 2](skills/run-long-horizon-spec-driven-coding-agent-workflows-with-gsd-2/) | run-long-horizon-spec-driven-coding-agent-workflows-with-gsd-2 | 7.3k | Templates & Workflows |
| [Build and inspect MCP apps and servers with mcp-use](skills/build-and-inspect-mcp-apps-and-servers-with-mcp-use/) | build-and-inspect-mcp-apps-and-servers-with-mcp-use | 9.9k | Integrations & Connectors |
| [Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe](skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe/) | find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe | 116.8k | Templates & Workflows |
| [Trace, evaluate, and monitor agentic workflows with Opik](skills/trace-evaluate-and-monitor-agentic-workflows-with-opik/) | trace-evaluate-and-monitor-agentic-workflows-with-opik | 19.1k | Monitoring & Alerts |
| [Build temporal context graphs for agent memory from evolving facts with Graphiti](skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/) | build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti | 24.9k | Library & API Reference |
| [Run long-horizon research and coding agent workflows with DeerFlow](skills/run-long-horizon-research-and-coding-agent-workflows-with-deerflow/) | run-long-horizon-research-and-coding-agent-workflows-with-deerflow | 67.5k | Code Quality & Review |
| [Run stealth Chromium browser automation with CloakBrowser](skills/run-stealth-chromium-browser-automation-with-cloakbrowser/) | run-stealth-chromium-browser-automation-with-cloakbrowser | 10.2k | Browser Automation |
| [Let agents control a logged-in Chrome browser through Playwriter MCP](skills/let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp/) | let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp | 3.5k | Browser Automation |
| [Preserve agent session context with Claude Mem](skills/preserve-agent-session-context-with-claude-mem/) | preserve-agent-session-context-with-claude-mem | 74.5k | Library & API Reference |
| [Optimize prompt and agent pipelines with DSPy programs and evaluators](skills/optimize-prompt-and-agent-pipelines-with-dspy-programs-and-evaluators/) | optimize-prompt-and-agent-pipelines-with-dspy-programs-and-evaluators | 34.3k | Code Quality & Review |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 314 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 226 | Vulnerability scanning, auth setup, compliance |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 183 | Linting, code review, test generators, coverage |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 169 | Incident response, troubleshooting, system diagnostics |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 169 | ETL pipelines, parsing, format conversion |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 156 | Scaffolders, boilerplate generators, workflow templates |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 129 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 122 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 121 | SDK docs, API parsers, symbol resolvers |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 118 | Third-party API bridges, webhooks, service connectors |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 106 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 104 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 98 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 89 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 77 | SEO content, blog automation, editorial workflows |

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
  "title": "Playwright MCP Browser Automation",
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
| 📋 **Published** | 2,468 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,463 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
