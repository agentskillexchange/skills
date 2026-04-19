---
title: "Kubernetes CrashLoop Diagnoser"
description: "The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes. The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches. Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval."
source: "https://github.com/kubernetes/kubernetes"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnoser

The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes. The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches. Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
