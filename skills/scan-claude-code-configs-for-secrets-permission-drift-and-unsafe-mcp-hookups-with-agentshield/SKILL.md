---
name: "Scan Claude Code configs for secrets permission drift and unsafe MCP hookups with AgentShield"
slug: "scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield"
description: "Audit a Claude Code setup before use by flagging hardcoded secrets, broad allow rules, risky hooks, and dangerous MCP server config."
github_stars: 388
verification: "security_reviewed"
source: "https://github.com/affaan-m/agentshield"
author: "affaan-m"
publisher_type: "individual"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "affaan-m/agentshield"
  github_stars: 388
---

# Scan Claude Code configs for secrets permission drift and unsafe MCP hookups with AgentShield

Audit a Claude Code setup before use by flagging hardcoded secrets, broad allow rules, risky hooks, and dangerous MCP server config.

## Prerequisites

Claude Code configuration directory, AgentShield CLI or npx path, local shell access, optional CI environment for GitHub Action usage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Run AgentShield with the no-install npx flow or install the documented package globally, then scan the target Claude Code configuration directory and review or apply the reported fixes.
```

## Documentation

- https://github.com/affaan-m/agentshield

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield/)
