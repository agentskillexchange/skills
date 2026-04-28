---
title: Add executable smoke tests for shell scripts and CLIs before refactors ship
description: Use Bats-core when an agent needs to turn fragile shell scripts or command-line
  workflows into something it can verify repeatedly after edits. The agent writes
  focused Bash tests for success paths, failure paths, and output contracts, then
  runs them locally or in CI before a refactor, release, or incident fix goes out.
verification: security_reviewed
source: https://github.com/bats-core/bats-core
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: bats-core/bats-core
  github_stars: 5974
---

# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/add-shell-and-cli-smoke-tests-before-refactors-ship
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/add-shell-and-cli-smoke-tests-before-refactors-ship`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
