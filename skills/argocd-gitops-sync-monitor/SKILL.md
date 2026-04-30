---
title: "ArgoCD GitOps Sync Monitor"
description: "Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API."
verification: "security_reviewed"
source: "https://github.com/argoproj/argo-cd"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD GitOps Sync Monitor

Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/)
