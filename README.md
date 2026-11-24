<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C287-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C690-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,287 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Audit a user journey into interaction counts and a UX budget](skills/audit-a-user-journey-into-interaction-counts-and-a-ux-budget/)** — Trace one user journey through its code, label interaction counts by evidence, and deliver ranked friction reductions with a proposed click and field budget.

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
| [Audit local coding-agent permissions and MCP configuration with Safe Anything](skills/audit-local-coding-agent-permissions-and-mcp-configuration-with-safe-anything/) | Review a selected project’s agent permissions, MCP launch pins, credentials and hooks with an offline scan and a... | 407 | Security & Verification |
| [Validate a managed JSON Goal deliverable in MateClaw](skills/validate-a-managed-json-goal-deliverable-in-mateclaw/) | Publish a scoped JSON report to a user-selected Goal slot, bind required-field checks to its exact version, and... | 1.2k | Templates & Workflows |
| [Inspect Open Agent API Runs](skills/open-agent-api-run-inspector/) | Inspect a previously submitted Open Agent API task with a read-only key. Distinguish a live task, an approval... | - | Runbooks & Diagnostics |
| [Patch one Obsidian note section with a version precondition](skills/patch-one-obsidian-note-section-with-a-version-precondition/) | Read a named note section, apply a version-conditional MCP patch, and return a verified change or an explicit... | 3.2k | Calendar, Email & Productivity |
| [Audit a user journey into interaction counts and a UX budget](skills/audit-a-user-journey-into-interaction-counts-and-a-ux-budget/) | Trace one user journey through its code, label interaction counts by evidence, and deliver ranked friction reductions with... | 2.1k | Code Quality & Review |
| [Move an existing coding mission between machines with Orb checkpoints](skills/move-an-existing-coding-mission-between-machines-with-orb-checkpoints/) | Prepare a verified workspace checkpoint, move one Orb mission to an eligible machine on the same Core, and... | 719 | Developer Tools |
| [Triage Camunda process incidents into a read-only evidence packet](skills/triage-camunda-process-incidents-into-a-read-only-evidence-packet/) | Search and inspect scoped Camunda 8 incidents, distinguish observed errors from suspected causes, and hand off a read-only... | 4.4k | Runbooks & Diagnostics |
| [Resume Tribunal](skills/resume-tribunal/) | Tailors a resume or CV to one job posting using only the user's own facts, then has an... | - | Templates & Workflows |
| [Build reviewed repository context packets with RepoPrompt CE MCP](skills/build-reviewed-repository-context-repoprompt-ce-mcp/) | Bind a repository workspace, discover relevant files, refine slices and code maps, inspect token usage, and export a... | 997 | Developer Tools |
| [Delegate bounded coding tasks and hand off sessions with Kimi Code](skills/delegate-coding-tasks-handoff-sessions-kimi-code/) | Coordinate local Kimi Code tasks with structured CLI output, or discover the installed KAP interface to hand off... | 8.3k | Developer Tools |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [jiangxingfan1-coder](https://github.com/jiangxingfan1-coder) | [Inspect Open Agent API Runs](skills/open-agent-api-run-inspector/) | Inspect a previously submitted Open Agent API task with a read-only key. Distinguish a live task, an approval... | Runbooks & Diagnostics |
| [dhyabi2](https://github.com/dhyabi2) | [Verify a Nano (XNO) Payment](skills/verify-nano-payment/) | Verify that a Nano (XNO) payment has settled: confirm a send/receive block, read its amount and pay-to account... | Integrations & Connectors |
| [mohiddin7](https://github.com/mohiddin7) | [Resume Tribunal](skills/resume-tribunal/) | Tailors a resume or CV to one job posting using only the user's own facts, then has an... | Templates & Workflows |
| [livejake](https://github.com/livejake) | [Van Westendorp Analysis](skills/van-westendorp-analysis/) | Compute a Van Westendorp price sensitivity meter (PSM) from a CSV of pricing survey answers: OPP, IPP, PMC... | Data Extraction & Transformation |
| [yssoft-gif](https://github.com/yssoft-gif) | [RELAY Paid Work Marketplace](skills/relay-paid-work/) | Find suitable paid requests from RELAY's encrypted snapshot, prepare a seller quote, or draft a buyer request for... | Integrations & Connectors |
| [antoinersx](https://github.com/antoinersx) | [StalkChain Trader Check](skills/stalkchain-trader-check/) | Review a public crypto trader’s attributed wallets, reported PnL and open positions using the StalkChain Data MCP | Research & Scraping |
| [jakemarsh](https://github.com/jakemarsh) | [CallForMe](skills/callforme/) | Phone a business for the user through the CallForMe remote MCP server (https://callforme.tel/mcp) or its REST API: get... | Integrations & Connectors |
| [al-global-tech](https://github.com/al-global-tech) | [Generate Images and Video with UberLLM](skills/generate-images-and-video-with-uberllm/) | Discovers current UberLLM image and video models, reads each model's live request schema, checks the price with a... | Image & Creative Automation |
| [JuampiHernandez](https://github.com/JuampiHernandez) | [Firecrawl Alexandria](skills/firecrawl-alexandria/) | Firecrawl Alexandria gives coding agents a direct path to structured data through ready-made website workflows, data APIs, and... | Research & Scraping |
| [KhademOHAli1](https://github.com/KhademOHAli1) | [Investigative Journalism and Fact-Checking](skills/investigate-and-fact-check/) | Conduct public-interest investigative journalism, rigorous fact-checking, and open-source intelligence (OSINT) research. Use for verifying claims, quotes, documents, photographs... | Research & Scraping |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Coordinate a scoped code change through Oh My Claudecode team stages](skills/coordinate-a-scoped-code-change-through-oh-my-claudecode-team-stages/) | Run a bounded Claude Code team task through planning, delegated implementation, verification and repair, then return the change... | 40.9k | Templates & Workflows |
| [Audit local agent runs and select hook policies with Failproof AI](skills/audit-local-agent-runs-and-select-hook-policies-with-failproof-ai/) | Review local harness history, identify risky tool patterns, and prepare a source-backed policy-pack rollout across supported agent runtimes | 8.9k | Security & Verification |
| [Review Master CSS output regressions through MCP snapshots](skills/review-master-css-output-regressions-through-mcp-snapshots/) | Capture project CSS snapshots, trace missing classes, compare generated output, and propose scoped fixes with evidence from the... | 2.0k | Code Quality & Review |
| [Record and replay FrontMCP calls to catch server regressions](skills/record-and-replay-frontmcp-calls-to-catch-server-regressions/) | Capture baseline MCP calls as JSONL, replay them against a changed FrontMCP server, and review answer differences and... | 151 | Code Quality & Review |
| [Record an agent-completed browser task as a parameterized Oya playbook](skills/record-agent-browser-task-as-parameterized-oya-playbook/) | Complete a test browser task once, save its learned steps as an Oya playbook, and verify a replay... | 349 | Browser Automation |
| [Triage Lunora deployment errors and migration status through MCP](skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/) | Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff... | 293 | Runbooks & Diagnostics |
| [Assemble and review local video cuts through Concat MCP](skills/assemble-and-review-local-video-cuts-through-concat-mcp/) | Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and... | 16.0k | Media & Transcription |
| [Diagnose remote server incidents with MCP SSH Manager before changing services](skills/diagnose-remote-incidents-mcp-ssh-manager/) | Collect host health, service status, bounded logs and process evidence through SSH tools before proposing a scoped repair | 546 | Runbooks & Diagnostics |
| [Audit local coding-agent permissions and MCP configuration with Safe Anything](skills/audit-local-coding-agent-permissions-and-mcp-configuration-with-safe-anything/) | Review a selected project’s agent permissions, MCP launch pins, credentials and hooks with an offline scan and a... | 407 | Security & Verification |
| [Validate and report completed external workflow usage to LoopForge](skills/validate-and-report-completed-external-workflow-usage-to-loopforge/) | Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for... | 2.8k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 550 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 274 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 266 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 246 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 221 | Linting, code review, test generators, coverage |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 195 | Third-party API bridges, webhooks, service connectors |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 194 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 193 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 165 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 148 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 136 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 132 | Email automation, calendar management, task coordination |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 131 | Image generation, asset processing, design automation |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 129 | Web scraping, UI testing, headless browser control |
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
| 📋 **Published** | 3,287 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,690 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
