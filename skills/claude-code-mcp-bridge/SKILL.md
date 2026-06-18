---
name: "Claude Code MCP Bridge"
slug: "claude-code-mcp-bridge"
description: "Run Claude Code as a one-shot MCP tool so other agents and editors can delegate coding tasks to it. An agent-in-agent orchestration bridge."
github_stars: 1290
verification: "security_reviewed"
source: "https://github.com/steipete/claude-code-mcp"
author: "Peter Steinberger"
publisher_type: "individual"
category: "Developer Tools"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "steipete/claude-code-mcp"
  github_stars: 1290
  npm_package: "@steipete/claude-code-mcp"
  npm_weekly_downloads: 423
---

# Claude Code MCP Bridge

Run Claude Code as a one-shot MCP tool so other agents and editors can delegate coding tasks to it. An agent-in-agent orchestration bridge.

## Prerequisites

Claude Code CLI (installed and authenticated), Node.js v20+, MCP-compatible client

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g @anthropic-ai/claude-code
- npm test
- npm run test:unit
- npm run test:e2e

Requirements and caveats from upstream:
- Node.js v20 or later (Use fnm or nvm to install)
- **Before the MCP server can use the default bypassPermissions mode, you must first run the Claude CLI manually once with the --dangerously-skip-permissions flag, login and accept the terms.**
- "Generate a Python script to parse CSV data and output JSON."

Basic usage or getting-started notes:
- Run Claude Code with all permissions bypassed by default (using --dangerously-skip-permissions)
- This server is a thin MCP wrapper around the local Claude Code CLI. By default it preserves the historic behavior and starts Claude Code with --dangerously-skip-permissions. Set the tool's permissionMode argument to d...
- The wrapper cannot approve prompts that belong to a parent MCP client, bypass macOS privacy prompts, or make another Claude Code session inherit its settings. If the calling client stalls while waiting for permission...

- Source: https://github.com/steipete/claude-code-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/steipete/claude-code-mcp/HEAD/README.md

## Documentation

- https://github.com/steipete/claude-code-mcp#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/claude-code-mcp-bridge/)
