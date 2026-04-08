---
title: Kubernetes Pod Crash Loop Analyzer
description: Overview The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck
  in CrashLoopBackOff state through systematic examination of container exit codes,
  event logs, and resource metrics. It automates the investigation workflow that SREs
  typically perform manually during incident response. Key Capabilities This skill
  runs kubectl describe pod to extract last termination reasons, exit codes (137 for
  OOMKill, 1 for application errors, 127 for missing binaries), and restart counts.
  It queries the Kubernetes Events API for related warnings and correlates OOMKilled
  signals with Prometheus container_memory_rss and container_memory_working_set_bytes
  metrics from cAdvisor. Diagnostic Workflow Examines init container failures, liveness
  and readiness probe misconfigurations, volume mount permission issues, and image
  pull backoff states. Cross-references node conditions from kubectl get nodes to
  identify resource pressure situations and generates remediation recommendations
  including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget
  configurations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---

# Kubernetes Pod Crash Loop Analyzer

Overview The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response. Key Capabilities This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor. Diagnostic Workflow Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
