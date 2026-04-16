---
title: "Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit"
description: "Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping."
verification: "listed"
source: "https://github.com/HeadyZhang/agent-audit"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "HeadyZhang/agent-audit"
  github_stars: 149
---

# Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit

Use Agent Audit when the goal is to run a focused static security pass on an agent repository before release or deployment. This is not a generic security platform listing and not just another code scanner. The boundary is narrow and operator-shaped: inspect prompts, agent code, and MCP configs for agent-specific security failures such as prompt injection surfaces, unsafe tool exposure, and taint-style flows. That makes it a publishable security workflow rather than a plain product card.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/)
