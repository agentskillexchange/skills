---
title: Kubernetes Pod Diagnostics Runbook
description: Automates Kubernetes troubleshooting using kubectl and the Kubernetes
  Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states.
  Collects pod logs, events, node conditions, and resource quotas systematically.
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category:
- Runbooks & Diagnostics
framework:
- OpenClaw
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
---

# Kubernetes Pod Diagnostics Runbook

Automates Kubernetes troubleshooting using kubectl and the Kubernetes Python client to diagnose CrashLoopBackOff, OOMKilled, and ImagePullBackOff states. Collects pod logs, events, node conditions, and resource quotas systematically.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-diagnostics-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-diagnostics-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostics-runbook/)
