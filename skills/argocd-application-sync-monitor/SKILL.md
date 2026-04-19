---
title: "ArgoCD Application Sync Monitor"
description: "The ArgoCD Application Sync Monitor skill provides continuous monitoring of GitOps application deployments managed by ArgoCD. It connects to the ArgoCD server via its REST API to query application sync status, health state, and resource details across multiple clusters. The skill polls application endpoints to detect OutOfSync conditions where the desired state in Git diverges from the live cluster state. When drift is detected, it uses argocd app diff to generate detailed resource-level comparisons showing exactly which Kubernetes manifests have changed, including annotation, label, and spec differences. Sync wave monitoring tracks multi-phase deployments where resources are applied in ordered waves using the argocd.argoproj.io/sync-wave annotation. The skill reports progress through each wave, identifies stuck resources that prevent wave advancement, and detects sync hook failures (PreSync, Sync, PostSync, SyncFail). Alerting integrates with Slack via incoming webhooks and email via SMTP. Alert payloads include the application name, sync status, health status, affected resources with their GVK (Group/Version/Kind), and direct links to the ArgoCD UI for investigation. The skill supports configurable alert thresholds to avoid notification fatigue during planned rollouts."
source: "https://github.com/argoproj/argo-cd"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Application Sync Monitor

The ArgoCD Application Sync Monitor skill provides continuous monitoring of GitOps application deployments managed by ArgoCD. It connects to the ArgoCD server via its REST API to query application sync status, health state, and resource details across multiple clusters. The skill polls application endpoints to detect OutOfSync conditions where the desired state in Git diverges from the live cluster state. When drift is detected, it uses argocd app diff to generate detailed resource-level comparisons showing exactly which Kubernetes manifests have changed, including annotation, label, and spec differences. Sync wave monitoring tracks multi-phase deployments where resources are applied in ordered waves using the argocd.argoproj.io/sync-wave annotation. The skill reports progress through each wave, identifies stuck resources that prevent wave advancement, and detects sync hook failures (PreSync, Sync, PostSync, SyncFail). Alerting integrates with Slack via incoming webhooks and email via SMTP. Alert payloads include the application name, sync status, health status, affected resources with their GVK (Group/Version/Kind), and direct links to the ArgoCD UI for investigation. The skill supports configurable alert thresholds to avoid notification fatigue during planned rollouts.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-application-sync-monitor/)
