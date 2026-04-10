---
title: "Buildkite Dynamic Pipeline Architect"
description: "Creates dynamic Buildkite pipelines using the Buildkite REST API and pipeline upload mechanism. Implements conditional step generation based on file change detection via git diff."
slug: "buildkite-dynamic-pipeline-architect"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/"
---

# Buildkite Dynamic Pipeline Architect

Creates dynamic Buildkite pipelines using the Buildkite REST API and pipeline upload mechanism. Implements conditional step generation based on file change detection via git diff.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install buildkite-dynamic-pipeline-architect
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Buildkite Dynamic Pipeline Architect enables intelligent, change-driven CI/CD pipelines on the Buildkite platform. It uses the Buildkite REST API for pipeline management and the dynamic pipeline upload mechanism to generate steps at runtime based on repository changes.
The skill analyzes git diff output to determine which components of a monorepo have changed, then generates targeted pipeline steps only for affected services. It supports Buildkite-specific features including block steps for manual approvals, group steps for logical organization, wait steps with continue_on_failure semantics, and trigger steps for cross-pipeline orchestration.
Agent targeting is handled through queue and tag-based routing, with automatic retry configuration based on historical flakiness data fetched via the Buildkite GraphQL API. The architect generates pipeline YAML with proper artifact passing between steps, plugin configurations for Docker and docker-compose, and notification hooks for Slack and PagerDuty integration.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/)
