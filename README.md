<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C205-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C624-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,205 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

*Star this repo to keep the agent skill catalog handy and follow new additions.*

</div>

---

## What is this?

An open, curated catalog of trusted reusable skills for AI agents, not a generic dump. Each skill wraps a real tool, API, or workflow into a format that agents and runtimes like OpenClaw, Claude Code, Codex, GitHub Copilot, Gemini, Cursor, MCP clients, LangChain, OpenAI Agents, Hermes, and custom agent workflows can install and use.

Every skill is backed by a real upstream project — a GitHub repo, npm package, or documented API. No synthetic entries.

---

## Quick Start

```bash
# OpenClaw native install
clawhub install <slug>

# Manual install for other agents
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/<slug> ~/.agent-skills/<slug>
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill <slug>
```

---

## Skill of the Day

**[Paperless-ngx Document OCR and Archive Management System](skills/paperless-ngx-document-ocr-archive-management-system/)** — Paperless-ngx is an open source document management system that turns scanned or uploaded paperwork into a searchable archive. It combines OCR-driven ingestion, indexing, tagging, storage, and retrieval for…

_Rotates daily across downloaded, starred, recent, verified, and industry-curated skills._

---

## Industry Collections

Curated skill sets organized by industry vertical:

| | Collection | Description |
|---|---|---|
| 🎙️ | [**Media & Publishing Systems**](industries/media-publishing-systems.md) | Transcription, subtitles, podcast workflows, chaptering, localization, loudness cleanup, and final-mile publishing prep. |
| 💼 | [**Finance & Filings**](industries/finance-filings.md) | Filings research, invoice intake, billing operations, reconciliation, and finance-adjacent reporting. |
| 🛒 | [**Ecommerce & Retail Operations**](industries/ecommerce-retail-operations.md) | Catalog management, storefront automation, orders, inventory sync, marketplace support, and review-driven merchandising. |
| ⚖️ | [**Legal Ops & Compliance**](industries/legal-ops-compliance.md) | Contract risk review, redline preparation, forms, document review, archive search, and evidence-oriented legal and compliance support. |
| 🩺 | [**Healthcare Documentation & Intake**](industries/healthcare-documentation-intake.md) | Documentation intake, OCR, transcription, structured extraction, and biomedical literature support for paperwork-heavy workflows. |
| 📈 | [**Product Analytics & Growth Ops**](industries/product-analytics-growth-ops.md) | Product analytics, feature flags, rollout checks, session replay, privacy-friendly web analytics, and experiment/evaluation workflows. |
| 📚 | [**DevRel & API Documentation Workflows**](industries/devrel-api-documentation.md) | API docs, OpenAPI references, SDK generation, docs-site publishing, prose linting, and developer enablement workflows. |
| 🎧 | [**Customer Support & Success**](industries/customer-support-success.md) | Helpdesk queues, ticket triage, conversation lookup, knowledge-base workflows, customer context, CRM sync, and reply-drafting support. |
| 🏠 | [**Real Estate Workflows**](industries/real-estate-workflows.md) | Property research support, transaction paperwork, signature routing, document intake, CRM context, and listing follow-up workflows for real-estate operations. |
| 🎓 | [**Education & Research Workflows**](industries/education-research-workflows.md) | Literature review, citation context, research synthesis, paper drafting, replication checks, and evidence packets for academic and technical teams. |
| 📣 | [**GTM & RevOps Workflows**](industries/gtm-revops-workflows.md) | Demand generation, SEO and content operations, lifecycle email, CRM enrichment, lead routing, social listening, trend monitoring, feedback capture, and sales/revenue operations workflows. |
| 🧭 | [**AI Agency Operations & FDE Workflows**](industries/ai-agency-operations.md) | Client-facing AI delivery, forward deployed engineering workflows, browser automation, implementation systems, documentation, spreadsheets, proposals, and client handoff workflows. |
| 🛠️ | [**Infrastructure, SRE & Incident Operations**](industries/infrastructure-sre-incident-operations.md) | Production reliability workflows for Kubernetes, incidents, observability, backups, deploy safety, infrastructure drift, alerts, and runbook-driven debugging. |
| 🛡️ | [**Security Operations & GRC Workflows**](industries/security-operations-grc-workflows.md) | Security operations and governance workflows for dependency risk, secrets, CI hardening, agent guardrails, approvals, policy evidence, threat hunting, red-team checks, and audit-ready releases. |
| 🗄️ | [**Data Platform & Analytics Engineering**](industries/data-platform-analytics-engineering.md) | Data engineering and analytics operations workflows for SQL, dbt, Airflow, warehouses, Postgres, CSV cleanup, schema quality, retrieval indexes, data catalogs, dashboards, and query tuning. |

