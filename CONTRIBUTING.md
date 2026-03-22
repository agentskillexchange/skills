# Contributing to Agent Skill Exchange

Thanks for your interest in contributing. Whether you're submitting a new skill, improving an existing one, or reporting issues — this guide covers what you need to know.

## Ways to Contribute

### 1. Submit a Skill via the Website (Recommended)

The easiest way is through our [Create Skill](https://agentskillexchange.com/create-skill/) page. It walks you through the format and publishes directly to the marketplace. Skills submitted this way are automatically synced to this repo.

### 2. Submit a Skill via Pull Request

Fork this repo, create a skill directory, and open a PR.

```bash
# Fork and clone
git clone https://github.com/YOUR-USERNAME/skills.git
cd skills

# Create your skill
mkdir -p skills/my-skill-name

# Write the SKILL.md
# (see format spec below)

# Open a PR
git add skills/my-skill-name/
git commit -m "Add my-skill-name"
git push origin main
```

### 3. Improve an Existing Skill

Found a typo, outdated info, or a way to make a skill better? Open a PR with the fix. We appreciate corrections to descriptions, install commands, and API references.

### 4. Report Issues

Use [GitHub Issues](https://github.com/agentskillexchange/skills/issues) for:
- Skills with incorrect or outdated content
- Missing or broken install commands
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
description: "One-paragraph description of what this skill does and when to use it. Be specific about APIs, tools, and techniques involved."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
rating: 4.5
reviews: 12
creator: "Your Name"
creator_handle: "your-github-handle"
creator_verified: false
source: "https://agentskillexchange.com/skill/your-skill-slug/"
---
```

### Frontmatter Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | ✅ | Display name of the skill |
| `description` | string | ✅ | What the skill does, when to use it. Reference real APIs and tools. |
| `category` | string | ✅ | One of the 17 marketplace categories (see below) |
| `framework` | string | ✅ | Primary framework: Claude Code, Cursor, Codex, OpenClaw, Gemini, etc. |
| `verification` | string | ✅ | `listed`, `verified_metadata`, or `security_reviewed` |
| `rating` | number | ❌ | Community rating (1.0–5.0). Set by marketplace, not by contributor. |
| `reviews` | number | ❌ | Review count. Set by marketplace. |
| `creator` | string | ✅ | Creator display name |
| `creator_handle` | string | ❌ | GitHub handle or marketplace handle |
| `creator_verified` | boolean | ❌ | Whether the creator is verified on the marketplace |
| `source` | string | ❌ | Link to the skill on agentskillexchange.com |

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

Claude Code, Cursor, Codex, OpenClaw, Gemini, Claude Agents, ChatGPT Agents, Custom Agents, MCP-compatible, WordPress, Google Workspace

### Markdown Body

After the frontmatter, include:

1. **Heading** matching the skill name
2. **Description paragraph** — what it does and when to use it
3. **Installation section** — commands for each supported agent
4. **Creator attribution** (optional)

Example:

```markdown
# My Skill Name

Description of what this skill does...

## Installation

### Any agent (npx skills)

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

Skills in this repo should:

- **Reference real APIs, tools, and techniques** — no placeholder or made-up API names
- **Have a clear use case** — the description should explain *when* to use this skill
- **Include working install commands** — test them before submitting
- **Use proper English** — clear, concise, no filler language
- **Fit a valid category** — don't invent new categories; pick the closest match
- **Be original** — don't duplicate existing skills without adding clear value

Skills that don't meet these standards will be asked to revise during PR review.

---

## Verification Process

All new skills enter at the **Listed** tier. They can advance through verification:

| Tier | What It Means |
|------|---------------|
| **Listed** | Published and indexed in the marketplace |
| **Verified Metadata** | Frontmatter, source links, and install instructions have been reviewed and confirmed accurate |
| **Security Reviewed** | Content scanned and manually reviewed for prompt injection, data exfiltration, credential harvesting, and malicious patterns |

Verification is handled by the marketplace team. You don't need to request it — skills are reviewed in batches. Higher-quality submissions get reviewed faster.

---

## PR Review Process

1. Open a PR with your new or updated skill
2. Automated checks validate the SKILL.md format
3. A reviewer checks the content for quality and accuracy
4. If approved, it merges to `main` and syncs to the marketplace within the hour
5. The skill enters the verification pipeline

Typical review time: 1–3 business days.

---

## Questions?

- Browse the [marketplace](https://agentskillexchange.com) to see how existing skills look
- Check our [blog](https://agentskillexchange.com/blog/) for guides and announcements
- Open an [issue](https://github.com/agentskillexchange/skills/issues) if something isn't clear
