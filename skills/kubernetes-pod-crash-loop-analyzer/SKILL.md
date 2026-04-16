---
title: "Kubernetes Pod Crash Loop Analyzer"
description: "Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Pod Crash Loop Analyzer

Overview

The Kubernetes Pod Crash Loop Analyzer diagnoses pods stuck in CrashLoopBackOff state through systematic examination of container exit codes, event logs, and resource metrics. It automates the investigation workflow that SREs typically perform manually during incident response.

Key Capabilities

This skill runs kubectl describe pod to extract last termination reasons, exit codes (137 for OOMKill, 1 for application errors, 127 for missing binaries), and restart counts. It queries the Kubernetes Events API for related warnings and correlates OOMKilled signals with Prometheus container_memory_rss and container_memory_working_set_bytes metrics from cAdvisor.

Diagnostic Workflow

Examines init container failures, liveness and readiness probe misconfigurations, volume mount permission issues, and image pull backoff states. Cross-references node conditions from kubectl get nodes to identify resource pressure situations and generates remediation recommendations including resource limit adjustments, probe timeout tuning, and PodDisruptionBudget configurations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
