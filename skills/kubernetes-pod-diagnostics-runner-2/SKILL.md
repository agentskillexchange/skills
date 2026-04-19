---
title: "Kubernetes Pod Diagnostics Runner"
description: "The Kubernetes Pod Diagnostics Runner skill automates troubleshooting of failing Kubernetes workloads. It uses the Kubernetes REST API (/api/v1/namespaces/{ns}/pods) and kubectl CLI to run comprehensive diagnostic sequences. When a pod is unhealthy, the skill collects: pod describe output including events and conditions, container logs with &#8211;previous flag for crashed containers, resource metrics from metrics-server API (/apis/metrics.k8s.io/v1beta1), and node conditions for the hosting node. It automatically identifies common failure patterns: OOMKilled exits with memory limit recommendations based on actual usage, CrashLoopBackOff with init container and readiness probe analysis, ImagePullBackOff with registry authentication verification, and Pending pods with scheduler event analysis. The skill generates structured runbook output with root cause identification, immediate remediation steps, and preventive configuration changes. It supports multi-container pods, sidecar analysis, and can exec into running containers to check filesystem state, network connectivity, and process health. Integrates with PodDisruptionBudget and HorizontalPodAutoscaler status for scaling-related issues."
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

# Kubernetes Pod Diagnostics Runner

The Kubernetes Pod Diagnostics Runner skill automates troubleshooting of failing Kubernetes workloads. It uses the Kubernetes REST API (/api/v1/namespaces/{ns}/pods) and kubectl CLI to run comprehensive diagnostic sequences. When a pod is unhealthy, the skill collects: pod describe output including events and conditions, container logs with &#8211;previous flag for crashed containers, resource metrics from metrics-server API (/apis/metrics.k8s.io/v1beta1), and node conditions for the hosting node. It automatically identifies common failure patterns: OOMKilled exits with memory limit recommendations based on actual usage, CrashLoopBackOff with init container and readiness probe analysis, ImagePullBackOff with registry authentication verification, and Pending pods with scheduler event analysis. The skill generates structured runbook output with root cause identification, immediate remediation steps, and preventive configuration changes. It supports multi-container pods, sidecar analysis, and can exec into running containers to check filesystem state, network connectivity, and process health. Integrates with PodDisruptionBudget and HorizontalPodAutoscaler status for scaling-related issues.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/)
