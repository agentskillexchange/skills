---
title: "Kubernetes CrashLoop Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes with OOM kills, readiness probe failures, and config errors."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes CrashLoop Diagnoser

The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes.

The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches.

Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
