---
title: "Persist reusable coding-agent memory across sessions with Engram"
description: "Keep searchable long-term memory for coding agents in a local SQLite store and expose it through MCP when sessions keep forgetting prior decisions, conventions, and useful findings."
verification: security_reviewed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/persist-reusable-coding-agent-memory-across-sessions-with-engram
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/persist-reusable-coding-agent-memory-across-sessions-with-engram` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/persist-reusable-coding-agent-memory-across-sessions-with-engram/)
