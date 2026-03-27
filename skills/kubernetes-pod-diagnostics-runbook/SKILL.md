---
name: "Kubernetes Pod Diagnostics Runbook"
description: "Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically."
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Kubernetes Pod Diagnostics Runbook

Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically.

## Overview

The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting procedures for common pod failure states in Kubernetes clusters. It uses the official Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically, collecting pod descriptions, container logs, node conditions, and resource quota utilization in a structured diagnostic report.

For CrashLoopBackOff pods, the runbook retrieves previous container logs, checks liveness probe configurations, and correlates restart timestamps with cluster events. OOMKilled diagnostics compare container memory limits against actual usage metrics from the Metrics Server API, suggesting right-sized resource requests.

ImagePullBackOff diagnosis validates image references against container registry APIs, checks imagePullSecrets configuration, and verifies registry authentication tokens. The runbook also covers Pending pods by analyzing node affinity rules, taint tolerations, and PersistentVolumeClaim binding status. All findings are compiled into a prioritized remediation checklist with kubectl commands ready for execution.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostics-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostics-runbook
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/
