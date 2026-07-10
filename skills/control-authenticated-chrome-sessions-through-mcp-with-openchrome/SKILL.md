---
title: "Control authenticated Chrome sessions through MCP with OpenChrome"
description: "Let an agent drive a real logged-in Chrome profile through MCP for authenticated browsing, parallel tab work, and token-efficient page interaction without re-authenticating each run."
verification: "security_reviewed"
source: "https://github.com/shaun0927/openchrome"
author: "shaun0927"
publisher_type: "individual"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "shaun0927/openchrome"
  github_stars: 206
  npm_package: "openchrome-mcp"
  npm_weekly_downloads: 12099
---

# Control authenticated Chrome sessions through MCP with OpenChrome

Let an agent drive a real logged-in Chrome profile through MCP for authenticated browsing, parallel tab work, and token-efficient page interaction without re-authenticating each run.

## Prerequisites

Node.js, npm, Google Chrome, MCP-compatible client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `npm install -g openchrome-mcp`, run `openchrome setup` for Claude Code or `openchrome setup --client codex` for Codex CLI, then restart the MCP client. For other clients, configure the MCP server command as `openchrome serve --auto-launch`.
```

## Documentation

- https://github.com/shaun0927/openchrome

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-authenticated-chrome-sessions-through-mcp-with-openchrome/)
