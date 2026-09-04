<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C965-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C514-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,965 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[esbuild Ultra-Fast JavaScript Bundler](skills/esbuild-ultra-fast-javascript-bundler/)** — esbuild is an extremely fast JavaScript and TypeScript bundler written in Go that delivers 10-100x faster build times than traditional tools like webpack. It handles bundling, minification, tree…

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
| [Render pull request architecture diagrams with PR Lens](skills/render-pull-request-architecture-diagrams-with-pr-lens/) | Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs... | 212 | Code Quality & Review |
| [BulkPublish Social Publishing](skills/bulkpublish-social-publishing/) | Adapt, review, schedule, and publish approved social content across multiple platforms through the BulkPublish API and hosted MCP | - | Integrations & Connectors |
| [Constrain coding-agent over-defense with HERO](skills/constrain-coding-agent-over-defense-with-hero/) | Paste HERO's scope-limits contract into always-loaded agent config so coding agents keep fixes proportionate and avoid unnecessary hashing... | 397 | Templates & Workflows |
| [Run one-shot and supervised browser automation workflows with AIHawk](skills/run-one-shot-and-supervised-browser-automation-workflows-with-aihawk/) | Use AIHawk when an agent needs a real browser for bounded web research, extraction, and task execution with... | 30.3k | Browser Automation |
| [Keep Claude Code skills current from real sessions with Autoharness](skills/keep-claude-code-skills-current-from-real-sessions-with-autoharness/) | Install Autoharness so Claude Code can distill, merge, update, and retire native skills from real operator sessions without... | 1.4k | Developer Tools |
| [Aperture Wallet Guide](skills/aperture-wallet-guide/) | Answer Aperture Wallet questions from first-party product, security, network, release, app-screen, and Journal sources while enforcing explicit wallet-secret... | - | Library & API Reference |
| [Pronounce Developer Jargon](skills/pronounce-developer-jargon/) | Answers short pronunciation questions about developer tools, AI models, acronyms, and project names by using the say-it CLI... | - | Developer Tools |
| [Run Chinese-first academic writing, Office, and scientific workflows with Academic Skills](skills/run-chinese-first-academic-writing-office-and-scientific-workflows-with-academic-skills/) | Install and invoke a Chinese-first academic skill bundle for paper writing, editable Word/PPT research documents, and scientific computing... | 3.4k | Templates & Workflows |
| [Rebuild public websites from evidence snapshots with website-rebuild-skill](skills/rebuild-public-websites-from-evidence-snapshots-with-website-rebuild-skill/) | Use website-rebuild-skill when an agent needs to classify a public site, capture a read-only evidence mirror, reconstruct behavior... | 656 | Developer Tools |
| [Prepare Indian ITR filings with deterministic tax checks through itr-wala](skills/prepare-indian-itr-filings-with-deterministic-tax-checks-through-itr-wala/) | Use itr-wala when an agent needs a review-first workflow for reading Indian tax documents, running deterministic AY 2026-27... | 839 | Templates & Workflows |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [azeemkafridi](https://github.com/azeemkafridi) | [BulkPublish Social Publishing](skills/bulkpublish-social-publishing/) | Adapt, review, schedule, and publish approved social content across multiple platforms through the BulkPublish API and hosted MCP | Integrations & Connectors |
| [devdasx](https://github.com/devdasx) | [Aperture Wallet Guide](skills/aperture-wallet-guide/) | Answer Aperture Wallet questions from first-party product, security, network, release, app-screen, and Journal sources while enforcing explicit wallet-secret... | Library & API Reference |
| [anzy-renlab-ai](https://github.com/anzy-renlab-ai) | [Pronounce Developer Jargon](skills/pronounce-developer-jargon/) | Answers short pronunciation questions about developer tools, AI models, acronyms, and project names by using the say-it CLI... | Developer Tools |
| [TianHengZhuang](https://github.com/TianHengZhuang) | [SandBase MCP](skills/sandbase-mcp/) | Access 2,000+ AI models and API tools through one MCP interface for inference, media generation, search, scraping, embeddings... | Integrations & Connectors |
| [liangfeng-hu](https://github.com/liangfeng-hu) | [Proofed Completion Gate](skills/proofed-completion-gate/) | Uses the Proofed CLI and current-subject completion receipts to reject unsupported coding-agent completion claims, rerun repository-configured tests, and... | Security & Verification |
| [haoranyu](https://github.com/haoranyu) | [Clean Closed Issue Worktrees](skills/clean-closed-issue-worktrees/) | Safely audits and removes Git worktrees linked to closed GitHub or GitLab issues with a mandatory scan-confirm-execute protocol... | Developer Tools |
| [TinyOps Studio LLC](https://github.com/tinyopsstudio) | [Automation Integration Preflight](skills/automation-integration-preflight/) | Assess a public HTTP(S) page before building browser automation, extraction, or an integration. Use this skill to collect... | Integrations & Connectors |
| [pranshuchittora](https://github.com/pranshuchittora) | [Author and Run Regression Tests with Agent QA](skills/author-and-run-regression-tests-with-agent-qa/) | Use Agent QA's CLI and MCP server to author, validate, run, debug, and triage natural-language web and mobile... | Browser Automation |
| [kantorcodes](https://github.com/kantorcodes) | [HOL Guard](skills/hol-guard/) | Protect local AI coding-agent harnesses before tools run, review approvals and evidence, and scan agent plugins, skills, MCP... | Security & Verification |
| [giltotherescue](https://github.com/giltotherescue) | [Slashbooks](skills/slashbooks/) | Replace QuickBooks with an AI agent you control: import bank and credit card activity, categorize and reconcile transactions... | Calendar, Email & Productivity |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Automate NotebookLM Studio generation and cited research batches with notebooklm-mcp](skills/automate-notebooklm-studio-generation-and-cited-research-batches-with-notebooklm-mcp/) | Use NotebookLM through MCP or a local REST API to run cited Q&A, generate Studio artifacts, and manage... | 161 | Research & Scraping |
| [Manage parallel coding agent sessions and worktrees with CCManager](skills/manage-parallel-coding-agent-sessions-and-worktrees-with-ccmanager/) | Run Claude Code, Codex CLI, Gemini CLI, Cursor Agent, Copilot CLI, Cline CLI, OpenCode, Kimi CLI, and related... | 1.2k | Developer Tools |
| [Run independent multi-agent build and review flows with OPC](skills/run-independent-multi-agent-build-and-review-flows-with-opc/) | Use OPC as a Claude Code skill to select a task flow, dispatch specialist roles, enforce independent review... | 192 | Code Quality & Review |
| [Render pull request architecture diagrams with PR Lens](skills/render-pull-request-architecture-diagrams-with-pr-lens/) | Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs... | 212 | Code Quality & Review |
| [Run CodeWhale terminal coding agent workflows](skills/run-codewhale-terminal-coding-agent-workflows/) | Use CodeWhale as a local terminal coding agent for repository edits, test repair, provider-switched sessions, approval-gated commands, MCP... | 40.8k | Developer Tools |
| [Run one-shot and supervised browser automation workflows with AIHawk](skills/run-one-shot-and-supervised-browser-automation-workflows-with-aihawk/) | Use AIHawk when an agent needs a real browser for bounded web research, extraction, and task execution with... | 30.3k | Browser Automation |
| [Enforce Coding-Agent Write and Shell Policies with Probity](skills/enforce-coding-agent-write-and-shell-policies-with-probity/) | Use Probity when Claude Code, Codex, or GitHub Copilot CLI should be blocked from unsafe file writes or... | 162 | Security & Verification |
| [Build production-ready n8n workflows with n8n-skills](skills/build-production-ready-n8n-workflows-with-n8n-skills/) | Give Claude Code a routed skill pack for designing, validating, debugging, and deploying n8n workflows through n8n-mcp | 6.2k | Templates & Workflows |
| [Run Chinese-first academic writing, Office, and scientific workflows with Academic Skills](skills/run-chinese-first-academic-writing-office-and-scientific-workflows-with-academic-skills/) | Install and invoke a Chinese-first academic skill bundle for paper writing, editable Word/PPT research documents, and scientific computing... | 3.4k | Templates & Workflows |
| [Block Risky Coding-Agent Commands with CC Safety Net](skills/block-risky-coding-agent-commands-with-cc-safety-net/) | Use CC Safety Net when coding-agent CLIs need pre-execution hooks that block destructive commands, secret access, and unsafe... | 1.5k | Security & Verification |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 460 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 247 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 239 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 220 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 200 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 178 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 167 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 155 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 128 | Web research, content discovery, data collection |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 127 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 127 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 123 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 109 | Audio/video processing, speech-to-text |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 108 | Image generation, asset processing, design automation |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 90 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,965 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,514 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
