---
title: "Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk"
description: "Create, switch, and clean per-branch worktrees so multiple coding agents can work the same repo in parallel without stomping each other."
verification: listed
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk/)
