---
title: "Add executable smoke tests for shell scripts and CLIs before refactors ship"
slug: "add-shell-and-cli-smoke-tests-before-refactors-ship"
verification: security_reviewed
source: "https://github.com/bats-core/bats-core"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bats-core/bats-core"
  github_stars: 5974
---
# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
