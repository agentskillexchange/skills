---
title: "CircleCI Workflow Analyzer"
description: "Analyzes and optimizes CircleCI workflows using the CircleCI v2 API. Identifies bottlenecks in job dependency graphs, suggests parallelism improvements, and monitors pipeline credit usage."
verification: security_reviewed
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Workflow Analyzer

The CircleCI Workflow Analyzer skill connects to the CircleCI v2 REST API to provide deep insights into your continuous integration pipelines. It fetches workflow run data, job timing metrics, and resource utilization to identify performance bottlenecks and optimization opportunities.

The skill builds a dependency graph of your workflow jobs and analyzes critical path timings to recommend where parallelism can be increased. It evaluates resource class allocations against actual CPU and memory usage reported by the CircleCI Insights API, suggesting right-sizing for cost optimization. Credit consumption tracking helps teams stay within budget by projecting monthly usage based on historical trends.

Configuration validation is handled through the CircleCI Config SDK, checking .circleci/config.yml files against the latest orb versions and deprecated syntax. The skill can automatically generate optimized workflow configurations with proper caching strategies using CircleCI cache keys, Docker layer caching directives, and workspace persistence between jobs. It outputs reports compatible with Datadog CI Visibility and Grafana dashboards for ongoing monitoring.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/circleci-workflow-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/circleci-workflow-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-workflow-analyzer/)
