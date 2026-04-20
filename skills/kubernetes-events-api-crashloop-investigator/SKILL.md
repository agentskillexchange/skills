---
title: "Kubernetes Events API CrashLoop Investigator"
description: "Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand."
verification: security_reviewed
source: "https://github.com/kubernetes/kubernetes"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "kubernetes/kubernetes"
  github_stars: 121439
---

# Kubernetes Events API CrashLoop Investigator

Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-events-api-crashloop-investigator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/kubernetes-events-api-crashloop-investigator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
