---
title: "Give agents persistent semantic memory with Memora"
description: "Use Memora to give MCP-compatible agents persistent semantic memory, document recall, and knowledge-graph context across sessions."
verification: "security_reviewed"
source: "https://github.com/agentic-box/memora"
author: "agentic-box"
publisher_type: "open_source"
category:
  - "Integrations & Connectors"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "agentic-box/memora"
  github_stars: 406
---

# Give agents persistent semantic memory with Memora

Use Memora to give MCP-compatible agents persistent semantic memory, document recall, and knowledge-graph context across sessions.

## Prerequisites

Python package installed from the Memora GitHub repository; MCP-compatible client such as Claude Code, Codex, Cursor, or another MCP host; optional SQLite, S3/R2, or Cloudflare D1 storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with pip install git+https://github.com/agentic-box/memora.git, then run memora-server for stdio MCP mode or configure memora-server --transport streamable-http for HTTP mode. Add the documented memora MCP server block to the target agent client and set storage environment variables such as MEMORA_DB_PATH or MEMORA_STORAGE_URI before using memory tools.
```

## Documentation

- https://github.com/agentic-box/memora

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-agents-persistent-semantic-memory-with-memora/)
