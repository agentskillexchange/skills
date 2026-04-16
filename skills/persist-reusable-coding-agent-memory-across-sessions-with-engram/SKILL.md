---
title: "Persist reusable coding-agent memory across sessions with Engram"
description: "Keep searchable long-term memory for coding agents in a local SQLite store and expose it through MCP when sessions keep forgetting prior decisions, conventions, and useful findings."
verification: "listed"
source: "https://github.com/Gentleman-Programming/engram"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "Gentleman-Programming/engram"
  github_stars: 2576
---

# Persist reusable coding-agent memory across sessions with Engram

Use Engram when a coding agent needs memory that survives the current session. The workflow is specific: install the single binary, connect it to an MCP-capable agent, save and search memory entries, and reuse prior decisions, code patterns, and notes instead of starting from zero every run.


This belongs in ASE because the job is not “use a database” or “browse a TUI.” The invocable skill is persistent memory management for coding agents through a local MCP-accessible store with CLI and TUI support. That boundary is concrete, operator-facing, and distinct from generic vector databases, generic SQLite tools, or broad agent frameworks.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/persist-reusable-coding-agent-memory-across-sessions-with-engram/)
