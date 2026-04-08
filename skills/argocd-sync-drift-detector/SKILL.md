---
title: "ArgoCD Sync Drift Detector"
slug: "argocd-sync-drift-detector"
verification: "security_reviewed"
description: "Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff."
category:
  - "CI/CD Integrations"
framework:
  - "OpenClaw"
source: "https://agentskillexchange.com/skills/argocd-sync-drift-detector/"
---

# ArgoCD Sync Drift Detector

Monitors ArgoCD applications for configuration drift using the ArgoCD REST API and grpc-gateway. Compares live Kubernetes manifests against Git-declared state and generates remediation playbooks via kubectl diff.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your local skills workspace.
2. Install it with ClawHub if it is available there.
3. Copy the folder into your OpenClaw or AgentSkills directory manually.
4. Add it as a git submodule if you manage skills as pinned dependencies.
5. Vendor it directly into a project repo when you need a fixed internal copy.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-drift-detector/)
