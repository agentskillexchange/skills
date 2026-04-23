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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/argocd-sync-drift-detector/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/argocd-sync-drift-detector
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/argocd-sync-drift-detector`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)
