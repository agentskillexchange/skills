---
title: "Add executable smoke tests for shell scripts and CLIs before refactors ship"
slug: "add-shell-and-cli-smoke-tests-before-refactors-ship"
description: "Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out."
verification: "security_reviewed"
source: "https://github.com/bats-core/bats-core"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bats-core/bats-core"
  github_stars: 5966
---

# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

Choose the install method that fits your setup:

1. Install from Agent Skill Exchange
2. Install with OpenClaw skill tools
3. Clone or copy the upstream project files
4. Add the skill to your local skills directory manually
5. Use the upstream package or repo install flow directly

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
