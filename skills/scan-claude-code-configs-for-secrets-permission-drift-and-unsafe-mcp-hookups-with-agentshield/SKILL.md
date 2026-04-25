---
title: "Scan Claude Code configs for secrets permission drift and unsafe MCP hookups with AgentShield"
description: "Audit a Claude Code setup before use by flagging hardcoded secrets, broad allow rules, risky hooks, and dangerous MCP server config."
verification: "listed"
source: "https://github.com/affaan-m/agentshield"
category:
  - "Security & Verification"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "affaan-m/agentshield"
  github_stars: 388
---

# Scan Claude Code configs for secrets permission drift and unsafe MCP hookups with AgentShield

Use AgentShield when an operator needs a preflight security audit of a Claude Code setup, not when they are simply using Claude Code normally. The invoke moment is concrete: scan a .claude directory before enabling a workflow, merging config changes, or trusting a new MCP connection. That scope boundary, static security review of Claude Code configuration, permissions, hooks, and MCP server exposure, keeps this distinct from a generic agent platform or broad security product listing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield/)
