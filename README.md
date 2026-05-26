<div align="center">

# Agent Skill Exchange

### The open catalog of AI agent skills

[![Published](https://img.shields.io/badge/published-2%2C513-6366f1?style=for-the-badge)](skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](categories/)
[![Security%20Reviewed](https://img.shields.io/badge/security--reviewed-2%2C161-10b981?style=for-the-badge)](verification/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Categories](categories/) · [Industry Collections](industries/README.md) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Catalog](CATALOG.md) · [Submit a Skill](#submit-a-skill)**

*2,513 published skills · 17 categories · Real ecosystem signals · Updated daily*

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

**[Format and lint TOML configuration with Tombi](skills/format-and-lint-toml-configuration-with-tombi/)** — Run Tombi as a TOML formatter, linter, and language server so agents can clean and validate pyproject, Cargo, and other TOML config files before committing changes.

_Rotates daily by UTC date from the Security Reviewed pool._

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

See the full overlay index in [industries/README.md](industries/README.md).

---

## Featured Skills

Mirrors the live ASE homepage featured shelf: recent-popular, diversified across tools and categories, rather than a frozen all-time-stars list. See [TOP-STARS.md](TOP-STARS.md) and [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) for raw rankings.

| Skill | Tool | ⭐ Stars | Category |
|-------|------|--------:|----------|
| [Run multi-harness coding-agent workflows with Oh My OpenAgent](skills/run-multi-harness-coding-agent-workflows-with-oh-my-openagent/) | run-multi-harness-coding-agent-workflows-with-oh-my-openagent | 58.9k | Developer Tools |
| [Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse](skills/parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse/) | parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse | 5.1k | Data Extraction & Transformation |
| [Run terminal-native coding agent workflows with GitHub Copilot CLI](skills/run-terminal-native-coding-agent-workflows-with-github-copilot-cli/) | run-terminal-native-coding-agent-workflows-with-github-copilot-cli | 10.6k | Developer Tools |
| [Run durable agent tasks and event-driven workflows with Hatchet](skills/run-durable-agent-tasks-and-event-driven-workflows-with-hatchet/) | run-durable-agent-tasks-and-event-driven-workflows-with-hatchet | 7.2k | Templates & Workflows |
| [Trace and evaluate agent runs with Phoenix](skills/trace-and-evaluate-agent-runs-with-phoenix/) | trace-and-evaluate-agent-runs-with-phoenix | 9.8k | Monitoring & Alerts |
| [Connect Azure DevOps projects, work items, repos, and pipelines to MCP agents](skills/connect-azure-devops-projects-work-items-repos-and-pipelines-to-mcp-agents/) | connect-azure-devops-projects-work-items-repos-and-pipelines-to-mcp-agents | 1.7k | Integrations & Connectors |
| [Operate Kubernetes and OpenShift clusters through MCP](skills/operate-kubernetes-and-openshift-clusters-through-mcp/) | operate-kubernetes-and-openshift-clusters-through-mcp | 1.6k | Runbooks & Diagnostics |
| [Inspect live web apps and apply code changes with Stagewise](skills/inspect-live-web-apps-and-apply-code-changes-with-stagewise/) | inspect-live-web-apps-and-apply-code-changes-with-stagewise | 6.7k | Templates & Workflows |
| [Trace, evaluate, simulate, and guardrail agent releases with Future AGI](skills/trace-evaluate-simulate-and-guardrail-agent-releases-with-future-agi/) | trace-evaluate-simulate-and-guardrail-agent-releases-with-future-agi | 1k | Monitoring & Alerts |
| [Format and lint TOML configuration with Tombi](skills/format-and-lint-toml-configuration-with-tombi/) | format-and-lint-toml-configuration-with-tombi | 937 | Code Quality & Review |
| [Control a real browser from MCP clients with Browser MCP](skills/control-a-real-browser-from-mcp-clients-with-browser-mcp/) | control-a-real-browser-from-mcp-clients-with-browser-mcp | 6.6k | Browser Automation |
| [Control authenticated Chrome sessions through MCP with OpenChrome](skills/control-authenticated-chrome-sessions-through-mcp-with-openchrome/) | control-authenticated-chrome-sessions-through-mcp-with-openchrome | 206 | Browser Automation |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | 327 | CLI tools, scaffolders, dev environment setup |
| 🔒 | [**Security & Verification**](categories/security-verification/) | 227 | Vulnerability scanning, auth setup, compliance |
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | 192 | Pipeline configs, deployment automation, build tooling |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | 184 | Linting, code review, test generators, coverage |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | 172 | ETL pipelines, parsing, format conversion |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | 171 | Incident response, troubleshooting, system diagnostics |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | 167 | Scaffolders, boilerplate generators, workflow templates |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | 133 | Metrics, alerting rules, observability |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | 123 | Email automation, calendar management, task coordination |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | 122 | SDK docs, API parsers, symbol resolvers |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | 120 | Third-party API bridges, webhooks, service connectors |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | 108 | Web scraping, UI testing, headless browser control |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | 107 | Web research, content discovery, data collection |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | 98 | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | 96 | Theme/plugin dev, WP-CLI automation, CMS management |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | 89 | Image generation, asset processing, design automation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | 78 | SEO content, blog automation, editorial workflows |

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
| 📋 **Published** | 2,513 | In the catalog — every skill is backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | 2,161 | Scanned for malicious patterns, prompt injection, and unsafe instructions |

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
