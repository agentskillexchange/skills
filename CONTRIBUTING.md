# Contributing to Agent Skill Exchange

Whether you're submitting a new skill, improving an existing one, or reporting issues — this guide covers what you need to know.

## Ways to Contribute

### 1. Submit a Skill via Pull Request

Fork this repo, create a skill directory, and open a PR.

```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/skills.git
cd skills

# Create your skill
mkdir -p skills/my-skill-name
cp template/SKILL.md skills/my-skill-name/SKILL.md

# Edit the SKILL.md (see format below)

# Open a PR
git add skills/my-skill-name/
git commit -m "Add my-skill-name"
git push origin main
```

### 2. Submit via the Website

Use the [Create Skill](https://agentskillexchange.com/create-skill/) page. Skills submitted this way are automatically synced to this repo.

### 3. Improve an Existing Skill

Found a typo, outdated info, or a way to make a skill better? Open a PR with the fix.

### 4. Report Issues

Use [GitHub Issues](https://github.com/agentskillexchange/skills/issues) for:
- Skills with incorrect or outdated content
- Broken install commands
- Category or framework misclassification
- General repo improvements

For security concerns (malicious skills, prompt injection), see [SECURITY.md](SECURITY.md).

---

## SKILL.md Format

Every skill lives in `skills/<slug>/SKILL.md`. The file has two parts: YAML frontmatter and a markdown body.

### Required Frontmatter

```yaml
---
name: "Human-Readable Skill Name"
description: "What this skill does and when to use it. Be specific about APIs, tools, and techniques."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://agentskillexchange.com/skills/your-skill-slug/"
---
```

### Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Display name of the skill |
| `description` | string | ✅ | What the skill does, when to use it. Reference real APIs and tools. |
| `category` | string | ✅ | One of the 17 categories (see below) |
| `framework` | string | ✅ | Primary framework: Claude Code, Cursor, Codex, OpenClaw, etc. |
| `verification` | string | ✅ | `listed` or `security_reviewed` |
| `source` | string | ❌ | Link to the skill on agentskillexchange.com |
| `tool_ecosystem` | object | ❌ | Real tool signals — only if backed by a verifiable tool (see [spec](spec/SKILL_SPEC.md)) |

### Valid Categories

- Browser Automation
- Calendar, Email & Productivity
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

### Valid Frameworks

Claude Code, Cursor, Codex, OpenClaw, Gemini, Claude Agents, ChatGPT Agents, Custom Agents, MCP, WordPress, Google Workspace

### Markdown Body

After the frontmatter, include:

1. **Heading** matching the skill name
2. **Description** — what it does and when to use it (100+ words with technical detail)
3. **Installation section** — commands for each supported agent

Example:

```markdown
# My Skill Name

Description of what this skill does...

## Installation

### Any Agent

\`\`\`bash
npx skills add agentskillexchange/skills --skill my-skill-name
\`\`\`

### Claude Code

\`\`\`bash
npx skills add agentskillexchange/skills --skill my-skill-name -a claude-code
\`\`\`

### OpenClaw

\`\`\`bash
clawhub install my-skill-name
\`\`\`
```

---

## Quality Standards

Skills should:

- **Reference real APIs, tools, and techniques** — no placeholder or made-up names
- **Have a clear use case** — the description should explain *when* to use this skill
- **Include working install commands**
- **Be backed by a real tool** — a GitHub repo, npm package, or documented API
- **Be original** — don't duplicate existing skills without adding clear value
- **Have 100+ words** of real technical content

---

## Trust Model

| Tier | Meaning |
|------|---------|
| 📋 **Listed** | Published — backed by a real tool, repo, or package |
| 🛡️ **Security Reviewed** | Scanned for malicious patterns, prompt injection, and unsafe instructions |

New skills enter as **Listed**. Security review is handled by the marketplace team in batches — higher-quality submissions get reviewed faster.

---

## PR Review Process

1. Open a PR with your new or updated skill
2. Automated checks validate the SKILL.md format and scan for security concerns
3. A reviewer checks the content for quality and accuracy
4. If approved, it merges to `main` and syncs to the marketplace within the hour

---

## Questions?

- Browse the [catalog](CATALOG.md) to see how existing skills look
- Check the [spec](spec/SKILL_SPEC.md) for the full format reference
- Open an [issue](https://github.com/agentskillexchange/skills/issues) if something isn't clear
