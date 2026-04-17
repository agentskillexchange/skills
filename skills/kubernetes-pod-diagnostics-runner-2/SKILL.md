---
title: "Kubernetes Pod Diagnostics Runner"
description: "Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Pod Diagnostics Runner

The Kubernetes Pod Diagnostics Runner skill automates troubleshooting of failing Kubernetes workloads. It uses the Kubernetes REST API (/api/v1/namespaces/{ns}/pods) and kubectl CLI to run comprehensive diagnostic sequences.

When a pod is unhealthy, the skill collects: pod describe output including events and conditions, container logs with –previous flag for crashed containers, resource metrics from metrics-server API (/apis/metrics.k8s.io/v1beta1), and node conditions for the hosting node.

It automatically identifies common failure patterns: OOMKilled exits with memory limit recommendations based on actual usage, CrashLoopBackOff with init container and readiness probe analysis, ImagePullBackOff with registry authentication verification, and Pending pods with scheduler event analysis.

The skill generates structured runbook output with root cause identification, immediate remediation steps, and preventive configuration changes. It supports multi-container pods, sidecar analysis, and can exec into running containers to check filesystem state, network connectivity, and process health. Integrates with PodDisruptionBudget and HorizontalPodAutoscaler status for scaling-related issues.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-diagnostics-runner-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-diagnostics-runner-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/)
