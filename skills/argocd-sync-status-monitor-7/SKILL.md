---
name: "ArgoCD Sync Status Monitor"
description: "Monitors ArgoCD application sync status via the ArgoCD REST API and gRPC gateway. Detects drift between desired and live Kubernetes manifests and triggers Slack notifications through the Slack Bolt SDK."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/"
category:
  - "CI/CD Integrations"
framework:
  - "Claude Agents"
---

# ArgoCD Sync Status Monitor

The ArgoCD Sync Status Monitor provides continuous oversight of GitOps deployments managed by ArgoCD. It connects to the ArgoCD server via its REST API (v1/applications) and the gRPC gateway to fetch real-time application sync and health status.
The skill performs deep comparison between desired Git state and live Kubernetes cluster manifests, detecting configuration drift including resource count mismatches, spec changes, and missing finalizers. It uses the ArgoCD diff engine to generate human-readable summaries of what changed.
When drift or degraded health is detected, alerts route through the Slack Bolt SDK (app.message) with structured Block Kit messages showing affected resources, sync wave details, and one-click re-sync buttons via Slack interactive components. The monitor supports multi-cluster ArgoCD installations and respects RBAC project scoping. It caches application trees using Redis to minimize API calls during high-frequency polling intervals.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-status-monitor-7/)
