---
name: "Buildkite Dynamic Pipeline Architect"
description: "Creates dynamic Buildkite pipelines using the Buildkite REST API and pipeline upload mechanism. Implements conditional step generation based on file change detection via git diff."
category: "CI/CD Integrations"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/"
tool_ecosystem:
  tool: docker
  github_stars: 71560
  github_repo: moby/moby
  license: Apache-2.0
  maintained: true
---

# Buildkite Dynamic Pipeline Architect

Creates dynamic Buildkite pipelines using the Buildkite REST API and pipeline upload mechanism. Implements conditional step generation based on file change detection via git diff.

## Overview

The Buildkite Dynamic Pipeline Architect enables intelligent, change-driven CI/CD pipelines on the Buildkite platform. It uses the Buildkite REST API for pipeline management and the dynamic pipeline upload mechanism to generate steps at runtime based on repository changes.

The skill analyzes git diff output to determine which components of a monorepo have changed, then generates targeted pipeline steps only for affected services. It supports Buildkite-specific features including block steps for manual approvals, group steps for logical organization, wait steps with continue_on_failure semantics, and trigger steps for cross-pipeline orchestration.

Agent targeting is handled through queue and tag-based routing, with automatic retry configuration based on historical flakiness data fetched via the Buildkite GraphQL API. The architect generates pipeline YAML with proper artifact passing between steps, plugin configurations for Docker and docker-compose, and notification hooks for Slack and PagerDuty integration.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-architect
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-architect -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-architect -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-dynamic-pipeline-architect -a codex
```

### OpenClaw

```bash
clawhub install buildkite-dynamic-pipeline-architect
```

## Source

- Marketplace: https://agentskillexchange.com/skills/buildkite-dynamic-pipeline-architect/
