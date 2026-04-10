---
title: "CircleCI Orb Composer"
description: "Composes and validates CircleCI Orbs using the circleci/circleci-cli and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with conventional-changelog, and publishing to the CircleCI Orb Registry."
slug: "circleci-orb-composer-7"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-composer-7/"
---

# CircleCI Orb Composer

Composes and validates CircleCI Orbs using the circleci/circleci-cli and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with conventional-changelog, and publishing to the CircleCI Orb Registry.

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
clawhub install circleci-orb-composer-7
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Composer skill streamlines the creation, validation, and publishing of CircleCI Orbs — reusable configuration packages for CircleCI pipelines. It uses the circleci/circleci-cli to validate orb source YAML and the circleci/orb-tools-orb to automate the full orb development lifecycle.
The skill handles orb structure scaffolding with proper src/ directory layouts for commands, jobs, executors, and examples. It integrates conventional-changelog for automatic semantic versioning based on commit messages, ensuring orb versions follow semver conventions.
Capabilities include generating parameterized commands with proper type validation, creating executor definitions for Docker/machine/macOS environments, building job templates with configurable steps, and producing comprehensive usage examples. The skill validates orbs against the CircleCI schema, runs integration tests using circleci local execute, and publishes to the CircleCI Orb Registry with proper namespace management. It also supports generating orb documentation using orb-tools/pack and orb-tools/review commands.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composer-7/)
