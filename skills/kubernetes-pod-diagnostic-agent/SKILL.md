---
name: "Kubernetes Pod Diagnostic Agent"
description: "Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources."
category: "Runbooks & Diagnostics"
framework: "Codex"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Kubernetes Pod Diagnostic Agent

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Overview

The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting for failing Kubernetes workloads. It interfaces with the Kubernetes API server through kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints to diagnose common pod failure patterns.

The skill systematically investigates pod issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError). It then retrieves container logs using the pod log subresource with previous=true for crashed containers and tailLines for recent output.

Diagnostic capabilities include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas, checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io, and reviewing NetworkPolicy rules that may block pod communication. The skill generates structured runbook output with root cause analysis, remediation commands, and links to relevant Kubernetes documentation. It also checks for common misconfigurations in Deployment, StatefulSet, and DaemonSet specs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostic-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/
