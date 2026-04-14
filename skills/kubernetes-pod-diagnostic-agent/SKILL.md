---
title: "Kubernetes Pod Diagnostic Agent"
description: "Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostic Agent

The Kubernetes Pod Diagnostic Agent skill provides automated troubleshooting for failing Kubernetes workloads. It interfaces with the Kubernetes API server through kubectl commands and direct REST API calls to /api/v1 and /apis/apps/v1 endpoints to diagnose common pod failure patterns.

The skill systematically investigates pod issues by first querying pod status via /api/v1/namespaces/{ns}/pods/{name} to identify the failure state (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, CreateContainerConfigError). It then retrieves container logs using the pod log subresource with previous=true for crashed containers and tailLines for recent output.

Diagnostic capabilities include analyzing resource quotas and LimitRange conflicts via /api/v1/namespaces/{ns}/resourcequotas, checking node capacity and taints through /api/v1/nodes, inspecting PersistentVolumeClaim bindings, verifying ServiceAccount and RBAC permissions via /apis/rbac.authorization.k8s.io, and reviewing NetworkPolicy rules that may block pod communication. The skill generates structured runbook output with root cause analysis, remediation commands, and links to relevant Kubernetes documentation. It also checks for common misconfigurations in Deployment, StatefulSet, and DaemonSet specs.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/)
