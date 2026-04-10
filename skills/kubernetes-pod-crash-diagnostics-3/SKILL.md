---
title: "Kubernetes Pod Crash Diagnostics"
description: "Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
slug: "kubernetes-pod-crash-diagnostics-3"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/"
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

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
clawhub install kubernetes-pod-crash-diagnostics-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Kubernetes Pod Crash Diagnostics is built around Kubernetes orchestration platform. The underlying ecosystem is represented by kubernetes/kubernetes (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to kubernetes so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis. The implementation typically relies on kubectl, API server, pods, deployments, events, logs, probes, RBAC, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.
- Accesses kubectl, API server, pods, deployments, events, logs, probes, RBAC instead of scraping a UI, which makes runs easier to audit and retry.
- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
- Fits into broader integration points such as cluster operations, workload health, scaling, and production troubleshooting.
As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include cluster operations, workload health, scaling, and production troubleshooting. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/)
