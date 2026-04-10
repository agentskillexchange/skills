---
name: "ArgoCD Sync Orchestrator"
description: "Manages ArgoCD application syncs using the argocd CLI and the Argo CD REST API (v1alpha1). Supports progressive delivery with Argo Rollouts integration and automated health checks via Kubernetes readiness probes."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/argocd-sync-orchestrator/"
category:
  - "CI/CD Integrations"
framework:
  - "ChatGPT Agents"
---

# ArgoCD Sync Orchestrator

The ArgoCD Sync Orchestrator skill automates GitOps deployment workflows through the Argo CD platform. It uses the argocd CLI and REST API (v1alpha1) to manage application synchronization, health monitoring, and rollback operations.
The skill implements progressive delivery patterns by integrating with Argo Rollouts for canary and blue-green deployment strategies. It monitors Kubernetes readiness and liveness probes to verify deployment health before promoting new versions.
Key capabilities include multi-cluster sync coordination, automatic drift detection and remediation, and integration with notification services like Slack and PagerDuty for deployment status updates. The skill supports Kustomize and Helm chart rendering, manages application sets for multi-tenant environments, and handles sync waves and hooks for complex deployment ordering.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-orchestrator/)
