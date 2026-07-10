---
title: "Give coding agents Figma layout context through MCP"
description: "Configure Framelink’s Figma MCP server so coding agents can fetch clean design layout context from Figma files before implementing UI."
verification: "security_reviewed"
source: "https://github.com/GLips/Figma-Context-MCP"
author: "GLips"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "GLips/Figma-Context-MCP"
  github_stars: 14915
  npm_package: "figma-developer-mcp"
  npm_weekly_downloads: 257887
---

# Give coding agents Figma layout context through MCP

Configure Framelink’s Figma MCP server so coding agents can fetch clean design layout context from Figma files before implementing UI.

## Prerequisites

Node.js, npm or npx, Figma personal access token, MCP-compatible coding client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Create a Figma access token, then add an MCP server command such as `npx -y figma-developer-mcp --figma-api-key=YOUR-KEY --stdio` to Cursor, Claude Desktop, VS Code, or another MCP client.
```

## Documentation

- https://www.framelink.ai/docs/quickstart

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-coding-agents-figma-layout-context-through-mcp/)
