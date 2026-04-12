---
title: "Add executable smoke tests for shell scripts and CLIs before refactors ship"
slug: "add-shell-and-cli-smoke-tests-before-refactors-ship"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
source: "https://github.com/bats-core/bats-core"
tool_ecosystem:
  github_repo: "bats-core/bats-core"
  github_stars: 5966
---

# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
