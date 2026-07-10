---
title: "Run supervised MCP browser automation with Auto Browser"
description: "Give an MCP-capable agent a local Playwright browser with human takeover, reusable auth profiles, approvals, audit trails, and repeatable browser workflow evidence."
verification: "security_reviewed"
source: "https://github.com/LvcidPsyche/auto-browser"
author: "LvcidPsyche"
publisher_type: "open_source"
category:
  - "Browser Automation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "LvcidPsyche/auto-browser"
  github_stars: 565
---

# Run supervised MCP browser automation with Auto Browser

Give an MCP-capable agent a local Playwright browser with human takeover, reusable auth profiles, approvals, audit trails, and repeatable browser workflow evidence.

## Prerequisites

Docker Compose, Auto Browser, MCP-compatible client or bundled stdio bridge, Playwright browser stack, optional noVNC operator dashboard

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone https://github.com/LvcidPsyche/auto-browser, run docker compose up --build, then connect an MCP client to the HTTP or stdio bridge. Optional Python clients are published as auto-browser-client and auto-browser-langchain.
```

## Documentation

- https://github.com/LvcidPsyche/auto-browser

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-supervised-mcp-browser-automation-with-auto-browser/)
