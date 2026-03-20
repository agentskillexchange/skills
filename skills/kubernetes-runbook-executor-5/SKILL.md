---
name: Kubernetes Runbook Executor
description: Executes diagnostic runbooks for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Python client. Automates pod restart analysis, resource quota checks, and node condition trou
category: Runbooks & Diagnostics
framework: Codex
verification: verified_metadata
rating: 4.9
reviews: 42
source: https://agentskillexchange.com/skill/kubernetes-runbook-executor-5/
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Python client. Automates pod restart analysis, resource quota checks, and node condition troubleshooting.

## Overview

The Kubernetes Runbook Executor skill automates operational diagnostics for Kubernetes clusters through structured runbook workflows. It interfaces with clusters via kubectl commands and the official Kubernetes Python client (kubernetes-client/python) to gather diagnostic data and execute remediation steps.
The skill runs predefined diagnostic procedures including pod crash loop analysis using kubectl describe pod and kubectl logs –previous, resource exhaustion detection via kube-state-metrics queries, node condition checks through the Node Status API, and PersistentVolume binding troubleshooting. Each runbook step captures structured output for downstream analysis.
Diagnostic capabilities leverage the Kubernetes API server directly: listing events with field selectors (kubectl get events –field-selector reason=FailedScheduling), checking resource quotas via /api/v1/namespaces/{ns}/resourcequotas, analyzing HPA status through autoscaling/v2 API, and verifying network policies with the networking.k8s.io API group.
Advanced features include automated thread dump collection from JVM pods via kubectl exec jstack, Prometheus PromQL query execution for historical metrics correlation, and integration with kube-capacity for cluster-wide resource utilization reporting. The skill supports both imperative and GitOps-based remediation workflows.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-runbook-executor-5
```

### OpenClaw

```bash
openclaw install kubernetes-runbook-executor-5
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (42 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-runbook-executor-5/)*
