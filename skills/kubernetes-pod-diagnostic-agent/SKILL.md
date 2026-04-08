---
title: Kubernetes Pod Diagnostic Agent
description: The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting
  for failing Kubernetes workloads. It interfaces with the Kubernetes API server through
  kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints
  to diagnose common pod failure patterns. The skill systematically investigates pod
  issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify
  the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError).
  It then retrieves container logs using the pod log subresource with previous=true
  for crashed containers and tailLines for recent output. Diagnostic capabilities
  include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas,
  checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim
  bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io,
  and reviewing NetworkPolicy rules that may block pod communication. The skill generates
  structured runbook output with root cause analysis, remediation commands, and links
  to relevant Kubernetes documentation. It also checks for common misconfigurations
  in Deployment, StatefulSet, and DaemonSet specs.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# Kubernetes Pod Diagnostic Agent

The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting for failing Kubernetes workloads. It interfaces with the Kubernetes API server through kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints to diagnose common pod failure patterns. The skill systematically investigates pod issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError). It then retrieves container logs using the pod log subresource with previous=true for crashed containers and tailLines for recent output. Diagnostic capabilities include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas, checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io, and reviewing NetworkPolicy rules that may block pod communication. The skill generates structured runbook output with root cause analysis, remediation commands, and links to relevant Kubernetes documentation. It also checks for common misconfigurations in Deployment, StatefulSet, and DaemonSet specs.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/)
