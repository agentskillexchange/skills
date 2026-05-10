---
title: "Gate risky agent actions behind approval checkpoints with Latch"
slug: "gate-risky-agent-actions-behind-approval-checkpoints-with-latch"
description: "Use Latch to put an MCP policy and approval layer between agents and tools so risky calls pause for review while safe calls continue automatically."
github_stars: 8
verification: "security_reviewed"
source: "https://github.com/latchagent/latch"
author: "Latch"
publisher_type: "organization"
category: "Security & Verification"
framework: "MCP"
tool_ecosystem:
  github_repo: "latchagent/latch"
  github_stars: 8
---

# Gate risky agent actions behind approval checkpoints with Latch

Use Latch to put an MCP policy and approval layer between agents and tools so risky calls pause for review while safe calls continue automatically.

## Prerequisites

Docker, Latch CLI, an upstream MCP server to wrap

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Clone the repository and start Latch with docker compose, create an account and API key, then run the Latch CLI in front of an upstream MCP server using the documented --upstream and --upstream-command flags.
```

## Documentation

- https://latch.mintlify.app/docs/introduction

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch/)
