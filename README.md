<div align="center">

# Agent Skill Exchange

### Open catalog of AI agent skills with live trust and ecosystem signals

[![Skills](https://img.shields.io/badge/skills-1%2C288-6366f1?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Categories](https://img.shields.io/badge/categories-17-0ea5e9?style=for-the-badge)](https://github.com/agentskillexchange/skills/tree/main/categories)
[![Frameworks](https://img.shields.io/badge/frameworks-11-8b5cf6?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Signal%20Coverage](https://img.shields.io/badge/signal_coverage-842-14b8a6?style=for-the-badge)](https://agentskillexchange.com/browse-skills/?sort=stars)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=for-the-badge)](LICENSE)

**[Browse Skills](https://agentskillexchange.com/browse-skills/) · [Categories](https://github.com/agentskillexchange/skills/tree/main/categories) · [Top Starred](TOP-STARS.md) · [Top Downloaded](TOP-DOWNLOADS.md) · [Create a Skill](https://agentskillexchange.com/create-skill/)**

*Updated hourly · Real ecosystem signals · Multi-framework*

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

## Start Here

If you're new to the repo, use these entry points first:

- **Browse by category:** [categories/](categories/)
- **Top Starred:** [TOP-STARS.md](TOP-STARS.md)
- **Top Downloaded:** [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md)
- **Live marketplace browse:** <https://agentskillexchange.com/browse-skills/>

---

## Featured Paths

| Section | Best for | Link |
|---|---|---|
| ⭐ **Top Starred** | Skills with the strongest GitHub traction | [TOP-STARS.md](TOP-STARS.md) |
| 🔥 **Top Downloaded** | Skills tied to widely-used npm ecosystems | [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) |
| 🛡️ **Security Reviewed** | Highest trust tier in ASE | [verification/security_reviewed.md](verification/security_reviewed.md) |

These are the repo-native equivalents of the strongest ASE homepage discovery sections.

---

## Categories

Categories are the best way to understand the shape of the catalog. For live sorting by stars, downloads, and verification, jump from a category into the ASE browse surface.

| | Category | Skills | What's inside |
|---|---|---:|---|
| 🔧 | [**CI/CD Integrations**](categories/ci-cd-integrations/) | **144** | Pipeline configs, deployment automation, build tooling |
| 📋 | [**Runbooks & Diagnostics**](categories/runbooks-diagnostics/) | **122** | Incident response, troubleshooting, system diagnostics |
| 🛠️ | [**Developer Tools**](categories/developer-tools/) | **120** | CLI helpers, scaffolders, dev environment setup |
| 📚 | [**Library & API Reference**](categories/library-api-reference/) | **102** | SDK docs, API parsers, symbol resolvers |
| 📊 | [**Monitoring & Alerts**](categories/monitoring-alerts/) | **91** | Metrics, alerting rules, observability |
| 🔄 | [**Data Extraction & Transformation**](categories/data-extraction-transformation/) | **88** | ETL pipelines, parsing, format conversion |
| ✅ | [**Code Quality & Review**](categories/code-quality-review/) | **88** | Linting, code review, test generators, coverage |
| 🔒 | [**Security & Verification**](categories/security-verification/) | **88** | Vulnerability scanning, auth setup, compliance |
| 📄 | [**Templates & Workflows**](categories/templates-workflows/) | **76** | Scaffolders, boilerplate generators, workflow templates |
| 📅 | [**Calendar, Email & Productivity**](categories/calendar-email-productivity/) | **58** | Email automation, calendar management, task coordination |
| 🎨 | [**Image & Creative Automation**](categories/image-creative-automation/) | **53** | Image generation, asset processing, design automation |
| 🔍 | [**Research & Scraping**](categories/research-scraping/) | **48** | Web research, content discovery, data collection |
| 🌐 | [**Browser Automation**](categories/browser-automation/) | **47** | Web scraping, UI testing, headless browser control |
| 🎙️ | [**Media & Transcription**](categories/media-transcription/) | **42** | Audio/video processing, speech-to-text |
| ✍️ | [**Content Writing & SEO**](categories/content-writing-seo/) | **41** | SEO content, blog automation, editorial workflows |
| 🔗 | [**Integrations & Connectors**](categories/integrations-connectors/) | **40** | Third-party API bridges, webhooks, service connectors |
| 📰 | [**WordPress & CMS**](categories/wordpress-cms/) | **28** | Theme/plugin dev, WP-CLI automation, CMS management |

Full listing: [CATALOG.md](CATALOG.md) · Browse by category: [categories/](categories/) · Live browse: <https://agentskillexchange.com/browse-skills/>

---

## At a Glance

| Metric | Count |
|--------|------:|
| Total skills | **1,288** |
| Categories | **17** |
| Frameworks | **11** |
| Skills with live signal data | **842** |

### Verification tiers

| Tier | Count |
|------|------:|
| 🛡️ Security Reviewed | **760** |
| ✅ Verified Metadata | **7** |
| 📋 Listed | **521** |

> Verification counts are **final-state buckets**, not cumulative stages. That means `listed` can be smaller than `security_reviewed` if many skills have already been promoted by the scanner.

---

## Verification Tiers

ASE uses these exact verification values:

| Tier | What it means |
|------|---|
| 🛡️ Security Reviewed | Content scanned for malicious patterns, unsafe instructions, and prompt-injection risks |
| ✅ Verified Metadata | Frontmatter schema, install commands, and linked tool ecosystem data verified |
| 📋 Listed | Published with baseline structure but not yet promoted to a higher trust tier |

More: [verification/README.md](verification/README.md)

---

## Browse by Signal

- [TOP-STARS.md](TOP-STARS.md) — highest GitHub stars where ASE has a matched source
- [TOP-DOWNLOADS.md](TOP-DOWNLOADS.md) — highest npm weekly downloads where ASE has a matched package
- Live browse by stars: <https://agentskillexchange.com/browse-skills/?sort=stars>
- Live browse by downloads: <https://agentskillexchange.com/browse-skills/?sort=downloads>

---

## Contributing

Skills are managed via [agentskillexchange.com](https://agentskillexchange.com/create-skill/). The repository is updated automatically when skills are published or updated.

- **[Submit a skill](https://agentskillexchange.com/create-skill/)** — publish your agent skill
- **[Browse skills](https://agentskillexchange.com/browse-skills/)** — explore the full catalog
- **[Verification](verification/README.md)** — learn how trust tiers work

---

<div align="center">

*Built by the [Agent Skill Exchange](https://agentskillexchange.com/) community*

</div>
