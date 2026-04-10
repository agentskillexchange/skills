---
name: Buildkite Pipeline Profiler
description: Profiles Buildkite pipeline performance using the Buildkite REST API
  and GraphQL API. Analyzes step durations, agent queue wait times, and artifact upload
  bottlenecks. Generates optimization reports with buildkite-agent meta-data analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/buildkite-pipeline-profiler/
category:
- CI/CD Integrations
framework:
- MCP
---
# Buildkite Pipeline Profiler

The Buildkite Pipeline Profiler skill analyzes CI/CD pipeline performance on the Buildkite platform to identify and eliminate bottlenecks. It queries the Buildkite REST API v2 (/organizations/{org}/pipelines/{pipeline}/builds) and GraphQL API for detailed build step timing data, agent assignment latency, and artifact transfer metrics.
The skill profiles individual pipeline steps by analyzing the scheduled_at, started_at, and finished_at timestamps to decompose total build time into queue wait, execution, and artifact phases. It identifies slow steps using statistical analysis across recent builds, calculating p50/p95/p99 duration percentiles per step label.
Performance optimization strategies include agent queue rebalancing based on buildkite-agent meta-data tag analysis, Docker layer caching improvements using buildkite-plugins/docker-buildkite-plugin configuration, parallel step group optimization for test splitting using buildkite-plugins/test-collector-buildkite-plugin, and artifact upload/download size reduction through compression and selective path patterns.
Advanced features include dynamic pipeline generation profiling (analyzing steps uploaded via buildkite-agent pipeline upload), triggered build chain analysis across parent-child pipelines, agent fleet utilization reporting via the Agents API, and cost estimation based on step duration and agent instance types. The skill supports webhook-driven real-time alerting for builds exceeding duration thresholds.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-profiler/)
