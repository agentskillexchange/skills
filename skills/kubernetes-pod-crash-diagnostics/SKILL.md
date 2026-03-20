---
name: Kubernetes Pod Crash Diagnostics
description: Diagnoses CrashLoopBackOff and OOMKilled pods using kubectl and the Kubernetes API /api/v1/pods endpoint. Correlates container logs, resource limits, and node conditions for root cause analysis.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.9
reviews: 43
source: https://agentskillexchange.com/skill/kubernetes-pod-crash-diagnostics/
---

# Kubernetes Pod Crash Diagnostics

Diagnoses CrashLoopBackOff and OOMKilled pods using kubectl and the Kubernetes API /api/v1/pods endpoint. Correlates container logs, resource limits, and node conditions for root cause analysis.

## Overview

Diagnoses CrashLoopBackOff and OOMKilled pods using kubectl and the Kubernetes API /api/v1/pods endpoint. Correlates container logs, resource limits, and node conditions for root cause analysis.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-diagnostics
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-diagnostics
```

### Claude Code

```bash
claude mcp add kubernetes-pod-crash-diagnostics
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-pod-crash-diagnostics/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.9/5 (43 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-diagnostics/)
