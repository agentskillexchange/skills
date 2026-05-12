---
title: "Kubernetes Rollback Runbook"
slug: "kubernetes-rollback-runbook-3"
description: "Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category: "Runbooks & Diagnostics"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Rollback Runbook

Executes structured Kubernetes rollback procedures using kubectl and the kubernetes/client-go library. Monitors rollout status via the apps/v1 Deployment API and triggers PagerDuty incidents through the PagerDuty Events API v2.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-rollback-runbook-3/)
