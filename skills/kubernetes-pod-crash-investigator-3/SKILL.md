---
name: "Kubernetes Pod Crash Investigator"
description: "Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes API via kubectl and the official kubernetes-client/python SDK. Correlates container logs, resource limits, and node conditions for root cause analysis."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Kubernetes Pod Crash Investigator

Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes API via kubectl and the official kubernetes-client/python SDK. Correlates container logs, resource limits, and node conditions for root cause analysis.

## Overview

The Kubernetes Pod Crash Investigator automates the diagnosis of pod failures in Kubernetes clusters. It connects to clusters via the official kubernetes-client/python SDK or kubectl CLI to gather comprehensive failure context.

When a pod enters CrashLoopBackOff or OOMKilled state, the skill retrieves container logs from the current and previous instances, examines resource requests and limits, and checks node-level conditions including memory pressure and disk pressure events.

The investigator correlates multiple data sources including Kubernetes Events API, container exit codes, liveness/readiness probe configurations, and PodDisruptionBudget status. It builds a timeline of events leading to the crash and identifies common root causes.

Supported diagnostics include memory leak detection through OOM score analysis, misconfigured health probes, image pull failures with registry authentication issues, and init container dependency failures. Results are formatted as actionable runbook steps with suggested kubectl commands for remediation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator-3 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-investigator-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/
