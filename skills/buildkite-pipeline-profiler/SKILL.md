---
title: "Buildkite Pipeline Profiler"
description: "Profiles Buildkite pipeline performance using the Buildkite REST API and GraphQL API. Analyzes step durations, agent queue wait times, and artifact upload bottlenecks. Generates optimization reports with buildkite-agent meta-data analysis."
slug: "buildkite-pipeline-profiler"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/buildkite-pipeline-profiler/"
---

# Buildkite Pipeline Profiler

Profiles Buildkite pipeline performance using the Buildkite REST API and GraphQL API. Analyzes step durations, agent queue wait times, and artifact upload bottlenecks. Generates optimization reports with buildkite-agent meta-data analysis.

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
clawhub install buildkite-pipeline-profiler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Buildkite Pipeline Profiler skill analyzes CI/CD pipeline performance on the Buildkite platform to identify and eliminate bottlenecks. It queries the Buildkite REST API v2 (/organizations/{org}/pipelines/{pipeline}/builds) and GraphQL API for detailed build step timing data, agent assignment latency, and artifact transfer metrics.
The skill profiles individual pipeline steps by analyzing the scheduled_at, started_at, and finished_at timestamps to decompose total build time into queue wait, execution, and artifact phases. It identifies slow steps using statistical analysis across recent builds, calculating p50/p95/p99 duration percentiles per step label.
Performance optimization strategies include agent queue rebalancing based on buildkite-agent meta-data tag analysis, Docker layer caching improvements using buildkite-plugins/docker-buildkite-plugin configuration, parallel step group optimization for test splitting using buildkite-plugins/test-collector-buildkite-plugin, and artifact upload/download size reduction through compression and selective path patterns.
Advanced features include dynamic pipeline generation profiling (analyzing steps uploaded via buildkite-agent pipeline upload), triggered build chain analysis across parent-child pipelines, agent fleet utilization reporting via the Agents API, and cost estimation based on step duration and agent instance types. The skill supports webhook-driven real-time alerting for builds exceeding duration thresholds.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buildkite-pipeline-profiler/)
