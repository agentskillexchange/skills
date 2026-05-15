---
title: "Let agents control a logged-in Chrome browser through Playwriter MCP"
slug: "let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp"
description: "Use Playwriter to give MCP-compatible agents a bounded, stateful Playwright control surface over an operator-approved Chrome session."
github_stars: 3507
verification: "security_reviewed"
source: "https://github.com/remorses/playwriter"
author: "remorses"
publisher_type: "open_source"
category: "Browser Automation"
framework: "MCP"
tool_ecosystem:
  github_repo: "remorses/playwriter"
  github_stars: 3507
---

# Let agents control a logged-in Chrome browser through Playwriter MCP

Use Playwriter to give MCP-compatible agents a bounded, stateful Playwright control surface over an operator-approved Chrome session.

## Prerequisites

Playwriter Chrome extension and CLI; MCP-compatible client when using MCP mode; Chrome/Chromium browser session

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Playwriter Chrome extension or start the bundled Playwriter browser, install the CLI with npm i -g playwriter, create a session with playwriter session new, and run scoped commands with playwriter -s <session> -e '<Playwright snippet>' or configure the MCP server for a compatible client.
```

## Documentation

- https://playwriter.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/let-agents-control-a-logged-in-chrome-browser-through-playwriter-mcp/)
