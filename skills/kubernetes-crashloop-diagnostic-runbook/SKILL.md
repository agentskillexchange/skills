---
title: "Kubernetes Crashloop Diagnostic Runbook"
description: "This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Crashloop Diagnostic Runbook

This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-crashloop-diagnostic-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-crashloop-diagnostic-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
