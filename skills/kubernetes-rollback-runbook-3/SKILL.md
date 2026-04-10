---
title: "Kubernetes Rollback Runbook"
description: "Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2."
slug: "kubernetes-rollback-runbook-3"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/"
listed: true
---

# Kubernetes Rollback Runbook

Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install kubernetes-rollback-runbook-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Kubernetes Rollback Runbook skill provides automated incident response procedures for failed Kubernetes deployments. It uses kubectl and the kubernetes/client-go library to interact with cluster resources, performing rollback operations with proper health verification at each step.
The runbook follows a structured sequence: first capturing the current deployment state including replica counts, resource versions, and container image tags. It then initiates a rollback using kubectl rollout undo or direct API calls to the apps/v1 Deployment endpoint, targeting either the previous revision or a specific known-good revision.
During rollback execution, the skill continuously monitors rollout status through the Deployment status conditions, checking for Available, Progressing, and ReplicaFailure conditions. It verifies pod health by inspecting container ready states and checking for CrashLoopBackOff or ImagePullBackOff events. If rollback fails or pods remain unhealthy, it escalates by creating PagerDuty incidents through the Events API v2 with detailed diagnostic context including pod logs and event timelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/)
