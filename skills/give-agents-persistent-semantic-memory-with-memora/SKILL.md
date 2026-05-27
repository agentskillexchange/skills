---
name: "Give agents persistent semantic memory with Memora"
slug: "give-agents-persistent-semantic-memory-with-memora"
description: "Use Memora to give MCP-compatible agents persistent semantic memory, document recall, and knowledge-graph context across sessions."
github_stars: 406
verification: "security_reviewed"
source: "https://github.com/agentic-box/memora"
author: "agentic-box"
publisher_type: "open_source"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "agentic-box/memora"
  github_stars: 406
---

# Give agents persistent semantic memory with Memora

Use Memora to give MCP-compatible agents persistent semantic memory, document recall, and knowledge-graph context across sessions.

## Prerequisites

Python package installed from the Memora GitHub repository; MCP-compatible client such as Claude Code, Codex, Cursor, or another MCP host; optional SQLite, S3/R2, or Cloudflare D1 storage

## Installation

Use the upstream install or setup path that matches your environment:
- pip install git+https://github.com/agentic-box/memora.git
- pip install "memora[local]" @ git+https://github.com/agentic-box/memora.git
- npx wrangler d1 create memora-graph
- npx wrangler d1 execute memora-graph --file=memora-graph/schema.sql

Requirements and caveats from upstream:
- ### Node Colors
- Node size reflects connection count.

Basic usage or getting-started notes:
- <b><a href="#features">Features</a></b> · <b><a href="#install">Install</a></b> · <b><a href="#usage">Usage</a></b> · <b><a href="#configuration">Config</a></b> · <b><a href="#live-graph-server">Live Graph</a></b> · <...
- 📊 **Statistics & Analytics** - Tag usage, trends, and connection insights
- bash

- Source: https://github.com/agentic-box/memora
- Extracted from upstream docs: https://raw.githubusercontent.com/agentic-box/memora/HEAD/README.md

## Documentation

- https://github.com/agentic-box/memora

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-agents-persistent-semantic-memory-with-memora/)
