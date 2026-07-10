---
title: "Build n8n workflows from node docs, templates, and schemas through MCP"
description: "Use n8n-MCP when an agent needs structured access to n8n nodes, properties, operations, and template examples while designing or debugging workflows, instead of guessing from raw docs or clicking through the n8n UI by hand."
verification: "security_reviewed"
source: "https://github.com/czlonkowski/n8n-mcp"
author: "czlonkowski"
publisher_type: "individual"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "czlonkowski/n8n-mcp"
  github_stars: 18088
  npm_package: "n8n-mcp"
  npm_weekly_downloads: 485039
---

# Build n8n workflows from node docs, templates, and schemas through MCP

Use n8n-MCP when an agent needs structured access to n8n nodes, properties, operations, and template examples while designing or debugging workflows, instead of guessing from raw docs or clicking through the n8n UI by hand.

## Prerequisites

n8n-MCP, an MCP-compatible client such as Claude Code, Cursor, Codex, or Windsurf, and optionally an n8n instance for validating generated workflows

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run n8n-MCP with the upstream npx or Docker self-hosting path, configure the required API key or local settings, then add the server to your MCP client so the agent can query n8n nodes, templates, and workflow guidance before editing flows.
```

## Documentation

- https://github.com/czlonkowski/n8n-mcp#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-n8n-workflows-from-node-docs-templates-and-schemas-through-mcp/)
