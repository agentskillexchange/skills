<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C259-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C669-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,259 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Search repository files by behavior with Localix decide](skills/search-repository-files-by-behavior-with-localix-decide/)** — Narrow repository paths with ripgrep, classify each candidate with llx decide, and inspect matching or uncertain files before returning a source-grounded handoff.

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
| [Prepare a read-only InnoShop low-stock report through MCP](skills/prepare-read-only-innoshop-low-stock-report-mcp/) | Query all low-stock SKU pages through InnoShop MCP and return a threshold-based inventory exception report for human restocking... | 671 | Integrations & Connectors |
| [Refresh Theia model aliases and provider capabilities with update-default-models](skills/refresh-theia-model-aliases-provider-capabilities/) | Research provider model changes, update Theia's default aliases and inferred capabilities, and return a tested maintenance patch using... | 21.8k | Developer Tools |
| [Render existing Mermaid files and PR diagrams in Claude Code with Termaid](skills/render-existing-mermaid-diagrams-claude-code-termaid/) | Invoke Termaid’s explicit Mermaid skill to render existing files, README blocks, or PR diagrams as terminal drawings and... | 583 | Image & Creative Automation |
| [Monitor one pull request through CI and review with Tstack babysit-pr](skills/monitor-pull-request-ci-review-tstack-babysit-pr/) | Watch a single owned pull request, verify new review findings, fix real CI failures, and return a current... | 4.1k | CI/CD Integrations |
| [Search repository files by behavior with Localix decide](skills/search-repository-files-by-behavior-with-localix-decide/) | Narrow repository paths with ripgrep, classify each candidate with llx decide, and inspect matching or uncertain files before... | 368 | Developer Tools |
| [Validate and report completed external workflow usage to LoopForge](skills/validate-and-report-completed-external-workflow-usage-to-loopforge/) | Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for... | 2.8k | Monitoring & Alerts |
| [Coordinate a scoped code change through Oh My Claudecode team stages](skills/coordinate-a-scoped-code-change-through-oh-my-claudecode-team-stages/) | Run a bounded Claude Code team task through planning, delegated implementation, verification and repair, then return the change... | 40.9k | Templates & Workflows |
| [Verify Nix package and option choices through MCP-NixOS](skills/verify-nix-package-and-option-choices-through-mcp-nixos/) | Search NixOS packages and configuration options, inspect exact results and version metadata, then hand off an evidenced configuration... | 889 | Library & API Reference |
| [Review changed-file code quality findings with Fallow](skills/review-changed-file-code-quality-findings-with-fallow/) | Audit a JavaScript or TypeScript change against its Git base, inspect structured findings, and return a focused merge-readiness... | 5.4k | Code Quality & Review |
| [Resolve Langfuse integration questions through its documentation MCP](skills/resolve-langfuse-integration-questions-through-documentation-mcp/) | Search current Langfuse documentation, fetch the relevant Markdown pages, and return a source-backed integration or migration plan through... | 253 | Library & API Reference |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [JuampiHernandez](https://github.com/JuampiHernandez) | [Firecrawl Alexandria](skills/firecrawl-alexandria/) | Firecrawl Alexandria gives coding agents a direct path to structured data through ready-made website workflows, data APIs, and... | Research & Scraping |
| [KhademOHAli1](https://github.com/KhademOHAli1) | [Investigative Journalism and Fact-Checking](skills/investigate-and-fact-check/) | Conduct public-interest investigative journalism, rigorous fact-checking, and open-source intelligence (OSINT) research. Use for verifying claims, quotes, documents, photographs... | Research & Scraping |
| [pushkarsingh32](https://github.com/pushkarsingh32) | [GetYouTubeTranscript: YouTube Transcripts, Search and Channel Data](skills/getyoutubetranscript-youtube-transcript/) | Fetch YouTube transcripts, search videos and channels, browse a channel's uploads and playlists, and find where something is... | Media & Transcription |
| [Samuel-Shek](https://github.com/Samuel-Shek) | [Prompt Optimizer](skills/prompt-optimizer-skill/) | Turns a rough request or an existing prompt into one copy-ready prompt for any AI agent that can... | Templates & Workflows |
| [estevecastells](https://github.com/estevecastells) | [Invokely Statistics](skills/invokely-statistics/) | Use Invokely's hosted MCP tools to find and cite official statistics. Use when an agent needs indicator discovery... | Data Extraction & Transformation |
| [waynehamadi](https://github.com/waynehamadi) | [Datacircle GTM API Benchmark](skills/datacircle-gtm-api-benchmark/) | Compare GTM APIs using Datacircle rankings. Call the open API at api.datacircle.dev/v1, with no key, to list covered... | Library & API Reference |
| [waynehamadi](https://github.com/waynehamadi) | [Datacircle](skills/datacircle/) | Every GTM API plan on datacircle.dev, as one file you download and query. LinkedIn profiles, people and company... | Library & API Reference |
| [zealous1](https://github.com/zealous1) | [Arcmira: YouTube Transcript Search](skills/arcmira-transcript-search/) | Search indexed YouTube and podcast transcripts through Arcmira MCP. Return quoted passages, speaker attribution when available, and timestamped... | Media & Transcription |
| [radres](https://github.com/radres) | [Call or Text Your Phone from an Agent with /call-me](skills/call-me/) | Lets an agent call or text the user's own phone (iPhone or Android) through the /call-me remote MCP... | Integrations & Connectors |
| [ADWilkinson](https://github.com/ADWilkinson) | [USDCtoFiat Cash-Out](skills/usdctofiat-cashout/) | Add non-custodial Base USDC-to-fiat cash-out with @usdctofiat/offramp cashout({ mode: "fast" \| "best" }). Use when an agent must... | Integrations & Connectors |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Coordinate a scoped code change through Oh My Claudecode team stages](skills/coordinate-a-scoped-code-change-through-oh-my-claudecode-team-stages/) | Run a bounded Claude Code team task through planning, delegated implementation, verification and repair, then return the change... | 40.9k | Templates & Workflows |
| [Audit local agent runs and select hook policies with Failproof AI](skills/audit-local-agent-runs-and-select-hook-policies-with-failproof-ai/) | Review local harness history, identify risky tool patterns, and prepare a source-backed policy-pack rollout across supported agent runtimes | 8.9k | Security & Verification |
| [Review Master CSS output regressions through MCP snapshots](skills/review-master-css-output-regressions-through-mcp-snapshots/) | Capture project CSS snapshots, trace missing classes, compare generated output, and propose scoped fixes with evidence from the... | 2.0k | Code Quality & Review |
| [Triage Lunora deployment errors and migration status through MCP](skills/triage-lunora-deployment-errors-and-migration-status-through-mcp/) | Inspect Lunora logs, grouped errors, query performance and pending migrations through MCP, then return a scoped incident handoff... | 293 | Runbooks & Diagnostics |
| [Record and replay FrontMCP calls to catch server regressions](skills/record-and-replay-frontmcp-calls-to-catch-server-regressions/) | Capture baseline MCP calls as JSONL, replay them against a changed FrontMCP server, and review answer differences and... | 151 | Code Quality & Review |
| [Record an agent-completed browser task as a parameterized Oya playbook](skills/record-agent-browser-task-as-parameterized-oya-playbook/) | Complete a test browser task once, save its learned steps as an Oya playbook, and verify a replay... | 349 | Browser Automation |
| [Diagnose incomplete web extraction with PageSift MCP audit evidence](skills/diagnose-incomplete-web-extraction-with-pagesift-mcp-audit-evidence/) | Triage missing web content across local agents using PageSift MCP audit records, HTML snapshots, and local extraction issue... | 162 | Data Extraction & Transformation |
| [Validate and report completed external workflow usage to LoopForge](skills/validate-and-report-completed-external-workflow-usage-to-loopforge/) | Validate a host-supplied terminal execution summary, report attributable model usage to LoopForge, and preserve stable execution IDs for... | 2.8k | Monitoring & Alerts |
| [Assemble and review local video cuts through Concat MCP](skills/assemble-and-review-local-video-cuts-through-concat-mcp/) | Turn local footage and an edit brief into a Concat timeline, inspect composited frames, save the project and... | 16.0k | Media & Transcription |
| [Refresh structured user profiles from chat buffers with Memobase](skills/refresh-structured-user-profiles-from-chat-buffers-with-memobase/) | Convert authorized chat batches into a user-scoped profile, wait for processing, and retrieve a bounded context string for... | 3.0k | Integrations & Connectors |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 545 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 272 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 265 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 244 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 218 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 194 | Pipeline configs, deployment automation, build tooling |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 193 | Third-party API bridges, webhooks, service connectors |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 187 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 165 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 146 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 136 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 131 | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 129 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 128 | Image generation, asset processing, design automation |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 113 | Audio/video processing, speech-to-text |
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
| 📋 **Published** | 3,259 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,669 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
