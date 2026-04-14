---
title: "Statically scan agent repos for prompt injection and unsafe MCP configs with Agent Audit"
description: "Audit agent code, prompts, and MCP configuration for prompt-injection surfaces, taint issues, and unsafe tool exposure before shipping."
verification: listed
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/statically-scan-agent-repos-for-prompt-injection-and-unsafe-mcp-configs-with-agent-audit/)
