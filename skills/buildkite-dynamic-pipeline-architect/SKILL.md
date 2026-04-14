---
title: "Buildkite Dynamic Pipeline Architect"
description: "Creates dynamic Buildkite pipelines using the Buildkite REST API and pipeline upload mechanism. Implements conditional step generation based on file change detection via git diff."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Buildkite Dynamic Pipeline Architect

The Buildkite Dynamic Pipeline Architect enables intelligent, change-driven CI/CD pipelines on the Buildkite platform. It uses the Buildkite REST API for pipeline management and the dynamic pipeline upload mechanism to generate steps at runtime based on repository changes.

The skill analyzes git diff output to determine which components of a monorepo have changed, then generates targeted pipeline steps only for affected services. It supports Buildkite-specific features including block steps for manual approvals, group steps for logical organization, wait steps with continue_on_failure semantics, and trigger steps for cross-pipeline orchestration.

Agent targeting is handled through queue and tag-based routing, with automatic retry configuration based on historical flakiness data fetched via the Buildkite GraphQL API. The architect generates pipeline YAML with proper artifact passing between steps, plugin configurations for Docker and docker-compose, and notification hooks for Slack and PagerDuty integration.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/)
