---
name: "CircleCI Orb Debugger"
description: "Diagnoses and fixes CircleCI orb configuration errors using the CircleCI v2 API and circleci config validate CLI. Parses orb source YAML against the orb development kit schema for type mismatches and parameter validation failures."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
tool_ecosystem:
  tool: circleci
  github_repo: circleci/circleci-docs
  github_stars: 841
  maintained: true
---
# CircleCI Orb Debugger

Diagnoses and fixes CircleCI orb configuration errors using the CircleCI v2 API and circleci config validate CLI. Parses orb source YAML against the orb development kit schema for type mismatches and parameter validation failures.

## Overview

The CircleCI Orb Debugger skill provides comprehensive diagnostics for CircleCI orb authoring and consumption issues. It connects to the CircleCI v2 API to fetch orb source definitions, inspect published versions, and validate configuration files against the orb schema specification.

When a pipeline fails due to orb configuration errors, this skill parses the error output and maps it back to specific YAML nodes in the config.yml. It understands orb parameter types (string, boolean, enum, executor, steps) and validates that invocations match declared parameter schemas including default value resolution.

The skill integrates with the circleci CLI config validate command to perform local validation before pushing changes. It can also diff orb versions to identify breaking changes when upgrading orb dependencies, checking for removed commands, renamed parameters, or changed executor definitions.

Advanced features include orb dependency resolution for nested orb references, detection of circular orb imports, and validation of conditional step logic using when/unless clauses with pipeline parameter expressions. It supports both inline and external orb development workflows.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-debugger
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-debugger -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-debugger -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-debugger -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-debugger
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-debugger/)
