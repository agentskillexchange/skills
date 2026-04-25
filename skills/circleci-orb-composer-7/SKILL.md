---
title: "CircleCI Orb Composer"
description: "Composes and validates CircleCI Orbs using the circleci/circleci-cli and circleci/orb-tools-orb SDK. Automates orb packaging, semantic versioning with conventional-changelog, and publishing to the CircleCI Orb Registry."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Composer

The CircleCI Orb Composer skill streamlines the creation, validation, and publishing of CircleCI Orbs — reusable configuration packages for CircleCI pipelines. It uses the circleci/circleci-cli to validate orb source YAML and the circleci/orb-tools-orb to automate the full orb development lifecycle. The skill handles orb structure scaffolding with proper src/ directory layouts for commands, jobs, executors, and examples. It integrates conventional-changelog for automatic semantic versioning based on commit messages, ensuring orb versions follow semver conventions. Capabilities include generating parameterized commands with proper type validation, creating executor definitions for Docker/machine/macOS environments, building job templates with configurable steps, and producing comprehensive usage examples. The skill validates orbs against the CircleCI schema, runs integration tests using circleci local execute, and publishes to the CircleCI Orb Registry with proper namespace management. It also supports generating orb documentation using orb-tools/pack and orb-tools/review commands.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/circleci-orb-composer-7/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-composer-7
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/circleci-orb-composer-7`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-composer-7/)
