---
title: "CircleCI Pipeline Manager"
description: "Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows."
slug: "circleci-pipeline-manager"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/circleci-pipeline-manager/"
listed: true
---

# CircleCI Pipeline Manager

Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows.

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
clawhub install circleci-pipeline-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline configuration and management through the CircleCI v2 API and .circleci/config.yml authoring. It creates pipeline configurations using CircleCI concepts including executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2), commands, and jobs with proper workflow orchestration using requires and filters. The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id}, and retrieves job artifacts. It supports advanced features including dynamic configuration with setup: true workflows and the continuation orb, workspace and cache management with persist_to_workspace and save_cache/restore_cache steps, and parallelism with circleci tests split. The manager handles context management for shared secrets, scheduled pipeline triggers via the API, and config validation using the circleci config validate command.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-manager/)
