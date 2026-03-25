---
name: "CircleCI Workflow Analyzer"
description: "Analyzes and optimizes CircleCI workflows using the CircleCI v2 API. Identifies bottlenecks in job dependency graphs, suggests parallelism improvements, and monitors pipeline credit usage."
category: "CI/CD Integrations"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-workflow-analyzer/"
tool_ecosystem:
  tool: "circleci"
  github_stars: 842
  github_repo: "circleci/circleci-docs"
  maintained: true
---

# CircleCI Workflow Analyzer

Analyzes and optimizes CircleCI workflows using the CircleCI v2 API. Identifies bottlenecks in job dependency graphs, suggests parallelism improvements, and monitors pipeline credit usage.

## Overview

The CircleCI Workflow Analyzer skill connects to the CircleCI v2 REST API to provide deep insights into your continuous integration pipelines. It fetches workflow run data, job timing metrics, and resource utilization to identify performance bottlenecks and optimization opportunities.

The skill builds a dependency graph of your workflow jobs and analyzes critical path timings to recommend where parallelism can be increased. It evaluates resource class allocations against actual CPU and memory usage reported by the CircleCI Insights API, suggesting right-sizing for cost optimization. Credit consumption tracking helps teams stay within budget by projecting monthly usage based on historical trends.

Configuration validation is handled through the CircleCI Config SDK, checking .circleci/config.yml files against the latest orb versions and deprecated syntax. The skill can automatically generate optimized workflow configurations with proper caching strategies using CircleCI cache keys, Docker layer caching directives, and workspace persistence between jobs. It outputs reports compatible with Datadog CI Visibility and Grafana dashboards for ongoing monitoring.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-workflow-analyzer -a codex
```

### OpenClaw

```bash
clawhub install circleci-workflow-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/circleci-workflow-analyzer/
