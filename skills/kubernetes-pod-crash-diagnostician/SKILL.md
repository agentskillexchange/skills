---
title: "Kubernetes Pod Crash Diagnostician"
description: "Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries."
slug: "kubernetes-pod-crash-diagnostician"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/"
listed: true
---

# Kubernetes Pod Crash Diagnostician

Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries.

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
clawhub install kubernetes-pod-crash-diagnostician
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes Pod Crash Diagnostician skill provides automated root cause analysis for pod crash loops in Kubernetes clusters. It connects to the Kubernetes API server to fetch pod events, container statuses, and recent restart history. For OOMKilled containers, it queries Prometheus via PromQL to retrieve historical memory usage patterns and container_memory_working_set_bytes metrics, identifying whether the OOM was caused by a memory leak, insufficient limits, or spike load. For CrashLoopBackOff pods, it analyzes container logs from the previous terminated instance, checks init container completion status, and validates volume mount accessibility. The skill inspects resource quotas, limit ranges, and pod disruption budgets that may constrain scheduling. Generates diagnostic reports with recommended resource limit adjustments based on P95 memory and CPU usage. Supports ephemeral debug containers via kubectl debug for live investigation. Integrates with Grafana dashboards for visual correlation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
