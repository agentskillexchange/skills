---
title: "Kubernetes Event Stream Analyzer"
description: "Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Monitoring & Alerts"
framework:
  - "Gemini"
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121700
  license: "Apache-2.0"
---

# Kubernetes Event Stream Analyzer

Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-event-stream-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-event-stream-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/)
