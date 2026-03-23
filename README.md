<div align="center">

# Agent Skill Exchange

### The largest open collection of verified AI agent skills

[![Skills](https://img.shields.io/badge/skills-1%2C200+-6366f1?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Verified](https://img.shields.io/badge/verified-1%2C200+-10b981?style=for-the-badge)](https://agentskillexchange.com/verified-skills/)
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

- **1,200+ skills and growing** — new skills added every hour, automatically synced from the [live marketplace](https://agentskillexchange.com)
- **Community-rated** — every skill has real ratings and reviews from users
- **3-tier verification** — Listed → Verified Metadata → Security Reviewed — every skill is vetted before reaching production-ready status
- **11 frameworks** — Claude Code, Cursor, Codex, Gemini, OpenClaw, and more — install for any agent with one command
- **Creator profiles** — every skill has an attributed creator with verification badges
- **Full catalog** — browse by [category](#categories), search the [CATALOG](CATALOG.md), or explore the [live marketplace](https://agentskillexchange.com/browse-skills/)

---

## Categories

| | Category | |
|---|---|---|
| 🔧 | CI/CD Integrations | [**213 skills →**](https://agentskillexchange.com/browse-skills/?category=ci-cd-integrations) |
| 📋 | Runbooks & Diagnostics | [**170 skills →**](https://agentskillexchange.com/browse-skills/?category=runbooks-diagnostics) |
| ✅ | Code Quality & Review | [**127 skills →**](https://agentskillexchange.com/browse-skills/?category=code-quality-review) |
| 🛠️ | Developer Tools | [**118 skills →**](https://agentskillexchange.com/browse-skills/?category=developer-tools) |
| 📚 | Library & API Reference | [**86 skills →**](https://agentskillexchange.com/browse-skills/?category=library-api-reference) |
| 📊 | Monitoring & Alerts | [**72 skills →**](https://agentskillexchange.com/browse-skills/?category=monitoring-alerts) |
| 🔄 | Data Extraction & Transformation | [**67 skills →**](https://agentskillexchange.com/browse-skills/?category=data-extraction-transformation) |
| 🔒 | Security & Verification | [**67 skills →**](https://agentskillexchange.com/browse-skills/?category=security-verification) |
| 📄 | Templates & Workflows | [**65 skills →**](https://agentskillexchange.com/browse-skills/?category=templates-workflows) |
| 📅 | Calendar, Email & Productivity | [**57 skills →**](https://agentskillexchange.com/browse-skills/?category=calendar-email-productivity) |
| 🔗 | Integrations & Connectors | [**45 skills →**](https://agentskillexchange.com/browse-skills/?category=integrations-connectors) |
| 🌐 | Browser Automation | [**35 skills →**](https://agentskillexchange.com/browse-skills/?category=browser-automation) |
| 🔍 | Research & Scraping | [**33 skills →**](https://agentskillexchange.com/browse-skills/?category=research-scraping) |
| 🎨 | Image & Creative Automation | [**31 skills →**](https://agentskillexchange.com/browse-skills/?category=image-creative-automation) |
| ✍️ | Content Writing & SEO | [**27 skills →**](https://agentskillexchange.com/browse-skills/?category=content-writing-seo) |
| 🎙️ | Media & Transcription | [**23 skills →**](https://agentskillexchange.com/browse-skills/?category=media-transcription) |
| 📰 | WordPress & CMS | [**20 skills →**](https://agentskillexchange.com/browse-skills/?category=wordpress-cms) |

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

All 1,200+ skills in this repo have reached **Verified Metadata** or higher. See the [verification criteria](https://agentskillexchange.com/verified-skills/) for details.

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
  ... 1,200+ skills
```

See [spec/SKILL_SPEC.md](spec/SKILL_SPEC.md) for the full format specification, or use the [template/SKILL.md](template/SKILL.md) to create your own.

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
