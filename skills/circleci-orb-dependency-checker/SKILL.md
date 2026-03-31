---
name: "CircleCI Orb Dependency Checker"
description: "Scans CircleCI config.yml for orb version conflicts and breaking changes using the CircleCI Orbs Registry API. Validates executor configurations against circleci/docker and circleci/node orb specs."
category: "CI/CD Integrations"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-dependency-checker/"
---
# CircleCI Orb Dependency Checker

Scans CircleCI config.yml for orb version conflicts and breaking changes using the CircleCI Orbs Registry API. Validates executor configurations against circleci/docker and circleci/node orb specs.

## Overview

The CircleCI Orb Dependency Checker analyzes CircleCI configuration files to identify orb version conflicts, deprecated parameters, and breaking changes. It queries the CircleCI Orbs Registry API to fetch latest orb versions and changelogs, comparing them against your pinned versions to surface available updates and potential incompatibilities. The checker validates executor configurations against popular orb specifications including circleci/docker, circleci/node, circleci/python, and circleci/aws-cli orbs. It performs deep parameter validation, ensuring that job parameters match expected types and constraints defined in the orb source. Workflow dependency analysis identifies circular dependencies, unreachable jobs, and filter misconfigurations. The skill generates a comprehensive compatibility report with automated upgrade paths, including orb version bump PRs via the CircleCI API v2 pipeline trigger endpoint. It also validates resource class allocations and suggests optimizations based on historical build metrics.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-checker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-checker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-checker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-dependency-checker -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-dependency-checker
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-dependency-checker/)
