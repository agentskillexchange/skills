---
name: Kubernetes Pod Crash Investigator
description: Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes
  API via kubectl and the official kubernetes-client/python SDK. Correlates container
  logs, resource limits, and node conditions for root cause analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---
# Kubernetes Pod Crash Investigator

The Kubernetes Pod Crash Investigator automates the diagnosis of pod failures in Kubernetes clusters. It connects to clusters via the official kubernetes-client/python SDK or kubectl CLI to gather comprehensive failure context.
When a pod enters CrashLoopBackOff or OOMKilled state, the skill retrieves container logs from the current and previous instances, examines resource requests and limits, and checks node-level conditions including memory pressure and disk pressure events.
The investigator correlates multiple data sources including Kubernetes Events API, container exit codes, liveness/readiness probe configurations, and PodDisruptionBudget status. It builds a timeline of events leading to the crash and identifies common root causes.
Supported diagnostics include memory leak detection through OOM score analysis, misconfigured health probes, image pull failures with registry authentication issues, and init container dependency failures. Results are formatted as actionable runbook steps with suggested kubectl commands for remediation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/)
