---
title: "Validate, dry-run, and expose YAML agent runbooks as MCP tools with DeclarAgent"
description: "Use DeclarAgent when an agent should follow a predefined multi-step runbook but you want the plan checked before anything real happens. It validates the YAML plan, explains or dry-runs the steps, blocks destructive actions unless approval is given, and can expose approved plans as MCP-callable tools for agent loops. The scope boundary is clear: guarded runbook execution and MCP plan exposure, not a generic agent framework or broad workflow platform listing."
source: "https://github.com/shiehn/DeclarAgent"
verification: "listed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "shiehn/DeclarAgent"
  github_stars: 11
---

# Validate, dry-run, and expose YAML agent runbooks as MCP tools with DeclarAgent

Use DeclarAgent when an agent should follow a predefined multi-step runbook but you want the plan checked before anything real happens. It validates the YAML plan, explains or dry-runs the steps, blocks destructive actions unless approval is given, and can expose approved plans as MCP-callable tools for agent loops. The scope boundary is clear: guarded runbook execution and MCP plan exposure, not a generic agent framework or broad workflow platform listing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/validate-dry-run-and-expose-yaml-agent-runbooks-as-mcp-tools-with-declaragent/)
