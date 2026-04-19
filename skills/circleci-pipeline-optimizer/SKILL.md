---
title: "CircleCI Pipeline Optimizer"
description: "The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow to map workflow structures, then fetches job details via /workflow/{id}/job to extract timing breakdowns for each step. The agent identifies bottlenecks by comparing step durations across recent runs and flagging jobs that consistently exceed expected execution times. It analyzes Docker image pull times and recommends Docker Layer Caching (DLC) for custom images, calculates optimal parallelism values based on test splitting data from circleci tests split, and suggests resource class upgrades where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml configurations with proper orb references, workspace persistence for artifact sharing between jobs, and conditional workflow execution using pipeline parameters and when/unless clauses. It also evaluates cache hit rates and recommends key rotation strategies."
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

# CircleCI Pipeline Optimizer

The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow to map workflow structures, then fetches job details via /workflow/{id}/job to extract timing breakdowns for each step. The agent identifies bottlenecks by comparing step durations across recent runs and flagging jobs that consistently exceed expected execution times. It analyzes Docker image pull times and recommends Docker Layer Caching (DLC) for custom images, calculates optimal parallelism values based on test splitting data from circleci tests split, and suggests resource class upgrades where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml configurations with proper orb references, workspace persistence for artifact sharing between jobs, and conditional workflow execution using pipeline parameters and when/unless clauses. It also evaluates cache hit rates and recommends key rotation strategies.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-optimizer/)
