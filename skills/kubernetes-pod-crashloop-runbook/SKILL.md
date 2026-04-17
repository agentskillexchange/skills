---
name: Kubernetes Pod Crashloop Runbook
description: Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped
  via the Kubernetes API server. Fetches recent events, container logs, and resource
  quota status to identify root causes such as OOMKilled, misconfigured liveness probes,
  or missing ConfigMaps. Generates a step-by-step remediation runbook.
category: Runbooks & Diagnostics
framework: Claude Agents
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
  tool: kubernetes
  license: Apache-2.0
  maintained: true
---
# Kubernetes Pod Crashloop Runbook
Automates diagnosis of CrashLoopBackOff pods using kubectl commands wrapped via the Kubernetes API server. Fetches recent events, container logs, and resource quota status to identify root causes such as OOMKilled, misconfigured liveness probes, or missing ConfigMaps. Generates a step-by-step remediation runbook.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crashloop-runbook
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-crashloop-runbook` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crashloop-runbook/)
