---
title: "Kubernetes Crashloop Diagnostic Runbook"
description: "Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors."
slug: "kubernetes-crashloop-diagnostic-runbook"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
---

# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

You can install this skill in any of these ways:

1. Install from Agent Skill Exchange in the OpenClaw UI
2. Clone or copy the skill folder into your local skills directory
3. Add it to your workspace-managed skills collection
4. Install via any compatible skill package manager or sync workflow
5. Copy the `SKILL.md` and any referenced files into a compatible AgentSkills directory

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
