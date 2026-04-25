---
title: "Kubernetes Diagnostic Runbook"
description: "Executes diagnostic workflows against Kubernetes clusters using kubectl and the Kubernetes Python client (kubernetes.client). Checks pod health, resource quotas, event logs, and node conditions for rapid incident triage."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Diagnostic Runbook

The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters using kubeconfig files or in-cluster service account tokens via the official Kubernetes Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic workflows for rapid incident triage and root cause analysis. The agent performs systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff, OOMKilled detection), resource quota utilization analysis, persistent volume claim binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure). It queries the Events API to correlate recent cluster events with observed symptoms. For deeper diagnostics, the agent retrieves container logs via the pod log endpoint, checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service endpoint connectivity. It supports multi-cluster configurations, namespace-scoped analysis, and RBAC permission verification before executing commands. Output includes a structured triage report with severity-ranked findings and recommended remediation actions for each detected issue.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-diagnostic-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-diagnostic-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/)
