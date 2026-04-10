---
name: "Kubernetes Pod Diagnostics Runbook"
description: "Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---

# Kubernetes Pod Diagnostics Runbook

The Kubernetes Pod Diagnostics Runbook provides systematic troubleshooting procedures for common pod failure states in Kubernetes clusters. It uses the official Kubernetes Python client (kubernetes-client/python) to query cluster state programmatically, collecting pod descriptions, container logs, node conditions, and resource quota utilization in a structured diagnostic report.
For CrashLoopBackOff pods, the runbook retrieves previous container logs, checks liveness probe configurations, and correlates restart timestamps with cluster events. OOMKilled diagnostics compare container memory limits against actual usage metrics from the Metrics Server API, suggesting right-sized resource requests.
ImagePullBackOff diagnosis validates image references against container registry APIs, checks imagePullSecrets configuration, and verifies registry authentication tokens. The runbook also covers Pending pods by analyzing node affinity rules, taint tolerations, and PersistentVolumeClaim binding status. All findings are compiled into a prioritized remediation checklist with kubectl commands ready for execution.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/)
