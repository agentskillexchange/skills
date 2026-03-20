# Agent Skill Exchange — Skills Repository

[![Skills](https://img.shields.io/badge/skills-100+-6366f1)](https://agentskillexchange.com)
[![npx skills](https://img.shields.io/badge/npx-skills-green)](https://www.npmjs.com/package/skills)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

**Curated, verified agent skills for every coding agent.**

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

This repo works with **40+ agents** via `npx skills`:

| Agent | Command |
|-------|---------|
| Claude Code | `npx skills add agentskillexchange/skills -a claude-code` |
| Cursor | `npx skills add agentskillexchange/skills -a cursor` |
| Codex | `npx skills add agentskillexchange/skills -a codex` |
| OpenClaw | `npx skills add agentskillexchange/skills -a openclaw` |
| Gemini CLI | `npx skills add agentskillexchange/skills -a gemini-cli` |
| Windsurf | `npx skills add agentskillexchange/skills -a windsurf` |
| Roo Code | `npx skills add agentskillexchange/skills -a roo` |
| [See all 40+](https://github.com/vercel-labs/skills#available-agents) | `npx skills add agentskillexchange/skills` |

### OpenClaw Native

```bash
# Via ClawHub
clawhub install <slug>

# Or directly
openclaw install <slug>
```

## What's Inside

Each skill is a directory with a `SKILL.md` file containing:

- **Frontmatter** — name, description, category, framework compatibility, verification status
- **Instructions** — what the skill does, how to use it, gotchas
- **Installation commands** — copy-paste ready for any agent

## Verification

Every skill in this repo has been through our verification pipeline:

| Status | Meaning |
|--------|---------|
| 🔒 **Security Reviewed** | Read-only/diagnostic skills — safe to run without supervision |
| ✅ **Verified Metadata** | Skills that write/create/send — metadata and behavior verified |

Learn more: [How We Verify Skills](https://agentskillexchange.com/how-we-verify-skills/)

## Categories

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

## Contributing

1. Create a skill using the [Skill Creation Wizard](https://agentskillexchange.com/create-skill/)
2. Submit a PR to this repo with your `skills/<your-skill>/SKILL.md`
3. Skills go through verification before merge

## License

MIT — see [LICENSE](LICENSE) for details.

---

**[Browse All Skills →](https://agentskillexchange.com/browse-skills/)**
