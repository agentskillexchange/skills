---
title: "Kubernetes Crashloop Diagnostic Runbook"
slug: "kubernetes-crashloop-diagnostic-runbook"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "OpenClaw"
---
# Kubernetes Crashloop Diagnostic Runbook

Diagnoses CrashLoopBackOff pods in Kubernetes clusters using kubectl and the Kubernetes API. Fetches pod events, container logs, and resource limits via the /api/v1/namespaces/{ns}/pods/{name}/log endpoint. Provides structured root-cause analysis covering OOMKilled, missing ConfigMaps, failed liveness probes, and image pull errors.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnostic-runbook/)
