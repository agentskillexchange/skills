<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C554-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C201-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*2,554 published skills · 17 categories · Real ecosystem signals · Updated daily*

</div>

---

## What is this?

An open, machine-readable catalog of reusable skills for AI coding agents. Each skill wraps a real tool, API, or workflow into a format that agents like Claude Code, Cursor, Codex, and OpenClaw can install and use.

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

**[Install Superpowers methodology for coding agents](skills/install-superpowers-methodology-for-coding-agents/)** — Use Superpowers to give coding agents a structured software-development method with discovery, spec review, planning, TDD, subagents, and review loops.

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
| 📚 | [**DevRel & API Documentation**](industries/devrel-api-documentation.md) | API docs, OpenAPI references, SDK generation, docs-site publishing, prose linting, and developer enablement workflows. |
| 🎧 | [**Customer Support & Success**](industries/customer-support-success.md) | Helpdesk queues, ticket triage, conversation lookup, knowledge-base workflows, customer context, CRM sync, and reply-drafting support. |
| 🏠 | [**Real Estate Workflows**](industries/real-estate-workflows.md) | Property research support, transaction paperwork, signature routing, document intake, CRM context, and listing follow-up workflows for real-estate operations. |
| 🎓 | [**Education & Research Workflows**](industries/education-research-workflows.md) | Literature review, citation context, research synthesis, paper drafting, replication checks, and evidence packets for academic and technical teams. |
| 🧭 | [**AI Agency Operations & FDE Workflows**](industries/ai-agency-operations.md) | Client-facing AI delivery, agency operations, forward deployed engineering workflows, automation consulting, and reusable implementation systems for client work. |

See the full overlay index in [industries/README.md](industries/README.md).

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | Tool | ⭐ Stars | Category |
|-------|------|--------:|----------|
| [Run durable agent tasks and event-driven workflows with Hatchet](skills/run-durable-agent-tasks-and-event-driven-workflows-with-hatchet/) | run-durable-agent-tasks-and-event-driven-workflows-with-hatchet | 7.2k | Templates & Workflows |
| [Run terminal-native coding agent workflows with GitHub Copilot CLI](skills/run-terminal-native-coding-agent-workflows-with-github-copilot-cli/) | run-terminal-native-coding-agent-workflows-with-github-copilot-cli | 10.6k | Developer Tools |
| [Use A2A for agent-to-agent interoperability workflows](skills/use-a2a-for-agent-to-agent-interoperability-workflows/) | use-a2a-for-agent-to-agent-interoperability-workflows | 24.1k | Integrations & Connectors |
| [Use Flowise for visual agent workflow orchestration](skills/use-flowise-for-visual-agent-workflow-orchestration/) | use-flowise-for-visual-agent-workflow-orchestration | 53.3k | Templates & Workflows |
| [Give coding agents Figma layout context through MCP](skills/give-coding-agents-figma-layout-context-through-mcp/) | give-coding-agents-figma-layout-context-through-mcp | 14.9k | Integrations & Connectors |
| [Build managed document parsing pipelines with LlamaCloud Services](skills/build-managed-document-parsing-pipelines-with-llamacloud-services/) | build-managed-document-parsing-pipelines-with-llamacloud-services | 4.2k | Data Extraction & Transformation |
| [Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse](skills/parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse/) | parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse | 5.1k | Data Extraction & Transformation |
| [Run autonomous deep research workflows with GPT Researcher](skills/run-autonomous-deep-research-workflows-with-gpt-researcher/) | run-autonomous-deep-research-workflows-with-gpt-researcher | 27.4k | Research & Scraping |
| [Give coding agents persistent project memory with AgentMemory](skills/give-coding-agents-persistent-project-memory-with-agentmemory/) | give-coding-agents-persistent-project-memory-with-agentmemory | 17.2k | Developer Tools |
| [Gate agent inputs and outputs with Superagent safety checks](skills/gate-agent-inputs-and-outputs-with-superagent-safety-checks/) | gate-agent-inputs-and-outputs-with-superagent-safety-checks | 6.6k | Security & Verification |
| [Read Google Drive files and edit Sheets through MCP](skills/read-google-drive-files-and-edit-sheets-through-mcp/) | read-google-drive-files-and-edit-sheets-through-mcp | 280 | Calendar, Email & Productivity |
| [Trace and evaluate agent runs with Phoenix](skills/trace-and-evaluate-agent-runs-with-phoenix/) | trace-and-evaluate-agent-runs-with-phoenix | 9.8k | Monitoring & Alerts |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 333 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 231 | Vulnerability scanning, auth setup, compliance |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 184 | Linting, code review, test generators, coverage |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 178 | ETL pipelines, parsing, format conversion |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 175 | Scaffolders, boilerplate generators, workflow templates |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 172 | Incident response, troubleshooting, system diagnostics |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 133 | Metrics, alerting rules, observability |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 127 | Third-party API bridges, webhooks, service connectors |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 124 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 122 | SDK docs, API parsers, symbol resolvers |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 111 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 110 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 99 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 89 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 79 | SEO content, blog automation, editorial workflows |

---

## Browse

| | View | What you'll find |
|---|---|---|
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
| 📋 **Published** | 2,554 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,201 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
