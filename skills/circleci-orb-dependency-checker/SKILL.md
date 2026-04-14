---
title: "CircleCI Orb Dependency Checker"
description: "Scans CircleCI config.yml for orb version conflicts and breaking changes using the CircleCI Orbs Registry API. Validates executor configurations against circleci/docker and circleci/node orb specs."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Dependency Checker

The CircleCI Orb Dependency Checker analyzes CircleCI configuration files to identify orb version conflicts, deprecated parameters, and breaking changes. It queries the CircleCI Orbs Registry API to fetch latest orb versions and changelogs, comparing them against your pinned versions to surface available updates and potential incompatibilities. The checker validates executor configurations against popular orb specifications including circleci/docker, circleci/node, circleci/python, and circleci/aws-cli orbs. It performs deep parameter validation, ensuring that job parameters match expected types and constraints defined in the orb source. Workflow dependency analysis identifies circular dependencies, unreachable jobs, and filter misconfigurations. The skill generates a comprehensive compatibility report with automated upgrade paths, including orb version bump PRs via the CircleCI API v2 pipeline trigger endpoint. It also validates resource class allocations and suggests optimizations based on historical build metrics.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-checker/)
