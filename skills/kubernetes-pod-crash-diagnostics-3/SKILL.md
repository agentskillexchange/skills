---
name: Kubernetes Pod Crash Diagnostics
description: Runs kubectl describe pod, kubectl logs –previous, and kubectl get events
  to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource
  limits, and liveness probe configurations for root cause analysis.
category: Developer Tools
framework: Custom Agents
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
  tool: kubernetes
  license: Apache-2.0
  maintained: true
---
# Kubernetes Pod Crash Diagnostics
Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-diagnostics-3
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-crash-diagnostics-3` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/)
