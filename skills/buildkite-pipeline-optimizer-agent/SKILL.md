---
name: Buildkite Pipeline Optimizer
description: Analyzes Buildkite pipeline YAML and optimizes parallelism using the
  Buildkite REST API v2 and GraphQL API. Reduces build times by identifying bottleneck
  steps and suggesting agent queue rebalancing.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/"
---
# Buildkite Pipeline Optimizer

Analyzes Buildkite pipeline YAML and optimizes parallelism using the Buildkite REST API v2 and GraphQL API. Reduces build times by identifying bottleneck steps and suggesting agent queue rebalancing.

The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline definitions and historical build data to recommend optimizations that reduce build times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing data, step dependencies, and agent queue utilization metrics.

The agent parses pipeline.yml files to build dependency graphs, identifies critical path bottlenecks, and suggests parallelism improvements. It can recommend step splitting, agent queue rebalancing, and artifact caching strategies based on actual build performance data. The optimizer also detects anti-patterns like unnecessary wait steps, serial test suites that could be parallelized, and redundant checkout operations.

Advanced features include automatic pipeline.yml generation with optimized step ordering, integration with Buildkite Test Analytics for flaky test detection, and cost-aware recommendations that balance speed against compute costs. Supports dynamic pipelines and matrix builds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-optimizer-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-optimizer-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-optimizer-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-optimizer-agent -a codex
```

### OpenClaw

```bash
clawhub install buildkite-pipeline-optimizer-agent
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/)
