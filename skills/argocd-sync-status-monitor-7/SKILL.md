---
title: "ArgoCD Sync Status Monitor"
description: "Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
  license: "Apache-2.0"
---

# ArgoCD Sync Status Monitor

Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-sync-status-monitor-7
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-sync-status-monitor-7`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/)
