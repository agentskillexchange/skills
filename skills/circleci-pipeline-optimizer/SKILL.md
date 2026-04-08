---
title: CircleCI Pipeline Optimizer
description: The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze
  pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow
  to map workflow structures, then fetches job details via /workflow/{id}/job to extract
  timing breakdowns for each step. The agent identifies bottlenecks by comparing step
  durations across recent runs and flagging jobs that consistently exceed expected
  execution times. It analyzes Docker image pull times and recommends Docker Layer
  Caching (DLC) for custom images, calculates optimal parallelism values based on
  test splitting data from circleci tests split, and suggests resource class upgrades
  where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml
  configurations with proper orb references, workspace persistence for artifact sharing
  between jobs, and conditional workflow execution using pipeline parameters and when/unless
  clauses. It also evaluates cache hit rates and recommends key rotation strategies.
verification: security_reviewed
source: https://agentskillexchange.com/skills/circleci-pipeline-optimizer/
category:
- CI/CD Integrations
framework:
- ChatGPT Agents
---

# CircleCI Pipeline Optimizer

The CircleCI Pipeline Optimizer connects to the CircleCI API v2 to analyze pipeline performance and identify optimization opportunities. It queries /pipeline/{pipeline-id}/workflow to map workflow structures, then fetches job details via /workflow/{id}/job to extract timing breakdowns for each step. The agent identifies bottlenecks by comparing step durations across recent runs and flagging jobs that consistently exceed expected execution times. It analyzes Docker image pull times and recommends Docker Layer Caching (DLC) for custom images, calculates optimal parallelism values based on test splitting data from circleci tests split, and suggests resource class upgrades where CPU/memory constraints cause slowdowns. The optimizer generates updated .circleci/config.yml configurations with proper orb references, workspace persistence for artifact sharing between jobs, and conditional workflow execution using pipeline parameters and when/unless clauses. It also evaluates cache hit rates and recommends key rotation strategies.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-pipeline-optimizer/)
