---
title: "Search NotebookLM notebooks, sources, and generated study artifacts from agents"
description: "Use notebooklm-mcp-cli when an agent needs to search NotebookLM notebooks, add sources, run notebook queries, and retrieve generated study artifacts without leaving an MCP workflow."
verification: "security_reviewed"
source: "https://github.com/jacob-bd/notebooklm-mcp-cli"
author: "jacob-bd"
publisher_type: "individual"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jacob-bd/notebooklm-mcp-cli"
  github_stars: 3558
---

# Search NotebookLM notebooks, sources, and generated study artifacts from agents

Use notebooklm-mcp-cli when an agent needs to search NotebookLM notebooks, add sources, run notebook queries, and retrieve generated study artifacts without leaving an MCP workflow.

## Prerequisites

A NotebookLM account, browser-based authentication or cookie import, Python tooling via uv, pip, or pipx, and an MCP-compatible client if you want agent-side access.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the unified package with uv tool install notebooklm-mcp-cli, pip install notebooklm-mcp-cli, or pipx install notebooklm-mcp-cli. Run nlm login to authenticate, then configure your client with nlm setup add claude-code, nlm setup add cursor, nlm setup add gemini, or point it directly at the notebooklm-mcp executable.
```

## Documentation

- https://github.com/jacob-bd/notebooklm-mcp-cli/blob/main/docs/MCP_GUIDE.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-notebooklm-notebooks-sources-and-generated-study-artifacts-from-agents/)
