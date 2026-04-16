---
title: "Inspect Claude Code multi-agent runs with Agents Observe"
description: "Gives Claude Code operators a live dashboard for multi-agent sessions, tool calls, file activity, and nested task progress so debugging starts from what the agents are actually doing."
verification: "security_reviewed"
source: "https://github.com/simple10/agents-observe"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "simple10/agents-observe"
  github_stars: 421
---

# Inspect Claude Code multi-agent runs with Agents Observe

Use Agents Observe when an agent or operator needs live visibility into Claude Code activity, especially multi-agent runs, tool calls, file touches, and nested task progress. It is the right invocation when work is already happening in Claude Code and the missing step is inspection, filtering, search, and debugging, not a general observability platform.

This is skill-shaped because the scope stays narrow and repeatable: capture Claude Code hook events, stream them to a local dashboard, and help diagnose what the agents are doing right now. It is not a generic APM product, cross-team telemetry stack, or broad logging platform listing. Invoke it to observe and debug Claude Code sessions, not to monitor an entire software estate.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agents-observe-claude-code-observability/)
