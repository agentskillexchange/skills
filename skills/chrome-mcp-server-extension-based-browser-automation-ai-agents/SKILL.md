---
title: "Chrome MCP Server Extension-Based Browser Automation for AI Agents"
description: "Chrome MCP Server uses a Chrome extension and local bridge to expose your everyday browser to MCP-compatible agents. It is designed for workflows where an agent should reuse real tabs, existing login state, browser history, bookmarks, and native Chrome APIs instead of launching a separate automation browser."
verification: "security_reviewed"
source: "https://github.com/hangwin/mcp-chrome"
author: "hangwin"
publisher_type: "Individual Developer"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "hangwin/mcp-chrome"
  github_stars: 11177
---

# Chrome MCP Server Extension-Based Browser Automation for AI Agents

Chrome MCP Server uses a Chrome extension and local bridge to expose your everyday browser to MCP-compatible agents. It is designed for workflows where an agent should reuse real tabs, existing login state, browser history, bookmarks, and native Chrome APIs instead of launching a separate automation browser.

## Prerequisites

Node.js >= 20, npm or pnpm, Chrome/Chromium, Chrome extension

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install -g mcp-chrome-bridge
```

## Documentation

- https://github.com/hangwin/mcp-chrome

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chrome-mcp-server-extension-based-browser-automation-ai-agents/)
