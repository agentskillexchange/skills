---
title: "Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk"
slug: "spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk"
description: "Create, switch, and clean per-branch worktrees so multiple coding agents can work the same repo in parallel without stomping each other."
github_stars: 4399
verification: "security_reviewed"
source: "https://github.com/max-sixty/worktrunk"
author: "max-sixty"
publisher_type: "individual"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "max-sixty/worktrunk"
  github_stars: 4399
---

# Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk

Create, switch, and clean per-branch worktrees so multiple coding agents can work the same repo in parallel without stomping each other.

## Prerequisites

Git repository, Worktrunk CLI, local shell access, one or more coding agents such as Claude Code or Codex

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Worktrunk from the upstream release or package instructions, initialize it in the target Git repository, then use the documented switch, list, and remove flows to manage per-agent worktrees.
```

## Documentation

- https://worktrunk.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk/)
