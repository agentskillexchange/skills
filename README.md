<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C785-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C385-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,785 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Run Parallel Divergent Ideation With ADHD](skills/run-parallel-divergent-ideation-with-adhd/)** — Use ADHD to fan out isolated reasoning branches for open-ended coding-agent decisions, then score, prune, and deepen the strongest options.

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
| [Run Agent-Assisted Notebook Workflows in JupyterLab With Notebook Intelligence](skills/run-agent-assisted-notebook-workflows-in-jupyterlab-with-notebook-intelligence/) | Use Notebook Intelligence to add chat, inline edit, autocomplete, MCP tools, Claude Code mode, and coding-agent launchers directly... | 322 | Developer Tools |
| [Coordinate Terminal Coding Agents With hcom](skills/coordinate-terminal-coding-agents-with-hcom/) | Use hcom to launch, message, watch, fork, and coordinate multiple terminal coding agents across Claude Code, Codex, Gemini... | 393 | Developer Tools |
| [Run Spec-Driven Agent Changes With OSpec](skills/run-spec-driven-agent-changes-with-ospec/) | Use OSpec to turn a coding request into a repo-persisted spec workflow with initialization, change advancement, verification evidence... | 524 | Templates & Workflows |
| [Index Large Codebases for Agent Search With Socraticode](skills/index-large-codebases-for-agent-search-with-socraticode/) | Use Socraticode to give coding agents a local codebase-intelligence layer for semantic search, dependency graphs, impact analysis, and... | 3.1k | Developer Tools |
| [Route Codex and Claude Code through an opencodex provider proxy](skills/route-codex-and-claude-code-through-an-opencodex-provider-proxy/) | Run a local proxy that lets Codex and Claude Code use configured LLM providers, routed models, and account... | 1.3k | Developer Tools |
| [Coordinate peer CLI agents with agmsg](skills/coordinate-peer-cli-agents-with-agmsg/) | Let Claude Code, Codex, Gemini CLI, Copilot CLI, and other terminal agents exchange messages through a shared local... | 1.3k | Developer Tools |
| [Govern coding-agent discovery and delivery through a project-local GAAI backlog](skills/govern-coding-agent-discovery-and-delivery-through-a-project-local-gaai-backlog/) | Drop a `.gaai/` folder into a project so agents separate scope discovery from isolated delivery, with acceptance criteria... | 152 | Templates & Workflows |
| [Run Apple-platform coding audits, diagnostics, and simulator checks with Axiom](skills/run-apple-platform-coding-audits-diagnostics-and-simulator-checks-with-axiom/) | Add Axiom's Apple OS skills, agents, and commands so coding assistants can diagnose Xcode builds, Swift issues, crashes... | 1.1k | Developer Tools |
| [Plan, draft, publish, and review social posts from Claude Code with social-post](skills/plan-draft-publish-and-review-social-posts-from-claude-code-with-social-post/) | Install a Claude Code skill that learns a user's social voice, builds a 14-day content calendar, drafts posts... | 555 | Developer Tools |
| [Turn Agent Corrections Into Durable Skills With claude-smart](skills/turn-agent-corrections-into-durable-skills-with-claude-smart/) | Use claude-smart to capture corrections and working patterns as preferences, project skills, and shared skills that Claude Code... | 748 | Templates & Workflows |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Run OpenCode specialist-agent workflows with Oh My Opencode Slim](skills/run-opencode-specialist-agent-workflows-with-oh-my-opencode-slim/) | Install an OpenCode orchestration plugin that routes codebase work across specialist agents, background tasks, model presets, bundled skills... | 7.0k | Templates & Workflows |
| [Bridge local coding agents into chat apps with cc-connect](skills/bridge-local-coding-agents-into-chat-apps-with-cc-connect/) | Let operators control local Claude Code, Codex, Cursor, Gemini CLI, and other coding agents from Slack, Discord, Telegram... | 14.2k | Integrations & Connectors |
| [Audit coding-agent token spend with CodeBurn](skills/audit-coding-agent-token-spend-with-codeburn/) | Run CodeBurn locally or as an MCP server so agents can inspect token usage, cost, model mix, project... | 8.7k | Monitoring & Alerts |
| [Route Codex and Claude Code through an opencodex provider proxy](skills/route-codex-and-claude-code-through-an-opencodex-provider-proxy/) | Run a local proxy that lets Codex and Claude Code use configured LLM providers, routed models, and account... | 1.3k | Developer Tools |
| [Review agent-authored diffs with Hunk](skills/review-agent-authored-diffs-with-hunk/) | Use Hunk to keep a live terminal review UI open for agent-authored code changes, with Git, Jujutsu, Sapling... | 6.9k | Code Quality & Review |
| [Route large codebase analysis through Gemini MCP Tool](skills/route-large-codebase-analysis-through-gemini-mcp-tool/) | Use Gemini MCP Tool to let MCP-capable coding agents delegate large file and codebase analysis to Gemini or... | 2.3k | Developer Tools |
| [Inspect BullMQ agent job queues with Bull Board](skills/inspect-bullmq-agent-job-queues-with-bull-board/) | Use Bull Board to add a protected dashboard for Bull and BullMQ queues so operators can inspect, retry... | 3.4k | Monitoring & Alerts |
| [Run Spec-Driven Agent Changes With OSpec](skills/run-spec-driven-agent-changes-with-ospec/) | Use OSpec to turn a coding request into a repo-persisted spec workflow with initialization, change advancement, verification evidence... | 524 | Templates & Workflows |
| [Drive ComfyUI generation workflows through comfyui-mcp](skills/drive-comfyui-generation-workflows-through-comfyui-mcp/) | Use comfyui-mcp to let an MCP-capable agent author, run, debug, and manage ComfyUI image, video, audio, model, and... | 386 | Image & Creative Automation |
| [Use Apify MCP for agent web extraction](skills/use-apify-mcp-for-agent-web-extraction/) | Use the Apify MCP server to let MCP-compatible agents run Apify Actors for structured extraction from search, maps... | 2.0k | Research & Scraping |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 386 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 239 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 217 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 216 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 194 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 175 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 153 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 151 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 126 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 124 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 120 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 118 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 105 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 94 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 80 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,785 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,385 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
