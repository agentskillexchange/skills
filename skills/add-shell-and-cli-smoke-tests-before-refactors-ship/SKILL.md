---
name: "add-shell-and-cli-smoke-tests-before-refactors-ship"
title: "Add executable smoke tests for shell scripts and CLIs before refactors ship"
description: "Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/bats-core/bats-core"
tool_ecosystem:
  github_repo: "bats-core/bats-core"
  github_stars: 5966
---

# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
