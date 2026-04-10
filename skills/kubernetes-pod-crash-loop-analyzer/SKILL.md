---
title: "Kubernetes Pod Crash Loop Analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
slug: "kubernetes-pod-crash-loop-analyzer"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/"
listed: true
---

# Kubernetes Pod Crash Loop Analyzer

Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.

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
clawhub install kubernetes-pod-crash-loop-analyzer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response.
Key Capabilities
This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor.
Diagnostic Workflow
Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
