---
title: "Kubernetes Crashloop Diagnostic Runbook"
description: "This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Crashloop Diagnostic Runbook

This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
