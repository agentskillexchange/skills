<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C419-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security_reviewed-2%2C078-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*2,419 published skills · 17 categories · Real ecosystem signals · Updated hourly*

</div>

---

## What is an Agent Skill

An agent skill is a reusable capability package for AI coding agents. Each entry here wraps a real tool, API, or workflow into a format agents like Claude Code, Cursor, Codex, and OpenClaw can install and use.

Every published skill is backed by a real upstream project or documented integration. No synthetic filler, no fake repo stars, no proxy download theater.

---

## Start Here

```bash
# Install any skill
npx skills add agentskillexchange/skills --skill <slug>

# Target a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code
npx skills add agentskillexchange/skills --skill <slug> -a cursor
npx skills add agentskillexchange/skills --skill <slug> -a codex

# OpenClaw
clawhub install <slug>
```

- Browse by category in [categories/](categories/)
- See strong signals in [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md)
- Use [CATALOG.md](CATALOG.md) for the full human-readable index

---

## Skill of the Day

### [Catch agent-era CI/CD and permission misconfigurations before shipping with Ship Safe](skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe/)

Run Ship Safe before a release when an agent needs one pre-ship pass for CI/CD misconfigurations, permission risks, secrets exposure, MCP-related hazards, and dependency issues.

- Tool: `catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe`
- Category: CI/CD Integrations
- Frameworks: Multi-Framework
- GitHub stars: 521
- Listing: https://agentskillexchange.com/skills/catch-agent-era-ci-cd-and-permission-misconfigurations-before-shipping-with-ship-safe/

---

## Featured Skills

A strong cross-section of high-signal skills across the catalog.

| Skill | Tool | ⭐ Stars | Category |
|-------|------|--------:|----------|
| [Preserve coding-agent context by sandboxing bulky tool output and retrieving only relevant session state with Context Mode](skills/preserve-coding-agent-context-by-sandboxing-bulky-tool-output-and-retrieving-only-relevant-session-state-with-context-mode/) | preserve-coding-agent-context-by-sandboxing-bulky-tool-output-and-retrieving-only-relevant-session-state-with-context-mode | 10k | Developer Tools |
| [Find likely duplicate GitHub issues through parallel search and evidence filtering with Claude Code dedupe](skills/find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe/) | find-likely-duplicate-github-issues-through-parallel-search-and-evidence-filtering-with-claude-code-dedupe | 116.8k | Templates &amp; Workflows |
| [Triage GitHub issues with body-first evidence checks and constrained label operations from Claude Code triage-issue](skills/triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue/) | triage-github-issues-with-body-first-evidence-checks-and-constrained-label-operations-from-claude-code-triage-issue | 116.8k | Templates &amp; Workflows |
| [Turn a code repository into an MCP-backed knowledge graph for agent code exploration with GitNexus](skills/turn-a-code-repository-into-an-mcp-backed-knowledge-graph-for-agent-code-exploration-with-gitnexus/) | turn-a-code-repository-into-an-mcp-backed-knowledge-graph-for-agent-code-exploration-with-gitnexus | 28.5k | Code Quality &amp; Review |
| [Build temporal context graphs for agent memory from evolving facts with Graphiti](skills/build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti/) | build-temporal-context-graphs-for-agent-memory-from-evolving-facts-with-graphiti | 24.9k | Library &amp; API Reference |
| [Search large codebases semantically from MCP-compatible coding agents with Claude Context](skills/search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context/) | search-large-codebases-semantically-from-mcp-compatible-coding-agents-with-claude-context | 9.2k | Developer Tools |
| [Trace, evaluate, and monitor agentic workflows with Opik](skills/trace-evaluate-and-monitor-agentic-workflows-with-opik/) | trace-evaluate-and-monitor-agentic-workflows-with-opik | 19.1k | Monitoring &amp; Alerts |
| [Run autonomous white-box pentests against web apps and APIs with Shannon](skills/run-autonomous-white-box-pentests-against-web-apps-and-apis-with-shannon/) | run-autonomous-white-box-pentests-against-web-apps-and-apis-with-shannon | 39.8k | Security &amp; Verification |
| [Trace Python memory allocation hotspots before leaks and spikes reach production with Memray](skills/trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray/) | trace-python-memory-allocation-hotspots-before-leaks-and-spikes-reach-production-with-memray | 15k | Monitoring &amp; Alerts |
| [Playwright Cross-Browser Testing and Automation Framework](skills/playwright-cross-browser-testing-and-automation-framework/) | playwright | 85.5k | Browser Automation |
| [Store selective long-term agent memories with Mem0 instead of replaying whole chats](skills/store-selective-long-term-agent-memories-with-mem0-instead-of-replaying-whole-chats/) | store-selective-long-term-agent-memories-with-mem0-instead-of-replaying-whole-chats | 53.5k | Library &amp; API Reference |
| [Search local notes, docs, and meeting transcripts for agent context with QMD](skills/search-local-notes-docs-and-meeting-transcripts-for-agent-context-with-qmd/) | search-local-notes-docs-and-meeting-transcripts-for-agent-context-with-qmd | 22.1k | Research &amp; Scraping |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 303 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 225 | Vulnerability scanning, auth setup, compliance |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 181 | Linting, code review, test generators, coverage |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 169 | Incident response, troubleshooting, system diagnostics |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 165 | ETL pipelines, parsing, format conversion |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 141 | Scaffolders, boilerplate generators, workflow templates |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 128 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 122 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 119 | SDK docs, API parsers, symbol resolvers |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 110 | Third-party API bridges, webhooks, service connectors |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 103 | Web research, content discovery, data collection |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 102 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 98 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 89 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 77 | SEO content, blog automation, editorial workflows |

