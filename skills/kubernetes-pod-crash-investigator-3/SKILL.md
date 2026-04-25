---
title: "Kubernetes Pod Crash Investigator"
description: "Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes API via kubectl and the official kubernetes-client/python SDK. Correlates container logs, resource limits, and node conditions for root cause analysis."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Investigator

The Kubernetes Pod Crash Investigator automates the diagnosis of pod failures in Kubernetes clusters. It connects to clusters via the official kubernetes-client/python SDK or kubectl CLI to gather comprehensive failure context. When a pod enters CrashLoopBackOff or OOMKilled state, the skill retrieves container logs from the current and previous instances, examines resource requests and limits, and checks node-level conditions including memory pressure and disk pressure events. The investigator correlates multiple data sources including Kubernetes Events API, container exit codes, liveness/readiness probe configurations, and PodDisruptionBudget status. It builds a timeline of events leading to the crash and identifies common root causes. Supported diagnostics include memory leak detection through OOM score analysis, misconfigured health probes, image pull failures with registry authentication issues, and init container dependency failures. Results are formatted as actionable runbook steps with suggested kubectl commands for remediation.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-investigator-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-crash-investigator-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/)
