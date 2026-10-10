<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C121-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C602-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,121 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[ESLint Rule Analyzer and Fixer](skills/eslint-rule-analyzer-fixer/)** — Performs deep ESLint configuration analysis using the ESLint Node.js API and flat config system. Auto-fixes rule conflicts, generates shareable configs, and produces code quality trend reports.

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
| [Deploy a private local agent stack with Self-Hosted AI Stack](skills/deploy-private-local-agent-stack-with-self-hosted-ai-stack/) | Stand up a local-first Docker Compose backend for agent work: LLM routing, chat, document parsing, embeddings, speech, and... | 163 | Developer Tools |
| [Control coding-agent terminals remotely with 9Remote](skills/control-coding-agent-terminals-remotely-with-9remote/) | Run and supervise Claude Code, Codex, Gemini CLI, and other terminal agents from a browser, desktop app, tablet... | 161 | Developer Tools |
| [Monitor Claude Code sessions with ccstatusline](skills/monitor-claude-code-sessions-with-ccstatusline/) | Configure Claude Code's status line with live model, token, cost, git, sandbox, cache, CI, and session health signals... | 13.2k | Developer Tools |
| [Run agentic quality engineering checks with Agentic QE](skills/run-agentic-quality-engineering-checks-with-agentic-qe/) | Configure Agentic QE in a repository so a coding agent can generate tests, inspect coverage gaps, investigate flaky... | 495 | Code Quality & Review |
| [Run code-generated short-film workflows with Lemo-Opuscar](skills/direct-code-generated-short-films-with-lemo-opuscar-styles/) | Use a Claude Code plugin to turn a story brief into a short film project built from reusable... | 1.5k | Image & Creative Automation |
| [Run Amazon marketplace research workflows through Sorftime MCP skills](skills/run-amazon-marketplace-research-workflows-through-sorftime-mcp-skills/) | Use a set of Amazon marketplace research skills to analyze ASINs, categories, keywords, reviews, listings, traffic, and advertising... | 954 | Research & Scraping |
| [Run multi-provider terminal coding sessions with Snow CLI](skills/run-multi-provider-terminal-coding-sessions-with-snow-cli/) | Use Snow CLI as a terminal coding agent that can route repository work through OpenAI, Gemini, Claude, DeepSeek... | 1.1k | Developer Tools |
| [Regression-test coding agents and skills with Coder Eval](skills/regression-test-coding-agents-and-skills-with-coder-eval/) | Run sandboxed YAML evaluation suites against Claude Code, Codex, Gemini, OpenCode, or Pi agents, then gate CI on... | 151 | Code Quality & Review |
| [Run RFC-driven product planning with AI PRD Workflow before agents code](skills/run-rfc-driven-product-planning-with-ai-prd-workflow-before-agents-code/) | Guide coding agents from idea or existing codebase through PRD, features, rules, RFCs, implementation, review, and workflow-status checks | 298 | Templates & Workflows |
| [Generate consistent hand-drawn image prompts with Hand Drawn Styles](skills/generate-consistent-hand-drawn-image-prompts-with-hand-drawn-styles/) | Apply verified hand-drawn style recipes to a subject so an agent can output clean, reusable prompts or production... | 2.0k | Image & Creative Automation |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [dskuldeep](https://github.com/dskuldeep) | [Work an SEO and AI-Visibility Backlog with LogNorm](skills/lognorm-seo-geo-backlog/) | Use LogNorm when Claude Code, Codex or Cursor should work a site's SEO and AI-visibility (GEO) backlog through... | Content Writing & SEO |
| [xiehuan123](https://github.com/xiehuan123) | [Browser Extension Launch](skills/browser-extension-launch/) | Turns a plain-language idea into a tested Chrome Manifest V3 extension, release bundle, store materials, and a resumable... | Templates & Workflows |
| [OssaBellator](https://github.com/OssaBellator) | [MCP Workflow Audit](skills/mcp-workflow-audit/) | Audit Claude Code, MCP, and AI-agent workflows for permissions, consequential actions, idempotency, failure recovery, verification, and operator handoff | Developer Tools |
| [Pangolin-spg](https://github.com/Pangolin-spg) | [Pangolinfo AI SERP](skills/pangolinfo-ai-serp/) | Retrieve structured Google SERP and AI Overviews, run AI Mode follow-up queries, and optionally capture screenshots through Pangolinfo... | Research & Scraping |
| [Pangolin-spg](https://github.com/Pangolin-spg) | [Pangolinfo Amazon Scraper](skills/pangolinfo-amazon-scraper/) | Retrieve structured Amazon product, keyword search, category, seller and bestseller data with Pangolinfo APIs for e-commerce research and... | Research & Scraping |
| [uglyrobot](https://github.com/uglyrobot) | [DocsBot Administration](skills/docsbot-administration/) | Administer DocsBot bots, knowledge sources, teams, and reporting through named MCP tools with browser OAuth and live role... | Integrations & Connectors |
| [jacobwell](https://github.com/jacobwell) | [Eye.Art Polyphemus Image Creation](skills/eye-art-polyphemus/) | Use Eye.Art Polyphemus as a no-key hosted MCP for conversational image creation, reference-preserving edits, artist-guided art, site-matched visuals... | Image & Creative Automation |
| [makoncline](https://github.com/makoncline) | [Read Ledger](skills/read-ledger/) | Track research source and text-range coverage across contexts using JSONL snapshots, SHA-256 hashes, Unicode code-point offsets, and bounded... | Research & Scraping |
| [SheriffMD](https://github.com/SheriffMD) | [WebAsk Results Digest](skills/webask-results-digest/) | Summarize WebAsk survey distributions, filtered reports and free-text answers with get_quiz_summary, get_quiz_report and get_quiz_report_inputs. Use for survey findings... | Data Extraction & Transformation |
| [OlyaTi](https://github.com/OlyaTi) | [Mnemoverse Memory MCP](skills/mnemoverse-memory-mcp/) | Give Claude Code, Cursor, VS Code and ChatGPT agents hosted persistent memory over MCP that learns from outcomes... | Integrations & Connectors |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Coordinate agent teams and governed work in Paperclip](skills/coordinate-agent-teams-and-governed-work-in-paperclip/) | Use Paperclip as a self-hosted control plane for assigning goals, tasks, budgets, approvals, routines, and run history across... | 98.2k | Templates & Workflows |
| [Monitor Claude Code sessions with ccstatusline](skills/monitor-claude-code-sessions-with-ccstatusline/) | Configure Claude Code's status line with live model, token, cost, git, sandbox, cache, CI, and session health signals... | 13.2k | Developer Tools |
| [Run a Docling API server for agent document conversion](skills/run-a-docling-api-server-for-agent-document-conversion/) | Deploy Docling API so agents can convert PDFs, Office files, images, HTML, CSV, and other documents into Markdown... | 1.7k | Data Extraction & Transformation |
| [Run IDE-wired terminal coding-agent workflows with Oh My Pi](skills/run-ide-wired-terminal-coding-agent-workflows-with-oh-my-pi/) | Use Oh My Pi when an operator wants a local terminal coding agent with IDE-grade context, built-in file... | 31.8k | Developer Tools |
| [Build TypeScript spreadsheet import and export workflows with hucre](skills/build-typescript-spreadsheet-import-and-export-workflows-with-hucre/) | Use hucre when a coding agent needs to add zero-dependency XLSX, CSV, ODS, JSON, NDJSON, or XML spreadsheet... | 2.2k | Data Extraction & Transformation |
| [Reverse-engineer apps and binaries with REA](skills/reverse-engineer-apps-and-binaries-with-rea/) | Connect coding agents to REA's MCP tools so they can inspect apps, binaries, websites, APKs, and runtime behavior... | 17.1k | Security & Verification |
| [Schedule Node Agent Jobs with node-cron](skills/schedule-node-agent-jobs-with-node-cron/) | Use node-cron to add recurring background jobs to Node.js agent services with overlap prevention, distributed coordination, background task... | 3.3k | Templates & Workflows |
| [Compile agent-ready documentation bundles with docmd](skills/compile-agent-ready-documentation-bundles-with-docmd/) | Use docmd when a project needs one Markdown documentation source to produce a site, search index, llms.txt, MCP... | 2.5k | Library & API Reference |
| [Run agentic quality engineering checks with Agentic QE](skills/run-agentic-quality-engineering-checks-with-agentic-qe/) | Configure Agentic QE in a repository so a coding agent can generate tests, inspect coverage gaps, investigate flaky... | 495 | Code Quality & Review |
| [Visualize OpenTelemetry agent traces with Agent Prism](skills/visualize-opentelemetry-agent-traces-with-agent-prism/) | Add Agent Prism's React trace viewer to inspect LLM calls, tool executions, retries, and agent workflows from OpenTelemetry... | 393 | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 520 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 264 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 254 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 229 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 206 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 179 | Third-party API bridges, webhooks, service connectors |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 178 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 162 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 138 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 130 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 128 | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 126 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 116 | Image generation, asset processing, design automation |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 109 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 95 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 3,121 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,602 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
