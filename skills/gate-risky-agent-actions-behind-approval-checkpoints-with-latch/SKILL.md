---
title: "Gate risky agent actions behind approval checkpoints with Latch"
description: "Use Latch to put an MCP policy and approval layer between agents and tools so risky calls pause for review while safe calls continue automatically."
verification: "security_reviewed"
source: "https://github.com/latchagent/latch"
category:
  - "Security & Verification"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "latchagent/latch"
  github_stars: 8
---

# Gate risky agent actions behind approval checkpoints with Latch

Use Latch when an agent already has MCP tool access and you need a concrete control point that classifies actions as allowed, approval-required, or denied before the upstream tool call executes. The upstream project is explicit here: Latch is an MCP proxy with a policy engine, approval workflow, audit log, and action classes such as READ, EXECUTE, SEND, and TRANSFER_VALUE.

Invoke this instead of using the product normally when the real task is not “run an MCP server” but “wrap an MCP server with review gates for risky actions”. The operator workflow is specific: launch Latch, point it at an upstream MCP server, define policy, inspect blocked or approval-bound actions, then resume or deny the exact tool call.

The scope boundary is clear and prevents this from being a plain product card. This is not publishing Latch as a generic platform or dashboard. It is the narrowly bounded skill of enforcing human approval checkpoints and policy decisions on MCP-mediated agent actions.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch/)
