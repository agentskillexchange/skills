---
title: "Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk"
description: "Create, switch, and clean per-branch worktrees so multiple coding agents can work the same repo in parallel without stomping each other."
verification: "listed"
source: "https://github.com/max-sixty/worktrunk"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "max-sixty/worktrunk"
  github_stars: 4399
---

# Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk

Use Worktrunk when an agent operator needs to create, enter, list, and clean isolated Git worktrees around parallel coding-agent tasks, not when they just need a general Git client. The invoke moment is specific: before or during multi-branch Claude Code or Codex work, give each run its own working directory and branch lifecycle so changes do not collide. That scope boundary, git worktree orchestration for parallel coding-agent branches, keeps this publishable as a skill instead of collapsing into a plain Git product card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk/)
