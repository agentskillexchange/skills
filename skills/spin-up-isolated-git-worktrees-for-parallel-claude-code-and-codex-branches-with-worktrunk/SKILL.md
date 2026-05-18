---
name: "Spin up isolated git worktrees for parallel Claude Code and Codex branches with Worktrunk"
slug: "spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk"
description: "Create, switch, and clean per-branch worktrees so multiple coding agents can work the same repo in parallel without stomping each other."
github_stars: 4399
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- brew install worktrunk && wt config shell install
- cargo install worktrunk && wt config shell install
- conda install -c conda-forge worktrunk && wt config shell install

Requirements and caveats from upstream:
- worktree requires typing the branch name three times: git worktree add -b feat

Basic usage or getting-started notes:
- **[Hooks](https://worktrunk.dev/hook/)** — run commands on create, pre-merge, post-merge, etc
- **Homebrew (macOS & Linux):**
- bash

- Source: https://github.com/max-sixty/worktrunk
- Extracted from upstream docs: https://raw.githubusercontent.com/max-sixty/worktrunk/HEAD/README.md

## Documentation

- https://worktrunk.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/spin-up-isolated-git-worktrees-for-parallel-claude-code-and-codex-branches-with-worktrunk/)
