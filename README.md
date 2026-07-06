<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C687-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C313-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,687 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[gRPC Service Tool](skills/grpc-service-tool/)** — gRPC Service Tool is built around gRPC remote procedure call framework. The underlying ecosystem is represented by grpc/grpc-node (4,816+ GitHub stars). It gives an agent a more technical…

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
| [Enforce pull-request approval policy with Policy Bot](skills/enforce-pull-request-approval-policy-with-policy-bot/) | Codify complex GitHub review rules, evaluate pull requests, and expose approval status as a required check | 1.0k | Code Quality & Review |
| [Parse documents into structured content for agent ingestion with Dedoc](skills/parse-documents-into-structured-content-for-agent-ingestion-with-dedoc/) | Extract document text, tables, logical structure, and metadata into normalized output before RAG, review, or workflow automation | 712 | Data Extraction & Transformation |
| [Query operational databases from MCP clients with DBHub](skills/query-operational-databases-from-mcp-clients-with-dbhub/) | Use DBHub to expose guarded, token-efficient database inspection and SQL tools to MCP clients across Postgres, MySQL, SQL... | 3.1k | Data Extraction & Transformation |
| [Inspect PDFs with evidence-first MCP workflows using PDF Reader MCP](skills/inspect-pdfs-with-evidence-first-mcp-workflows-using-pdf-reader-mcp/) | Connect PDF Reader MCP when an agent needs source-backed PDF extraction with page evidence, visual crops, OCR provenance... | 807 | Data Extraction & Transformation |
| [Review GitHub repository settings as pull requests with repository-settings](skills/review-github-repository-settings-as-pull-requests-with-repository-settings/) | Use repository-settings when an operator wants GitHub repository configuration changes reviewed as code before branch protection, labels, teams... | 1.0k | Code Quality & Review |
| [Search and automate X/Twitter from OpenClaw with TweetClaw](skills/search-and-automate-x-twitter-from-openclaw-with-tweetclaw/) | Install and configure TweetClaw, the OpenClaw plugin for X/Twitter automation through Xquik. Use it when an agent needs... | 84 | Integrations & Connectors |
| [Control launch behavior with GO Feature Flag](skills/control-launch-behavior-with-go-feature-flag/) | Use GO Feature Flag as an OpenFeature-compatible control plane for rollout rules, targeting, experiments, remote config, and launch... | 2.0k | Monitoring & Alerts |
| [Build production Go agents with tRPC-Agent-Go](skills/build-production-go-agents-with-trpc-agent-go/) | Model Go-native agent systems with graph workflows, tool calls, memory, MCP, A2A, evaluation, and OpenTelemetry observability | 1.5k | Developer Tools |
| [Build production agent harnesses with Strands Agents](skills/build-production-agent-harnesses-with-strands-agents/) | Use Strands Agents to assemble model-agnostic Python or TypeScript agent harnesses with tools, MCP, guardrails, tracing, streaming, and... | 6.4k | Developer Tools |
| [Build streaming voice LLM agents with Vocode](skills/build-streaming-voice-llm-agents-with-vocode/) | Use Vocode to compose transcription, LLM, speech synthesis, and telephony components into reviewable real-time voice-agent workflows | 3.8k | Media & Transcription |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Query operational databases from MCP clients with DBHub](skills/query-operational-databases-from-mcp-clients-with-dbhub/) | Use DBHub to expose guarded, token-efficient database inspection and SQL tools to MCP clients across Postgres, MySQL, SQL... | 3.1k | Data Extraction & Transformation |
| [Run multi-provider coding-agent sessions with OpenClaude](skills/run-multi-provider-coding-agent-sessions-with-openclaude/) | Use OpenClaude when a repository task needs one terminal-first coding-agent workflow that can switch across cloud, local, Codex... | 29.5k | Developer Tools |
| [Give OpenCode project sessions persistent memory with opencode-mem](skills/give-opencode-project-sessions-persistent-memory-with-opencode-mem/) | Add opencode-mem to OpenCode so coding sessions can store, search, and reuse project memories through a local SQLite... | 1.0k | Developer Tools |
| [Coordinate multi-agent Claude Code and Codex workflows with Ruflo](skills/coordinate-multi-agent-claude-code-and-codex-workflows-with-ruflo/) | Install Ruflo when an operator needs Claude Code or Codex agents to coordinate swarms, memory, hooks, and MCP... | 59.0k | Templates & Workflows |
| [Run durable scheduled agent jobs in Node.js with Agenda](skills/run-durable-scheduled-agent-jobs-in-node-js-with-agenda/) | Use Agenda when a custom Node.js agent needs persistent scheduled jobs, retries, locking, and background workers backed by... | 9.7k | Templates & Workflows |
| [Give MCP agents structured graph memory with RushDB](skills/give-mcp-agents-structured-graph-memory-with-rushdb/) | Connect RushDB's MCP server so agents can store, search, update, and traverse persistent structured memory without hand-building a... | 308 | Integrations & Connectors |
| [Inspect PDFs with evidence-first MCP workflows using PDF Reader MCP](skills/inspect-pdfs-with-evidence-first-mcp-workflows-using-pdf-reader-mcp/) | Connect PDF Reader MCP when an agent needs source-backed PDF extraction with page evidence, visual crops, OCR provenance... | 807 | Data Extraction & Transformation |
| [Operate multi-provider AI gateway traffic with Bifrost](skills/operate-multi-provider-ai-gateway-traffic-with-bifrost/) | Run Bifrost as an OpenAI-compatible gateway so agents can route model calls across providers with failover, load balancing... | 6.0k | Integrations & Connectors |
| [Trace coding-agent and LLM workflows with OpenLIT](skills/trace-coding-agent-and-llm-workflows-with-openlit/) | Use OpenLIT to instrument coding agents and LLM applications with OpenTelemetry traces, metrics, costs, prompts, tool calls, and... | 2.5k | Monitoring & Alerts |
| [Control launch behavior with GO Feature Flag](skills/control-launch-behavior-with-go-feature-flag/) | Use GO Feature Flag as an OpenFeature-compatible control plane for rollout rules, targeting, experiments, remote config, and launch... | 2.0k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 356 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 236 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 210 | ETL pipelines, parsing, format conversion |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 191 | Scaffolders, boilerplate generators, workflow templates |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 188 | Linting, code review, test generators, coverage |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 173 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 147 | Metrics, alerting rules, observability |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 144 | Third-party API bridges, webhooks, service connectors |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 125 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 123 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 118 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 116 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 105 | Audio/video processing, speech-to-text |
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
| 📋 **Published** | 2,687 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,313 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
