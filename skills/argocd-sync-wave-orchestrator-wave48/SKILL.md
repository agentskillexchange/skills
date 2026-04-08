---
title: ArgoCD Sync Wave Orchestrator
description: 'The ArgoCD Sync Wave Orchestrator skill manages complex multi-application
  deployment sequences in ArgoCD-managed Kubernetes environments. It uses the ArgoCD
  REST API and argocd CLI to configure sync waves, define resource hooks, and coordinate
  deployment ordering across dependent applications. This skill generates proper sync-wave
  annotations (argocd.argoproj.io/sync-wave) for Kubernetes manifests to ensure resources
  are created in the correct order: namespaces and CRDs first, then configmaps and
  secrets, followed by deployments and services, and finally ingress resources and
  monitoring configurations. Key capabilities include ApplicationSet template generation
  for managing multiple environments, sync policy configuration with automated self-healing
  and pruning, and hook definition for PreSync database migrations, Sync deployment
  steps, and PostSync verification tests. The skill understands ArgoCD health assessment
  for custom resources via lua health checks. Advanced features include progressive
  delivery integration with Argo Rollouts for canary and blue-green deployment strategies,
  notification configuration via argocd-notifications for Slack and webhook alerts
  on sync failures, and multi-cluster application distribution using placement policies
  and cluster generators.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/
category:
- CI/CD Integrations
framework:
- MCP
---

# ArgoCD Sync Wave Orchestrator

The ArgoCD Sync Wave Orchestrator skill manages complex multi-application deployment sequences in ArgoCD-managed Kubernetes environments. It uses the ArgoCD REST API and argocd CLI to configure sync waves, define resource hooks, and coordinate deployment ordering across dependent applications. This skill generates proper sync-wave annotations (argocd.argoproj.io/sync-wave) for Kubernetes manifests to ensure resources are created in the correct order: namespaces and CRDs first, then configmaps and secrets, followed by deployments and services, and finally ingress resources and monitoring configurations. Key capabilities include ApplicationSet template generation for managing multiple environments, sync policy configuration with automated self-healing and pruning, and hook definition for PreSync database migrations, Sync deployment steps, and PostSync verification tests. The skill understands ArgoCD health assessment for custom resources via lua health checks. Advanced features include progressive delivery integration with Argo Rollouts for canary and blue-green deployment strategies, notification configuration via argocd-notifications for Slack and webhook alerts on sync failures, and multi-cluster application distribution using placement policies and cluster generators.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/argocd-sync-wave-orchestrator-wave48/)
