---
name: Kubernetes CrashLoop Diagnoser
description: Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API
  /api/v1/namespaces/{ns}/pods/{pod}/log endpoint. Correlates container exit codes
  with OOM kills, readiness probe failures, and config errors.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---
# Kubernetes CrashLoop Diagnoser

The Kubernetes CrashLoop Diagnoser automates the investigation of pods stuck in CrashLoopBackOff state. Using the Kubernetes API directly and kubectl commands, it gathers container logs, event histories, resource specifications, and node conditions to determine root causes.
The agent retrieves pod logs via /api/v1/namespaces/{ns}/pods/{pod}/log with previous=true to capture crash logs, analyzes container exit codes (mapping code 137 to OOM kills, 1 to application errors, etc.), checks resource limits against actual usage from metrics-server, and inspects readiness/liveness probe configurations for mismatches.
Diagnostic capabilities include detecting missing ConfigMaps or Secrets, image pull failures, volume mount issues, init container failures, and resource quota exhaustion. The agent cross-references pod events with node conditions and cluster events to identify infrastructure-level causes. It generates actionable remediation steps and can apply common fixes like resource limit adjustments automatically with approval.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-crashloop-diagnoser-agent/)
