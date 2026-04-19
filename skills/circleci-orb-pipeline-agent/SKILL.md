---
title: "CircleCI Orb Pipeline Agent"
description: "The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation. The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection. Test splitting is optimized via circleci tests split &#8211;split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API. Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection."
source: "https://github.com/circleci/circleci-docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Agent

The CircleCI Orb Pipeline Agent creates and optimizes CircleCI pipelines using config.yml v2.1 syntax, the CircleCI API v2 (circleci.com/api/v2/project, /pipeline, /workflow), and reusable Orbs from the CircleCI Orb Registry. It generates efficient pipeline configurations with proper resource allocation. The agent leverages CircleCI Orbs for common tasks including circleci/node, circleci/python, circleci/docker, circleci/aws-cli, and circleci/kubernetes. It configures orb commands, jobs, and executors with version pinning and vulnerability scanning through orb source inspection. Test splitting is optimized via circleci tests split &#8211;split-by=timings with historical timing data to balance parallel containers. The agent configures resource_class selection (small, medium, large, xlarge) based on job requirements and cost analysis via the API. Dynamic configuration through setup workflows enables monorepo path filtering, conditional job execution, and generated config patterns. The agent manages pipeline parameters, contexts for secret management, and scheduled pipeline triggers. Performance optimization includes Docker layer caching, workspace persistence across jobs, and test result aggregation for flaky test detection.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-agent/)
