---
title: "Lefthook Git Hooks Manager"
description: "Lefthook is a fast, dependency-free Git hooks manager written in Go that runs pre-commit, pre-push, and custom hook commands in parallel. It integrates with Node.js, Ruby, Python, and any other project type through a simple YAML configuration."
verification: "security_reviewed"
source: "https://github.com/evilmartians/lefthook"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "evilmartians/lefthook"
  github_stars: 7894
  npm_package: "lefthook"
  npm_weekly_downloads: 1640769
---

# Lefthook Git Hooks Manager

Lefthook (github.com/evilmartians/lefthook) is a high-performance Git hooks manager built in Go by Evil Martians. Unlike Husky or pre-commit, Lefthook ships as a single binary with zero runtime dependencies, making it portable across any development environment without requiring Node.js or Python.

The tool manages Git hooks through a declarative lefthook.yml configuration file. You define hook stages (pre-commit, pre-push, commit-msg, etc.) and the commands or scripts to run at each stage. Lefthook supports parallel execution of hook jobs, glob-based file filtering, tag-based command grouping, and Docker integration. It can pass staged files, changed files, or all files to your commands using template variables like {staged_files} and {all_files}.

Installation is available through multiple package managers: npm, gem, pip, Homebrew, apt, winget, and direct Go installation. After installing, a single “lefthook install” command wires everything into your .git/hooks directory. The tool also supports lefthook-local.yml for developer-specific overrides that are not committed to version control.

Lefthook produces structured output showing which jobs passed or failed, with configurable output verbosity. It can run linters like ESLint, Rubocop, or Ruff against only the relevant changed files, keeping hook execution fast even in large monorepos. The parallel execution model means a pre-commit hook running three linters simultaneously finishes in the time of the slowest one, not the sum of all three.

The tool integrates with CI/CD by supporting direct invocation via “lefthook run pre-commit” without requiring a Git context. Custom hook groups can be defined for tasks like auto-fixing code style issues across multiple languages. With over 5,000 GitHub stars and active maintenance, Lefthook has become a standard choice for teams that need fast, reliable Git hooks without the overhead of a JavaScript runtime.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/lefthook-git-hooks-manager/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/lefthook-git-hooks-manager
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/lefthook-git-hooks-manager`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lefthook-git-hooks-manager/)
