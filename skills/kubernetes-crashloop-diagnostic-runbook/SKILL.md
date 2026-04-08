---
title: Kubernetes Crashloop Diagnostic Runbook
description: 'This runbook skill automates diagnosis of CrashLoopBackOff conditions
  in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server
  to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log,
  and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill
  analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns.
  For each failure mode it provides specific remediation commands: adjusting memory
  limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness
  probe thresholds, and resolving image pull authentication errors. It integrates
  with Datadog APM via the Datadog API to correlate crash events with latency spikes,
  and posts structured runbook results to PagerDuty incident notes using the PagerDuty
  Events API v2.'
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
