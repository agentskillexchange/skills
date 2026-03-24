<div align="center">

# Agent Skill Exchange

### The largest open collection of verified AI agent skills

[![Skills](https://img.shields.io/badge/skills-1%2C500+-6366f1?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Security Reviewed](https://img.shields.io/badge/security_reviewed-810-10b981?style=for-the-badge)](https://agentskillexchange.com/verified-skills/)
[![Frameworks](https://img.shields.io/badge/frameworks-11-8b5cf6?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Browse Skills](https://agentskillexchange.com/browse-skills/) · [Categories](https://agentskillexchange.com/categories/) · [Rankings](https://agentskillexchange.com/rankings/) · [Verified Skills](https://agentskillexchange.com/verified-skills/) · [Create a Skill](https://agentskillexchange.com/create-skill/)**

*Updated hourly · Community-rated · Security-reviewed · Multi-framework*

</div>

---

## Quick Start

```bash
# Install any skill (works with 40+ agents)
npx skills add agentskillexchange/skills --skill <slug>

# Install for a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code
npx skills add agentskillexchange/skills --skill <slug> -a cursor
npx skills add agentskillexchange/skills --skill <slug> -a codex

# Browse all skills
npx skills add agentskillexchange/skills --list
```

### OpenClaw

```bash
clawhub install <slug>
```

---

## At a Glance

| Metric | Count |
|--------|------:|
| Total skills | **1,580+** |
| 🛡️ Security Reviewed | **810** |
| ✅ Verified Metadata | **379** |
| 📝 Listed | **391** |
| Categories | **17** |
| Frameworks | **11** |
| Creators | **25+** |

---

## Categories

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | **251** | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | **186** | Incident response, troubleshooting, system diagnostics |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | **147** | Linting, code review, test generators, coverage |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | **119** | CLI helpers, scaffolders, dev environment setup |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | **119** | SDK docs, API parsers, symbol resolvers |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | **101** | Metrics, alerting rules, observability |
| 🔒 | [**Security & Verification**](categories/security-verification/) | **99** | Vulnerability scanning, auth setup, compliance |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | **90** | ETL pipelines, parsing, format conversion |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | **84** | Scaffolders, boilerplate generators, workflow templates |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | **72** | Email automation, calendar management, task coordination |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | **61** | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative**](categories/image-creative-automation/) | **51** | Image generation, asset processing, design automation |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | **46** | Third-party API bridges, webhooks, service connectors |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | **39** | Web research, content discovery, data collection |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | **37** | SEO content, blog automation, editorial workflows |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | **31** | Audio/video processing, speech-to-text |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | **24** | Theme/plugin dev, WP-CLI automation, CMS management |

Full listing: [CATALOG.md](CATALOG.md) · Browse by category: [categories/](categories/)

---

## Frameworks

Skills support all major AI agent frameworks. The install command adapts automatically.

| Framework | Skills | Install |
|-----------|------:|---------|
| Claude Code | **250** | `npx skills add ... -a claude-code` |
| OpenClaw | **243** | `clawhub install <slug>` |
| Custom Agents | **218** | `npx skills add ... -a <agent>` |
| MCP | **192** | `npx skills add ... -a mcp` |
| Cursor | **150** | `npx skills add ... -a cursor` |
| Codex | **129** | `npx skills add ... -a codex` |
| Claude Agents | **129** | `npx skills add ...` |
| Gemini | **124** | `npx skills add ... -a gemini-cli` |
| ChatGPT Agents | **122** | `npx skills add ...` |

[All 40+ supported agents →](https://github.com/vercel-labs/skills#available-agents)

---

## Verification

Every skill goes through a transparent verification pipeline:

```
📝 Listed                  Published and indexed — basic format validation
     ↓
✅ Verified Metadata       Frontmatter, source links, and install instructions confirmed
     ↓
🛡️ Security Reviewed      Scanned for prompt injection, data exfiltration,
                           and malicious patterns — safe for production
```

**Current stats:** 810 Security Reviewed · 379 Verified Metadata · 391 Listed

See [verification/](verification/) for full criteria and [SECURITY_PATTERNS.md](verification/SECURITY_PATTERNS.md) for what gets flagged.

---

## Skill Format

Each skill lives in `skills/<slug>/SKILL.md`:

```yaml
---
name: "Stripe Webhook Verifier"
description: "Verifies Stripe webhook signatures using HMAC-SHA256."
category: "Security & Verification"
framework: "Claude Code"
verification: security_reviewed
rating: 4.7
reviews: 43
creator: "Elena Rodriguez"
creator_handle: "@elena_dev"
creator_verified: true
source: "https://agentskillexchange.com/skills/stripe-webhook-verifier/"
---
```

```markdown
# Stripe Webhook Verifier

Verifies Stripe webhook payload signatures using HMAC-SHA256 to prevent
replay attacks and forged events.

## Installation

### Any Agent (npx)
npx skills add agentskillexchange/skills --skill stripe-webhook-verifier

### Claude Code
npx skills add agentskillexchange/skills --skill stripe-webhook-verifier -a claude-code

### OpenClaw
clawhub install stripe-webhook-verifier
```

Full spec: [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md) · Template: [template/SKILL.md](template/SKILL.md)

---

## Repository Structure

```
├── skills/                   # 1,580+ skill directories
│   └── <slug>/SKILL.md       # One file per skill
├── categories/               # Auto-generated category READMEs
├── scripts/                  # Automation tooling
│   ├── generate-catalog.sh   # Regenerates CATALOG.md
│   ├── generate-categories.sh# Regenerates category READMEs
│   └── validate-skill.sh     # Validates SKILL.md format
├── spec/SKILL_SPEC.md        # Format specification
├── template/SKILL.md         # Starter template for new skills
├── verification/             # Verification criteria and security patterns
├── CATALOG.md                # Full searchable catalog (auto-generated)
├── CONTRIBUTING.md           # Contribution guide
└── SECURITY.md               # Security policy
```

---

## Live Marketplace

This repo syncs hourly with **[agentskillexchange.com](https://agentskillexchange.com)**.

The marketplace offers search, filtering, community ratings, creator profiles, and one-click install. Skills submitted on the website sync to this repo automatically.

---

## Contributing

Submit a skill via the [website](https://agentskillexchange.com/create-skill/) (recommended) or open a PR. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

## Security

Found a malicious skill? See [SECURITY.md](SECURITY.md) to report it privately.

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

**[agentskillexchange.com](https://agentskillexchange.com)** · Marketplace for trusted AI agent skills

</div>
