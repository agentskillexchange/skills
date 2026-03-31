---
name: "Kubernetes Diagnostic Runbook"
description: "Executes diagnostic workflows against Kubernetes clusters using kubectl and the Kubernetes Python client (kubernetes.client). Checks pod health, resource quotas, event logs, and node conditions for rapid incident triage."
category: "Runbooks & Diagnostics"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/"
---
# Kubernetes Diagnostic Runbook

Executes diagnostic workflows against Kubernetes clusters using kubectl and the Kubernetes Python client (kubernetes.client). Checks pod health, resource quotas, event logs, and node conditions for rapid incident triage.

## Overview

The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters using kubeconfig files or in-cluster service account tokens via the official Kubernetes Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic workflows for rapid incident triage and root cause analysis.

The agent performs systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff, OOMKilled detection), resource quota utilization analysis, persistent volume claim binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure). It queries the Events API to correlate recent cluster events with observed symptoms.

For deeper diagnostics, the agent retrieves container logs via the pod log endpoint, checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service endpoint connectivity. It supports multi-cluster configurations, namespace-scoped analysis, and RBAC permission verification before executing commands. Output includes a structured triage report with severity-ranked findings and recommended remediation actions for each detected issue.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostic-runbook
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostic-runbook -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostic-runbook -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-diagnostic-runbook -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-diagnostic-runbook
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/)
