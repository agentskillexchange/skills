<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C004-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C509-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,004 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Wire transcript-derived coding-agent memory with deja-vu](skills/wire-transcript-derived-coding-agent-memory-with-deja-vu/)** — Use deja-vu when Codex, Claude Code, Cursor, OpenClaw, Copilot, and other local coding agents need shared recall from session history already written on disk.

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
| [Build agent-maintainable reactive UI with ArrowJS](skills/build-agent-maintainable-reactive-ui-with-arrowjs/) | Use ArrowJS when a coding agent needs to add or maintain small reactive web interfaces using DOM-native JavaScript... | 3.8k | Developer Tools |
| [Use production-agent tutorial playbooks from Agents Towards Production](skills/use-production-agent-tutorial-playbooks-from-agents-towards-production/) | Use Agents Towards Production when an agent needs code-first tutorial playbooks for production agent features such as state... | 21.5k | Templates & Workflows |
| [Inspect and export Excel workbooks from the terminal with xleak](skills/inspect-and-export-excel-workbooks-from-the-terminal-with-xleak/) | Use xleak when an agent needs to inspect, search, verify formulas, and export Excel, ODS, CSV, or TSV... | 1.5k | Data Extraction & Transformation |
| [Wire transcript-derived coding-agent memory with deja-vu](skills/wire-transcript-derived-coding-agent-memory-with-deja-vu/) | Use deja-vu when Codex, Claude Code, Cursor, OpenClaw, Copilot, and other local coding agents need shared recall from... | 831 | Developer Tools |
| [Run IDE-wired terminal coding-agent workflows with Oh My Pi](skills/run-ide-wired-terminal-coding-agent-workflows-with-oh-my-pi/) | Use Oh My Pi when an operator wants a local terminal coding agent with IDE-grade context, built-in file... | 31.8k | Developer Tools |
| [Run graph and vector memory backends for agents with NornicDB](skills/run-graph-and-vector-memory-backends-for-agents-with-nornicdb/) | Use NornicDB when an agent workflow needs a local or self-hosted graph, vector, and temporal database for GraphRAG... | 878 | Integrations & Connectors |
| [Run sandboxed multi-language code execution with Judge0](skills/run-sandboxed-multi-language-code-execution-with-judge0/) | Use Judge0 when an agent workflow needs a self-hostable HTTP API for compiling and running untrusted or model-generated... | 4.4k | Developer Tools |
| [Build and optimize agent eval workflows with Kiln](skills/build-and-optimize-agent-eval-workflows-with-kiln/) | Use Kiln to create eval datasets, rate outputs, optimize prompts and models, and ship the same AI task... | 5.1k | Monitoring & Alerts |
| [Run private RAG and MCP skill workspaces with Yuxi](skills/run-private-rag-and-mcp-skill-workspaces-with-yuxi/) | Deploy Yuxi when an agent team needs a private, multi-tenant knowledge workspace that combines document RAG, knowledge graphs... | 7.0k | Data Extraction & Transformation |
| [Run repo-local story, handover, and review workflows with Storybloq](skills/run-repo-local-story-handover-and-review-workflows-with-storybloq/) | Use Storybloq when Claude Code or Codex needs durable repo-local stories, plans, handovers, lessons, and review evidence instead... | 738 | Developer Tools |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [InsightFactoryAPP](https://github.com/InsightFactoryAPP) | [YYLO Ledger Task Management](skills/ledger-tasks-yylo/) | Operate a YYLO Ledger Kanban board from the command line with the yy ledger CLI; create, search, update... | Developer Tools |
| [Ares3333333](https://github.com/Ares3333333) | [SHAR Production Metadata Validation](skills/shar-production-metadata-validation/) | Uses the SHAR Production Metadata MCP local stdio server to validate rights-aware production metadata manifests before an AI-hybrid... | Security & Verification |
| [azeemkafridi](https://github.com/azeemkafridi) | [BulkPublish Social Publishing](skills/bulkpublish-social-publishing/) | Adapt, review, schedule, and publish approved social content across multiple platforms through the BulkPublish API and hosted MCP | Integrations & Connectors |
| [devdasx](https://github.com/devdasx) | [Aperture Wallet Guide](skills/aperture-wallet-guide/) | Answer Aperture Wallet questions from first-party product, security, network, release, app-screen, and Journal sources while enforcing explicit wallet-secret... | Library & API Reference |
| [anzy-renlab-ai](https://github.com/anzy-renlab-ai) | [Pronounce Developer Jargon](skills/pronounce-developer-jargon/) | Answers short pronunciation questions about developer tools, AI models, acronyms, and project names by using the say-it CLI... | Developer Tools |
| [TianHengZhuang](https://github.com/TianHengZhuang) | [SandBase MCP](skills/sandbase-mcp/) | Access 2,000+ AI models and API tools through one MCP interface for inference, media generation, search, scraping, embeddings... | Integrations & Connectors |
| [liangfeng-hu](https://github.com/liangfeng-hu) | [Proofed Completion Gate](skills/proofed-completion-gate/) | Uses the Proofed CLI and current-subject completion receipts to reject unsupported coding-agent completion claims, rerun repository-configured tests, and... | Security & Verification |
| [haoranyu](https://github.com/haoranyu) | [Clean Closed Issue Worktrees](skills/clean-closed-issue-worktrees/) | Safely audits and removes Git worktrees linked to closed GitHub or GitLab issues with a mandatory scan-confirm-execute protocol... | Developer Tools |
| [TinyOps Studio LLC](https://github.com/tinyopsstudio) | [Automation Integration Preflight](skills/automation-integration-preflight/) | Assess a public HTTP(S) page before building browser automation, extraction, or an integration. Use this skill to collect... | Integrations & Connectors |
| [pranshuchittora](https://github.com/pranshuchittora) | [Author and Run Regression Tests with Agent QA](skills/author-and-run-regression-tests-with-agent-qa/) | Use Agent QA's CLI and MCP server to author, validate, run, debug, and triage natural-language web and mobile... | Browser Automation |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Run IDE-wired terminal coding-agent workflows with Oh My Pi](skills/run-ide-wired-terminal-coding-agent-workflows-with-oh-my-pi/) | Use Oh My Pi when an operator wants a local terminal coding agent with IDE-grade context, built-in file... | 31.8k | Developer Tools |
| [Build agent-maintainable reactive UI with ArrowJS](skills/build-agent-maintainable-reactive-ui-with-arrowjs/) | Use ArrowJS when a coding agent needs to add or maintain small reactive web interfaces using DOM-native JavaScript... | 3.8k | Developer Tools |
| [Render pull request architecture diagrams with PR Lens](skills/render-pull-request-architecture-diagrams-with-pr-lens/) | Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs... | 212 | Code Quality & Review |
| [Collect TikTok and Douyin data through a self-hosted MCP server](skills/collect-tiktok-and-douyin-data-through-a-self-hosted-mcp-server/) | Run Douyin_TikTok_Download_API as a private MCP-backed service so agents can parse, archive, and retrieve TikTok or Douyin posts... | 20.1k | Research & Scraping |
| [Serve codebase impact context to agents with Trace MCP](skills/serve-codebase-impact-context-to-agents-with-trace-mcp/) | Use Trace MCP to index a repository once and let MCP-capable coding agents query framework-aware code, dependency, and... | 154 | Code Quality & Review |
| [Draw and verify Excalidraw diagrams through an agent canvas](skills/draw-and-verify-excalidraw-diagrams-through-an-agent-canvas/) | Use mcp_excalidraw to let coding agents create, inspect, revise, export, and commit editable Excalidraw diagrams from a local... | 2.4k | Image & Creative Automation |
| [Use production-agent tutorial playbooks from Agents Towards Production](skills/use-production-agent-tutorial-playbooks-from-agents-towards-production/) | Use Agents Towards Production when an agent needs code-first tutorial playbooks for production agent features such as state... | 21.5k | Templates & Workflows |
| [Run private RAG and MCP skill workspaces with Yuxi](skills/run-private-rag-and-mcp-skill-workspaces-with-yuxi/) | Deploy Yuxi when an agent team needs a private, multi-tenant knowledge workspace that combines document RAG, knowledge graphs... | 7.0k | Data Extraction & Transformation |
| [Inspect and export Excel workbooks from the terminal with xleak](skills/inspect-and-export-excel-workbooks-from-the-terminal-with-xleak/) | Use xleak when an agent needs to inspect, search, verify formulas, and export Excel, ODS, CSV, or TSV... | 1.5k | Data Extraction & Transformation |
| [Build and optimize agent eval workflows with Kiln](skills/build-and-optimize-agent-eval-workflows-with-kiln/) | Use Kiln to create eval datasets, rate outputs, optimize prompts and models, and ship the same AI task... | 5.1k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 476 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 249 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 243 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 223 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 202 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 178 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 170 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 156 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 131 | Web research, content discovery, data collection |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 127 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 127 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 123 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 111 | Image generation, asset processing, design automation |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 109 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 92 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 3,004 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,509 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
