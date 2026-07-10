---
title: "Read and modify Figma designs from coding agents with Talk to Figma MCP"
description: "Bridge Cursor, Claude Code, and other MCP clients into Figma so agents can inspect selections, create nodes, annotate designs, and apply bulk edits."
verification: "security_reviewed"
source: "https://github.com/grab/cursor-talk-to-figma-mcp"
author: "Grab"
publisher_type: "organization"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "grab/cursor-talk-to-figma-mcp"
  github_stars: 6832
  npm_package: "cursor-talk-to-figma-mcp"
  npm_weekly_downloads: 11128
---

# Read and modify Figma designs from coding agents with Talk to Figma MCP

Bridge Cursor, Claude Code, and other MCP clients into Figma so agents can inspect selections, create nodes, annotate designs, and apply bulk edits.

## Prerequisites

Bun, MCP-compatible client, Figma desktop or web app, Talk to Figma Figma plugin

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Bun, run `bun setup`, start the bridge with `bun socket`, install the Talk to Figma plugin from Figma Community or locally, then connect the plugin channel and register the MCP server in the agent client.
```

## Documentation

- https://www.figma.com/community/plugin/1485687494525374295/cursor-talk-to-figma-mcp-plugin

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/read-and-modify-figma-designs-from-coding-agents-with-talk-to-figma-mcp/)
