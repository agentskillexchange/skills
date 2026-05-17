---
name: "Your Skill Name"
description: "A clear description of what this skill does and when to use it. Reference specific APIs, tools, or techniques."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://agentskillexchange.com/skills/your-skill-slug/"
---

# Your Skill Name

<!-- What does this skill do? When should someone use it? Be specific. -->

A clear description of the skill. Mention the APIs, tools, or techniques it uses.
Explain the problem it solves and who benefits from it.

## Installation

### OpenClaw

```bash
clawhub install your-skill-slug
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/your-skill-slug ~/.agent-skills/your-skill-slug
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill your-skill-slug
```

