---
title: "Kubernetes Pod Crash Investigator"
description: "Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes API via kubectl and the official kubernetes-client/python SDK. Correlates container logs, resource limits, and node conditions for root cause analysis."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Pod Crash Investigator

Diagnoses CrashLoopBackOff and OOMKilled pod failures using the Kubernetes API via kubectl and the official kubernetes-client/python SDK. Correlates container logs, resource limits, and node conditions for root cause analysis.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-investigator-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-crash-investigator-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-investigator-3/)
