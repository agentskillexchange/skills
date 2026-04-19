---
title: "Kubernetes Diagnostic Runbook"
description: "The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters using kubeconfig files or in-cluster service account tokens via the official Kubernetes Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic workflows for rapid incident triage and root cause analysis. The agent performs systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff, OOMKilled detection), resource quota utilization analysis, persistent volume claim binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure). It queries the Events API to correlate recent cluster events with observed symptoms. For deeper diagnostics, the agent retrieves container logs via the pod log endpoint, checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service endpoint connectivity. It supports multi-cluster configurations, namespace-scoped analysis, and RBAC permission verification before executing commands. Output includes a structured triage report with severity-ranked findings and recommended remediation actions for each detected issue."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Diagnostic Runbook

The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters using kubeconfig files or in-cluster service account tokens via the official Kubernetes Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic workflows for rapid incident triage and root cause analysis. The agent performs systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff, OOMKilled detection), resource quota utilization analysis, persistent volume claim binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure). It queries the Events API to correlate recent cluster events with observed symptoms. For deeper diagnostics, the agent retrieves container logs via the pod log endpoint, checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service endpoint connectivity. It supports multi-cluster configurations, namespace-scoped analysis, and RBAC permission verification before executing commands. Output includes a structured triage report with severity-ranked findings and recommended remediation actions for each detected issue.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/)
