---
title: Buildkite Pipeline Optimizer
description: The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline
  definitions and historical build data to recommend optimizations that reduce build
  times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing
  data, step dependencies, and agent queue utilization metrics. The agent parses pipeline.yml
  files to build dependency graphs, identifies critical path bottlenecks, and suggests
  parallelism improvements. It can recommend step splitting, agent queue rebalancing,
  and artifact caching strategies based on actual build performance data. The optimizer
  also detects anti-patterns like unnecessary wait steps, serial test suites that
  could be parallelized, and redundant checkout operations. Advanced features include
  automatic pipeline.yml generation with optimized step ordering, integration with
  Buildkite Test Analytics for flaky test detection, and cost-aware recommendations
  that balance speed against compute costs. Supports dynamic pipelines and matrix
  builds.
verification: security_reviewed
source: https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/
category:
- CI/CD Integrations
framework:
- OpenClaw
---

# Buildkite Pipeline Optimizer

The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline definitions and historical build data to recommend optimizations that reduce build times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing data, step dependencies, and agent queue utilization metrics. The agent parses pipeline.yml files to build dependency graphs, identifies critical path bottlenecks, and suggests parallelism improvements. It can recommend step splitting, agent queue rebalancing, and artifact caching strategies based on actual build performance data. The optimizer also detects anti-patterns like unnecessary wait steps, serial test suites that could be parallelized, and redundant checkout operations. Advanced features include automatic pipeline.yml generation with optimized step ordering, integration with Buildkite Test Analytics for flaky test detection, and cost-aware recommendations that balance speed against compute costs. Supports dynamic pipelines and matrix builds.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/)
