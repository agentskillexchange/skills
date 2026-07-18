---
name: "Give coding agents AST-backed semantic code search with CocoIndex Code"
slug: "give-coding-agents-ast-backed-semantic-code-search-with-cocoindex-code"
description: "Install CocoIndex Code as a skill, plugin, CLI, or MCP server so coding agents can initialize, update, and query local AST-backed semantic code indexes."
github_stars: 2517
verification: "security_reviewed"
source: "https://github.com/cocoindex-io/cocoindex-code"
author: "CocoIndex"
publisher_type: "organization"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "cocoindex-io/cocoindex-code"
  github_stars: 2517
---

# Give coding agents AST-backed semantic code search with CocoIndex Code

Install CocoIndex Code as a skill, plugin, CLI, or MCP server so coding agents can initialize, update, and query local AST-backed semantic code indexes.

## Prerequisites

Python tool install via pipx or uv; optional local or cloud embedding provider; Claude Code/Grok skill support or an MCP-capable coding agent

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install 'cocoindex-code[full]' # batteries included (local embeddings)
- pipx upgrade cocoindex-code # upgrade
- uv tool install --upgrade 'cocoindex-code[full]'
- npx skills add cocoindex-io/cocoindex-code

Requirements and caveats from upstream:
- Two install styles — they mirror the Docker image variants of the same names:
- cocoindex-code[full] — batteries-included. Pulls in sentence-transformers so local embeddings (no API key required) work out of the box. The ccc init interactive prompt defaults to [Snowflake/snowflake-arctic-embed-xs...
- cocoindex-code (slim) — LiteLLM-only; requires a cloud embedding provider and API key. Use when you don't want the local-embedding deps (~1 GB of torch + transformers).

Basic usage or getting-started notes:
- Using [pipx](https://pipx.pypa.io/stable/installation/):
- Using [uv](https://docs.astral.sh/uv/getting-started/installation/):
- Next, set up your [coding agent integration](#coding-agent-integration) — or jump to [Manual CLI Usage](#manual-cli-usage) if you prefer direct control.

- Source: https://github.com/cocoindex-io/cocoindex-code
- Extracted from upstream docs: https://raw.githubusercontent.com/cocoindex-io/cocoindex-code/HEAD/README.md

## Documentation

- https://cocoindex.io/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-coding-agents-ast-backed-semantic-code-search-with-cocoindex-code/)
