---
title: CircleCI Pipeline Manager
description: 'The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline
  configuration and management through the CircleCI v2 API and .circleci/config.yml
  authoring. It creates pipeline configurations using CircleCI concepts including
  executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2),
  commands, and jobs with proper workflow orchestration using requires and filters.
  The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with
  pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id},
  and retrieves job artifacts. It supports advanced features including dynamic configuration
  with setup: true workflows and the continuation orb, workspace and cache management
  with persist_to_workspace and save_cache/restore_cache steps, and parallelism with
  circleci tests split. The manager handles context management for shared secrets,
  scheduled pipeline triggers via the API, and config validation using the circleci
  config validate command.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-pipeline-manager/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---

# CircleCI Pipeline Manager

The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline configuration and management through the CircleCI v2 API and .circleci/config.yml authoring. It creates pipeline configurations using CircleCI concepts including executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2), commands, and jobs with proper workflow orchestration using requires and filters. The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id}, and retrieves job artifacts. It supports advanced features including dynamic configuration with setup: true workflows and the continuation orb, workspace and cache management with persist_to_workspace and save_cache/restore_cache steps, and parallelism with circleci tests split. The manager handles context management for shared secrets, scheduled pipeline triggers via the API, and config validation using the circleci config validate command.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-manager/)
