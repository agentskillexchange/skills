<div align="center">

# Agent Skill Exchange

### The largest open collection of verified AI agent skills

[![Skills](https://img.shields.io/badge/skills-1%2C268+-6366f1?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Verified](https://img.shields.io/badge/verified-1%2C268+-10b981?style=for-the-badge)](https://agentskillexchange.com/verified-skills/)
[![Frameworks](https://img.shields.io/badge/frameworks-11-8b5cf6?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Browse Skills](https://agentskillexchange.com/browse-skills/) · [Categories](https://agentskillexchange.com/categories/) · [Rankings](https://agentskillexchange.com/rankings/) · [Verified Skills](https://agentskillexchange.com/verified-skills/) · [Create a Skill](https://agentskillexchange.com/create-skill/)**

*Updated hourly · Community-rated · Multi-framework*

</div>

---

## Quick Start

```bash
# Install any skill
npx skills add agentskillexchange/skills --skill <slug>

# Browse available skills
npx skills add agentskillexchange/skills --list

# Install for a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code
npx skills add agentskillexchange/skills --skill <slug> -a cursor
npx skills add agentskillexchange/skills --skill <slug> -a codex
```

### OpenClaw Native

```bash
clawhub install <slug>
```

---

## Why This Repo?

- **1568+ skills and growing** — new skills added every hour, automatically synced from the [live marketplace](https://agentskillexchange.com)
- **Community-rated** — every skill has real ratings and reviews from users
- **3-tier verification** — Listed → Verified Metadata → Security Reviewed — every skill is vetted before reaching production-ready status
- **11 frameworks** — Claude Code, Cursor, Codex, Gemini, OpenClaw, and more — install for any agent with one command
- **Creator profiles** — every skill has an attributed creator with verification badges
- **Full catalog** — browse by [category](#categories), search the [CATALOG](CATALOG.md), or explore the [live marketplace](https://agentskillexchange.com/browse-skills/)

---

## Categories

### 🏆 Top Categories

| | Category | Skills | Popularity |
|---|---|:---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | **213** | `████████████████████` |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | **170** | `████████████████` |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | **131** | `████████████` |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | **118** | `███████████` |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | **86** | `████████` |

<details>
<summary><b>📂 All 17 Categories</b></summary>

<br>

| | Category | Skills | Description |
|---|---|:---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | **213** | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | **170** | Incident response, troubleshooting guides, system diagnostics |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | **131** | Linting rules, review checklists, code standards enforcement |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | **118** | CLI helpers, dev environment setup, productivity utilities |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | **86** | SDK docs, API guides, framework reference material |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | **72** | Metrics collection, alerting rules, observability setup |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | **71** | Parsing, ETL pipelines, format conversion, data wrangling |
| 🔒 | [**Security & Verification**](categories/security-verification/) | **67** | Auth setup, vulnerability scanning, compliance checks |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | **65** | Project scaffolding, boilerplate generators, workflow templates |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | **57** | Email automation, calendar management, task coordination |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | **45** | Third-party API bridges, webhook handlers, service connectors |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | **35** | Web scraping, UI testing, headless browser control |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | **35** | Image generation, asset processing, design automation |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | **33** | Web research, data collection, content aggregation |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | **27** | Blog posts, SEO optimization, content strategy |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | **23** | Audio/video processing, speech-to-text, media conversion |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | **20** | Theme/plugin dev, WP-CLI automation, CMS management |

</details>

See the full [CATALOG.md](CATALOG.md) for a detailed listing of every skill, or browse by category in the [categories/](categories/) directory.

---

## Supported Agents

| Agent | Install Command |
|-------|----------------|
| **Any Agent** (npx skills) | `npx skills add agentskillexchange/skills --skill <slug>` |
| **Claude Code** | `npx skills add agentskillexchange/skills --skill <slug> -a claude-code` |
| **Cursor** | `npx skills add agentskillexchange/skills --skill <slug> -a cursor` |
| **Codex** | `npx skills add agentskillexchange/skills --skill <slug> -a codex` |
| **OpenClaw** | `clawhub install <slug>` |
| **Gemini CLI** | `npx skills add agentskillexchange/skills --skill <slug> -a gemini-cli` |
| **Windsurf** | `npx skills add agentskillexchange/skills --skill <slug> -a windsurf` |
| **Roo Code** | `npx skills add agentskillexchange/skills --skill <slug> -a roo` |
| [See all 40+](https://github.com/vercel-labs/skills#available-agents) | `npx skills add agentskillexchange/skills` |

---

## Verification

Every skill goes through a transparent verification pipeline:

```
📝 Listed                  Base marketplace listing — published and indexed
     ↓
✅ Verified Metadata       Frontmatter, source links, and install instructions reviewed
     ↓
🛡️ Security Reviewed      Content scanned for prompt injection, data exfiltration,
                           and malicious patterns. Safe for production use.
```

All 1568+ skills in this repo have reached **Verified Metadata** or higher. See the [verification criteria](verification/) for details.

---

## What's Inside

Each skill directory contains a `SKILL.md` with:

- **YAML frontmatter** — name, description, category, framework, verification status, rating, creator
- **Overview** — what the skill does, key APIs and tools used
- **Install commands** — copy-paste for every supported agent
- **Creator attribution** — who built it, with verified badge where applicable

```
skills/
  a-b-test-analyzer/
    SKILL.md
  api-rate-limiter/
    SKILL.md
  ... 1568+ skills
```

See [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md) for the full format specification, or use the [template/SKILL.md](template/SKILL.md) to create your own.

---

## Repository Tooling

This repo includes automation scripts in [`scripts/`](scripts/):

- **`validate-skill.sh`** — Validates SKILL.md files against the format specification
- **`generate-catalog.sh`** — Regenerates CATALOG.md from the live marketplace API
- **`generate-categories.sh`** — Regenerates category READMEs in `categories/`

---

## Live Marketplace

This repo syncs hourly with the live marketplace at **[agentskillexchange.com](https://agentskillexchange.com)**, where you can:

- Search and filter skills by category, framework, and keyword
- See community ratings and reviews
- View creator profiles and verification badges
- Install with one click
- Submit your own skills

---

## Contributing

We welcome contributions. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide, including:

- How to submit a skill (via [the website](https://agentskillexchange.com/create-skill/) or direct PR)
- SKILL.md format specification
- Quality and verification standards
- Review process

---

## Security

Found a skill with malicious content or a security concern? See [SECURITY.md](SECURITY.md) for how to report it responsibly.

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

**[agentskillexchange.com](https://agentskillexchange.com)** — The marketplace for trusted AI agent skills

</div>
