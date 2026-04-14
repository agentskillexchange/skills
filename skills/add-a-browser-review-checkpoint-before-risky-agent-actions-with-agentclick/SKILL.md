---
title: "Add a browser review checkpoint before risky agent actions with AgentClick"
description: "Use AgentClick when an agent should pause before risky commands, plans, drafts, or code changes so a human can inspect, edit, approve, or reject them in a purpose-built browser UI."
verification: listed
source: "https://github.com/agentlayer-io/AgentClick"
category:
  - "Code Quality &amp; Review"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "agentlayer-io/agentclick"
  github_stars: 22
  npm_package: "@harvenstar/agentclick"
  npm_weekly_downloads: 9
---

# Add a browser review checkpoint before risky agent actions with AgentClick

Use AgentClick when an autonomous agent needs a human-in-the-loop review step before execution. The agent can open a local browser UI for command approval, plan review, code diff review, email or draft editing, trajectory inspection, selection capture, and memory review, then continue with the human’s edits or decision. The boundary is narrow and publishable: this is a browser review layer for agent actions, not a generic web app listing and not a broad agent platform card. Invoke it when terminal-only approval is too thin and a richer review checkpoint is the actual missing workflow.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/add-a-browser-review-checkpoint-before-risky-agent-actions-with-agentclick/)
