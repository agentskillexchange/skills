---
title: "Benchmark virtual agents with scripted multi-turn conversations using Agent Evaluation"
description: "Run concurrent scripted conversations against a target agent to measure whether it stays on task, responds correctly, and holds up in repeatable test cases."
verification: "listed"
source: "https://github.com/awslabs/agent-evaluation"
category:
  - "Runbooks & Diagnostics"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "awslabs/agent-evaluation"
  github_stars: 358
---

# Benchmark virtual agents with scripted multi-turn conversations using Agent Evaluation

Use Agent Evaluation when you want an evaluator agent to run scripted, multi-turn test conversations against a target agent and score the responses. The upstream project is explicit about this workflow: define cases, orchestrate conversations, evaluate results during the run, and plug the checks into CI or broader testing.

Invoke this instead of manual spot-checking or a generic hosted agent platform when the need is repeatable conversation-based benchmarking. The scope boundary is clear: Agent Evaluation tests target agents through scripted interactions. It is not a general AWS product listing or broad agent framework card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/benchmark-virtual-agents-with-scripted-multi-turn-conversations-using-agent-evaluation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/benchmark-virtual-agents-with-scripted-multi-turn-conversations-using-agent-evaluation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/benchmark-virtual-agents-with-scripted-multi-turn-conversations-using-agent-evaluation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/benchmark-virtual-agents-with-scripted-multi-turn-conversations-using-agent-evaluation/)
