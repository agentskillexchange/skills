---
title: "Buildkite Pipeline Optimizer"
description: "Analyzes Buildkite pipeline YAML and optimizes parallelism using the Buildkite REST API v2 and GraphQL API. Reduces build times by identifying bottleneck steps and suggesting agent queue rebalancing."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-optimizer-agent/)
