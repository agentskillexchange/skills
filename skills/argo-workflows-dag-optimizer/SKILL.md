---
name: "Argo Workflows DAG Optimizer"
description: "Analyzes Argo Workflows DAG templates to identify parallelization opportunities. Uses the Argo Server API to fetch workflow execution history and critical path analysis."
category: "Templates & Workflows"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/"
---
# Argo Workflows DAG Optimizer

Analyzes Argo Workflows DAG templates to identify parallelization opportunities. Uses the Argo Server API to fetch workflow execution history and critical path analysis.

## Overview

The Argo Workflows DAG Optimizer connects to the Argo Server REST API to analyze workflow execution patterns and identify optimization opportunities. It fetches completed workflow runs and performs critical path analysis on DAG task dependencies, highlighting sequential bottlenecks that could be parallelized. The skill parses workflow templates written in YAML, understanding DAG task dependencies, artifact passing between steps, and resource template references. It suggests dependency graph restructuring to maximize parallelism while respecting data dependencies. Resource optimization analyzes container resource requests vs actual usage from workflow metrics, recommending right-sized CPU and memory allocations. The skill handles workflow-of-workflows patterns, cluster workflow templates, and parameterized workflow submissions. It generates optimized workflow YAML with added retry strategies, timeout configurations, and memoization cache keys for expensive steps that produce deterministic outputs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-optimizer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-optimizer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-optimizer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill argo-workflows-dag-optimizer -a codex
```

### OpenClaw

```bash
clawhub install argo-workflows-dag-optimizer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/)
