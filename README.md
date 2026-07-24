<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C801-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C396-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,801 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[ESLint Rule Violation Summarizer](skills/eslint-rule-violation-summarizer-2/)** — Runs ESLint against a JS/TS codebase, groups violations by rule and file, and produces a prioritized fix plan. Distinguishes auto-fixable violations from manual ones. Outputs Markdown for GitHub…

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
| [Run generative media agent recipes with MuAPI Skills](skills/run-generative-media-agent-recipes-with-muapi-skills/) | Use Generative Media Skills when an agent should turn a creative brief into repeatable image, video, audio, product-ad... | 3.9k | Image & Creative Automation |
| [Manage CLI coding-agent sessions with Claude Code Tools](skills/manage-cli-coding-agent-sessions-with-claude-code-tools/) | Use Claude Code Tools when an operator needs installable CLI utilities, hooks, skills, and plugins for session management... | 1.9k | Developer Tools |
| [Trace coding agent API traffic locally with Claude Tap](skills/trace-coding-agent-api-traffic-locally-with-claude-tap/) | Run Claude Code, Codex CLI, Gemini CLI, Cursor CLI, OpenCode, and related coding agents through a local proxy... | 2.6k | Monitoring & Alerts |
| [Run ecommerce operator skills across marketplace workflows](skills/run-ecommerce-operator-skills-across-marketplace-workflows/) | Use eCommerce-Skills to give compatible agents plain-text workflows for product research, listing optimization, review analysis, pricing, marketing, supply-chain... | 458 | Templates & Workflows |
| [Manage cross-agent skill files from Obsidian with Agentfiles](skills/manage-cross-agent-skill-files-from-obsidian-with-agentfiles/) | Use Agentfiles when an operator wants to browse, create, edit, install, and audit skills, commands, agents, rules, memories... | 679 | Developer Tools |
| [Install Chinese-localized Superpowers workflows for coding agents](skills/install-chinese-localized-superpowers-workflows-for-coding-agents/) | Use superpowers-zh to install Chinese-localized coding-agent methods, China-specific development skills, and cross-tool setup for Claude Code, Codex, Cursor... | 7.2k | Templates & Workflows |
| [Give teams shared coding-agent memory with Stash](skills/give-teams-shared-coding-agent-memory-with-stash/) | Connect coding agents to a shared Stash knowledge base so sessions, files, pages, and team context can be... | 246 | Developer Tools |
| [Develop Power BI and Fabric artifacts with agent plugins](skills/develop-power-bi-and-fabric-artifacts-with-agent-plugins/) | Install Power BI and Microsoft Fabric plugins so Claude Code can author, validate, and review PBIP, TMDL, DAX... | 801 | Developer Tools |
| [Run bioinformatics analysis workflows with bioSkills](skills/run-bioinformatics-analysis-workflows-with-bioskills/) | Use bioSkills to give an agent domain-specific bioinformatics procedures, tool choices, and guardrails for omics analysis workflows | 1.1k | Templates & Workflows |
| [Draft and audit LinkedIn content with LinkedIn Skills](skills/draft-and-audit-linkedin-content-with-linkedin-skills/) | Use LinkedIn Skills when an agent needs to draft posts, comments, replies, audits, profile rewrites, or content plans... | 420 | Content Writing & SEO |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Audit coding-agent token spend with CodeBurn](skills/audit-coding-agent-token-spend-with-codeburn/) | Run CodeBurn locally or as an MCP server so agents can inspect token usage, cost, model mix, project... | 8.7k | Monitoring & Alerts |
| [Install Chinese-localized Superpowers workflows for coding agents](skills/install-chinese-localized-superpowers-workflows-for-coding-agents/) | Use superpowers-zh to install Chinese-localized coding-agent methods, China-specific development skills, and cross-tool setup for Claude Code, Codex, Cursor... | 7.2k | Templates & Workflows |
| [Coordinate visible multi-agent CLI workspaces with CCB](skills/coordinate-visible-multi-agent-cli-workspaces-with-ccb/) | Use CCB to run Codex, Claude, Gemini, Cursor, OpenCode, and other CLI agents in a visible project workspace... | 3.2k | Developer Tools |
| [Bridge local coding agents into chat apps with cc-connect](skills/bridge-local-coding-agents-into-chat-apps-with-cc-connect/) | Let operators control local Claude Code, Codex, Cursor, Gemini CLI, and other coding agents from Slack, Discord, Telegram... | 14.2k | Integrations & Connectors |
| [Install verified Codex planning and completion loops with LazyCodex](skills/install-verified-codex-planning-and-completion-loops-with-lazycodex/) | Add Codex commands, skills, hooks, diagnostics, and sub-agent roles for deep repository initialization, planning, execution, and evidence-backed completion | 2.8k | Developer Tools |
| [Run OpenCode specialist-agent workflows with Oh My Opencode Slim](skills/run-opencode-specialist-agent-workflows-with-oh-my-opencode-slim/) | Install an OpenCode orchestration plugin that routes codebase work across specialist agents, background tasks, model presets, bundled skills... | 7.0k | Templates & Workflows |
| [Review agent-authored diffs with Hunk](skills/review-agent-authored-diffs-with-hunk/) | Use Hunk to keep a live terminal review UI open for agent-authored code changes, with Git, Jujutsu, Sapling... | 6.9k | Code Quality & Review |
| [Keep coding agents from over-building implementations with Ponytail](skills/keep-coding-agents-from-over-building-implementations-with-ponytail/) | Ponytail gives coding agents a portable minimal-implementation ruleset, plugin hooks, and review commands so they reuse existing code... | 85.5k | Code Quality & Review |
| [Run generative media agent recipes with MuAPI Skills](skills/run-generative-media-agent-recipes-with-muapi-skills/) | Use Generative Media Skills when an agent should turn a creative brief into repeatable image, video, audio, product-ad... | 3.9k | Image & Creative Automation |
| [Inspect BullMQ agent job queues with Bull Board](skills/inspect-bullmq-agent-job-queues-with-bull-board/) | Use Bull Board to add a protected dashboard for Bull and BullMQ queues so operators can inspect, retry... | 3.4k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 392 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 239 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 220 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 216 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 194 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 175 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 154 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 152 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 126 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 124 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 120 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 118 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 105 | Audio/video processing, speech-to-text |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 96 | Image generation, asset processing, design automation |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 83 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,801 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,396 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
