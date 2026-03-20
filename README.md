# Agent Skill Exchange — Skills Repository

[![Skills](https://img.shields.io/badge/skills-626+-6366f1)](https://agentskillexchange.com/browse-skills/)
[![Verified](https://img.shields.io/badge/verified-626+-10b981)](https://agentskillexchange.com/verified-skills/)
[![npx skills](https://img.shields.io/badge/npx-skills-green)](https://www.npmjs.com/package/skills)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Curated, verified agent skills for every coding agent.** Updated hourly.

Browse the full marketplace at **[agentskillexchange.com](https://agentskillexchange.com)**

## Quick Start

```bash
# Install any skill to your agent
npx skills add agentskillexchange/skills --skill <slug>

# List available skills
npx skills add agentskillexchange/skills --list

# Install to a specific agent
npx skills add agentskillexchange/skills --skill <slug> -a claude-code

# Install all skills
npx skills add agentskillexchange/skills --all
```

## Supported Agents

This repo works with **40+ agents** via [`npx skills`](https://github.com/vercel-labs/skills):

| Agent | Command |
|-------|---------|
| Claude Code | `npx skills add agentskillexchange/skills -a claude-code` |
| Cursor | `npx skills add agentskillexchange/skills -a cursor` |
| Codex | `npx skills add agentskillexchange/skills -a codex` |
| OpenClaw | `npx skills add agentskillexchange/skills -a openclaw` |
| Gemini CLI | `npx skills add agentskillexchange/skills -a gemini-cli` |
| Windsurf | `npx skills add agentskillexchange/skills -a windsurf` |
| Roo Code | `npx skills add agentskillexchange/skills -a roo` |
| ChatGPT | `npx skills add agentskillexchange/skills -a chatgpt` |
| [See all 40+](https://github.com/vercel-labs/skills#available-agents) | `npx skills add agentskillexchange/skills` |

### OpenClaw Native

```bash
clawhub install <slug>
```

## What's Inside

Each skill directory contains a `SKILL.md` with:

- **Frontmatter** — name, description, category, framework, creator, verification status, rating
- **Overview** — what it does, key APIs/tools used
- **Installation** — copy-paste commands for every agent
- **Creator** — who built it, with verified badge where applicable

## Verification

Every skill goes through our review process:

| Tier | Meaning |
|------|---------|
| 🟢 **Security Reviewed** | Read-only skills — code inspected, no write/send/exec risk |
| 🔵 **Verified Metadata** | Write/create skills — metadata, source, and install instructions verified |
| ⚪ **Listed** | Published with baseline marketplace structure |

Learn more: [How We Verify Skills](https://agentskillexchange.com/how-we-verify-skills/)

## Categories

Skills span 15+ categories:

- Browser Automation
- CI/CD Integrations
- Code Quality & Review
- Content Writing & SEO
- Data Extraction & Transformation
- Developer Tools
- Image & Creative Automation
- Integrations & Connectors
- Library & API Reference
- Media & Transcription
- Monitoring & Alerts
- Research & Scraping
- Runbooks & Diagnostics
- Security & Verification
- Templates & Workflows
- WordPress & CMS

## Top Creators

| Creator | Skills | Verified |
|---------|--------|----------|
| Priya Sharma | 33 | ✓ |
| Alex Thompson | 27 | ✓ |
| Yuki Tanaka | 27 | ✓ |
| Elena Kowalski | 27 | ✓ |
| Raj Gupta | 27 | ✓ |
| Mia Zhang | 28 | ✓ |
| Ava Wilson | 28 | ✓ |

[See all creators →](https://agentskillexchange.com/browse-skills/)

## Contributing

1. Create a skill using the [Skill Creation Wizard](https://agentskillexchange.com/create-skill/)
2. Submit a PR to this repo with your `skills/<your-skill>/SKILL.md`
3. Skills go through verification before merge

## Repo Stats

- **590+ skills** across 15+ categories
- **25 creators** contributing skills
- **Updated hourly** via automated sync from [agentskillexchange.com](https://agentskillexchange.com)
- **Compatible with 40+ agents** via npx skills

## License

MIT — see [LICENSE](LICENSE) for details.

---

**[Browse All Skills →](https://agentskillexchange.com/browse-skills/)** · **[Verified Skills →](https://agentskillexchange.com/verified-skills/)** · **[Create a Skill →](https://agentskillexchange.com/create-skill/)**
