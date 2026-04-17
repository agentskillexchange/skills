---
name: Kubernetes Events API CrashLoop Investigator
description: Diagnoses restart storms with the Kubernetes Events API, Pod status conditions,
  and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great
  for agents that need to summarize cluster evidence before an operator starts digging
  through kubectl output by hand.
category: Runbooks & Diagnostics
framework: MCP
verification: security_reviewed
source: https://github.com/kubernetes/kubernetes
tool_ecosystem:
  github_repo: kubernetes/kubernetes
  github_stars: 121439
  tool: kubernetes
---
# Kubernetes Events API CrashLoop Investigator
Diagnoses restart storms with the Kubernetes Events API, Pod status conditions, and the Metrics API to explain why workloads are stuck in CrashLoopBackOff. Great for agents that need to summarize cluster evidence before an operator starts digging through kubectl output by hand.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/kubernetes-events-api-crashloop-investigator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/kubernetes-events-api-crashloop-investigator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-events-api-crashloop-investigator/)
