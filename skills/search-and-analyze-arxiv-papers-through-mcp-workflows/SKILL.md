---
title: "Search and analyze arXiv papers through MCP workflows"
description: "Connect an MCP-capable assistant to arXiv search, paper download, local paper storage, and research prompts for grounded literature review workflows."
verification: "security_reviewed"
source: "https://github.com/blazickjp/arxiv-mcp-server"
author: "blazickjp"
publisher_type: "individual"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "blazickjp/arxiv-mcp-server"
  github_stars: 2760
---

# Search and analyze arXiv papers through MCP workflows

Connect an MCP-capable assistant to arXiv search, paper download, local paper storage, and research prompts for grounded literature review workflows.

## Prerequisites

Python 3.11+, uv or supported MCP bundle installer, MCP-compatible client such as Claude Desktop, VS Code, Kiro, or another stdio MCP host

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with Smithery, a Claude Desktop .mcpb release bundle, or manually with uv tool install arxiv-mcp-server, then register the arxiv-mcp-server stdio command in the MCP client. Use the optional [pdf] extra when older PDF-only arXiv papers must be parsed.
```

## Documentation

- https://github.com/blazickjp/arxiv-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-analyze-arxiv-papers-through-mcp-workflows/)
