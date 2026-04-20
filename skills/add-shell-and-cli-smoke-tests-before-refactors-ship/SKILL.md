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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
