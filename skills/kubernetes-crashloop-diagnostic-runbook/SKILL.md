---
name: Kubernetes Crashloop Diagnostic Runbook
description: Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.5
reviews: 59
source: https://agentskillexchange.com/skill/kubernetes-crashloop-diagnostic-runbook/
---

# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Overview

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloop-diagnostic-runbook
```

### OpenClaw

```bash
clawhub install kubernetes-crashloop-diagnostic-runbook
```

### Claude Code

```bash
claude mcp add kubernetes-crashloop-diagnostic-runbook
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-crashloop-diagnostic-runbook/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.5/5 (59 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-crashloop-diagnostic-runbook/)
