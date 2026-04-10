---
name: "CircleCI Pipeline Manager"
description: "Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-pipeline-manager/"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
---

# CircleCI Pipeline Manager

The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline configuration and management through the CircleCI v2 API and .circleci/config.yml authoring. It creates pipeline configurations using CircleCI concepts including executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2), commands, and jobs with proper workflow orchestration using requires and filters. The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id}, and retrieves job artifacts. It supports advanced features including dynamic configuration with setup: true workflows and the continuation orb, workspace and cache management with persist_to_workspace and save_cache/restore_cache steps, and parallelism with circleci tests split. The manager handles context management for shared secrets, scheduled pipeline triggers via the API, and config validation using the circleci config validate command.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-manager/)
