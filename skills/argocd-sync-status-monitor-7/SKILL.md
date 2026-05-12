---
title: "ArgoCD Sync Status Monitor"
slug: "argocd-sync-status-monitor-7"
description: "Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-cd"
category: "CI/CD Integrations"
framework: "Claude Agents"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Sync Status Monitor

Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/)
