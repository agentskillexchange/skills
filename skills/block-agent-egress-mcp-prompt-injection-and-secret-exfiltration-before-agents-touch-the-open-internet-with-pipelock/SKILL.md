---
title: "Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock"
description: "Put an inline firewall and containment layer in front of agent network traffic, tool calls, and MCP traffic before you trust an agent with local secrets."
verification: "listed"
source: "https://github.com/luckyPipewrench/pipelock"
author: "luckyPipewrench"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "luckyPipewrench/pipelock"
  github_stars: 333
---

# Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock

Put an inline firewall and containment layer in front of agent network traffic, tool calls, and MCP traffic before you trust an agent with local secrets.

## Prerequisites

Homebrew or Go, terminal, supported agent runtime or IDE integration

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `brew install luckyPipewrench/tap/pipelock` or `go install github.com/luckyPipewrench/pipelock/cmd/pipelock@latest`, run `pipelock init`, then place the agent behind `pipelock sandbox` or `pipelock mcp proxy` with your policy config.
```

## Documentation

- https://pipelab.org

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/)
