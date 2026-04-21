---
title: "Add executable smoke tests for shell scripts and CLIs before refactors ship"
slug: "add-shell-and-cli-smoke-tests-before-refactors-ship"
description: "Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out."
verification: security_reviewed
source: "https://github.com/bats-core/bats-core"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bats-core/bats-core"
  github_stars: 5974
---

# Add executable smoke tests for shell scripts and CLIs before refactors ship

Use Bats-core when an agent needs to turn fragile shell scripts or command-line workflows into something it can verify repeatedly after edits. The agent writes focused Bash tests for success paths, failure paths, and output contracts, then runs them locally or in CI before a refactor, release, or incident fix goes out.

## Installation

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-shell-and-cli-smoke-tests-before-refactors-ship/)
