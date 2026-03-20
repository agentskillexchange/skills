---
name: Kubernetes Pod Diagnostic Agent
description: Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.9
reviews: 15
source: https://agentskillexchange.com/skill/kubernetes-pod-diagnostic-agent/
---

# Kubernetes Pod Diagnostic Agent

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Overview

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-diagnostic-agent
```

### OpenClaw

```bash
clawhub install kubernetes-pod-diagnostic-agent
```

### Claude Code

```bash
claude mcp add kubernetes-pod-diagnostic-agent
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-pod-diagnostic-agent/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.9/5 (15 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-diagnostic-agent/)
