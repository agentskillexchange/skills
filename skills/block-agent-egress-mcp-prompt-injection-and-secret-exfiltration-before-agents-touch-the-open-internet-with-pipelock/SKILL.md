---
title: "Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock"
description: "Use Pipelock when the problem is not just running an agent, but safely containing what that agent can send, fetch, and execute once it has credentials or shell access. It sits at the boundary between the agent and the outside world, scans outbound and inbound traffic, wraps MCP servers, and enforces pre-execution policy before risky actions land. The scope boundary is clear: this is an operator workflow for guarding live agent egress and tool use, not a generic security product card or broad SDK listing."
source: "https://github.com/luckyPipewrench/pipelock"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "luckyPipewrench/pipelock"
  github_stars: 333
---

# Block agent egress, MCP prompt injection, and secret exfiltration before agents touch the open internet with Pipelock

Use Pipelock when the problem is not just running an agent, but safely containing what that agent can send, fetch, and execute once it has credentials or shell access. It sits at the boundary between the agent and the outside world, scans outbound and inbound traffic, wraps MCP servers, and enforces pre-execution policy before risky actions land. The scope boundary is clear: this is an operator workflow for guarding live agent egress and tool use, not a generic security product card or broad SDK listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/)
