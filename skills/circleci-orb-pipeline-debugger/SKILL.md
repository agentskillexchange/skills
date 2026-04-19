---
title: "CircleCI Orb Pipeline Debugger"
description: "The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments."
source: "https://github.com/circleci/circleci-docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Orb Pipeline Debugger

The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/)
