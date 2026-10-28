<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-3%2C190-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C616-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*3,190 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Lightning CSS High-Performance CSS Parser Transformer and Minifier](skills/lightning-css-high-performance-css-parser-transformer-and-minifier/)** — Lightning CSS is a Rust-based CSS parser, transformer, bundler, and minifier from the Parcel team. This skill is for agents that need to optimize stylesheets, lower modern CSS…

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
| [Review Rust code with rule-cited findings using BeautifulRust](skills/review-rust-code-with-rule-cited-findings-using-beautifulrust/) | Review a Rust file, crate or diff with scoped tool checks and prioritized findings that cite source rules... | 1.3k | Code Quality & Review |
| [Diagnose Paradev host and terminal failures with the doctor skill](skills/diagnose-paradev-host-and-terminal-failures-with-the-doctor-skill/) | Capture Paradev service, account, host and version evidence, propose one symptom-matched repair, and verify the original failure before... | 15.6k | Runbooks & Diagnostics |
| [PopNow Video Generation](skills/popnow-video/) | Use the existing MIT-licensed PopNow video skill to quote and create AI videos from text or an image... | - | Image & Creative Automation |
| [Publish Files to a Permanent URL with deed.page](skills/deed-page/) | Publishes a generated HTML file or a static folder to a permanent https://.deed.page/ URL with one curl PUT... | - | Developer Tools |
| [Preflight Nudgebee runbooks before saving or execution](skills/preflight-nudgebee-runbooks-before-saving-or-execution/) | Validate a proposed Nudgebee runbook, repair supported schema errors, and return an operator review packet without saving, activating... | 520 | Runbooks & Diagnostics |
| [Bootstrap and verify self-hosted Rakazo from published images](skills/bootstrap-and-verify-self-hosted-rakazo-from-published-images/) | Prepare a Docker-based Rakazo installation, preserve private configuration, and verify service health, the selected sandbox, and an optional... | 5.8k | Developer Tools |
| [Audit performance claims with Pstack benchmark-checklist](skills/audit-performance-claims-with-pstack-benchmark-checklist/) | Check tuning, bottlenecks, correctness, repeatability, and end-to-end relevance before an agent reports a measured speedup or regression | 2.8k | Code Quality & Review |
| [Email Voice](skills/email-voice/) | Learn a user's email voice from authorized sent samples, export a private style profile, and draft fact-preserving replies... | - | Calendar, Email & Productivity |
| [Query isolated Git worktree code maps with ProjectAtlas](skills/query-isolated-git-worktree-code-maps-with-projectatlas/) | Register existing Git worktrees under explicit MCP aliases, refresh their separate code maps, and return bounded source evidence... | 456 | Developer Tools |
| [AI Services Market MCP](skills/ai-services-market-mcp/) | Teaches an agent to connect to the AI Services Market MCP server (https://aiservicesmarket.lol/mcp) and use its seven tools... | - | Integrations & Connectors |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [ADWilkinson](https://github.com/ADWilkinson) | [HyperGrok Trading Desk](skills/hypergrok-trading-desk/) | Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven... | Integrations & Connectors |
| [kyuminjo](https://github.com/kyuminjo) | [PopNow Video Generation](skills/popnow-video/) | Use the existing MIT-licensed PopNow video skill to quote and create AI videos from text or an image... | Image & Creative Automation |
| [f-o-x11](https://github.com/f-o-x11) | [Publish Files to a Permanent URL with deed.page](skills/deed-page/) | Publishes a generated HTML file or a static folder to a permanent https://.deed.page/ URL with one curl PUT... | Developer Tools |
| [DEX-XL](https://github.com/DEX-XL) | [Email Voice](skills/email-voice/) | Learn a user's email voice from authorized sent samples, export a private style profile, and draft fact-preserving replies... | Calendar, Email & Productivity |
| [yasuo22](https://github.com/yasuo22) | [AI Services Market MCP](skills/ai-services-market-mcp/) | Teaches an agent to connect to the AI Services Market MCP server (https://aiservicesmarket.lol/mcp) and use its seven tools... | Integrations & Connectors |
| [wu736139669](https://github.com/wu736139669) | [Goal Instruction Writer](skills/goal-instruction-writer/) | Preview, draft, refine, and audit durable Goal instructions in Codex. Define observable acceptance evidence, bounded execution loops, checkpoints... | Templates & Workflows |
| [waynehamadi](https://github.com/waynehamadi) | [Datacircle](skills/datacircle/) | Every GTM API plan on datacircle.dev, as one file you download and query. LinkedIn profiles, people and company... | Library & API Reference |
| [livastic-vm1-primary](https://github.com/livastic-vm1-primary) | [PaperPilot CSV Preflight](skills/paperpilot-csv-preflight/) | Inspect up to 32 KiB of UTF-8 CSV locally with dependency-free Node.js, detecting inconsistent column widths, quoted-field errors... | Data Extraction & Transformation |
| [gagankcai-jpg](https://github.com/gagankcai-jpg) | [Install and write Faber Romanus](skills/install-and-write-faber-romanus/) | Download the Faber CLI and write Faber Romanus programs using the official agent skill guides (install, English reader... | Developer Tools |
| [MAGA2010](https://github.com/MAGA2010) | [Turn messy datasets into auditable reports with data-master](skills/turn-messy-datasets-into-auditable-reports-with-data-master/) | Use data-master to preserve raw tabular data, hold ambiguous cleaning decisions for review, run unit-aware statistics and sensitivity... | Data Extraction & Transformation |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Coordinate agent teams and governed work in Paperclip](skills/coordinate-agent-teams-and-governed-work-in-paperclip/) | Use Paperclip as a self-hosted control plane for assigning goals, tasks, budgets, approvals, routines, and run history across... | 98.2k | Templates & Workflows |
| [Monitor Claude Code sessions with ccstatusline](skills/monitor-claude-code-sessions-with-ccstatusline/) | Configure Claude Code's status line with live model, token, cost, git, sandbox, cache, CI, and session health signals... | 13.2k | Developer Tools |
| [Reverse-engineer apps and binaries with REA](skills/reverse-engineer-apps-and-binaries-with-rea/) | Connect coding agents to REA's MCP tools so they can inspect apps, binaries, websites, APKs, and runtime behavior... | 17.1k | Security & Verification |
| [Resolve coding questions from upstream evidence with Firecrawl Developer Index](skills/resolve-coding-questions-with-firecrawl-developer-index/) | Find public issues, merged fixes and API-contract passages with Firecrawl’s named Developer Index skill, then return a cited... | 653 | Research & Scraping |
| [Diagnose Paradev host and terminal failures with the doctor skill](skills/diagnose-paradev-host-and-terminal-failures-with-the-doctor-skill/) | Capture Paradev service, account, host and version evidence, propose one symptom-matched repair, and verify the original failure before... | 15.6k | Runbooks & Diagnostics |
| [Run owned terminal coding-agent workflows with Zero](skills/run-owned-terminal-coding-agent-workflows-with-zero/) | Use Zero to run local, scriptable coding-agent sessions with operator-controlled models, permissions, tools, skills, MCP servers, and durable... | 1.7k | Developer Tools |
| [Run code-generated short-film workflows with Lemo-Opuscar](skills/direct-code-generated-short-films-with-lemo-opuscar-styles/) | Use a Claude Code plugin to turn a story brief into a short film project built from reusable... | 1.5k | Image & Creative Automation |
| [Co-edit and verify a live spreadsheet session through GridCraft MCP](skills/co-edit-and-verify-a-live-spreadsheet-session-through-gridcraft-mcp/) | Connect an agent to the GridCraft workbook open on a user’s desktop, make scoped edits, and return formula... | 6.2k | Data Extraction & Transformation |
| [Review Rust code with rule-cited findings using BeautifulRust](skills/review-rust-code-with-rule-cited-findings-using-beautifulrust/) | Review a Rust file, crate or diff with scoped tool checks and prioritized findings that cite source rules... | 1.3k | Code Quality & Review |
| [Annotate Classical Chinese corpora with HanLP](skills/annotate-classical-chinese-corpora-with-hanlp/) | Produce reviewable token, lemma, POS and dependency annotations for Classical Chinese passages with HanLP’s dedicated Ancient Chinese model | 36.5k | Data Extraction & Transformation |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 535 | CLI tools, scaffolders, dev environment setup |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 267 | Scaffolders, boilerplate generators, workflow templates |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 257 | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 237 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 210 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 193 | Pipeline configs, deployment automation, build tooling |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 189 | Third-party API bridges, webhooks, service connectors |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 184 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 163 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 141 | Web research, content discovery, data collection |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 133 | SDK docs, API parsers, symbol resolvers |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 129 | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 128 | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 121 | Image generation, asset processing, design automation |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 110 | Audio/video processing, speech-to-text |
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
| 📋 **Published** | 3,190 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,616 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
