---
title: Kubernetes Crashloop Diagnostic Runbook
description: Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl
  and the Kubernetes API. Fetches pod events, container logs, and resource limits
  via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause
  analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image
  pull errors.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/
category:
- Runbooks & Diagnostics
framework:
- OpenClaw
---


# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
