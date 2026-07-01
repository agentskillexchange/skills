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

Use the upstream install or setup path that matches your environment:
- brew install portofcontext/tap/pctx
- npm i -g @portofcontext/pctx
- pip install pctx-client
- brew upgrade pctx

Requirements and caveats from upstream:
- [![Python](https://img.shields.io/pypi/v/pctx-client?color=blue)](https://pctx.readthedocs.io/en/latest/)
- Use the Python SDK if building agents in Python and want to run Code Mode with custom tools and/or MCP servers. The Python SDK is an HTTP client to the pctx server.
- python

Basic usage or getting-started notes:
- pctx can be run as a stateless HTTP server for Code Mode sessions or as a unified MCP server that exposes Code Mode functionality for registered upstream MCP servers.
- pctx start
- pctx mcp init

- Source: https://github.com/portofcontext/pctx
- Extracted from upstream docs: https://raw.githubusercontent.com/portofcontext/pctx/HEAD/README.md

## Documentation

- https://github.com/portofcontext/pctx

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agent-tool-calls-through-pctx-code-mode-and-unified-mcp/)
