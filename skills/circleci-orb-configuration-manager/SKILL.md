---
title: "CircleCI Orb Configuration Manager"
description: "Manages CircleCI pipeline configurations using orbs like circleci/node, circleci/docker, and circleci/aws-s3. Handles workflow orchestration, parallelism, and resource class selection via .circleci/config.yml."
slug: "circleci-orb-configuration-manager"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-orb-configuration-manager/"
---

# CircleCI Orb Configuration Manager

Manages CircleCI pipeline configurations using orbs like circleci/node, circleci/docker, and circleci/aws-s3. Handles workflow orchestration, parallelism, and resource class selection via .circleci/config.yml.

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
clawhub install circleci-orb-configuration-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Orb Configuration Manager skill generates and maintains .circleci/config.yml files using the CircleCI 2.1 configuration specification. It integrates certified orbs including circleci/node@5, circleci/docker@2, circleci/aws-s3@4, circleci/slack@4, and circleci/browser-tools@1 to streamline pipeline setup.
The skill configures job executors (Docker, machine, macOS, Windows), sets resource classes (small, medium, large, xlarge, 2xlarge) for cost optimization, and manages workspace persistence using persist_to_workspace and attach_workspace steps. It supports test splitting with circleci tests split –split-by=timings for parallel execution across containers.
Advanced features include pipeline parameter definition using the parameters key, conditional workflow execution with when/unless clauses, scheduled workflow triggers via cron expressions, and dynamic configuration using the continuation orb (circleci/continuation@1). The manager also handles SSH key management for deployment, Docker layer caching (DLC) configuration, and custom orb development using the circleci CLI (circleci orb init, circleci orb publish).

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-configuration-manager/)
