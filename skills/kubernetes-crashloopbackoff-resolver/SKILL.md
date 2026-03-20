---
name: Kubernetes CrashLoopBackOff Resolver
description: Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs --previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.
category: Runbooks &amp; Diagnostics
framework: Any Agent
verification: security_reviewed
rating: 4.3
reviews: 48
source: https://agentskillexchange.com/skill/kubernetes-crashloopbackoff-resolver/
---

# Kubernetes CrashLoopBackOff Resolver

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs --previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Overview

Diagnoses CrashLoopBackOff pods using the Kubernetes API /api/v1/pods endpoint, kubectl logs --previous, and container runtime inspection via crictl. Identifies OOMKilled events, missing ConfigMaps, and image pull failures.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-crashloopbackoff-resolver
```

### OpenClaw

```bash
clawhub install kubernetes-crashloopbackoff-resolver
```

### Claude Code

```bash
claude mcp add kubernetes-crashloopbackoff-resolver
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/kubernetes-crashloopbackoff-resolver/) for detailed installation instructions.

## Verification

- **Status**: security_reviewed
- **Category**: Runbooks &amp; Diagnostics
- **Framework**: Any Agent
- **Rating**: 4.3/5 (48 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-crashloopbackoff-resolver/)
