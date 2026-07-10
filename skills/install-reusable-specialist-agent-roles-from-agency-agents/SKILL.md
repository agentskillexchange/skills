---
title: "Install reusable specialist agent roles from Agency Agents"
description: "Install and adapt Agency Agents’ curated specialist role files so coding agents can switch into focused engineering, product, marketing, support, or operations workflows."
verification: "security_reviewed"
source: "https://github.com/msitarzewski/agency-agents"
author: "Marcin Sitarzewski"
publisher_type: "individual"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "msitarzewski/agency-agents"
  github_stars: 95921
---

# Install reusable specialist agent roles from Agency Agents

Install and adapt Agency Agents’ curated specialist role files so coding agents can switch into focused engineering, product, marketing, support, or operations workflows.

## Prerequisites

Agency Agents repository scripts; a supported agent runtime such as Claude Code, OpenClaw, Cursor, Gemini CLI, OpenCode, Copilot, Aider, Windsurf, Kimi, or Antigravity

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository, run ./scripts/convert.sh to generate integration files when needed, then run ./scripts/install.sh or ./scripts/install.sh --tool <runtime>; for Claude Code-only use, copy selected agent markdown files into ~/.claude/agents/.
```

## Documentation

- https://github.com/msitarzewski/agency-agents

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/install-reusable-specialist-agent-roles-from-agency-agents/)
