---
title: "CircleCI Pipeline Manager"
description: "Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows."
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

# CircleCI Pipeline Manager

The CircleCI Pipeline Manager skill handles end-to-end CI/CD pipeline configuration and management through the CircleCI v2 API and .circleci/config.yml authoring. It creates pipeline configurations using CircleCI concepts including executors (docker, machine, macos), orbs (circleci/node@5, circleci/aws-cli@4, circleci/docker@2), commands, and jobs with proper workflow orchestration using requires and filters. The skill triggers pipelines via POST /api/v2/project/{project-slug}/pipeline with pipeline parameters, monitors workflow status through GET /api/v2/workflow/{id}, and retrieves job artifacts. It supports advanced features including dynamic configuration with setup: true workflows and the continuation orb, workspace and cache management with persist_to_workspace and save_cache/restore_cache steps, and parallelism with circleci tests split. The manager handles context management for shared secrets, scheduled pipeline triggers via the API, and config validation using the circleci config validate command.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-manager/)
