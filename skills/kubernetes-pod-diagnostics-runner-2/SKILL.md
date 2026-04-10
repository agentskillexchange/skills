---
name: Kubernetes Pod Diagnostics Runner
description: Runs automated diagnostic sequences on Kubernetes pods using kubectl
  exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled
  events, CrashLoopBackOff analysis, and resource utilization via metrics-server.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/
category:
- Runbooks &amp; Diagnostics
framework:
- Cursor
---
# Kubernetes Pod Diagnostics Runner

The Kubernetes Pod Diagnostics Runner skill automates troubleshooting of failing Kubernetes workloads. It uses the Kubernetes REST API (/api/v1/namespaces/{ns}/pods) and kubectl CLI to run comprehensive diagnostic sequences.
When a pod is unhealthy, the skill collects: pod describe output including events and conditions, container logs with -previous flag for crashed containers, resource metrics from metrics-server API (/apis/metrics.k8s.io/v1beta1), and node conditions for the hosting node.
It automatically identifies common failure patterns: OOMKilled exits with memory limit recommendations based on actual usage, CrashLoopBackOff with init container and readiness probe analysis, ImagePullBackOff with registry authentication verification, and Pending pods with scheduler event analysis.
The skill generates structured runbook output with root cause identification, immediate remediation steps, and preventive configuration changes. It supports multi-container pods, sidecar analysis, and can exec into running containers to check filesystem state, network connectivity, and process health. Integrates with PodDisruptionBudget and HorizontalPodAutoscaler status for scaling-related issues.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/)
