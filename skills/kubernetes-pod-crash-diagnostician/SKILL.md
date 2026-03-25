---
name: "Kubernetes Pod Crash Diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
category: "Runbooks & Diagnostics"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/
