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
  license: "Apache-2.0"
---

# Argo Workflows DAG Optimizer

The Argo Workflows DAG Optimizer connects to the Argo Server REST API to analyze workflow execution patterns and identify optimization opportunities. It fetches completed workflow runs and performs critical path analysis on DAG task dependencies, highlighting sequential bottlenecks that could be parallelized. The skill parses workflow templates written in YAML, understanding DAG task dependencies, artifact passing between steps, and resource template references. It suggests dependency graph restructuring to maximize parallelism while respecting data dependencies. Resource optimization analyzes container resource requests vs actual usage from workflow metrics, recommending right-sized CPU and memory allocations. The skill handles workflow-of-workflows patterns, cluster workflow templates, and parameterized workflow submissions. It generates optimized workflow YAML with added retry strategies, timeout configurations, and memoization cache keys for expensive steps that produce deterministic outputs.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argo-workflows-dag-optimizer/)
