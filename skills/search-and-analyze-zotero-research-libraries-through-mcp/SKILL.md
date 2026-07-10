---
title: "Search and analyze Zotero research libraries through MCP"
description: "Use Zotero MCP to let research agents search papers, retrieve metadata, inspect annotations, and analyze citation context from a Zotero library."
verification: "listed"
source: "https://github.com/54yyyu/zotero-mcp"
author: "54yyyu"
publisher_type: "open_source_project"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "54yyyu/zotero-mcp"
  github_stars: 3353
---

# Search and analyze Zotero research libraries through MCP

Use Zotero MCP to let research agents search papers, retrieve metadata, inspect annotations, and analyze citation context from a Zotero library.

## Prerequisites

Zotero, Zotero local API or web API credentials, Python package tooling such as uv, pip, or pipx, and an MCP-capable client

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the base server with uv tool install zotero-mcp-server, pip install zotero-mcp-server, or pipx install zotero-mcp-server, then run zotero-mcp setup to configure supported MCP clients. Add optional extras such as zotero-mcp-server[semantic], zotero-mcp-server[pdf], zotero-mcp-server[scite], or zotero-mcp-server[all] when semantic search, PDF extraction, or citation intelligence is needed.
```

## Documentation

- https://stevenyuyy.com/zotero-mcp/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-analyze-zotero-research-libraries-through-mcp/)
