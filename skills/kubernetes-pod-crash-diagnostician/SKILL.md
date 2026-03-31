---
name: "Kubernetes Pod Crash Diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
category: "Runbooks &amp; Diagnostics"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
tool_ecosystem:
  tool: kubernetes
  github_repo: kubernetes/kubernetes
  github_stars: 121388
  license: Apache-2.0
  maintained: true
---
# Kubernetes Pod Crash Diagnostician

Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries.

## Overview

The Kubernetes Pod Crash Diagnostician skill provides automated root cause analysis for pod crash loops in Kubernetes clusters. It connects to the Kubernetes API server to fetch pod events, container statuses, and recent restart history. For OOMKilled containers, it queries Prometheus via PromQL to retrieve historical memory usage patterns and container_memory_working_set_bytes metrics, identifying whether the OOM was caused by a memory leak, insufficient limits, or spike load. For CrashLoopBackOff pods, it analyzes container logs from the previous terminated instance, checks init container completion status, and validates volume mount accessibility. The skill inspects resource quotas, limit ranges, and pod disruption budgets that may constrain scheduling. Generates diagnostic reports with recommended resource limit adjustments based on P95 memory and CPU usage. Supports ephemeral debug containers via kubectl debug for live investigation. Integrates with Grafana dashboards for visual correlation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostician -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-diagnostician
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
