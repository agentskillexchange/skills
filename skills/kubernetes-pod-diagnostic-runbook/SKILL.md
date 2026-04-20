---
title: "Kubernetes Pod Diagnostic Runbook"
description: "Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Diagnostic Runbook

Automated K8s pod troubleshooting using kubectl, crictl, and the Kubernetes API. Runs diagnostic sequences for CrashLoopBackOff, ImagePullBackOff, OOMKilled, and pending pod states.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-diagnostic-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-diagnostic-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-runbook/)
