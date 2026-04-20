---
title: Kubernetes Pod Crashloop Runbook
description: Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped
  via the Kubernetes API server. Fetches recent events, container logs, and resource
  quota status to identify root causes such as OOMKilled, misconfigured liveness probes,
  or missing ConfigMaps. Generates a step-by-step remediation runbook.
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category:
- Runbooks &amp; Diagnostics
framework:
- Claude Agents
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
---

# Kubernetes Pod Crashloop Runbook

Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
