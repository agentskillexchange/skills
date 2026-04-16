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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-claude-code-configs-for-secrets-permission-drift-and-unsafe-mcp-hookups-with-agentshield/)
