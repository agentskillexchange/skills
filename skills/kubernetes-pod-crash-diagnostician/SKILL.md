---
name: Kubernetes Pod Crash Diagnostician
description: Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource
  quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with
  container memory profiles from Prometheus queries.
category: Runbooks & Diagnostics
framework: Claude Code
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
  tool: kubernetes
  license: Apache-2.0
  maintained: true
---
# Kubernetes Pod Crash Diagnostician
Diagnoses Kubernetes pod crash loops by analyzing events, logs, and resource quotas via the Kubernetes API and kubectl debug. Correlates OOMKill signals with container memory profiles from Prometheus queries.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-diagnostician
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-pod-crash-diagnostician` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-diagnostician/)
