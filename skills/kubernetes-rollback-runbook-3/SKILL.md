---
title: "Kubernetes Rollback Runbook"
description: "Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Rollback Runbook

The Kubernetes Rollback Runbook skill provides automated incident response procedures for failed Kubernetes deployments. It uses kubectl and the kubernetes/client-go library to interact with cluster resources, performing rollback operations with proper health verification at each step.

The runbook follows a structured sequence: first capturing the current deployment state including replica counts, resource versions, and container image tags. It then initiates a rollback using kubectl rollout undo or direct API calls to the apps/v1 Deployment endpoint, targeting either the previous revision or a specific known-good revision.

During rollback execution, the skill continuously monitors rollout status through the Deployment status conditions, checking for Available, Progressing, and ReplicaFailure conditions. It verifies pod health by inspecting container ready states and checking for CrashLoopBackOff or ImagePullBackOff events. If rollback fails or pods remain unhealthy, it escalates by creating PagerDuty incidents through the Events API v2 with detailed diagnostic context including pod logs and event timelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-rollback-runbook-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-rollback-runbook-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/)
