---
name: "Enforce red-green-refactor discipline in Claude Code sessions with TDD Guard"
slug: "enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard"
description: "Block implementation-first agent behavior and keep Claude Code anchored to failing-tests-first TDD loops."
github_stars: 1997
verification: "security_reviewed"
source: "https://github.com/nizos/tdd-guard"
author: "nizos"
publisher_type: "individual"
category: "Code Quality & Review"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "nizos/tdd-guard"
  github_stars: 1997
  npm_package: "tdd-guard"
  npm_weekly_downloads: 35484
---

# Enforce red-green-refactor discipline in Claude Code sessions with TDD Guard

Block implementation-first agent behavior and keep Claude Code anchored to failing-tests-first TDD loops.

## Prerequisites

Claude Code, Node.js 22+, supported test framework

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the marketplace in Claude Code, install `tdd-guard`, then run `/tdd-guard:setup` to configure the project test reporter and enforcement hooks.
```

## Documentation

- https://github.com/nizos/tdd-guard#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/enforce-red-green-refactor-discipline-in-claude-code-with-tdd-guard/)
