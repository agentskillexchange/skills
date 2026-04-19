---
title: "Tekton Pipeline Resource Optimizer"
description: "The Tekton Pipeline Resource Optimizer skill analyzes your Tekton CI/CD pipeline configurations to identify resource waste and optimization opportunities. It queries the Tekton Results API to fetch historical TaskRun and PipelineRun execution data, then correlates with Prometheus metrics for actual CPU and memory consumption during builds. For each Task step, the skill compares declared resource requests/limits against actual usage percentiles (p50, p95, p99) from historical runs. It identifies over-provisioned steps wasting cluster capacity and under-provisioned steps causing OOMKills or CPU throttling. Recommendations include right-sized resource values with configurable headroom percentages. Pipeline-level analysis examines Task parallelism opportunities, identifying sequential Tasks that could run concurrently based on dependency analysis of workspace, result, and when-expression relationships. It also detects redundant git-clone operations across Tasks and recommends workspace sharing patterns. The skill validates Tekton resource definitions against the Tekton API specification, checks for deprecated fields across Tekton versions, and ensures compatibility with your installed Tekton Pipelines version. Output includes formatted optimization reports with estimated cost savings, Tekton YAML patches for recommended changes, and Grafana dashboard JSON for ongoing monitoring."
source: "https://github.com/tektoncd/pipeline"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "tektoncd/pipeline"
  github_stars: 8936
---

# Tekton Pipeline Resource Optimizer

The Tekton Pipeline Resource Optimizer skill analyzes your Tekton CI/CD pipeline configurations to identify resource waste and optimization opportunities. It queries the Tekton Results API to fetch historical TaskRun and PipelineRun execution data, then correlates with Prometheus metrics for actual CPU and memory consumption during builds. For each Task step, the skill compares declared resource requests/limits against actual usage percentiles (p50, p95, p99) from historical runs. It identifies over-provisioned steps wasting cluster capacity and under-provisioned steps causing OOMKills or CPU throttling. Recommendations include right-sized resource values with configurable headroom percentages. Pipeline-level analysis examines Task parallelism opportunities, identifying sequential Tasks that could run concurrently based on dependency analysis of workspace, result, and when-expression relationships. It also detects redundant git-clone operations across Tasks and recommends workspace sharing patterns. The skill validates Tekton resource definitions against the Tekton API specification, checks for deprecated fields across Tekton versions, and ensures compatibility with your installed Tekton Pipelines version. Output includes formatted optimization reports with estimated cost savings, Tekton YAML patches for recommended changes, and Grafana dashboard JSON for ongoing monitoring.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-resource-optimizer/)
