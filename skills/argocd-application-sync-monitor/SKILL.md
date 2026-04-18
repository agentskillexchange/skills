---
title: "ArgoCD Application Sync Monitor"
description: "Monitors ArgoCD application sync status via the ArgoCD REST API and argocd CLI. Detects OutOfSync conditions, tracks sync wave progress, and alerts on failed sync operations with detailed resource diff analysis using argocd app diff."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Application Sync Monitor

The ArgoCD Application Sync Monitor skill provides continuous monitoring of GitOps application deployments managed by ArgoCD. It connects to the ArgoCD server via its REST API to query application sync status, health state, and resource details across multiple clusters.

The skill polls application endpoints to detect OutOfSync conditions where the desired state in Git diverges from the live cluster state. When drift is detected, it uses argocd app diff to generate detailed resource-level comparisons showing exactly which Kubernetes manifests have changed, including annotation, label, and spec differences.

Sync wave monitoring tracks multi-phase deployments where resources are applied in ordered waves using the argocd.argoproj.io/sync-wave annotation. The skill reports progress through each wave, identifies stuck resources that prevent wave advancement, and detects sync hook failures (PreSync, Sync, PostSync, SyncFail).

Alerting integrates with Slack via incoming webhooks and email via SMTP. Alert payloads include the application name, sync status, health status, affected resources with their GVK (Group/Version/Kind), and direct links to the ArgoCD UI for investigation. The skill supports configurable alert thresholds to avoid notification fatigue during planned rollouts.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-application-sync-monitor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/argocd-application-sync-monitor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-sync-monitor/)
