---
title: "Kubernetes Crashloop Diagnostic Runbook"
description: "Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors."
slug: "kubernetes-crashloop-diagnostic-runbook"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/"
---

# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-crashloop-diagnostic-runbook
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This runbook skill automates diagnosis of CrashLoopBackOff conditions in Kubernetes clusters. It uses kubectl and direct calls to the Kubernetes API server to fetch pod events from /api/v1/namespaces/{ns}/events, container logs from /api/v1/namespaces/{ns}/pods/{name}/log, and resource quota usage from /api/v1/namespaces/{ns}/resourcequotas. The skill analyzes exit codes, OOMKilled reasons, and liveness/readiness probe failure patterns. For each failure mode it provides specific remediation commands: adjusting memory limits for OOMKilled pods, creating missing ConfigMaps or Secrets, fixing liveness probe thresholds, and resolving image pull authentication errors. It integrates with Datadog APM via the Datadog API to correlate crash events with latency spikes, and posts structured runbook results to PagerDuty incident notes using the PagerDuty Events API v2.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
