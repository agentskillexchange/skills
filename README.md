<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C022-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C527-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,022 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Decompile Android APKs into readable source with jadx for review and analysis](skills/decompile-android-apks-into-readable-source-with-jadx-for-review-and-analysis/)** — Turn an APK into readable Java or decompiled source artifacts so an agent can inspect behavior before deeper reverse-engineering or triage.

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
| [Audit clickstream analytics with Retentioneering agents](skills/audit-clickstream-analytics-with-retentioneering-agents/) | Use Retentioneering's Python toolkit, MCP server, and agent skills to run reproducible customer-journey and event-log analytics that agents... | 919 | Data Extraction & Transformation |
| [Run local multi-agent work sessions with Orkas](skills/run-local-multi-agent-work-sessions-with-orkas/) | Use Orkas to coordinate local-first multi-agent desktop work sessions across built-in specialist agents and installed coding CLIs such... | 2.1k | Developer Tools |
| [Compile agent-ready documentation bundles with docmd](skills/compile-agent-ready-documentation-bundles-with-docmd/) | Use docmd when a project needs one Markdown documentation source to produce a site, search index, llms.txt, MCP... | 2.5k | Library & API Reference |
| [Create voiceover-synced explainer videos with video-talkcraft](skills/create-voiceover-synced-explainer-videos-with-video-talkcraft/) | Use video-talkcraft when a coding agent needs to turn a script and finished voiceover into a Remotion-rendered explainer... | 1.2k | Image & Creative Automation |
| [Connect coding agents to shared local memory with Memmy](skills/connect-coding-agents-to-shared-local-memory-with-memmy/) | Use Memmy when Claude Code, Codex, OpenClaw, Cursor, or another local agent needs one controlled local memory service... | 2.0k | Developer Tools |
| [Benchmark enterprise RAG agents with EnterpriseRAG-Bench](skills/benchmark-enterprise-rag-agents-with-enterpriserag-bench/) | Use EnterpriseRAG-Bench to evaluate an enterprise RAG or knowledge-agent system against a realistic synthetic company corpus with answer... | 562 | Security & Verification |
| [Run agent sandboxes and GPU jobs with Beam](skills/run-agent-sandboxes-and-gpu-jobs-with-beam/) | Use Beam when an agent needs remote Python sandboxes, serverless GPU inference endpoints, or retryable background tasks without... | 1.8k | Developer Tools |
| [Auto-instrument Kubernetes apps with Odigos](skills/auto-instrument-kubernetes-apps-with-odigos/) | Use Odigos to add OpenTelemetry tracing to Kubernetes or VM workloads without code changes, then route the traces... | 3.7k | Monitoring & Alerts |
| [Build spec-driven full-stack apps with Wasp](skills/build-spec-driven-full-stack-apps-with-wasp/) | Use Wasp when an agent needs to scaffold or modify a React, Node.js, and Prisma app from a... | 18.7k | Templates & Workflows |
| [Maintain a Git-versioned codebase index for coding agents with AOCI-CODE](skills/maintain-a-git-versioned-codebase-index-for-coding-agents-with-aoci-code/) | Initialize a local MCP server and repository-owned index so coding agents can read durable code and database context... | 443 | Developer Tools |

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
| [Build spec-driven full-stack apps with Wasp](skills/build-spec-driven-full-stack-apps-with-wasp/) | Use Wasp when an agent needs to scaffold or modify a React, Node.js, and Prisma app from a... | 18.7k | Templates & Workflows |
| [Build agent-maintainable reactive UI with ArrowJS](skills/build-agent-maintainable-reactive-ui-with-arrowjs/) | Use ArrowJS when a coding agent needs to add or maintain small reactive web interfaces using DOM-native JavaScript... | 3.8k | Developer Tools |
| [Build TypeScript spreadsheet import and export workflows with hucre](skills/build-typescript-spreadsheet-import-and-export-workflows-with-hucre/) | Use hucre when a coding agent needs to add zero-dependency XLSX, CSV, ODS, JSON, NDJSON, or XML spreadsheet... | 2.2k | Data Extraction & Transformation |
| [Compile agent-ready documentation bundles with docmd](skills/compile-agent-ready-documentation-bundles-with-docmd/) | Use docmd when a project needs one Markdown documentation source to produce a site, search index, llms.txt, MCP... | 2.5k | Library & API Reference |
| [Query HyperDX logs, traces, metrics, and session replay from agent incident workflows](skills/query-hyperdx-logs-traces-and-session-replay-from-agent-incident-workflows/) | Use HyperDX and its agent-friendly CLI output to search, live-tail, and correlate OpenTelemetry signals during supervised production investigations | 9.9k | Monitoring & Alerts |
| [Render pull request architecture diagrams with PR Lens](skills/render-pull-request-architecture-diagrams-with-pr-lens/) | Have an agent turn a code diff into validated architecture and data-flow diagrams, then attach the rendered SVGs... | 212 | Code Quality & Review |
| [Collect TikTok and Douyin data through a self-hosted MCP server](skills/collect-tiktok-and-douyin-data-through-a-self-hosted-mcp-server/) | Run Douyin_TikTok_Download_API as a private MCP-backed service so agents can parse, archive, and retrieve TikTok or Douyin posts... | 20.1k | Research & Scraping |
| [Serve codebase impact context to agents with Trace MCP](skills/serve-codebase-impact-context-to-agents-with-trace-mcp/) | Use Trace MCP to index a repository once and let MCP-capable coding agents query framework-aware code, dependency, and... | 154 | Code Quality & Review |
| [Draw and verify Excalidraw diagrams through an agent canvas](skills/draw-and-verify-excalidraw-diagrams-through-an-agent-canvas/) | Use mcp_excalidraw to let coding agents create, inspect, revise, export, and commit editable Excalidraw diagrams from a local... | 2.4k | Image & Creative Automation |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 483 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 250 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 246 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 225 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 202 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 178 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 170 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 159 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 131 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 128 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 127 | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 123 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 112 | Image generation, asset processing, design automation |
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
| 📋 **Published** | 3,022 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,527 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
