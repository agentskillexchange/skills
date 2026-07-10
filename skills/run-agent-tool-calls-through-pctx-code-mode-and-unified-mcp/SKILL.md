---
name: "Run agent tool calls through pctx Code Mode and unified MCP"
slug: "run-agent-tool-calls-through-pctx-code-mode-and-unified-mcp"
description: "Put pctx between agents and tools so MCP servers and custom tools can run through a code-oriented execution layer instead of one-off tool calls."
github_stars: 264
verification: "security_reviewed"
source: "https://github.com/portofcontext/pctx"
author: "Port of Context"
publisher_type: "organization"
category: "Developer Tools"
framework: "MCP"
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

Install the pctx CLI and the client library that matches your agent stack:

```bash
brew install portofcontext/tap/pctx
npm i -g @portofcontext/pctx
pip install pctx-client
```

Use the Python client when building Python agents that call pctx as an HTTP service. Use the npm package or Homebrew CLI when you want pctx available as a local command for Code Mode or MCP setup. Existing Homebrew installs can be updated separately with `brew upgrade pctx`; do not treat that as the first-install path.

Basic setup:

```bash
pctx start
pctx mcp init
```

Run pctx as the boundary between your agent and registered tools/MCP servers. Keep the MCP server list explicit, review which tools are exposed through Code Mode, and avoid giving the bridge broader filesystem or network access than the workflow needs.

## Documentation

- https://github.com/portofcontext/pctx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-tool-calls-through-pctx-code-mode-and-unified-mcp/)
