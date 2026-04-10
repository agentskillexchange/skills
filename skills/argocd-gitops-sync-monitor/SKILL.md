---
name: "ArgoCD GitOps Sync Monitor"
description: "Monitors ArgoCD application sync status using the ArgoCD REST API /api/v1/applications endpoint. Detects drift between Git manifests and live Kubernetes cluster state via the Kubernetes API."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/"
category:
  - "CI/CD Integrations"
framework:
  - "Gemini"
---

# ArgoCD GitOps Sync Monitor

The ArgoCD GitOps Sync Monitor provides real-time monitoring of ArgoCD application synchronization status across Kubernetes clusters. It connects to the ArgoCD REST API /api/v1/applications endpoint to poll sync states, health statuses, and revision histories. The skill detects configuration drift by comparing Git repository manifests against live cluster state via the Kubernetes API, identifying out-of-sync resources and unauthorized manual changes. It supports multi-cluster setups through the ArgoCD cluster API, monitoring applications across development, staging, and production environments. Automated alerting triggers notifications for sync failures, degraded health conditions, and resource hook failures. The monitor integrates with the ArgoCD ApplicationSet API to validate generator configurations and template rendering. It generates drift reports showing exact resource differences using structured diff comparisons, and provides one-click sync triggers through the ArgoCD sync API with configurable prune and force options.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-gitops-sync-monitor/)
