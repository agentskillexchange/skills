---
title: "Kubernetes CrashLoopBackOff Diagnoser"
description: "Diagnoses CrashLoopBackOff pods using kubectl and the Kubernetes API. Inspects container logs, exit codes, OOMKilled events, and liveness probe configurations to generate actionable remediation steps."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
---

# Kubernetes CrashLoopBackOff Diagnoser

The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure.

The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations.

The skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/)
