---
title: CircleCI Orb Debugger
description: The CircleCI Orb Debugger skill provides comprehensive diagnostics for
  CircleCI orb authoring and consumption issues. It connects to the CircleCI v2 API
  to fetch orb source definitions, inspect published versions, and validate configuration
  files against the orb schema specification. When a pipeline fails due to orb configuration
  errors, this skill parses the error output and maps it back to specific YAML nodes
  in the config.yml. It understands orb parameter types (string, boolean, enum, executor,
  steps) and validates that invocations match declared parameter schemas including
  default value resolution. The skill integrates with the circleci CLI config validate
  command to perform local validation before pushing changes. It can also diff orb
  versions to identify breaking changes when upgrading orb dependencies, checking
  for removed commands, renamed parameters, or changed executor definitions. Advanced
  features include orb dependency resolution for nested orb references, detection
  of circular orb imports, and validation of conditional step logic using when/unless
  clauses with pipeline parameter expressions. It supports both inline and external
  orb development workflows.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-debugger/
category:
- CI/CD Integrations
framework:
- Claude Agents
---

# CircleCI Orb Debugger

The CircleCI Orb Debugger skill provides comprehensive diagnostics for CircleCI orb authoring and consumption issues. It connects to the CircleCI v2 API to fetch orb source definitions, inspect published versions, and validate configuration files against the orb schema specification. When a pipeline fails due to orb configuration errors, this skill parses the error output and maps it back to specific YAML nodes in the config.yml. It understands orb parameter types (string, boolean, enum, executor, steps) and validates that invocations match declared parameter schemas including default value resolution. The skill integrates with the circleci CLI config validate command to perform local validation before pushing changes. It can also diff orb versions to identify breaking changes when upgrading orb dependencies, checking for removed commands, renamed parameters, or changed executor definitions. Advanced features include orb dependency resolution for nested orb references, detection of circular orb imports, and validation of conditional step logic using when/unless clauses with pipeline parameter expressions. It supports both inline and external orb development workflows.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-debugger/)
