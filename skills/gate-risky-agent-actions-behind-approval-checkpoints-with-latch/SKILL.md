---
name: "Gate risky agent actions behind approval checkpoints with Latch"
slug: "gate-risky-agent-actions-behind-approval-checkpoints-with-latch"
description: "Use Latch to put an MCP policy and approval layer between agents and tools so risky calls pause for review while safe calls continue automatically."
github_stars: 8
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/latchagent/latch
- docker compose up -d
- npx @latchagent/cli@latest run \

Requirements and caveats from upstream:
- **Risky actions** (shell commands, external sends) → Require human approval
- # Start Latch with Docker
- Policy is evaluated (allow / deny / require approval)

Basic usage or getting-started notes:
- Security guardrails for AI agents. Safe actions run automatically. Risky actions wait for approval.
- bash
- cd latch

- Source: https://github.com/latchagent/latch
- Extracted from upstream docs: https://raw.githubusercontent.com/latchagent/latch/HEAD/README.md

## Documentation

- https://latch.mintlify.app/docs/introduction

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/gate-risky-agent-actions-behind-approval-checkpoints-with-latch/)
