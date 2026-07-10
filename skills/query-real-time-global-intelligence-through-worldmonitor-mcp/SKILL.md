---
title: "Query real-time global intelligence through Worldmonitor MCP"
description: "Give MCP-capable agents a live global-intelligence surface for country briefs, risk scores, conflict, cyber, market, weather, and infrastructure monitoring."
verification: "security_reviewed"
source: "https://github.com/koala73/worldmonitor"
author: "koala73"
publisher_type: "individual"
category:
  - "Monitoring & Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "koala73/worldmonitor"
  github_stars: 61437
  npm_package: "worldmonitor"
  npm_weekly_downloads: 602
---

# Query real-time global intelligence through Worldmonitor MCP

Give MCP-capable agents a live global-intelligence surface for country briefs, risk scores, conflict, cyber, market, weather, and infrastructure monitoring.

## Prerequisites

MCP-compatible client, Worldmonitor API key for authenticated tool calls, Node.js/npm for CLI usage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
For MCP, configure the Streamable HTTP endpoint at `https://worldmonitor.app/mcp` and provide `X-WorldMonitor-Key` for authenticated tool calls. For CLI use, run `npx worldmonitor tools` to list available tools or install globally with `npm install -g worldmonitor`.
```

## Documentation

- https://www.worldmonitor.app/docs/getting-started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/query-real-time-global-intelligence-through-worldmonitor-mcp/)
