---
name: "Argo Workflows DAG Optimizer"
description: "Analyzes Argo Workflows DAG templates to identify parallelization opportunities. Uses the Argo Server API to fetch workflow execution history and critical path analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/"
category:
  - "Templates &amp; Workflows"
framework:
  - "Custom Agents"
---

# Argo Workflows DAG Optimizer

The Argo Workflows DAG Optimizer connects to the Argo Server REST API to analyze workflow execution patterns and identify optimization opportunities. It fetches completed workflow runs and performs critical path analysis on DAG task dependencies, highlighting sequential bottlenecks that could be parallelized. The skill parses workflow templates written in YAML, understanding DAG task dependencies, artifact passing between steps, and resource template references. It suggests dependency graph restructuring to maximize parallelism while respecting data dependencies. Resource optimization analyzes container resource requests vs actual usage from workflow metrics, recommending right-sized CPU and memory allocations. The skill handles workflow-of-workflows patterns, cluster workflow templates, and parameterized workflow submissions. It generates optimized workflow YAML with added retry strategies, timeout configurations, and memoization cache keys for expensive steps that produce deterministic outputs.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/)
