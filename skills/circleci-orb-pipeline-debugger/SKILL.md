---
title: CircleCI Orb Pipeline Debugger
description: The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed
  CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a
  pipeline fails, the skill fetches the workflow graph, identifies the failed job
  step, and pulls detailed executor logs. It parses orb definitions from the project
  config.yml, validates orb version pins against the CircleCI orb registry, and checks
  for deprecated parameters or removed commands. The skill can detect common issues
  like Docker image pull failures, resource class mismatches, cache key collisions,
  and parallelism configuration errors. It generates actionable fix suggestions with
  corrected YAML snippets and supports bulk analysis across multiple branches. Integrates
  with Slack webhooks to post diagnostic summaries to team channels. Compatible with
  CircleCI server and cloud environments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/
category:
- CI/CD Integrations
framework:
- Claude Code
---

# CircleCI Orb Pipeline Debugger

The CircleCI Orb Pipeline Debugger skill automates diagnosis of failed CircleCI pipelines by interfacing directly with the CircleCI v2 REST API. When a pipeline fails, the skill fetches the workflow graph, identifies the failed job step, and pulls detailed executor logs. It parses orb definitions from the project config.yml, validates orb version pins against the CircleCI orb registry, and checks for deprecated parameters or removed commands. The skill can detect common issues like Docker image pull failures, resource class mismatches, cache key collisions, and parallelism configuration errors. It generates actionable fix suggestions with corrected YAML snippets and supports bulk analysis across multiple branches. Integrates with Slack webhooks to post diagnostic summaries to team channels. Compatible with CircleCI server and cloud environments.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-debugger/)
