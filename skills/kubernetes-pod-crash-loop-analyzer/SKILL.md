---
title: "Kubernetes Pod Crash Loop Analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Loop Analyzer

Overview The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response. Key Capabilities This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor. Diagnostic Workflow Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-loop-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-crash-loop-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
