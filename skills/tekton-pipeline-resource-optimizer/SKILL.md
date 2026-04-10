---
name: "Tekton Pipeline Resource Optimizer"
description: "Analyzes Tekton Pipeline and Task resource definitions using the Tekton Results API. Recommends CPU/memory request adjustments based on historical TaskRun metrics from Prometheus."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/tekton-pipeline-resource-optimizer/"
category:
  - "CI/CD Integrations"
framework:
  - "Cursor"
---

# Tekton Pipeline Resource Optimizer

The Tekton Pipeline Resource Optimizer skill analyzes your Tekton CI/CD pipeline configurations to identify resource waste and optimization opportunities. It queries the Tekton Results API to fetch historical TaskRun and PipelineRun execution data, then correlates with Prometheus metrics for actual CPU and memory consumption during builds.
For each Task step, the skill compares declared resource requests/limits against actual usage percentiles (p50, p95, p99) from historical runs. It identifies over-provisioned steps wasting cluster capacity and under-provisioned steps causing OOMKills or CPU throttling. Recommendations include right-sized resource values with configurable headroom percentages.
Pipeline-level analysis examines Task parallelism opportunities, identifying sequential Tasks that could run concurrently based on dependency analysis of workspace, result, and when-expression relationships. It also detects redundant git-clone operations across Tasks and recommends workspace sharing patterns.
The skill validates Tekton resource definitions against the Tekton API specification, checks for deprecated fields across Tekton versions, and ensures compatibility with your installed Tekton Pipelines version. Output includes formatted optimization reports with estimated cost savings, Tekton YAML patches for recommended changes, and Grafana dashboard JSON for ongoing monitoring.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tekton-pipeline-resource-optimizer/)
