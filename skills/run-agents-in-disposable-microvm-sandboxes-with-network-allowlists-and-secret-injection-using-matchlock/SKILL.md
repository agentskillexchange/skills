---
title: "Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock"
description: "Use Matchlock when an agent must run code, install packages, and touch external APIs, but you do not want it operating directly on the host. The workflow is explicit: install Matchlock, verify host support, declare allowed hosts and secret mappings, run the agent inside a disposable microVM, and tear the environment down when the task is done.\nThe skill boundary is concrete and narrower than a generic VM or sandbox product listing. This is about microVM-based agent execution with network allowlisting and in-flight secret injection, not general virtualization, not a broad agent framework, and not a generic container runtime card."
verification: listed
source: "https://github.com/jingkaihe/matchlock"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jingkaihe/matchlock"
  github_stars: 552
---

# Run agents in disposable microVM sandboxes with network allowlists and secret injection using Matchlock

Use Matchlock when an agent must run code, install packages, and touch external APIs, but you do not want it operating directly on the host. The workflow is explicit: install Matchlock, verify host support, declare allowed hosts and secret mappings, run the agent inside a disposable microVM, and tear the environment down when the task is done.
The skill boundary is concrete and narrower than a generic VM or sandbox product listing. This is about microVM-based agent execution with network allowlisting and in-flight secret injection, not general virtualization, not a broad agent framework, and not a generic container runtime card.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-agents-in-disposable-microvm-sandboxes-with-network-allowlists-and-secret-injection-using-matchlock/)
