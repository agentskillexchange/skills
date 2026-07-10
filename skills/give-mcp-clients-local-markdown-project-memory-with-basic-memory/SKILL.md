---
title: "Give MCP clients local Markdown project memory with Basic Memory"
description: "Connect Claude, Codex, Cursor, ChatGPT, or any MCP-capable client to a local-first Markdown knowledge graph so agents can write, search, and reuse project context across sessions."
verification: "security_reviewed"
source: "https://github.com/basicmachines-co/basic-memory"
author: "Basic Machines"
publisher_type: "organization"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "basicmachines-co/basic-memory"
  github_stars: 3192
---

# Give MCP clients local Markdown project memory with Basic Memory

Connect Claude, Codex, Cursor, ChatGPT, or any MCP-capable client to a local-first Markdown knowledge graph so agents can write, search, and reuse project context across sessions.

## Prerequisites

Python 3.12+, uv, Basic Memory CLI, an MCP-capable client such as Claude, Codex, Cursor, ChatGPT, or VS Code, and a local Markdown workspace

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `uv tool install basic-memory`, create or select a local Basic Memory project, then configure the Basic Memory MCP server in the target AI client so the agent can write, search, and fetch Markdown-backed memories.
```

## Documentation

- https://github.com/basicmachines-co/basic-memory#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-mcp-clients-local-markdown-project-memory-with-basic-memory/)
