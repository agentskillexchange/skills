---
title: "Claude Code MCP Bridge"
description: "Run Claude Code as a one-shot MCP tool so other agents and editors can delegate coding tasks to it. An agent-in-agent orchestration bridge."
verification: security_reviewed
source: "https://github.com/steipete/claude-code-mcp"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
  - "MCP"
tool_ecosystem:
  github_repo: "steipete/claude-code-mcp"
  github_stars: 1229
---

# Claude Code MCP Bridge

Claude Code MCP Bridge exposes Claude Code as a single MCP tool. When an MCP client calls it with a prompt, the server runs Claude Code in one-shot mode, letting it execute file reads and writes, git operations, terminal commands, and multi-step refactoring.

Best for

Agent-in-agent orchestration where one model delegates coding to another
Cursor, Windsurf, or custom pipeline users who want Claude Code as a sub-agent
Complex multi-step file operations that benefit from Claude Code capabilities

How it differs from Coding Agent
Coding Agent is about running coding agents directly. This bridge is about embedding Claude Code inside another MCP workflow as infrastructure — orchestration, not direct assistance.

Install notes
Install the Claude CLI globally (npm install -g @anthropic-ai/claude-code), accept the permissions flag once, then configure: npx -y @steipete/claude-code-mcp@latest in your MCP client config. Requires Node.js v20+ and an authenticated Claude CLI.

Source: github.com/steipete/claude-code-mcp

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/claude-code-mcp-bridge/)
