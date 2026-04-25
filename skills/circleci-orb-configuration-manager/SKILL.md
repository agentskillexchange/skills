---
title: "CircleCI Orb Configuration Manager"
description: "Manages CircleCI pipeline configurations using orbs like circleci/node, circleci/docker, and circleci/aws-s3. Handles workflow orchestration, parallelism, and resource class selection via .circleci/config.yml."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Configuration Manager

The CircleCI Orb Configuration Manager skill generates and maintains .circleci/config.yml files using the CircleCI 2.1 configuration specification. It integrates certified orbs including circleci/node@5, circleci/docker@2, circleci/aws-s3@4, circleci/slack@4, and circleci/browser-tools@1 to streamline pipeline setup. The skill configures job executors (Docker, machine, macOS, Windows), sets resource classes (small, medium, large, xlarge, 2xlarge) for cost optimization, and manages workspace persistence using persist_to_workspace and attach_workspace steps. It supports test splitting with circleci tests split –split-by=timings for parallel execution across containers. Advanced features include pipeline parameter definition using the parameters key, conditional workflow execution with when/unless clauses, scheduled workflow triggers via cron expressions, and dynamic configuration using the continuation orb (circleci/continuation@1). The manager also handles SSH key management for deployment, Docker layer caching (DLC) configuration, and custom orb development using the circleci CLI (circleci orb init, circleci orb publish).

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/circleci-orb-configuration-manager/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-orb-configuration-manager
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/circleci-orb-configuration-manager`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-configuration-manager/)
