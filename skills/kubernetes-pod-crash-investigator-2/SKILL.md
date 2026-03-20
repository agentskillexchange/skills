---
name: Kubernetes Pod Crash Investigator
description: Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remedia
category: Runbooks & Diagnostics
framework: Codex
verification: verified_metadata
rating: 4.9
reviews: 68
source: https://agentskillexchange.com/skill/kubernetes-pod-crash-investigator-2/
---

# Kubernetes Pod Crash Investigator

Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.

## Overview

Identifies CrashLoopBackOff and OOMKilled pods in a Kubernetes namespace, retrieves logs from crashed containers, inspects events and resource limits, and produces a root cause hypothesis with remediation steps. Works with kubectl or the Kubernetes API.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill kubernetes-pod-crash-investigator-2
```

### OpenClaw

```bash
openclaw install kubernetes-pod-crash-investigator-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | Codex |
| Verification | Verified Metadata |
| Rating | ⭐⭐⭐⭐ 4.9/5.0 (68 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/kubernetes-pod-crash-investigator-2/)*
