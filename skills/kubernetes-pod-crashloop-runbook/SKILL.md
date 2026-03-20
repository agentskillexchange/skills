---
name: Kubernetes Pod Crashloop Runbook
description: Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
rating: 4.8
reviews: 61
source: https://agentskillexchange.com/skill/kubernetes-pod-crashloop-runbook/
---

# Kubernetes Pod Crashloop Runbook

Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Overview

This skill queries the Kubernetes API server (typically at /api/v1 and /apis/apps/v1) using a kubeconfig or in-cluster service account token. When a pod enters CrashLoopBackOff, the skill fetches the last 100 lines of container logs via the pods/log subresource, retrieves pod events from the Events API, and checks resource quota limits in the namespace. It distinguishes between OOMKilled (memory limit exceeded), probe failures (liveness/readiness misconfiguration), and missing dependencies (ConfigMap or Secret not found). The skill cross-references the pod spec against the namespace ResourceQuota and LimitRange objects. A step-by-step Markdown runbook is generated with specific kubectl commands to apply, including suggested resource limit adjustments and probe timeout fixes. Compatible with Kubernetes 1.25+.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crashloop-runbook
```

### OpenClaw

```bash
openclaw install kubernetes-pod-crashloop-runbook
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (61 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crashloop-runbook/)*
