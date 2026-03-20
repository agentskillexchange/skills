---
name: Kubernetes CrashLoopBackOff Diagnoser
description: Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps.
category: Runbooks & Diagnostics
framework: Codex
verification: security_reviewed
rating: 4.8
reviews: 85
source: https://agentskillexchange.com/skill/k8s-crashloopbackoff-diagnoser/
---

# Kubernetes CrashLoopBackOff Diagnoser

Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps.

## Overview

The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure.
The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations.
The skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill k8s-crashloopbackoff-diagnoser
```

### OpenClaw

```bash
openclaw install k8s-crashloopbackoff-diagnoser
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (85 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/k8s-crashloopbackoff-diagnoser/)*
