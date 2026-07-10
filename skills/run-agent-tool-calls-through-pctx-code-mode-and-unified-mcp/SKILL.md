---
title: "Run agent tool calls through pctx Code Mode and unified MCP"
description: "Put pctx between agents and tools so MCP servers and custom tools can run through a code-oriented execution layer instead of one-off tool calls."
verification: "security_reviewed"
source: "https://github.com/portofcontext/pctx"
author: "Port of Context"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "portofcontext/pctx"
  github_stars: 264
  npm_package: "@portofcontext/pctx"
  npm_weekly_downloads: 285
---

# Run agent tool calls through pctx Code Mode and unified MCP

Put pctx between agents and tools so MCP servers and custom tools can run through a code-oriented execution layer instead of one-off tool calls.

## Prerequisites

pctx CLI, Python SDK or npm package, MCP-compatible client or OpenAI Agents SDK

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with Homebrew using brew install portofcontext/tap/pctx or npm using npm i -g @portofcontext/pctx. Start Code Mode with pctx start, or initialize a unified MCP setup with pctx mcp init, add upstream servers with pctx mcp add, and run it with pctx mcp dev or pctx mcp start --stdio.
```

## Documentation

- https://github.com/portofcontext/pctx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-tool-calls-through-pctx-code-mode-and-unified-mcp/)
