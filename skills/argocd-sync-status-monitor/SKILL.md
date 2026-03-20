---
name: ArgoCD Sync Status Monitor
description: Polls ArgoCD application sync status via its REST API, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git and outputs a diff-style summary for GitOps teams.
category: CI/CD Integrations
framework: Any Agent
verification: listed
rating: 4.6
reviews: 57
source: https://agentskillexchange.com/skill/argocd-sync-status-monitor/
---

# ArgoCD Sync Status Monitor

Polls ArgoCD application sync status via its REST API, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git and outputs a diff-style summary for GitOps teams.

## Overview

Polls ArgoCD application sync status via its REST API, detects OutOfSync and Degraded states, and reports which Kubernetes resources drifted and why. Compares live cluster state against Git and outputs a diff-style summary for GitOps teams.

## Installation

### Using npx skills (any agent)

```bash
npx skills add agentskillexchange/skills --skill argocd-sync-status-monitor
```

### OpenClaw

```bash
clawhub install argocd-sync-status-monitor
```

### Claude Code

```bash
claude mcp add argocd-sync-status-monitor
```

### Manual

Visit the [skill page](https://agentskillexchange.com/skill/argocd-sync-status-monitor/) for detailed installation instructions.

## Verification

- **Status**: listed
- **Category**: CI/CD Integrations
- **Framework**: Any Agent
- **Rating**: 4.6/5 (57 reviews)

## Source

[View on Agent Skill Exchange](https://agentskillexchange.com/skill/argocd-sync-status-monitor/)
