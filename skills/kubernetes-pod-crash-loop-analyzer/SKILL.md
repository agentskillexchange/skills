---
title: "Kubernetes Pod Crash Loop Analyzer"
description: "Overview The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response. Key Capabilities This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor. Diagnostic Workflow Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Loop Analyzer

Overview The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response. Key Capabilities This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor. Diagnostic Workflow Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
