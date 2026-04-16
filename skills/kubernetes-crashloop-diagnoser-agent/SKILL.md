---
title: "Kubernetes CrashLoop Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
verification: "security_reviewed"
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes CrashLoop Diagnoser

The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes.


The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches.


Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
