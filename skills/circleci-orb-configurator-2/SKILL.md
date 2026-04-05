---
name: "CircleCI Orb Configurator"
description: "Builds and validates CircleCI orb configurations using the CircleCI CLI and Orb Development Kit. Supports orb packing, linting with yamllint, and publishing to the CircleCI Orb Registry via circleci orb publish."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-configurator-2/"
---
# CircleCI Orb Configurator

Builds and validates CircleCI orb configurations using the CircleCI CLI and Orb Development Kit. Supports orb packing, linting with yamllint, and publishing to the CircleCI Orb Registry via circleci orb publish.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configurator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configurator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configurator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-configurator-2 -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-configurator-2
```

## Details

The CircleCI Orb Configurator skill streamlines the creation and maintenance of reusable CircleCI orbs for CI/CD pipelines. It uses the CircleCI CLI (circleci orb validate, circleci orb pack) to validate orb source files and pack them into single-file orbs ready for publishing.

The skill manages the full orb development lifecycle: scaffolding new orbs with circleci orb init, defining commands/jobs/executors using YAML templating, running integration tests with circleci local execute, and publishing via circleci orb publish. It integrates with the CircleCI v2 API for orb version management and namespace administration.

Configuration generation leverages the Orb Development Kit patterns including parameterized commands with type validation (string, boolean, integer, enum, executor, steps), executor definitions for Docker/machine/macOS environments, and job templates with proper workspace/cache handling. The skill validates all configurations against CircleCI schema definitions.

Advanced features include orb dependency resolution for private orbs, inline orb expansion for debugging, and automated semantic versioning based on conventional commits using the circleci orb publish promote workflow.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-configurator-2/)
