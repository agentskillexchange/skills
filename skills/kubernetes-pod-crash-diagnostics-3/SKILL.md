---
name: "Kubernetes Pod Crash Diagnostics"
description: "Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
category: "Developer Tools"
framework: "Codex"
verification: listed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Overview

The Kubernetes Pod Crash Diagnostics skill provides structured troubleshooting for failing Kubernetes workloads. It executes a diagnostic sequence starting with kubectl get pods to identify unhealthy pods by status including CrashLoopBackOff, Error, OOMKilled, and ImagePullBackOff. It then runs kubectl describe pod to extract event history, container states, and restart counts. For crashed containers, it retrieves previous container logs to identify application-level errors. The skill analyzes container exit codes (137 for OOMKill, 1 for application error, 143 for SIGTERM) and cross-references with resource requests and limits from the pod spec. It examines liveness and readiness probe configurations for misconfigured timeouts, incorrect paths, or port mismatches. Output is a structured diagnostic report with root cause classification and remediation steps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-diagnostics-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/
