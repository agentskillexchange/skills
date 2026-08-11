<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C884-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C459-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,884 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[CSV Schema Validator & Auto-Fixer](skills/csv-schema-validator-auto-fixer/)** — Validates CSV files against JSON Schema definitions using AJV and csv-parse. Automatically detects and repairs type mismatches, missing required columns, and encoding issues with configurable strictness levels.

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
| [BRAINIALL Diarized Transcription](skills/brainiall-diarized-transcription/) | Transcribes one explicitly authorized Brazilian Portuguese or Spanish audio or video file through the metered BRAINIALL API, then... | - | Media & Transcription |
| [Manage Cross-Agent Skill Libraries with Skills Manager](skills/manage-cross-agent-skill-libraries-with-skills-manager/) | Use Skills Manager when an operator needs one auditable library for installing, inspecting, tagging, syncing, backing up, and... | 3.7k | Developer Tools |
| [Keep Agent Engineering Decisions Current with Haft](skills/keep-agent-engineering-decisions-current-with-haft/) | Use Haft when an agent needs source-backed decision framing, comparison, authorization records, and stale-evidence checks across supported coding-agent... | 1.4k | Developer Tools |
| [Run Specification-First Coding Workflows with Ouroboros](skills/run-specification-first-coding-workflows-with-ouroboros/) | Use Ouroboros when a coding agent should turn a vague request into a replayable spec, execute it across... | 5.4k | Developer Tools |
| [Unified AI System Gateway](skills/unified-ai-gateway/) | Turn plain-language requests into structured, reviewable prompts and inspect a self-hosted MCP gateway with provider-free defaults | - | Developer Tools |
| [Enforce Coding-Agent Write and Shell Policies with Probity](skills/enforce-coding-agent-write-and-shell-policies-with-probity/) | Use Probity when Claude Code, Codex, or GitHub Copilot CLI should be blocked from unsafe file writes or... | 162 | Security & Verification |
| [Prepare Evidence-Backed Open Source Contribution Proposals with ContribAI](skills/prepare-evidence-backed-open-source-contribution-proposals-with-contribai/) | Use ContribAI when an agent should analyze a repository, respect maintainer consent, and prepare bounded draft contribution proposals... | 246 | Code Quality & Review |
| [Design and Audit Agent Harnesses with Agents Best Practices](skills/design-and-audit-agent-harnesses-with-agents-best-practices/) | Use Agents Best Practices when an agent should produce concrete harness designs, permission models, memory plans, eval gates... | 2.2k | Templates & Workflows |
| [Stress-Test Research Papers Before Submission with PaperJury](skills/stress-test-research-papers-before-submission-with-paperjury/) | Use PaperJury when a Claude Code workflow should review a LaTeX research paper, classify reviewer-style objections, revise bounded... | 926 | Templates & Workflows |
| [Block Risky Coding-Agent Commands with CC Safety Net](skills/block-risky-coding-agent-commands-with-cc-safety-net/) | Use CC Safety Net when coding-agent CLIs need pre-execution hooks that block destructive commands, secret access, and unsafe... | 1.5k | Security & Verification |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Run open-source terminal coding workflows with Qwen Code](skills/run-open-source-terminal-coding-workflows-with-qwen-code/) | Use Qwen Code as a repeatable terminal coding agent: install the CLI, authenticate a provider, run interactive or... | 26.6k | Developer Tools |
| [Install Chinese-localized Superpowers workflows for coding agents](skills/install-chinese-localized-superpowers-workflows-for-coding-agents/) | Use superpowers-zh to install Chinese-localized coding-agent methods, China-specific development skills, and cross-tool setup for Claude Code, Codex, Cursor... | 7.2k | Templates & Workflows |
| [Block Risky Coding-Agent Commands with CC Safety Net](skills/block-risky-coding-agent-commands-with-cc-safety-net/) | Use CC Safety Net when coding-agent CLIs need pre-execution hooks that block destructive commands, secret access, and unsafe... | 1.5k | Security & Verification |
| [Install verified Codex planning and completion loops with LazyCodex](skills/install-verified-codex-planning-and-completion-loops-with-lazycodex/) | Add Codex commands, skills, hooks, diagnostics, and sub-agent roles for deep repository initialization, planning, execution, and evidence-backed completion | 2.8k | Developer Tools |
| [Enforce Coding-Agent Write and Shell Policies with Probity](skills/enforce-coding-agent-write-and-shell-policies-with-probity/) | Use Probity when Claude Code, Codex, or GitHub Copilot CLI should be blocked from unsafe file writes or... | 162 | Security & Verification |
| [Audit coding-agent token spend with CodeBurn](skills/audit-coding-agent-token-spend-with-codeburn/) | Run CodeBurn locally or as an MCP server so agents can inspect token usage, cost, model mix, project... | 8.7k | Monitoring & Alerts |
| [Keep coding agents from over-building implementations with Ponytail](skills/keep-coding-agents-from-over-building-implementations-with-ponytail/) | Ponytail gives coding agents a portable minimal-implementation ruleset, plugin hooks, and review commands so they reuse existing code... | 85.5k | Code Quality & Review |
| [Bridge local coding agents into chat apps with cc-connect](skills/bridge-local-coding-agents-into-chat-apps-with-cc-connect/) | Let operators control local Claude Code, Codex, Cursor, Gemini CLI, and other coding agents from Slack, Discord, Telegram... | 14.2k | Integrations & Connectors |
| [Control Blender Scenes from MCP Agents with BlenderMCP](skills/control-blender-scenes-from-mcp-agents-with-blendermcp/) | Use BlenderMCP when an MCP-capable agent needs to inspect, create, and modify Blender scenes through a controlled Blender... | 25.6k | Integrations & Connectors |
| [Design and Audit Agent Harnesses with Agents Best Practices](skills/design-and-audit-agent-harnesses-with-agents-best-practices/) | Use Agents Best Practices when an agent should produce concrete harness designs, permission models, memory plans, eval gates... | 2.2k | Templates & Workflows |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 426 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 243 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 233 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 217 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 198 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 177 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 160 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 152 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 126 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 124 | SDK docs, API parsers, symbol resolvers |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 124 | Web research, content discovery, data collection |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 121 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 107 | Audio/video processing, speech-to-text |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 102 | Image generation, asset processing, design automation |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 87 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,884 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,459 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
