---
title: "Enforce red-green-refactor discipline in Claude Code sessions with TDD Guard"
description: "Block implementation-first agent behavior and keep Claude Code anchored to failing-tests-first TDD loops."
verification: "listed"
source: "https://github.com/nizos/tdd-guard"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "nizos/tdd-guard"
  github_stars: 1997
  npm_package: "tdd-guard"
  npm_weekly_downloads: 35484
---

# Enforce red-green-refactor discipline in Claude Code sessions with TDD Guard

Use TDD Guard when Claude Code is about to code ahead of the test signal. It intercepts the session, checks whether the change started from a failing test, and pushes the workflow back toward red, then green, then refactor before the agent keeps going. Invoke this instead of relying on normal Claude Code prompting when you need active enforcement of TDD discipline rather than best-effort instructions. The scope is tightly bounded to hook-based TDD validation inside Claude Code sessions, not a generic test runner or broad developer toolkit.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard/)
