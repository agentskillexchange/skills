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

The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline definitions and historical build data to recommend optimizations that reduce build times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing data, step dependencies, and agent queue utilization metrics.

The agent parses pipeline.yml files to build dependency graphs, identifies critical path bottlenecks, and suggests parallelism improvements. It can recommend step splitting, agent queue rebalancing, and artifact caching strategies based on actual build performance data. The optimizer also detects anti-patterns like unnecessary wait steps, serial test suites that could be parallelized, and redundant checkout operations.

Advanced features include automatic pipeline.yml generation with optimized step ordering, integration with Buildkite Test Analytics for flaky test detection, and cost-aware recommendations that balance speed against compute costs. Supports dynamic pipelines and matrix builds.

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
