---
title: "Argo Workflows DAG Optimizer"
description: "Analyzes Argo Workflows DAG templates to identify parallelization opportunities. Uses the Argo Server API to fetch workflow execution history and critical path analysis."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-workflows"
category:
  - "Templates & Workflows"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "argoproj/argo-workflows"
  github_stars: 16616
---

# Argo Workflows DAG Optimizer

The Argo Workflows DAG Optimizer connects to the Argo Server REST API to analyze workflow execution patterns and identify optimization opportunities. It fetches completed workflow runs and performs critical path analysis on DAG task dependencies, highlighting sequential bottlenecks that could be parallelized. The skill parses workflow templates written in YAML, understanding DAG task dependencies, artifact passing between steps, and resource template references. It suggests dependency graph restructuring to maximize parallelism while respecting data dependencies. Resource optimization analyzes container resource requests vs actual usage from workflow metrics, recommending right-sized CPU and memory allocations. The skill handles workflow-of-workflows patterns, cluster workflow templates, and parameterized workflow submissions. It generates optimized workflow YAML with added retry strategies, timeout configurations, and memoization cache keys for expensive steps that produce deterministic outputs.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argo-workflows-dag-optimizer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argo-workflows-dag-optimizer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/)
