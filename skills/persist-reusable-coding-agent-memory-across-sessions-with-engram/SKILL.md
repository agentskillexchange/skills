---
title: "Persist reusable coding-agent memory across sessions with Engram"
slug: "persist-reusable-coding-agent-memory-across-sessions-with-engram"
description: "Keep searchable long-term memory for coding agents in a local SQLite store and expose it through MCP when sessions keep forgetting prior decisions, conventions, and useful findings."
github_stars: 2576
verification: "security_reviewed"
source: "https://github.com/Gentleman-Programming/engram"
author: "Gentleman Programming"
publisher_type: "organization"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "Gentleman-Programming/engram"
  github_stars: 2576
---

# Persist reusable coding-agent memory across sessions with Engram

Keep searchable long-term memory for coding agents in a local SQLite store and expose it through MCP when sessions keep forgetting prior decisions, conventions, and useful findings.

## Prerequisites

Local shell, Engram binary, and an MCP-compatible coding agent such as Claude Code, Codex, Gemini CLI, Cursor, or VS Code

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the Engram binary, then use the agent-specific setup instructions in the repository, for example `engram setup codex` or `engram setup gemini-cli`, or register `engram mcp` manually with your MCP client.
```

## Documentation

- https://github.com/Gentleman-Programming/engram

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/persist-reusable-coding-agent-memory-across-sessions-with-engram/)
