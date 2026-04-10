---
title: "CircleCI Orb Dependency Checker"
description: "Scans CircleCI config.yml for orb version conflicts and breaking changes using the CircleCI Orbs Registry API. Validates executor configurations against circleci/docker and circleci/node orb specs."
slug: "circleci-orb-dependency-checker"
category:
  - "CI/CD Integrations"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-checker/"
---

# CircleCI Orb Dependency Checker

Scans CircleCI config.yml for orb version conflicts and breaking changes using the CircleCI Orbs Registry API. Validates executor configurations against circleci/docker and circleci/node orb specs.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install circleci-orb-dependency-checker
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Dependency Checker analyzes CircleCI configuration files to identify orb version conflicts, deprecated parameters, and breaking changes. It queries the CircleCI Orbs Registry API to fetch latest orb versions and changelogs, comparing them against your pinned versions to surface available updates and potential incompatibilities. The checker validates executor configurations against popular orb specifications including circleci/docker, circleci/node, circleci/python, and circleci/aws-cli orbs. It performs deep parameter validation, ensuring that job parameters match expected types and constraints defined in the orb source. Workflow dependency analysis identifies circular dependencies, unreachable jobs, and filter misconfigurations. The skill generates a comprehensive compatibility report with automated upgrade paths, including orb version bump PRs via the CircleCI API v2 pipeline trigger endpoint. It also validates resource class allocations and suggests optimizations based on historical build metrics.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-checker/)
