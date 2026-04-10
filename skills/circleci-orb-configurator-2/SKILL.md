---
title: "CircleCI Orb Configurator"
description: "Builds and validates CircleCI orb configurations using the CircleCI CLI and Orb Development Kit. Supports orb packing, linting with yamllint, and publishing to the CircleCI Orb Registry via circleci orb publish."
slug: "circleci-orb-configurator-2"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-configurator-2/"
listed: true
---

# CircleCI Orb Configurator

Builds and validates CircleCI orb configurations using the CircleCI CLI and Orb Development Kit. Supports orb packing, linting with yamllint, and publishing to the CircleCI Orb Registry via circleci orb publish.

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
clawhub install circleci-orb-configurator-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Configurator skill streamlines the creation and maintenance of reusable CircleCI orbs for CI/CD pipelines. It uses the CircleCI CLI (circleci orb validate, circleci orb pack) to validate orb source files and pack them into single-file orbs ready for publishing.
The skill manages the full orb development lifecycle: scaffolding new orbs with circleci orb init, defining commands/jobs/executors using YAML templating, running integration tests with circleci local execute, and publishing via circleci orb publish. It integrates with the CircleCI v2 API for orb version management and namespace administration.
Configuration generation leverages the Orb Development Kit patterns including parameterized commands with type validation (string, boolean, integer, enum, executor, steps), executor definitions for Docker/machine/macOS environments, and job templates with proper workspace/cache handling. The skill validates all configurations against CircleCI schema definitions.
Advanced features include orb dependency resolution for private orbs, inline orb expansion for debugging, and automated semantic versioning based on conventional commits using the circleci orb publish promote workflow.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-configurator-2/)
