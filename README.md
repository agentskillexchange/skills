<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C308-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C702-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,308 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Open WebUI Self-Hosted AI Interface for LLMs](skills/open-webui-self-hosted-ai-interface/)** — Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform designed to operate entirely offline. It supports various LLM runners like Ollama and OpenAI-compatible APIs with built-in…

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
| [Complete website tasks in Comma’s native desktop browser](skills/complete-website-tasks-in-comma-native-desktop-browser/) | Invoke Comma’s browser-use skill for a bounded website task on the initiating desktop, with action receipts, user handoffs... | 726 | Browser Automation |
| [Prepare engineering decisions with AI-SDLC decision-rubric](skills/prepare-engineering-decisions-with-ai-sdlc-decision-rubric/) | Frame one consequential engineering choice with sourced evidence, distinct options, a counterargument, dependency checks and an operator decision | 456 | Templates & Workflows |
| [Assemble PR verification evidence with Roam Guard](skills/assemble-pr-verification-evidence-with-roam-guard/) | Collect a branch’s Roam analysis evidence into a strict local PR verdict, with explicit required checks, missing evidence... | 516 | Code Quality & Review |
| [Validate Team Brain retrieval and access boundaries](skills/validate-team-brain-retrieval-and-access-boundaries/) | Run Team Brain’s seeded Oracle test-schema diagnostic and return retrieval, permission-check and setup failures before connecting real team... | 4.5k | Runbooks & Diagnostics |
| [Pay a Nano (XNO) 402 and Fetch](skills/nano-fetch/) | Fetch a URL and, when it answers HTTP 402 with an x402 nano:mainnet exact quote, pay it once... | - | Integrations & Connectors |
| [AI Dance Video with Danceo](skills/danceo-ai-dance-video/) | Use Danceo Video MCP to select a dance template, check credits, create a portrait-based dance video, and poll... | - | Image & Creative Automation |
| [Corral — Exclusive Android Device Leases for Coding Agents](skills/corral-android-device-leases-for-coding-agents/) | Lease one Android device (USB, WiFi or emulator) exclusively to one agent session through the corral CLI or... | - | Developer Tools |
| [Reconcile CCCC agent-message delivery and reply evidence](skills/reconcile-cccc-agent-message-delivery-and-reply-evidence/) | Inspect an existing CCCC delegation, separate runtime handoff from reads and replies, and return evidence before retrying uncertain... | 1.3k | Runbooks & Diagnostics |
| [Google Flights Fare Search](skills/google-flights-fare-search/) | Search Google Flights by route and date through the Apify Google Flights Actor (johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search) and get one JSON... | - | Research & Scraping |
| [Review repository changes for destructive commands with dcg](skills/review-repository-changes-for-destructive-commands-with-dcg/) | Scan staged changes or selected automation files with Destructive Command Guard and return rule-level findings before commit or... | 6.4k | Security & Verification |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [dhyabi2](https://github.com/dhyabi2) | [Pay a Nano (XNO) 402 and Fetch](skills/nano-fetch/) | Fetch a URL and, when it answers HTTP 402 with an x402 nano:mainnet exact quote, pay it once... | Integrations & Connectors |
| [jasonliu119](https://github.com/jasonliu119) | [AI Dance Video with Danceo](skills/danceo-ai-dance-video/) | Use Danceo Video MCP to select a dance template, check credits, create a portrait-based dance video, and poll... | Image & Creative Automation |
| [ciszkin](https://github.com/ciszkin) | [Corral — Exclusive Android Device Leases for Coding Agents](skills/corral-android-device-leases-for-coding-agents/) | Lease one Android device (USB, WiFi or emulator) exclusively to one agent session through the corral CLI or... | Developer Tools |
| [johnisanerd](https://github.com/johnisanerd) | [Google Flights Fare Search](skills/google-flights-fare-search/) | Search Google Flights by route and date through the Apify Google Flights Actor (johnvc/Google-Flights-Data-Scraper-Flight-and-Price-Search) and get one JSON... | Research & Scraping |
| [darynaivanova-mt](https://github.com/darynaivanova-mt) | [Mailtrap Sending Emails](skills/mailtrap-sending-emails/) | Official Mailtrap skill for wiring outbound email into an app through Mailtrap Email Live Sending: pick the transactional... | Calendar, Email & Productivity |
| [mandrillxx](https://github.com/mandrillxx) | [BloxStack Onboarding](skills/bloxstack-onboarding/) | Help Roblox teams start using BloxStack Studio to organize their own games, tasks, and files. Use when a... | Integrations & Connectors |
| [jakemarsh](https://github.com/jakemarsh) | [Runheed](skills/runheed/) | Read and resolve production errors through the Runheed remote MCP server (https://runheed.com/api/mcp): search error groups, read stack traces... | Integrations & Connectors |
| [dhyabi2](https://github.com/dhyabi2) | [Verify a Nano (XNO) Payment](skills/verify-nano-payment/) | Verify that a Nano (XNO) payment has settled: confirm a send/receive block, read its amount and pay-to account... | Integrations & Connectors |
| [mohiddin7](https://github.com/mohiddin7) | [Resume Tribunal](skills/resume-tribunal/) | Tailors a resume or CV to one job posting using only the user's own facts, then has an... | Templates & Workflows |
| [livejake](https://github.com/livejake) | [Van Westendorp Analysis](skills/van-westendorp-analysis/) | Compute a Van Westendorp price sensitivity meter (PSM) from a CSV of pricing survey answers: OPP, IPP, PMC... | Data Extraction & Transformation |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Coordinate a scoped code change through Oh My Claudecode team stages](skills/coordinate-a-scoped-code-change-through-oh-my-claudecode-team-stages/) | Run a bounded Claude Code team task through planning, delegated implementation, verification and repair, then return the change... | 40.9k | Templates & Workflows |
| [Inspect a scoped workspace hierarchy through PipesHub MCP](skills/inventory-a-scoped-workspace-hierarchy-through-pipeshub-mcp/) | Paginate a named folder, space, or epic into a source-linked record inventory, preserving scope and reporting indexing, access... | 4.1k | Integrations & Connectors |
| [Audit local agent runs and select hook policies with Failproof AI](skills/audit-local-agent-runs-and-select-hook-policies-with-failproof-ai/) | Review local harness history, identify risky tool patterns, and prepare a source-backed policy-pack rollout across supported agent runtimes | 8.9k | Security & Verification |
| [Review Master CSS output regressions through MCP snapshots](skills/review-master-css-output-regressions-through-mcp-snapshots/) | Capture project CSS snapshots, trace missing classes, compare generated output, and propose scoped fixes with evidence from the... | 2.0k | Code Quality & Review |
| [Record an agent-completed browser task as a parameterized Oya playbook](skills/record-agent-browser-task-as-parameterized-oya-playbook/) | Complete a test browser task once, save its learned steps as an Oya playbook, and verify a replay... | 349 | Browser Automation |
| [Record and replay FrontMCP calls to catch server regressions](skills/record-and-replay-frontmcp-calls-to-catch-server-regressions/) | Capture baseline MCP calls as JSONL, replay them against a changed FrontMCP server, and review answer differences and... | 151 | Code Quality & Review |
| [Triage Lunora deployment errors and migration status through MCP](skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/) | Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff... | 293 | Runbooks & Diagnostics |
| [Find evidence across a PDF corpus with Semtools](skills/find-evidence-across-pdf-corpus-with-semtools/) | Parse a selected PDF batch, search the cached Markdown locally, and return an agent answer backed by inspected... | 1.9k | Data Extraction & Transformation |
| [Assemble and review local video cuts through Concat MCP](skills/assemble-and-review-local-video-cuts-through-concat-mcp/) | Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and... | 16.0k | Media & Transcription |
| [Validate and report completed external workflow usage to LoopForge](skills/validate-and-report-completed-external-workflow-usage-to-loopforge/) | Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for... | 2.8k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 552 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 276 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 267 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 247 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 223 | Linting, code review, test generators, coverage |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 199 | Third-party API bridges, webhooks, service connectors |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 196 | Incident response, troubleshooting, system diagnostics |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 195 | Pipeline configs, deployment automation, build tooling |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 165 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 149 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 137 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 133 | Email automation, calendar management, task coordination |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 132 | Image generation, asset processing, design automation |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 130 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 114 | Audio/video processing, speech-to-text |
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
| 📋 **Published** | 3,308 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,702 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
