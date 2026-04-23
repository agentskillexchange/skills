---
title: "Kubernetes Diagnostic Runbook"
description: "Executes diagnostic workflows against Kubernetes clusters using kubectl and the Kubernetes Python client (kubernetes.client). Checks pod health, resource quotas, event logs, and node conditions for rapid incident triage."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Diagnostic Runbook

Executes diagnostic workflows against Kubernetes clusters using kubectl and the Kubernetes Python client (kubernetes.client). Checks pod health, resource quotas, event logs, and node conditions for rapid incident triage.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-diagnostic-runbook
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-diagnostic-runbook`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-diagnostic-runbook/)
