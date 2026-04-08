---
title: Kubernetes Rollback Runbook
description: 'The Kubernetes Rollback Runbook skill provides automated incident response
  procedures for failed Kubernetes deployments. It uses kubectl and the kubernetes/client-go
  library to interact with cluster resources, performing rollback operations with
  proper health verification at each step. The runbook follows a structured sequence:
  first capturing the current deployment state including replica counts, resource
  versions, and container image tags. It then initiates a rollback using kubectl rollout
  undo or direct API calls to the apps/v1 Deployment endpoint, targeting either the
  previous revision or a specific known-good revision. During rollback execution,
  the skill continuously monitors rollout status through the Deployment status conditions,
  checking for Available, Progressing, and ReplicaFailure conditions. It verifies
  pod health by inspecting container ready states and checking for CrashLoopBackOff
  or ImagePullBackOff events. If rollback fails or pods remain unhealthy, it escalates
  by creating PagerDuty incidents through the Events API v2 with detailed diagnostic
  context including pod logs and event timelines.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/
category:
- Runbooks &amp; Diagnostics
framework:
- OpenClaw
---

# Kubernetes Rollback Runbook

The Kubernetes Rollback Runbook skill provides automated incident response procedures for failed Kubernetes deployments. It uses kubectl and the kubernetes/client-go library to interact with cluster resources, performing rollback operations with proper health verification at each step. The runbook follows a structured sequence: first capturing the current deployment state including replica counts, resource versions, and container image tags. It then initiates a rollback using kubectl rollout undo or direct API calls to the apps/v1 Deployment endpoint, targeting either the previous revision or a specific known-good revision. During rollback execution, the skill continuously monitors rollout status through the Deployment status conditions, checking for Available, Progressing, and ReplicaFailure conditions. It verifies pod health by inspecting container ready states and checking for CrashLoopBackOff or ImagePullBackOff events. If rollback fails or pods remain unhealthy, it escalates by creating PagerDuty incidents through the Events API v2 with detailed diagnostic context including pod logs and event timelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/)
