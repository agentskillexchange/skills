---
title: "ArgoCD Sync Drift Detector"
slug: "argocd-sync-drift-detector"
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

1. Clone this skill into your local skills directory.
2. Review the required tools and environment variables.
3. Install dependencies with your preferred package manager or runtime.
4. Run the upstream install command from the project documentation, if needed.
5. Validate the installation and test the skill in your agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)