---

## Industry Collections

Curated editorial overlays for teams that want repo navigation by real workflow clusters without replacing the core category taxonomy.

| | Collection | Stage | What you'll find |
|---|---|---|---|
| 🎙️ | [**Media & Publishing Systems**](industries/media-publishing-systems.md) | Wave 1 | Transcription, subtitles, podcast workflows, chaptering, localization, loudness cleanup, and final-mile publishing prep |
| 💼 | [**Finance & Filings**](industries/finance-filings.md) | Wave 1 | Filings research, invoice intake, billing operations, reconciliation, and finance-adjacent reporting |
| 🛒 | [**Ecommerce & Retail Operations**](industries/ecommerce-retail-operations.md) | Wave 1 | Catalog management, storefront automation, orders, inventory sync, marketplace support, and review-driven merchandising |
| ⚖️ | [**Legal Ops & Compliance**](industries/legal-ops-compliance.md) | Wave 1 | Contract workflows, forms, document review, archive search, and evidence-oriented legal and compliance support |
| 🩺 | [**Healthcare Documentation & Intake**](industries/healthcare-documentation-intake.md) | Wave 2 | Documentation intake, OCR, transcription, structured extraction, and biomedical literature support for paperwork-heavy workflows |
| 📈 | [**Product Analytics & Growth Ops**](industries/product-analytics-growth-ops.md) | Wave 3 | Product analytics, feature flags, rollout checks, session replay, privacy-friendly web analytics, and experiment/evaluation workflows |
| 📚 | [**DevRel & API Documentation**](industries/devrel-api-documentation.md) | Wave 3 | API docs, OpenAPI references, SDK generation, docs-site publishing, prose linting, and developer enablement workflows |
| 🎧 | [**Customer Support & Success**](industries/customer-support-success.md) | Wave 4 | Helpdesk queues, ticket triage, conversation lookup, knowledge-base workflows, customer context, CRM sync, and reply-drafting support |
| 🏠 | [**Real Estate Workflows**](industries/real-estate-workflows.md) | Wave 4 | Property research support, transaction paperwork, signature routing, document intake, CRM context, and listing follow-up workflows for real-estate operations |

See the full overlay index in [industries/README.md](industries/README.md).

---

## Browse

| | View | What you'll find |
|---|---|---|
| ⭐ | [**Top Starred**](TOP-STARS.md) | Skills backed by the most popular GitHub repos |
| 🔥 | [**Top Downloaded**](TOP-DOWNLOADS.md) | Skills backed by the most-used npm packages |
| 📖 | [**Full Catalog**](CATALOG.md) | Every skill, sorted by category and stars |
| 🔌 | [**JSON Index**](skills.json) | Machine-readable catalog for programmatic access |

---

## Trust & Safety

Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.

| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Published** | 2,419 | In the catalog, every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,078 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

More: [verification/](verification/)

---

## Submit a Skill

1. Fork this repo and add a `skills/<slug>/SKILL.md` entry, or
2. Submit through [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) for hourly sync

---

<div align="center">

*[agentskillexchange.com](https://agentskillexchange.com/)*

</div>
