---
name: "Kubernetes Pod Crash Loop Analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
category: "Runbooks & Diagnostics"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/"
tool_ecosystem:
  tool: "kubernetes"
  github_stars: 121334
  github_repo: "kubernetes/kubernetes"
  license: "Apache-2.0"
  maintained: true
---

# Kubernetes Pod Crash Loop Analyzer

Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.

## Overview

Overview

The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response.

Key Capabilities

This skill runs `kubectl describe pod` to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus `container_memory_rss` and `container_memory_working_set_bytes` metrics from cAdvisor.

Diagnostic Workflow

Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from `kubectl get nodes` to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-loop-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-loop-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-loop-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-loop-analyzer -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-loop-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/
