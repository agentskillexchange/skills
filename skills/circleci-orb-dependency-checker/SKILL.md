---
name: CircleCI Orb Dependency Checker
description: Scans CircleCI config.yml for orb version conflicts and breaking changes
  using the CircleCI Orbs Registry API. Validates executor configurations against
  circleci/docker and circleci/node orb specs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-dependency-checker/
category:
- CI/CD Integrations
framework:
- Codex
---
# CircleCI Orb Dependency Checker

The CircleCI Orb Dependency Checker analyzes CircleCI configuration files to identify orb version conflicts, deprecated parameters, and breaking changes. It queries the CircleCI Orbs Registry API to fetch latest orb versions and changelogs, comparing them against your pinned versions to surface available updates and potential incompatibilities. The checker validates executor configurations against popular orb specifications including circleci/docker, circleci/node, circleci/python, and circleci/aws-cli orbs. It performs deep parameter validation, ensuring that job parameters match expected types and constraints defined in the orb source. Workflow dependency analysis identifies circular dependencies, unreachable jobs, and filter misconfigurations. The skill generates a comprehensive compatibility report with automated upgrade paths, including orb version bump PRs via the CircleCI API v2 pipeline trigger endpoint. It also validates resource class allocations and suggests optimizations based on historical build metrics.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-checker/)
