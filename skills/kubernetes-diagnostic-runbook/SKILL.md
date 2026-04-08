---
title: Kubernetes Diagnostic Runbook
description: The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters
  using kubeconfig files or in-cluster service account tokens via the official Kubernetes
  Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic
  workflows for rapid incident triage and root cause analysis. The agent performs
  systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff,
  OOMKilled detection), resource quota utilization analysis, persistent volume claim
  binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure).
  It queries the Events API to correlate recent cluster events with observed symptoms.
  For deeper diagnostics, the agent retrieves container logs via the pod log endpoint,
  checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service
  endpoint connectivity. It supports multi-cluster configurations, namespace-scoped
  analysis, and RBAC permission verification before executing commands. Output includes
  a structured triage report with severity-ranked findings and recommended remediation
  actions for each detected issue.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---

# Kubernetes Diagnostic Runbook

The Kubernetes Diagnostic Runbook agent connects to Kubernetes clusters using kubeconfig files or in-cluster service account tokens via the official Kubernetes Python client (kubernetes.client.CoreV1Api, AppsV1Api). It executes structured diagnostic workflows for rapid incident triage and root cause analysis. The agent performs systematic health checks including pod status inspection (CrashLoopBackOff, ImagePullBackOff, OOMKilled detection), resource quota utilization analysis, persistent volume claim binding status, and node condition evaluation (MemoryPressure, DiskPressure, PIDPressure). It queries the Events API to correlate recent cluster events with observed symptoms. For deeper diagnostics, the agent retrieves container logs via the pod log endpoint, checks HorizontalPodAutoscaler status and scaling events, and validates Ingress/Service endpoint connectivity. It supports multi-cluster configurations, namespace-scoped analysis, and RBAC permission verification before executing commands. Output includes a structured triage report with severity-ranked findings and recommended remediation actions for each detected issue.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/)
