<div align="center">

# Agent Skill Exchange

### Curated and trusted AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C938-6366f1?style=for-the-badge)](CATALOG.md)
[![Industry%20Collections](https://img.shields.io/badge/industry--collections-15-14b8a6?style=for-the-badge)](industries/README.md)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/README.md)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C496-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Catalog](CATALOG.md) · [Live Browse](https://agentskillexchange.com/browse-skills/) · [Categories](categories/README.md) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Submit a Skill](#submit-a-skill)**

*2,938 published skills · 15 Industry Collections · 17 categories · Real ecosystem signals · Updated daily*

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

**[Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify](skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)** — Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup…

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
| [Design, render, and visually QA editable PowerPoint decks with PPT Design Skill](skills/design-render-and-visually-qa-editable-powerpoint-decks-with-ppt-design-skill/) | Run a presentation-design workflow that turns a confirmed brief into editable PPTX output, rendered PNG previews, and revision... | 1.0k | Image & Creative Automation |
| [Operate Rails Active Job queues with Mission Control Jobs](skills/operate-rails-active-job-queues-with-mission-control-jobs/) | Use Mission Control Jobs when an operator needs a Rails-mounted dashboard to inspect Active Job queues, review failed... | 1.1k | Runbooks & Diagnostics |
| [Monitor local coding-agent sessions and token usage with Loongsuite Pilot](skills/monitor-local-coding-agent-sessions-and-token-usage-with-loongsuite-pilot/) | Collect local telemetry from Claude Code, Codex, Cursor, OpenClaw, OpenCode, and related coding agents, then inspect token usage... | 152 | Monitoring & Alerts |
| [Run social media research workflows with ScrapeCreators skills](skills/run-social-media-research-workflows-with-scrapecreators-skills/) | Use Social Media Research Skills when an agent needs to find outlier posts, mine comments, compare competitors, inspect... | 1.8k | Research & Scraping |
| [Run ComfyUI workflows as agent-callable skills](skills/run-comfyui-workflows-as-agent-callable-skills/) | Use ComfyUI Skills for OpenClaw when an agent needs to import, parameterize, route, and run repeatable ComfyUI workflows... | 395 | Image & Creative Automation |
| [HOL Guard](skills/hol-guard/) | Protect local AI coding-agent harnesses before tools run, review approvals and evidence, and scan agent plugins, skills, MCP... | - | Security & Verification |
| [Run symbol-aware coding sessions with Empryo](skills/run-symbol-aware-coding-sessions-with-empryo/) | Use Empryo when a coding agent should map symbols, blast radius, and dependencies before making AST-backed edits across... | 984 | Developer Tools |
| [Produce Chinese video recaps with video-recap-skills](skills/produce-chinese-video-recaps-with-video-recap-skills/) | Use video-recap-skills when an agent should turn source video into a Chinese narration recap with scene understanding, scripting... | 471 | Media & Transcription |
| [Slashbooks](skills/slashbooks/) | Replace QuickBooks with an AI agent you control: import bank and credit card activity, categorize and reconcile transactions... | - | Calendar, Email & Productivity |
| [Harden Claude Code plans with claudex-loop](skills/harden-claude-code-plans-with-claudex-loop/) | Use claudex-loop when a Claude Code operator should lock intent, stress-test a plan with Codex, and cross-inspect the... | 1.2k | Developer Tools |

---

## Recent Community Contributions

| Contributor | Skill | What it helps with | Category |
|---|---|---|---|
| [kantorcodes](https://github.com/kantorcodes) | [HOL Guard](skills/hol-guard/) | Protect local AI coding-agent harnesses before tools run, review approvals and evidence, and scan agent plugins, skills, MCP... | Security & Verification |
| [giltotherescue](https://github.com/giltotherescue) | [Slashbooks](skills/slashbooks/) | Replace QuickBooks with an AI agent you control: import bank and credit card activity, categorize and reconcile transactions... | Calendar, Email & Productivity |
| [bekservice](https://github.com/bekservice) | [Famulor Assistants & Omnichannel History](skills/famulor-assistants-history/) | Use Famulor's OAuth-secured, read-only MCP profile to inspect assistant configurations, versions, workspace catalogs, and unified call, messaging, and... | Integrations & Connectors |
| [ADWilkinson](https://github.com/ADWilkinson) | [HyperGrok Trading Desk](skills/hypergrok-trading-desk/) | Turn Claude Code, Cursor, or Grok Bot into a 7-role Hyperliquid trading desk. Sixteen SKILL.md skills plus seven... | Integrations & Connectors |
| [MM-sheng](https://github.com/MM-sheng) | [Use 404.directory](skills/use-404-directory/) | Use the public 404.directory MCP server to search current official OpenAI, Microsoft Learn, AWS, and Cloudflare documentation, verify... | Library & API Reference |
| [ADWilkinson](https://github.com/ADWilkinson) | [USDCtoFiat Cash-Out](skills/usdctofiat-cashout/) | Add non-custodial Base USDC-to-fiat cash-out with @usdctofiat/offramp cashout({ mode: "fast" \| "best" }). Use when an agent must... | Integrations & Connectors |
| [ADWilkinson](https://github.com/ADWilkinson) | [Sell unused tokens](skills/sell-unused-tokens/) | List leftover LLM API capacity on tokensto.cash (OpenRouter, OpenAI, Anthropic, Venice, Capminal, and 20+ others) and cash out... | Developer Tools |
| [Anil-matcha](https://github.com/Anil-matcha) | [Generate Images with MuAPI](skills/generate-images-with-muapi/) | Discovers current MuAPI image models, builds a model-specific request, and validates asynchronous image artifacts. Use when an agent... | Image & Creative Automation |
| [ChuYiCui1](https://github.com/ChuYiCui1) | [AShareHub Chinese Market Data](skills/asharehub/) | Query Chinese A-share, ETF, index, financial statement, valuation, capital-flow, and technical-indicator data through the AShareHub Python SDK and... | Library & API Reference |
| [denial123789](https://github.com/denial123789) | [Cross-validate research with SandBase Multi-Source Search](skills/cross-validate-research-with-sandbase-multi-source-search/) | Use SandBase Multi-Source Search to fact-check claims across independent web and academic sources, record disagreements, score confidence, and... | Research & Scraping |

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | What it helps with | Stars | Category |
|---|---|---:|---|
| [Run CodeWhale terminal coding agent workflows](skills/run-codewhale-terminal-coding-agent-workflows/) | Use CodeWhale as a local terminal coding agent for repository edits, test repair, provider-switched sessions, approval-gated commands, MCP... | 40.8k | Developer Tools |
| [Add Claude design-system and accessibility workflows with UX/UI Agent Skills](skills/add-claude-design-system-and-accessibility-workflows-with-ux-ui-agent-skills/) | Use UX/UI Agent Skills when Claude should generate tokens, component specs, accessibility audits, and framework-specific UI code from... | 694 | Developer Tools |
| [Automate NotebookLM Studio generation and cited research batches with notebooklm-mcp](skills/automate-notebooklm-studio-generation-and-cited-research-batches-with-notebooklm-mcp/) | Use NotebookLM through MCP or a local REST API to run cited Q&A, generate Studio artifacts, and manage... | 161 | Research & Scraping |
| [Run independent multi-agent build and review flows with OPC](skills/run-independent-multi-agent-build-and-review-flows-with-opc/) | Use OPC as a Claude Code skill to select a task flow, dispatch specialist roles, enforce independent review... | 192 | Code Quality & Review |
| [Enforce Coding-Agent Write and Shell Policies with Probity](skills/enforce-coding-agent-write-and-shell-policies-with-probity/) | Use Probity when Claude Code, Codex, or GitHub Copilot CLI should be blocked from unsafe file writes or... | 162 | Security & Verification |
| [Block Risky Coding-Agent Commands with CC Safety Net](skills/block-risky-coding-agent-commands-with-cc-safety-net/) | Use CC Safety Net when coding-agent CLIs need pre-execution hooks that block destructive commands, secret access, and unsafe... | 1.5k | Security & Verification |
| [Run social media research workflows with ScrapeCreators skills](skills/run-social-media-research-workflows-with-scrapecreators-skills/) | Use Social Media Research Skills when an agent needs to find outlier posts, mine comments, compare competitors, inspect... | 1.8k | Research & Scraping |
| [Design, render, and visually QA editable PowerPoint decks with PPT Design Skill](skills/design-render-and-visually-qa-editable-powerpoint-decks-with-ppt-design-skill/) | Run a presentation-design workflow that turns a confirmed brief into editable PPTX output, rendered PNG previews, and revision... | 1.0k | Image & Creative Automation |
| [Operate Rails Active Job queues with Mission Control Jobs](skills/operate-rails-active-job-queues-with-mission-control-jobs/) | Use Mission Control Jobs when an operator needs a Rails-mounted dashboard to inspect Active Job queues, review failed... | 1.1k | Runbooks & Diagnostics |
| [Use 404.directory](skills/use-404-directory/) | Use the public 404.directory MCP server to search current official OpenAI, Microsoft Learn, AWS, and Cloudflare documentation, verify... | - | Library & API Reference |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 450 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 246 | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 233 | Scaffolders, boilerplate generators, workflow templates |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 220 | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 199 | Linting, code review, test generators, coverage |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 178 | Incident response, troubleshooting, system diagnostics |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 164 | Third-party API bridges, webhooks, service connectors |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 155 | Metrics, alerting rules, observability |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 127 | Web research, content discovery, data collection |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 127 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 126 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 121 | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 109 | Audio/video processing, speech-to-text |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 107 | Image generation, asset processing, design automation |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 89 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,938 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,496 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
