---
title: "CircleCI Orb Validator"
description: "Validates and lints CircleCI orb configurations using the CircleCI CLI and circleci-config-sdk. Checks for deprecated keys, version constraints, and executor compatibility before publishing."
slug: "circleci-orb-validator"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-validator/"
listed: true
---

# CircleCI Orb Validator

Validates and lints CircleCI orb configurations using the CircleCI CLI and circleci-config-sdk. Checks for deprecated keys, version constraints, and executor compatibility before publishing.

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
clawhub install circleci-orb-validator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Validator skill provides comprehensive validation of CircleCI orb packages before they are published to the CircleCI Orb Registry. It uses the official CircleCI CLI for schema validation and the circleci-config-sdk for programmatic analysis of orb structure.
The validator checks for deprecated configuration keys, ensures executor definitions are compatible with the target CircleCI server version, and validates that all referenced orb dependencies exist and meet version constraints. It performs semantic analysis beyond basic YAML validation, catching common mistakes like missing docker image tags, invalid resource class specifications, and circular command references.
Integration with the CircleCI REST API v2 allows the skill to verify that referenced contexts, environment variables, and project settings exist before deployment. It can also perform dry-run pipeline triggers to validate orb behavior in a sandboxed environment.
The skill supports inline orb definitions, external orb references, and parameterized orb configurations. It generates detailed validation reports with specific line numbers and suggested fixes for each issue found.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-validator/)
