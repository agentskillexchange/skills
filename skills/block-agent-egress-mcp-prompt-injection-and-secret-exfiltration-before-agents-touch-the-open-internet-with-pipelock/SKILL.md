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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/block-agent-egress-mcp-prompt-injection-and-secret-exfiltration-before-agents-touch-the-open-internet-with-pipelock/)