See the full overlay index in [industries/README.md](industries/README.md).

---

## Recently Published Skills

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Invokely Statistics](skills/invokely-statistics/) | Use Invokely's hosted MCP tools to find and cite official statistics. Use when an agent needs indicator discovery... | - | Data Extraction & Transformation |
| [Imagera Media Generation](skills/imagera-media/) | Generates and edits images, video clips, voiceovers and music from a coding agent through the hosted Imagera MCP... | - | Image & Creative Automation |
| [Assemble and review local video cuts through Concat MCP](skills/assemble-and-review-local-video-cuts-through-concat-mcp/) | Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and... | 16.0k | Media & Transcription |
| [Build and resume checked repository task graphs with Memdoor](skills/build-and-resume-checked-repository-task-graphs-with-memdoor/) | Turn a repository procedure into Memdoor YAML tasks with explicit dependencies, completion checks, human approval gates and resumable... | 382 | Templates & Workflows |
| [Datacircle GTM API Benchmark](skills/datacircle-gtm-api-benchmark/) | Compare GTM APIs using Datacircle rankings. Call the open API at api.datacircle.dev/v1, with no key, to list covered... | - | Library & API Reference |
| [Call or Text Your Phone from an Agent with /call-me](skills/call-me/) | Lets an agent call or text the user's own phone (iPhone or Android) through the /call-me remote MCP... | 41 | Integrations & Connectors |
| [Compare retriever rankings on fixed relevance datasets with BEIR](skills/compare-retriever-rankings-on-fixed-relevance-datasets-with-beir/) | Compare baseline and candidate retrievers on the same labeled dataset, then hand off ranking metrics, saved runs and... | 2.3k | Security & Verification |
| [Triage Lunora deployment errors and migration status through MCP](skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/) | Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff... | 293 | Runbooks & Diagnostics |
| [Arcmira: YouTube Transcript Search](skills/arcmira-transcript-search/) | Search indexed YouTube and podcast transcripts through Arcmira MCP. Return quoted passages, speaker attribution when available, and timestamped... | - | Media & Transcription |
| [Berlin Job Search](skills/berlin-job-search/) | AI job-search coach for Berlin and the rest of Germany. Searches live postings (Bundesagentur für Arbeit API, Arbeitnow... | 31 | Templates & Workflows |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [estevecastells](https://github.com/estevecastells) | [Invokely Statistics](skills/invokely-statistics/) | Use Invokely's hosted MCP tools to find and cite official statistics. Use when an agent needs indicator discovery... | Data Extraction & Transformation |
| [waynehamadi](https://github.com/waynehamadi) | [Datacircle GTM API Benchmark](skills/datacircle-gtm-api-benchmark/) | Compare GTM APIs using Datacircle rankings. Call the open API at api.datacircle.dev/v1, with no key, to list covered... | Library & API Reference |
| [waynehamadi](https://github.com/waynehamadi) | [Datacircle](skills/datacircle/) | Every GTM API plan on datacircle.dev, as one file you download and query. LinkedIn profiles, people and company... | Library & API Reference |
| [zealous1](https://github.com/zealous1) | [Arcmira: YouTube Transcript Search](skills/arcmira-transcript-search/) | Search indexed YouTube and podcast transcripts through Arcmira MCP. Return quoted passages, speaker attribution when available, and timestamped... | Media & Transcription |
| [radres](https://github.com/radres) | [Call or Text Your Phone from an Agent with /call-me](skills/call-me/) | Lets an agent call or text the user's own phone (iPhone or Android) through the /call-me remote MCP... | Integrations & Connectors |
| [ADWilkinson](https://github.com/ADWilkinson) | [USDCtoFiat Cash-Out](skills/usdctofiat-cashout/) | Add non-custodial Base USDC-to-fiat cash-out with @usdctofiat/offramp cashout({ mode: "fast" \| "best" }). Use when an agent must... | Integrations & Connectors |
| [OathWallet](https://github.com/OathWallet) | [Oath Wallet Guide](skills/aperture-wallet-guide/) | Answer Oath Wallet questions from first-party product, security, network, release, app-screen, and Journal sources while enforcing explicit wallet-secret... | Library & API Reference |
| [umutyesildal](https://github.com/umutyesildal) | [Berlin Job Search](skills/berlin-job-search/) | AI job-search coach for Berlin and the rest of Germany. Searches live postings (Bundesagentur für Arbeit API, Arbeitnow... | Templates & Workflows |
| [f-o-x11](https://github.com/f-o-x11) | [Give an Agent Its Own Email Inbox with Cooper Email](skills/cooper-email/) | Gives an AI agent its own email inbox at username@cooperemail.com through the Cooper Email REST API or remote... | Calendar, Email & Productivity |
| [ADWilkinson](https://github.com/ADWilkinson) | [HyperGrok Trading Desk](skills/hypergrok-trading-desk/) | Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven... | Integrations & Connectors |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Triage Lunora deployment errors and migration status through MCP](skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/) | Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff... | 293 | Runbooks & Diagnostics |
| [Diagnose incomplete web extraction with PageSift MCP audit evidence](skills/diagnose-incomplete-web-extraction-with-pagesift-mcp-audit-evidence/) | Triage missing web content across local agents using PageSift MCP audit records, HTML snapshots, and local extraction issue... | 162 | Data Extraction & Transformation |
| [Diagnose Paradev host and terminal failures with the doctor skill](skills/diagnose-paradev-host-and-terminal-failures-with-the-doctor-skill/) | Capture Paradev service, account, host and version evidence, propose one symptom-matched repair, and verify the original failure before... | 15.6k | Runbooks & Diagnostics |
| [Resolve coding questions from upstream evidence with Firecrawl Developer Index](skills/resolve-coding-questions-with-firecrawl-developer-index/) | Find public issues, merged fixes and API-contract passages with Firecrawl’s named Developer Index skill, then return a cited... | 653 | Research & Scraping |
| [Assemble and review local video cuts through Concat MCP](skills/assemble-and-review-local-video-cuts-through-concat-mcp/) | Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and... | 16.0k | Media & Transcription |
| [Monitor Claude Code sessions with ccstatusline](skills/monitor-claude-code-sessions-with-ccstatusline/) | Configure Claude Code's status line with live model, token, cost, git, sandbox, cache, CI, and session health signals... | 13.2k | Developer Tools |
| [Coordinate agent teams and governed work in Paperclip](skills/coordinate-agent-teams-and-governed-work-in-paperclip/) | Use Paperclip as a self-hosted control plane for assigning goals, tasks, budgets, approvals, routines, and run history across... | 98.2k | Templates & Workflows |
| [Ground React UI edits in project components and tokens with the Onsystem skill](skills/ground-react-ui-edits-in-project-components-and-tokens-with-onsystem-skill/) | Discover project-specific React components and tokens, implement a bounded UI change, and repair new design-system violations with Onsystem... | 165 | Code Quality & Review |
| [Reverse-engineer apps and binaries with REA](skills/reverse-engineer-apps-and-binaries-with-rea/) | Connect coding agents to REA's MCP tools so they can inspect apps, binaries, websites, APKs, and runtime behavior... | 17.1k | Security & Verification |
| [Datacircle GTM API Benchmark](skills/datacircle-gtm-api-benchmark/) | Compare GTM APIs using Datacircle rankings. Call the open API at api.datacircle.dev/v1, with no key, to list covered... | - | Library & API Reference |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 536 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 269 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 258 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 240 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 211 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 193 | Pipeline configs, deployment automation, build tooling |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 190 | Third-party API bridges, webhooks, service connectors |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 185 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 163 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 141 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 134 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 130 | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 128 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 122 | Image generation, asset processing, design automation |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 112 | Audio/video processing, speech-to-text |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 98 | SEO content, blog automation, editorial workflows |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |

---

## Browse The Catalog

| | View | What you'll find |
|---|---|---|
| 🧭 | [**Live Browse**](https://agentskillexchange.com/browse-skills/) | Search, filters, skill detail panels, and install links on agentskillexchange.com |
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
  "name": "Playwright MCP Browser Automation",
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

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
# List all skills
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --list

# Search
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --search kubernetes

# Install
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill <slug> -a <agent>
```

---

## Trust & Safety

Every skill is backed by a real tool, repo, or package. New skills require real provenance before publishing.

| Tier | Count | Meaning |
|------|------:|---|
| 📋 **Published** | 3,205 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,624 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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

### Option 2: Create Skill Wizard

Use [agentskillexchange.com/create-skill](https://agentskillexchange.com/create-skill/) to generate a repo-ready `SKILL.md`, then open a pull request with the generated file.

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
