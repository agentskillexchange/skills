---
title: "Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock"
description: "Put an inline firewall and containment layer in front of agent network traffic, tool calls, and MCP traffic before you trust an agent with local secrets."
verification: "listed"
source: "https://github.com/luckyPipewrench/pipelock"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "luckyPipewrench/pipelock"
  github_stars: 333
---

# Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock

Use Pipelock when the problem is not just running an agent, but safely containing what that agent can send, fetch, and execute once it has credentials or shell access. It sits at the boundary between the agent and the outside world, scans outbound and inbound traffic, wraps MCP servers, and enforces pre-execution policy before risky actions land. The scope boundary is clear: this is an operator workflow for guarding live agent egress and tool use, not a generic security product card or broad SDK listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/)
