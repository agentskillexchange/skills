---
title: "Inspect Claude Code multi-agent runs with Agents Observe"
description: "Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing."
verification: "security_reviewed"
source: "https://github.com/simple10/agents-observe"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "simple10/agents-observe"
  github_stars: 421
---

# Inspect Claude Code multi-agent runs with Agents Observe

Use Agents Observe when an agent or operator needs live visibility into Claude Code activity, especially multi-agent runs, tool calls, file touches, and nested task progress. It is the right invocation when work is already happening in Claude Code and the missing step is inspection, filtering, search, and debugging, not a general observability platform. This is skill-shaped because the scope stays narrow and repeatable: capture Claude Code hook events, stream them to a local dashboard, and help diagnose what the agents are doing right now. It is not a generic APM product, cross-team telemetry stack, or broad logging platform listing. Invoke it to observe and debug Claude Code sessions, not to monitor an entire software estate.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/agents-observe-claude-code-observability/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/agents-observe-claude-code-observability
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/agents-observe-claude-code-observability`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agents-observe-claude-code-observability/)
