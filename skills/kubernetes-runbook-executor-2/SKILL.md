---
name: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/"
---
# Kubernetes Runbook Executor

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Overview

The Kubernetes Runbook Executor skill provides automated diagnostic procedures for Kubernetes cluster troubleshooting. Built on the official kubernetes/client-go SDK, it connects to clusters via kubeconfig and executes structured diagnostic sequences across namespaces and resource types.

Core diagnostic capabilities include pod health verification through the /healthz and /readyz probe endpoints, event stream analysis using the CoreV1 Events API to correlate warning events with pod restart patterns, and resource quota analysis to detect throttling. The skill queries the Metrics API (metrics.k8s.io/v1beta1) for real-time CPU and memory utilization data.

Runbook templates cover common failure scenarios including CrashLoopBackOff diagnosis, ImagePullBackOff resolution, PVC binding failures, and node NotReady conditions. Each runbook follows a decision-tree structure that progressively narrows root causes through API queries and log analysis via the container log endpoint.

The skill supports multi-cluster environments and can compare configurations across staging and production clusters to identify deployment drift. Output includes remediation commands ready for direct execution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-2 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-runbook-executor-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/)
