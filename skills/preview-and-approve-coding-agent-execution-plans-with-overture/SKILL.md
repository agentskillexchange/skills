---
title: "Preview and approve coding-agent execution plans with Overture"
description: "Render an AI coding agent’s plan as an interactive flowchart so a human can inspect dependencies, attach context, choose branches, and approve execution before code changes begin."
verification: "security_reviewed"
source: "https://github.com/SixHq/Overture"
author: "SixHq"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "SixHq/Overture"
  github_stars: 619
  npm_package: "overture-mcp"
  npm_weekly_downloads: 320
---

# Preview and approve coding-agent execution plans with Overture

Render an AI coding agent’s plan as an interactive flowchart so a human can inspect dependencies, attach context, choose branches, and approve execution before code changes begin.

## Prerequisites

Node.js, npx or npm, an MCP-compatible coding agent such as Claude Code, Cursor, Cline, Copilot, or Windsurf

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run `claude mcp add overture-mcp -- npx overture-mcp` for Claude Code, or add an MCP server entry with command `npx` and args ["overture-mcp"] in another MCP-compatible client. Overture opens a local visual plan interface at `http://localhost:3031` when the agent produces a plan.
```

## Documentation

- https://github.com/SixHq/Overture

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/preview-and-approve-coding-agent-execution-plans-with-overture/)
