---
name: Kubernetes Pod Crash Investigator
description: Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: listed
rating: 4.0
reviews: 81
source: https://agentskillexchange.com/skill/kubernetes-pod-crash-investigator/
---

# Kubernetes Pod Crash Investigator

Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.

## Overview

Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator
```

### OpenClaw

```bash
clawhub install kubernetes-pod-crash-investigator
```

### Claude Code

```bash
claude mcp add kubernetes-pod-crash-investigator
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-pod-crash-investigator/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.0/5 (81 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-investigator/)
