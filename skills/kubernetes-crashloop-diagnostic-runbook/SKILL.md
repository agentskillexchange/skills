---
name: Kubernetes Crashloop Diagnostic Runbook
description: Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl
  and the Kubernetes API. Fetches pod events, container logs, and resource limits
  via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause
  analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image
  pull errors.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---
# Kubernetes Crashloop Diagnostic Runbook

This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
