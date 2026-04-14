---
title: "CircleCI Pipeline Manager"
description: "Configure and trigger CircleCI pipelines using the CircleCI v2 API and config.yml orbs. Manages pipeline parameters, workspace persistence, and dynamic configuration with setup workflows."
verification: security_reviewed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-manager/)
