<div align="center">

# Agent Skill Exchange

### The largest open collection of verified AI agent skills

[![Skills](https://img.shields.io/badge/skills-1%2C000+-6366f1?style=for-the-badge)](https://agentskillexchange.com/browse-skills/)
[![Verified](https://img.shields.io/badge/verified-1%2C000+-10b981?style=for-the-badge)](https://agentskillexchange.com/verified-skills/)
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

|  | Agent Skill Exchange | anthropics/skills | sickn33/antigravity | obra/superpowers |
|---|:---:|:---:|:---:|:---:|
| **Total Skills** | **1,000+** | 17 | 1,306 | ~20 |
| **Community Ratings** | ✅ | ❌ | ❌ | ❌ |
| **Verification Tiers** | ✅ 3-tier | ❌ | ❌ | ❌ |
| **Multi-Framework** | ✅ 11 | Claude only | Claude only | Claude + Cursor |
| **Live Marketplace** | ✅ | ❌ | ❌ | ❌ |
| **Auto-Updated** | ✅ Hourly | Manual | Manual | Manual |
| **Creator Profiles** | ✅ | ❌ | ❌ | ❌ |

---

## Categories

| Category | Skills | Browse |
|----------|-------:|--------|
| 🔧 CI/CD Integrations | 193 | [Browse →](https://agentskillexchange.com/categories/?cat=ci-cd-integrations) |
| 📋 Runbooks & Diagnostics | 157 | [Browse →](https://agentskillexchange.com/categories/?cat=runbooks-diagnostics) |
| ✅ Code Quality & Review | 111 | [Browse →](https://agentskillexchange.com/categories/?cat=code-quality-review) |
| 🛠️ Developer Tools | 102 | [Browse →](https://agentskillexchange.com/categories/?cat=developer-tools) |
| 📚 Library & API Reference | 74 | [Browse →](https://agentskillexchange.com/categories/?cat=library-api-reference) |
| 📄 Templates & Workflows | 56 | [Browse →](https://agentskillexchange.com/categories/?cat=templates-workflows) |
| 🔄 Data Extraction & Transformation | 48 | [Browse →](https://agentskillexchange.com/categories/?cat=data-extraction-transformation) |
| 🔒 Security & Verification | 45 | [Browse →](https://agentskillexchange.com/categories/?cat=security-verification) |
| 📊 Monitoring & Alerts | 43 | [Browse →](https://agentskillexchange.com/categories/?cat=monitoring-alerts) |
| 📅 Calendar, Email & Productivity | 41 | [Browse →](https://agentskillexchange.com/categories/?cat=calendar-email-productivity) |
| 🔗 Integrations & Connectors | 41 | [Browse →](https://agentskillexchange.com/categories/?cat=integrations-connectors) |
| ✍️ Content Writing & SEO | 19 | [Browse →](https://agentskillexchange.com/categories/?cat=content-writing-seo) |
| 🎙️ Media & Transcription | 19 | [Browse →](https://agentskillexchange.com/categories/?cat=media-transcription) |
| 🎨 Image & Creative Automation | 18 | [Browse →](https://agentskillexchange.com/categories/?cat=image-creative-automation) |
| 🔍 Research & Scraping | 17 | [Browse →](https://agentskillexchange.com/categories/?cat=research-scraping) |
| 🌐 Browser Automation | 16 | [Browse →](https://agentskillexchange.com/categories/?cat=browser-automation) |
| 📰 WordPress & CMS | 16 | [Browse →](https://agentskillexchange.com/categories/?cat=wordpress-cms) |

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

All 1,000+ skills in this repo have reached **Verified Metadata** or higher. See [how we verify](https://agentskillexchange.com/how-we-verify/) for the full criteria.

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
  ... 1,000+ skills
```

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
