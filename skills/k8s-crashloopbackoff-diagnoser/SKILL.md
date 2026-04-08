---
title: Kubernetes CrashLoopBackOff Diagnoser
description: 'The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause
  analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes
  API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically
  inspects container logs, exit codes, and pod events to identify the underlying failure.
  The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff
  using the Kubernetes List API with field selectors. For each affected pod, it retrieves
  the last N log lines from each container, checks for OOMKilled termination reasons
  via the container lastState.terminated.reason field, and inspects liveness and readiness
  probe configurations. The skill correlates exit codes with known failure patterns:
  exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and
  exit code 127 to missing binaries. It also checks resource requests and limits against
  node allocatable resources, validates environment variable references to ConfigMaps
  and Secrets, and verifies volume mount paths exist. Output includes a structured
  diagnosis with confidence levels and specific remediation steps.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/
category:
- Runbooks &amp; Diagnostics
framework:
- Codex
---

# Kubernetes CrashLoopBackOff Diagnoser

The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure. The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations. The skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/)
