---
title: "Kubernetes CrashLoopBackOff Diagnoser"
description: "The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure.\nThe diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations.\nThe skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/"
framework:
  - "Codex"
---

# Kubernetes CrashLoopBackOff Diagnoser

The Kubernetes CrashLoopBackOff Diagnoser skill automates root cause analysis for pods stuck in CrashLoopBackOff state. Using kubectl and direct Kubernetes API calls to the /api/v1/namespaces/{ns}/pods/{pod}/log endpoint, it systematically inspects container logs, exit codes, and pod events to identify the underlying failure.
The diagnosis workflow begins by listing all pods with status.containerStatuses[].state.waiting.reason=CrashLoopBackOff using the Kubernetes List API with field selectors. For each affected pod, it retrieves the last N log lines from each container, checks for OOMKilled termination reasons via the container lastState.terminated.reason field, and inspects liveness and readiness probe configurations.
The skill correlates exit codes with known failure patterns: exit code 137 maps to OOMKilled or SIGKILL, exit code 1 to application errors, and exit code 127 to missing binaries. It also checks resource requests and limits against node allocatable resources, validates environment variable references to ConfigMaps and Secrets, and verifies volume mount paths exist. Output includes a structured diagnosis with confidence levels and specific remediation steps.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/k8s-crashloopbackoff-diagnoser
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/k8s-crashloopbackoff-diagnoser` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/k8s-crashloopbackoff-diagnoser/)
