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
---

# Kubernetes Event Stream Analyzer

Watches Kubernetes event streams via the Watch API and correlates pod lifecycle events with resource metrics from Metrics Server. Detects CrashLoopBackOff patterns and OOMKilled signals for automated triage.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-event-stream-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-event-stream-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-event-stream-analyzer/)
