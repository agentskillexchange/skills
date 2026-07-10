---
title: "Control Windows desktop apps through MCP with Terminator"
description: "Connect Terminator MCP to an agent so it can inspect and automate real Windows desktop and browser workflows with pixels, DOM, and accessibility context."
verification: "security_reviewed"
source: "https://github.com/mediar-ai/terminator"
author: "Mediar AI"
publisher_type: "organization"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "mediar-ai/terminator"
  github_stars: 1534
  npm_package: "terminator-mcp-agent"
  npm_weekly_downloads: 57
---

# Control Windows desktop apps through MCP with Terminator

Connect Terminator MCP to an agent so it can inspect and automate real Windows desktop and browser workflows with pixels, DOM, and accessibility context.

## Prerequisites

MCP-capable client such as Claude Code, Cursor, or VS Code, Node.js/npx, Terminator MCP agent package, Windows desktop environment for full native automation

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the MCP server with claude mcp add terminator "npx -y terminator-mcp-agent@latest" or the equivalent MCP client configuration, verify the desktop automation permissions and environment, then run supervised UI automation tasks against the target desktop or browser workflow.
```

## Documentation

- https://github.com/mediar-ai/terminator/tree/main/terminator-mcp-agent

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-windows-desktop-apps-through-mcp-with-terminator/)
