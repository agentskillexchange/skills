---
title: "Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit"
description: "Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping."
verification: "listed"
source: "https://github.com/HeadyZhang/agent-audit"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "HeadyZhang/agent-audit"
  github_stars: 149
---

# Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit

Use Agent Audit when the goal is to run a focused static security pass on an agent repository before release or deployment. This is not a generic security platform listing and not just another code scanner. The boundary is narrow and operator-shaped: inspect prompts, agent code, and MCP configs for agent-specific security failures such as prompt injection surfaces, unsafe tool exposure, and taint-style flows. That makes it a publishable security workflow rather than a plain product card.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/)
