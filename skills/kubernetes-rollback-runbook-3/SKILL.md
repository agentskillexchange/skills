---
name: "Kubernetes Rollback Runbook"
description: "Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2."
category: "Runbooks &amp; Diagnostics"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/"
---
# Kubernetes Rollback Runbook

Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill kubernetes-rollback-runbook-3 -a codex
```

### OpenClaw

```bash
clawhub install kubernetes-rollback-runbook-3
```

## Details

The Kubernetes Rollback Runbook skill provides automated incident response procedures for failed Kubernetes deployments. It uses kubectl and the kubernetes/client-go library to interact with cluster resources, performing rollback operations with proper health verification at each step.

The runbook follows a structured sequence: first capturing the current deployment state including replica counts, resource versions, and container image tags. It then initiates a rollback using kubectl rollout undo or direct API calls to the apps/v1 Deployment endpoint, targeting either the previous revision or a specific known-good revision.

During rollback execution, the skill continuously monitors rollout status through the Deployment status conditions, checking for Available, Progressing, and ReplicaFailure conditions. It verifies pod health by inspecting container ready states and checking for CrashLoopBackOff or ImagePullBackOff events. If rollback fails or pods remain unhealthy, it escalates by creating PagerDuty incidents through the Events API v2 with detailed diagnostic context including pod logs and event timelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/)
