---
title: "Kubernetes Pod Diagnostic Agent"
description: "The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting for failing Kubernetes workloads. It interfaces with the Kubernetes API server through kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints to diagnose common pod failure patterns. The skill systematically investigates pod issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError). It then retrieves container logs using the pod log subresource with previous=true for crashed containers and tailLines for recent output. Diagnostic capabilities include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas, checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io, and reviewing NetworkPolicy rules that may block pod communication. The skill generates structured runbook output with root cause analysis, remediation commands, and links to relevant Kubernetes documentation. It also checks for common misconfigurations in Deployment, StatefulSet, and DaemonSet specs."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostic Agent

The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting for failing Kubernetes workloads. It interfaces with the Kubernetes API server through kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints to diagnose common pod failure patterns. The skill systematically investigates pod issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError). It then retrieves container logs using the pod log subresource with previous=true for crashed containers and tailLines for recent output. Diagnostic capabilities include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas, checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io, and reviewing NetworkPolicy rules that may block pod communication. The skill generates structured runbook output with root cause analysis, remediation commands, and links to relevant Kubernetes documentation. It also checks for common misconfigurations in Deployment, StatefulSet, and DaemonSet specs.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/)
