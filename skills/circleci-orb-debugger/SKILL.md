---
title: "CircleCI Orb Debugger"
description: "Diagnoses and fixes CircleCI orb configuration errors using the CircleCI v2 API and circleci config validate CLI. Parses orb source YAML against the orb development kit schema for type mismatches and parameter validation failures."
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

# CircleCI Orb Debugger

The CircleCI Orb Debugger skill provides comprehensive diagnostics for CircleCI orb authoring and consumption issues. It connects to the CircleCI v2 API to fetch orb source definitions, inspect published versions, and validate configuration files against the orb schema specification.

When a pipeline fails due to orb configuration errors, this skill parses the error output and maps it back to specific YAML nodes in the config.yml. It understands orb parameter types (string, boolean, enum, executor, steps) and validates that invocations match declared parameter schemas including default value resolution.

The skill integrates with the circleci CLI config validate command to perform local validation before pushing changes. It can also diff orb versions to identify breaking changes when upgrading orb dependencies, checking for removed commands, renamed parameters, or changed executor definitions.

Advanced features include orb dependency resolution for nested orb references, detection of circular orb imports, and validation of conditional step logic using when/unless clauses with pipeline parameter expressions. It supports both inline and external orb development workflows.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-debugger/)
