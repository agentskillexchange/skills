---
title: "CircleCI Orb Validator"
description: "Validates and lints CircleCI orb configurations using the CircleCI CLI and circleci-config-sdk. Checks for deprecated keys, version constraints, and executor compatibility before publishing."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Validator

The CircleCI Orb Validator skill provides comprehensive validation of CircleCI orb packages before they are published to the CircleCI Orb Registry. It uses the official CircleCI CLI for schema validation and the circleci-config-sdk for programmatic analysis of orb structure.

The validator checks for deprecated configuration keys, ensures executor definitions are compatible with the target CircleCI server version, and validates that all referenced orb dependencies exist and meet version constraints. It performs semantic analysis beyond basic YAML validation, catching common mistakes like missing docker image tags, invalid resource class specifications, and circular command references.

Integration with the CircleCI REST API v2 allows the skill to verify that referenced contexts, environment variables, and project settings exist before deployment. It can also perform dry-run pipeline triggers to validate orb behavior in a sandboxed environment.

The skill supports inline orb definitions, external orb references, and parameterized orb configurations. It generates detailed validation reports with specific line numbers and suggested fixes for each issue found.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-validator/)
