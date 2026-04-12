---
title: "Kubernetes Pod Crashloop Runbook"
description: "Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/"
categories:
  - "Runbooks &amp; Diagnostics"
frameworks:
  - "Claude Agents"
---

# Kubernetes Pod Crashloop Runbook

Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Installation

You can install this skill using one of these methods:

1. Install from Agent Skill Exchange in OpenClaw
2. Install from ClawHub
3. Copy the skill folder into your local skills directory
4. Add it as a git submodule or synced folder in your workspace
5. Use your team or org skill distribution workflow

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
