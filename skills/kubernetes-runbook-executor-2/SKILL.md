---
title: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Runbook Executor

The Kubernetes Runbook Executor skill provides automated diagnostic procedures for Kubernetes cluster troubleshooting. Built on the official kubernetes/client-go SDK, it connects to clusters via kubeconfig and executes structured diagnostic sequences across namespaces and resource types.

Core diagnostic capabilities include pod health verification through the /healthz and /readyz probe endpoints, event stream analysis using the CoreV1 Events API to correlate warning events with pod restart patterns, and resource quota analysis to detect throttling. The skill queries the Metrics API (metrics.k8s.io/v1beta1) for real-time CPU and memory utilization data.

Runbook templates cover common failure scenarios including CrashLoopBackOff diagnosis, ImagePullBackOff resolution, PVC binding failures, and node NotReady conditions. Each runbook follows a decision-tree structure that progressively narrows root causes through API queries and log analysis via the container log endpoint.

The skill supports multi-cluster environments and can compare configurations across staging and production clusters to identify deployment drift. Output includes remediation commands ready for direct execution.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-runbook-executor-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-runbook-executor-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/)
