---
title: "Inspect Claude Code multi-agent runs with Agents Observe"
description: "Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing."
verification: "security_reviewed"
source: "https://github.com/simple10/agents-observe"
author: "Joe Johnston"
publisher_type: "individual"
category:
  - "Monitoring & Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "simple10/agents-observe"
  github_stars: 421
---

# Inspect Claude Code multi-agent runs with Agents Observe

Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing.

## Prerequisites

Claude Code, Docker, Node.js, and a local browser. The plugin runs a local server/container and captures Claude Code hook events for dashboard inspection.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Add the repository as a Claude Code plugin marketplace with claude plugin marketplace add simple10/agents-observe, install it with claude plugin install agents-observe, then start claude. The plugin auto-starts its local server and event capture. Open http://localhost:4981 to view the dashboard. Docker and Node.js must already be installed on the host.
```

## Documentation

- https://github.com/simple10/agents-observe#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agents-observe-claude-code-observability/)
