---
title: "Buildkite Pipeline Optimizer"
description: "Analyzes Buildkite pipeline YAML and optimizes parallelism using the Buildkite REST API v2 and GraphQL API. Reduces build times by identifying bottleneck steps and suggesting agent queue rebalancing."
verification: "security_reviewed"
source: "https://buildkite.com/docs"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# Buildkite Pipeline Optimizer

Analyzes Buildkite pipeline YAML and optimizes parallelism using the Buildkite REST API v2 and GraphQL API. Reduces build times by identifying bottleneck steps and suggesting agent queue rebalancing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/buildkite-pipeline-optimizer-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/buildkite-pipeline-optimizer-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/)
