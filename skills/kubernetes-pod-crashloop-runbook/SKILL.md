---
name: Kubernetes Pod Crashloop Runbook
description: Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped
  via the Kubernetes API server. Fetches recent events, container logs, and resource
  quota status to identify root causes such as OOMKilled, misconfigured liveness probes,
  or missing ConfigMaps. Generates a step-by-step remediation runbook.
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

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
