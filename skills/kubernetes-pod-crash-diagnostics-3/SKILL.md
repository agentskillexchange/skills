---
name: "Kubernetes Pod Crash Diagnostics"
description: "Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
category: "Developer Tools"
framework: "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/"
tool_ecosystem:
  tool: kubernetes
  github_stars: 121334
  github_repo: kubernetes/kubernetes
  license: Apache-2.0
  maintained: true
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Overview

**Kubernetes Pod Crash Diagnostics** is built around Kubernetes orchestration platform. The underlying ecosystem is represented by `kubernetes/kubernetes` (121,313+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like kubectl, API server, pods, deployments, events, logs, probes, RBAC and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to kubernetes so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis. The implementation typically relies on kubectl, API server, pods, deployments, events, logs, probes, RBAC, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses kubectl, API server, pods, deployments, events, logs, probes, RBAC instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as cluster operations, workload health, scaling, and production troubleshooting.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include cluster operations, workload health, scaling, and production troubleshooting. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics-3 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-diagnostics-3
```

## Source

- Marketplace: https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/
