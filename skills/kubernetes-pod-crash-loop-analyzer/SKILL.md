---
title: Kubernetes Pod Crash Loop Analyzer
description: Diagnoses CrashLoopBackOff pods using kubectl describe, container exit
  code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals
  with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
category:
- Runbooks & Diagnostics
framework:
- Cursor
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121700
---

# Kubernetes Pod Crash Loop Analyzer

Diagnoses CrashLoopBackOff pods using kubectl describe, container exit code analysis, and the Kubernetes Events API. Cross-references OOMKilled signals with Prometheus container_memory_rss metrics and cAdvisor stats for root cause identification.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-pod-crash-loop-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-pod-crash-loop-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-crash-loop-analyzer/)
