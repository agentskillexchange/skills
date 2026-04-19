---
title: "Kubernetes Pod Diagnostics Runbook"
description: "The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting procedures for common pod failure states in Kubernetes clusters. It uses the official Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically, collecting pod descriptions, container logs, node conditions, and resource quota utilization in a structured diagnostic report. For CrashLoopBackOff pods, the runbook retrieves previous container logs, checks liveness probe configurations, and correlates restart timestamps with cluster events. OOMKilled diagnostics compare container memory limits against actual usage metrics from the Metrics Server API, suggesting right-sized resource requests. ImagePullBackOff diagnosis validates image references against container registry APIs, checks imagePullSecrets configuration, and verifies registry authentication tokens. The runbook also covers Pending pods by analyzing node affinity rules, taint tolerations, and PersistentVolumeClaim binding status. All findings are compiled into a prioritized remediation checklist with kubectl commands ready for execution."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics Runbook

The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting procedures for common pod failure states in Kubernetes clusters. It uses the official Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically, collecting pod descriptions, container logs, node conditions, and resource quota utilization in a structured diagnostic report. For CrashLoopBackOff pods, the runbook retrieves previous container logs, checks liveness probe configurations, and correlates restart timestamps with cluster events. OOMKilled diagnostics compare container memory limits against actual usage metrics from the Metrics Server API, suggesting right-sized resource requests. ImagePullBackOff diagnosis validates image references against container registry APIs, checks imagePullSecrets configuration, and verifies registry authentication tokens. The runbook also covers Pending pods by analyzing node affinity rules, taint tolerations, and PersistentVolumeClaim binding status. All findings are compiled into a prioritized remediation checklist with kubectl commands ready for execution.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/)
