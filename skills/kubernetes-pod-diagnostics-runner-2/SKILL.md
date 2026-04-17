---
title: "Kubernetes Pod Diagnostics Runner"
description: "Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostics Runner

Runs automated diagnostic sequences on Kubernetes pods using kubectl exec, kubectl logs, and the Kubernetes API /api/v1/pods endpoint. Captures OOMKilled events, CrashLoopBackOff analysis, and resource utilization via metrics-server.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-diagnostics-runner-2
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-diagnostics-runner-2` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runner-2/)
