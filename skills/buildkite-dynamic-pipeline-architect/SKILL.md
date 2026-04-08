---
title: Buildkite Dynamic Pipeline Architect
description: The Buildkite Dynamic Pipeline Architect enables intelligent, change-driven
  CI/CD pipelines on the Buildkite platform. It uses the Buildkite REST API for pipeline
  management and the dynamic pipeline upload mechanism to generate steps at runtime
  based on repository changes. The skill analyzes git diff output to determine which
  components of a monorepo have changed, then generates targeted pipeline steps only
  for affected services. It supports Buildkite-specific features including block steps
  for manual approvals, group steps for logical organization, wait steps with continue_on_failure
  semantics, and trigger steps for cross-pipeline orchestration. Agent targeting is
  handled through queue and tag-based routing, with automatic retry configuration
  based on historical flakiness data fetched via the Buildkite GraphQL API. The architect
  generates pipeline YAML with proper artifact passing between steps, plugin configurations
  for Docker and docker-compose, and notification hooks for Slack and PagerDuty integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/
category:
- CI/CD Integrations
framework:
- Cursor
---

# Buildkite Dynamic Pipeline Architect

The Buildkite Dynamic Pipeline Architect enables intelligent, change-driven CI/CD pipelines on the Buildkite platform. It uses the Buildkite REST API for pipeline management and the dynamic pipeline upload mechanism to generate steps at runtime based on repository changes. The skill analyzes git diff output to determine which components of a monorepo have changed, then generates targeted pipeline steps only for affected services. It supports Buildkite-specific features including block steps for manual approvals, group steps for logical organization, wait steps with continue_on_failure semantics, and trigger steps for cross-pipeline orchestration. Agent targeting is handled through queue and tag-based routing, with automatic retry configuration based on historical flakiness data fetched via the Buildkite GraphQL API. The architect generates pipeline YAML with proper artifact passing between steps, plugin configurations for Docker and docker-compose, and notification hooks for Slack and PagerDuty integration.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/)
