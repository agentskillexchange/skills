---
name: "CircleCI Config Validator"
description: "Validates and optimizes CircleCI configuration files using the CircleCI v2 API and circleci config validate CLI. Analyzes orb usage, parallelism settings, and resource class allocation."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-config-validator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Config Validator

Validates and optimizes CircleCI configuration files using the CircleCI v2 API and circleci config validate CLI. Analyzes orb usage, parallelism settings, and resource class allocation.

## Overview

The CircleCI Config Validator skill ensures CircleCI pipeline configurations are correct, efficient, and follow best practices. It uses the CircleCI v2 API to fetch pipeline definitions, workflow structures, and job configurations for analysis. The circleci config validate command is invoked to catch syntax errors and schema violations before commits. The skill analyzes orb usage patterns, recommending version pinning and identifying deprecated orb features. Parallelism settings are evaluated against test suite sizes to optimize execution time. Resource class allocation is reviewed to balance cost and performance, suggesting machine executor upgrades or Docker image optimizations where beneficial. The skill also checks for proper caching strategies, workspace persistence between jobs, and approval job configurations for deployment gates.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-config-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-config-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-config-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-config-validator -a codex
```

### OpenClaw

```bash
clawhub install circleci-config-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-config-validator/
