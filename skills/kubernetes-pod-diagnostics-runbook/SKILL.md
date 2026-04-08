---
title: Kubernetes Pod Diagnostics Runbook
description: The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting
  procedures for common pod failure states in Kubernetes clusters. It uses the official
  Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically,
  collecting pod descriptions, container logs, node conditions, and resource quota
  utilization in a structured diagnostic report. For CrashLoopBackOff pods, the runbook
  retrieves previous container logs, checks liveness probe configurations, and correlates
  restart timestamps with cluster events. OOMKilled diagnostics compare container
  memory limits against actual usage metrics from the Metrics Server API, suggesting
  right-sized resource requests. ImagePullBackOff diagnosis validates image references
  against container registry APIs, checks imagePullSecrets configuration, and verifies
  registry authentication tokens. The runbook also covers Pending pods by analyzing
  node affinity rules, taint tolerations, and PersistentVolumeClaim binding status.
  All findings are compiled into a prioritized remediation checklist with kubectl
  commands ready for execution.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Kubernetes Pod Diagnostics Runbook

The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting procedures for common pod failure states in Kubernetes clusters. It uses the official Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically, collecting pod descriptions, container logs, node conditions, and resource quota utilization in a structured diagnostic report. For CrashLoopBackOff pods, the runbook retrieves previous container logs, checks liveness probe configurations, and correlates restart timestamps with cluster events. OOMKilled diagnostics compare container memory limits against actual usage metrics from the Metrics Server API, suggesting right-sized resource requests. ImagePullBackOff diagnosis validates image references against container registry APIs, checks imagePullSecrets configuration, and verifies registry authentication tokens. The runbook also covers Pending pods by analyzing node affinity rules, taint tolerations, and PersistentVolumeClaim binding status. All findings are compiled into a prioritized remediation checklist with kubectl commands ready for execution.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/)
