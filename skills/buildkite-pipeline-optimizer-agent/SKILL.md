---
title: "Buildkite Pipeline Optimizer"
description: "The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline definitions and historical build data to recommend optimizations that reduce build times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing data, step dependencies, and agent queue utilization metrics. The agent parses pipeline.yml files to build dependency graphs, identifies critical path bottlenecks, and suggests parallelism improvements. It can recommend step splitting, agent queue rebalancing, and artifact caching strategies based on actual build performance data. The optimizer also detects anti-patterns like unnecessary wait steps, serial test suites that could be parallelized, and redundant checkout operations. Advanced features include automatic pipeline.yml generation with optimized step ordering, integration with Buildkite Test Analytics for flaky test detection, and cost-aware recommendations that balance speed against compute costs. Supports dynamic pipelines and matrix builds."
source: "https://buildkite.com/docs"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
---

# Buildkite Pipeline Optimizer

The Buildkite Pipeline Optimizer agent analyzes your Buildkite pipeline definitions and historical build data to recommend optimizations that reduce build times. Using the Buildkite REST API v2 and GraphQL API, it fetches build timing data, step dependencies, and agent queue utilization metrics. The agent parses pipeline.yml files to build dependency graphs, identifies critical path bottlenecks, and suggests parallelism improvements. It can recommend step splitting, agent queue rebalancing, and artifact caching strategies based on actual build performance data. The optimizer also detects anti-patterns like unnecessary wait steps, serial test suites that could be parallelized, and redundant checkout operations. Advanced features include automatic pipeline.yml generation with optimized step ordering, integration with Buildkite Test Analytics for flaky test detection, and cost-aware recommendations that balance speed against compute costs. Supports dynamic pipelines and matrix builds.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/)
