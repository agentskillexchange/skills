---
title: Kubernetes Pod Crashloop Runbook
description: This skill queries the Kubernetes API server (typically at /api/v1 and
  /apis/apps/v1) using a kubeconfig or in-cluster service account token. When a pod
  enters CrashLoopBackOff, the skill fetches the last 100 lines of container logs
  via the pods/log subresource, retrieves pod events from the Events API, and checks
  resource quota limits in the namespace. It distinguishes between OOMKilled (memory
  limit exceeded), probe failures (liveness/readiness misconfiguration), and missing
  dependencies (ConfigMap or Secret not found). The skill cross-references the pod
  spec against the namespace ResourceQuota and LimitRange objects. A step-by-step
  Markdown runbook is generated with specific kubectl commands to apply, including
  suggested resource limit adjustments and probe timeout fixes. Compatible with Kubernetes
  1.25+.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
---

# Kubernetes Pod Crashloop Runbook

This skill queries the Kubernetes API server (typically at /api/v1 and /apis/apps/v1) using a kubeconfig or in-cluster service account token. When a pod enters CrashLoopBackOff, the skill fetches the last 100 lines of container logs via the pods/log subresource, retrieves pod events from the Events API, and checks resource quota limits in the namespace. It distinguishes between OOMKilled (memory limit exceeded), probe failures (liveness/readiness misconfiguration), and missing dependencies (ConfigMap or Secret not found). The skill cross-references the pod spec against the namespace ResourceQuota and LimitRange objects. A step-by-step Markdown runbook is generated with specific kubectl commands to apply, including suggested resource limit adjustments and probe timeout fixes. Compatible with Kubernetes 1.25+.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
