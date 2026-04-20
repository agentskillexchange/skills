---
title: "ArgoCD Sync Drift Detector"
description: "Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff."
verification: security_reviewed
source: "https://github.com/argoproj/argo-cd"
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "argoproj/argo-cd"
  github_stars: 22593
---

# ArgoCD Sync Drift Detector

Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)
