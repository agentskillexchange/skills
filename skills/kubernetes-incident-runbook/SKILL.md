---
title: Kubernetes Incident Runbook
description: Executes structured incident response procedures for Kubernetes clusters
  using kubectl, kube-state-metrics, and the Kubernetes Events API. Automates pod
  crash diagnosis, OOMKill analysis, and node pressure triage.
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category:
- Runbooks & Diagnostics
framework:
- Claude Code
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
---

# Kubernetes Incident Runbook

Executes structured incident response procedures for Kubernetes clusters using kubectl, kube-state-metrics, and the Kubernetes Events API. Automates pod crash diagnosis, OOMKill analysis, and node pressure triage.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-incident-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-incident-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-incident-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-incident-runbook/)
