---
name: "CircleCI Orb Validator"
description: "Validates and lints CircleCI orb configurations using the CircleCI CLI and circleci-config-sdk. Checks for deprecated keys, version constraints, and executor compatibility before publishing."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/circleci-orb-validator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "circleci"  # from ase_tool_match
  github_stars: 842  # from ase_github_stars (integer, not string)
  github_repo: "circleci/circleci-docs"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# CircleCI Orb Validator

Validates and lints CircleCI orb configurations using the CircleCI CLI and circleci-config-sdk. Checks for deprecated keys, version constraints, and executor compatibility before publishing.

## Overview

The CircleCI Orb Validator skill provides comprehensive validation of CircleCI orb packages before they are published to the CircleCI Orb Registry. It uses the official CircleCI CLI for schema validation and the circleci-config-sdk for programmatic analysis of orb structure.

The validator checks for deprecated configuration keys, ensures executor definitions are compatible with the target CircleCI server version, and validates that all referenced orb dependencies exist and meet version constraints. It performs semantic analysis beyond basic YAML validation, catching common mistakes like missing docker image tags, invalid resource class specifications, and circular command references.

Integration with the CircleCI REST API v2 allows the skill to verify that referenced contexts, environment variables, and project settings exist before deployment. It can also perform dry-run pipeline triggers to validate orb behavior in a sandboxed environment.

The skill supports inline orb definitions, external orb references, and parameterized orb configurations. It generates detailed validation reports with specific line numbers and suggested fixes for each issue found.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-validator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-validator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-validator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-validator -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-validator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-orb-validator/
