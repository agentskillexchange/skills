---
title: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API."
slug: "kubernetes-runbook-executor-2"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/"
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-runbook-executor-2
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes Runbook Executor skill provides automated diagnostic procedures for Kubernetes cluster troubleshooting. Built on the official kubernetes/client-go SDK, it connects to clusters via kubeconfig and executes structured diagnostic sequences across namespaces and resource types.
Core diagnostic capabilities include pod health verification through the /healthz and /readyz probe endpoints, event stream analysis using the CoreV1 Events API to correlate warning events with pod restart patterns, and resource quota analysis to detect throttling. The skill queries the Metrics API (metrics.k8s.io/v1beta1) for real-time CPU and memory utilization data.
Runbook templates cover common failure scenarios including CrashLoopBackOff diagnosis, ImagePullBackOff resolution, PVC binding failures, and node NotReady conditions. Each runbook follows a decision-tree structure that progressively narrows root causes through API queries and log analysis via the container log endpoint.
The skill supports multi-cluster environments and can compare configurations across staging and production clusters to identify deployment drift. Output includes remediation commands ready for direct execution.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/)
