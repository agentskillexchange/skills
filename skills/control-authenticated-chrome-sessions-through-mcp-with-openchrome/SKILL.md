---
name: "Control authenticated Chrome sessions through MCP with OpenChrome"
slug: "control-authenticated-chrome-sessions-through-mcp-with-openchrome"
description: "Let an agent drive a real logged-in Chrome profile through MCP for authenticated browsing, parallel tab work, and token-efficient page interaction without re-authenticating each run."
github_stars: 206
verification: "security_reviewed"
source: "https://github.com/shaun0927/openchrome"
author: "shaun0927"
publisher_type: "individual"
category: "Browser Automation"
framework: "MCP"
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

Use the upstream install or setup path that matches your environment:
- npm install -g openchrome-mcp
- npx openchrome-mcp setup --client opencode # OpenCode

Requirements and caveats from upstream:
- (macOS / Windows / Linux, beta) runs the server with no Node.js setup.
- launched it (Docker, systemd, CI):
- openchrome doctor # Node, disk, Chrome binary/port, orphans, perms, locks

Basic usage or getting-started notes:
- bash
- openchrome setup # Claude Code
- openchrome setup --client codex # Codex CLI

- Source: https://github.com/shaun0927/openchrome
- Extracted from upstream docs: https://raw.githubusercontent.com/shaun0927/openchrome/HEAD/README.md

## Documentation

- https://github.com/shaun0927/openchrome

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/control-authenticated-chrome-sessions-through-mcp-with-openchrome/)
