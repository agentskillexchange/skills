---
title: Kubernetes Pod Crash Investigator
description: The Kubernetes Pod Crash Investigator automates the diagnosis of pod
  failures in Kubernetes clusters. It connects to clusters via the official kubernetes-client/python
  SDK or kubectl CLI to gather comprehensive failure context. When a pod enters CrashLoopBackOff
  or OOMKilled state, the skill retrieves container logs from the current and previous
  instances, examines resource requests and limits, and checks node-level conditions
  including memory pressure and disk pressure events. The investigator correlates
  multiple data sources including Kubernetes Events API, container exit codes, liveness/readiness
  probe configurations, and PodDisruptionBudget status. It builds a timeline of events
  leading to the crash and identifies common root causes. Supported diagnostics include
  memory leak detection through OOM score analysis, misconfigured health probes, image
  pull failures with registry authentication issues, and init container dependency
  failures. Results are formatted as actionable runbook steps with suggested kubectl
  commands for remediation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# Kubernetes Pod Crash Investigator

The Kubernetes Pod Crash Investigator automates the diagnosis of pod failures in Kubernetes clusters. It connects to clusters via the official kubernetes-client/python SDK or kubectl CLI to gather comprehensive failure context. When a pod enters CrashLoopBackOff or OOMKilled state, the skill retrieves container logs from the current and previous instances, examines resource requests and limits, and checks node-level conditions including memory pressure and disk pressure events. The investigator correlates multiple data sources including Kubernetes Events API, container exit codes, liveness/readiness probe configurations, and PodDisruptionBudget status. It builds a timeline of events leading to the crash and identifies common root causes. Supported diagnostics include memory leak detection through OOM score analysis, misconfigured health probes, image pull failures with registry authentication issues, and init container dependency failures. Results are formatted as actionable runbook steps with suggested kubectl commands for remediation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/)
