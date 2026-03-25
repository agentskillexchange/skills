---
name: "Buildkite Pipeline Profiler"
description: "Profiles Buildkite pipeline performance using the Buildkite REST API and GraphQL API. Analyzes step durations, agent queue wait times, and artifact upload bottlenecks. Generates optimization reports with buildkite-agent meta-data analysis."
category: "CI/CD Integrations"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/buildkite-pipeline-profiler/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "docker"  # from ase_tool_match
  github_stars: 71560  # from ase_github_stars (integer, not string)
  github_repo: "moby/moby"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Buildkite Pipeline Profiler

Profiles Buildkite pipeline performance using the Buildkite REST API and GraphQL API. Analyzes step durations, agent queue wait times, and artifact upload bottlenecks. Generates optimization reports with buildkite-agent meta-data analysis.

## Overview

The Buildkite Pipeline Profiler skill analyzes CI/CD pipeline performance on the Buildkite platform to identify and eliminate bottlenecks. It queries the Buildkite REST API v2 (/organizations/{org}/pipelines/{pipeline}/builds) and GraphQL API for detailed build step timing data, agent assignment latency, and artifact transfer metrics.

The skill profiles individual pipeline steps by analyzing the scheduled_at, started_at, and finished_at timestamps to decompose total build time into queue wait, execution, and artifact phases. It identifies slow steps using statistical analysis across recent builds, calculating p50/p95/p99 duration percentiles per step label.

Performance optimization strategies include agent queue rebalancing based on buildkite-agent meta-data tag analysis, Docker layer caching improvements using buildkite-plugins/docker-buildkite-plugin configuration, parallel step group optimization for test splitting using buildkite-plugins/test-collector-buildkite-plugin, and artifact upload/download size reduction through compression and selective path patterns.

Advanced features include dynamic pipeline generation profiling (analyzing steps uploaded via buildkite-agent pipeline upload), triggered build chain analysis across parent-child pipelines, agent fleet utilization reporting via the Agents API, and cost estimation based on step duration and agent instance types. The skill supports webhook-driven real-time alerting for builds exceeding duration thresholds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-profiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-profiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-profiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buildkite-pipeline-profiler -a codex
```

### OpenClaw

```bash
clawhub install buildkite-pipeline-profiler
```

## Source

- Marketplace: https://agentskillexchange.com/skills/buildkite-pipeline-profiler/
