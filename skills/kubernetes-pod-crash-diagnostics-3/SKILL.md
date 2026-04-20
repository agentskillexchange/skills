---
title: "Kubernetes Pod Crash Diagnostics"
description: "Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Developer Tools"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Diagnostics

Runs kubectl describe pod, kubectl logs –previous, and kubectl get events to diagnose CrashLoopBackOff and OOMKilled pods. Parses container exit codes, resource limits, and liveness probe configurations for root cause analysis.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-diagnostics-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-crash-diagnostics-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostics-3/)
