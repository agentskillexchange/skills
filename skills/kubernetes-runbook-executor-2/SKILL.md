---
title: "Kubernetes Runbook Executor"
description: "Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks & Diagnostics"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
---

# Kubernetes Runbook Executor

Executes diagnostic runbooks against Kubernetes clusters using the official kubernetes/client-go SDK and kubectl commands. Checks pod health via the /healthz and /readyz endpoints and analyzes events with the CoreV1 Events API.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-runbook-executor-2
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-runbook-executor-2`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-runbook-executor-2/)
