<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C636-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C274-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,636 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Swagger UI Documentation Deployer](skills/swagger-ui-documentation-deployer/)** — Deploys interactive Swagger UI documentation sites from OpenAPI specs with custom branding, authentication presets, and CDN-hosted static builds. Integrates with Redoc for alternative rendering.

_Rotates daily across downloaded, starred, recent, verified, and industry-curated skills._

---

## Industry Collections

Curated skill sets organized by industry vertical:

| | Collection | Description |
|---|---|---|
| 🎙️ | [**Media & Publishing Systems**](industries/media-publishing-systems.md) | Transcription, subtitles, podcast workflows, chaptering, localization, loudness cleanup, and final-mile publishing prep. |
| 💼 | [**Finance & Filings**](industries/finance-filings.md) | Filings research, invoice intake, billing operations, reconciliation, and finance-adjacent reporting. |
| 🛒 | [**Ecommerce & Retail Operations**](industries/ecommerce-retail-operations.md) | Catalog management, storefront automation, orders, inventory sync, marketplace support, and review-driven merchandising. |
| ⚖️ | [**Legal Ops & Compliance**](industries/legal-ops-compliance.md) | Contract workflows, forms, document review, archive search, and evidence-oriented legal and compliance support. |
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
| [Add multimodal lifelong memory to MCP and Python agents with SimpleMem](skills/add-multimodal-lifelong-memory-to-mcp-and-python-agents-with-simplemem/) | Use SimpleMem to store, compress, index, and retrieve text or multimodal memories for agents through MCP or Python... | 3.5k | Integrations & Connectors |
| [Build multimodal retrieval context layers with Deep Lake](skills/build-multimodal-retrieval-context-layers-with-deep-lake/) | Store raw multimodal data, embeddings, and vector-search indexes in Deep Lake so agents can retrieve grounded context for... | 9.2k | Data Extraction & Transformation |
| [Parse multi-format RAG inputs with OmniParse](skills/parse-multi-format-rag-inputs-with-omniparse/) | Run OmniParse locally or as an API service to turn documents, images, audio, video, and web pages into... | 7.6k | Data Extraction & Transformation |
| [Parse agent-ready PDFs and document images with MonkeyOCR](skills/parse-agent-ready-pdfs-and-document-images-with-monkeyocr/) | Run MonkeyOCR over PDFs, scanned pages, formulas, and tables to produce structured Markdown/text that downstream agents can ingest... | 6.6k | Data Extraction & Transformation |
| [Expose database APIs and SQL MCP tools with Azure Data API Builder](skills/expose-database-apis-and-sql-mcp-tools-with-azure-data-api-builder/) | Use Azure Data API Builder to generate secure REST, GraphQL, and SQL MCP access for supported databases so... | 1.4k | Integrations & Connectors |
| [Build and debug AI pipelines in an IDE with RocketRide](skills/build-and-debug-ai-pipelines-in-an-ide-with-rocketride/) | Use RocketRide to compose, run, observe, and deploy portable AI pipelines from an IDE or CLI across model... | 3.9k | Developer Tools |
| [Index codebases into MCP knowledge graphs with codebase-memory-mcp](skills/index-codebases-into-mcp-knowledge-graphs-with-codebase-memory-mcp/) | Give coding agents a local MCP code intelligence graph for fast architecture, symbol, route, impact, and call-path queries... | 7.3k | Integrations & Connectors |
| [Build Go MCP servers with MCP Go](skills/build-go-mcp-servers-with-mcp-go/) | Use MCP Go to implement typed Model Context Protocol servers in Go that expose tools, resources, prompts, and... | 8.8k | Integrations & Connectors |
| [Hermes Tweet](skills/hermes-tweet/) | Use Hermes Tweet when Hermes Agent needs a native X/Twitter plugin for reading posts, exploring public data, and... | 10 | Integrations & Connectors |
| [Run TypeScript-native LLM eval suites with Evalite](skills/run-typescript-native-llm-eval-suites-with-evalite/) | Use Evalite when a TypeScript team needs repeatable Vitest-style eval runs for LLM apps before prompt, model, or... | 1.6k | Code Quality & Review |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Run DeepSeek-oriented terminal coding workflows with Reasonix](skills/run-deepseek-oriented-terminal-coding-workflows-with-reasonix/) | Use Reasonix when an operator wants a persistent terminal coding agent tuned for DeepSeek-style prefix caching, project memory... | 21.8k | Developer Tools |
| [Coordinate multi-agent Claude Code and Codex workflows with Ruflo](skills/coordinate-multi-agent-claude-code-and-codex-workflows-with-ruflo/) | Install Ruflo when an operator needs Claude Code or Codex agents to coordinate swarms, memory, hooks, and MCP... | 59.0k | Templates & Workflows |
| [Build managed document parsing pipelines with LlamaCloud Services](skills/build-managed-document-parsing-pipelines-with-llamacloud-services/) | Use LlamaCloud Services to parse, index, and manage document knowledge pipelines that feed LlamaIndex retrieval and agent workflows | 4.2k | Data Extraction & Transformation |
| [Extract OCR-ready Markdown from documents with Zerox](skills/extract-ocr-ready-markdown-from-documents-with-zerox/) | Use Zerox to convert PDFs, images, and office documents into Markdown or structured extraction outputs using vision models | 12.2k | Data Extraction & Transformation |
| [Build portable single-file agent memory with Memvid](skills/build-portable-single-file-agent-memory-with-memvid/) | Use Memvid when an agent needs local, portable long-term memory and retrieval without running a vector database or... | 15.7k | Integrations & Connectors |
| [Trace coding-agent and LLM workflows with OpenLIT](skills/trace-coding-agent-and-llm-workflows-with-openlit/) | Use OpenLIT to instrument coding agents and LLM applications with OpenTelemetry traces, metrics, costs, prompts, tool calls, and... | 2.5k | Monitoring & Alerts |
| [Index codebases into MCP knowledge graphs with codebase-memory-mcp](skills/index-codebases-into-mcp-knowledge-graphs-with-codebase-memory-mcp/) | Give coding agents a local MCP code intelligence graph for fast architecture, symbol, route, impact, and call-path queries... | 7.3k | Integrations & Connectors |
| [Run durable agent tasks and event-driven workflows with Hatchet](skills/run-durable-agent-tasks-and-event-driven-workflows-with-hatchet/) | Use Hatchet to queue, retry, pause, resume, observe, and scale long-running agent tasks and background workflows | 7.2k | Templates & Workflows |
| [Embed an in-page GUI agent with Page Agent](skills/embed-an-in-page-gui-agent-with-page-agent/) | Add a JavaScript GUI agent to a web app so users or agents can complete UI tasks through... | 18.6k | Browser Automation |
| [Run local Pi coding-agent workflows with sandbox and session-sharing guardrails](skills/run-local-pi-coding-agent-workflows-with-sandbox-and-session-sharing-guardrails/) | Use Pi when an operator needs a local coding-agent CLI with explicit sandboxing, provider setup, and reviewable session... | 63.1k | Developer Tools |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 344 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 234 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 200 | ETL pipelines, parsing, format conversion |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 185 | Linting, code review, test generators, coverage |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 185 | Scaffolders, boilerplate generators, workflow templates |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 173 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 144 | Metrics, alerting rules, observability |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 138 | Third-party API bridges, webhooks, service connectors |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 125 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 122 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 116 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 114 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 101 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 89 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 79 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,636 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,274 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
