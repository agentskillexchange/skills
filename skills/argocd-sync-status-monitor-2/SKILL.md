---
name: ArgoCD Sync Status Monitor
description: Polls ArgoCD application sync status, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git source-of-truth.
category: CI/CD Integrations
framework: OpenClaw
verification: security_reviewed
rating: 4.8
reviews: 86
source: https://agentskillexchange.com/skill/argocd-sync-status-monitor-2/
---

# ArgoCD Sync Status Monitor

Polls ArgoCD application sync status, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git source-of-truth.

## Overview

Polls ArgoCD application sync status, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git source-of-truth.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor-2
```

### OpenClaw

```bash
openclaw install argocd-sync-status-monitor-2
```

### Manual

Download this `SKILL.md` file and place it in your agent's skills directory.

## Metadata

| Field | Value |
|-------|-------|
| Category | CI/CD Integrations |
| Framework | OpenClaw |
| Verification | Security Reviewed |
| Rating | ⭐⭐⭐⭐ 4.8/5.0 (86 reviews) |

---

*Published on [Agent Skill Exchange](https://agentskillexchange.com/skill/argocd-sync-status-monitor-2/)*
