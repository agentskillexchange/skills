---
title: Claude Code MCP Bridge
description: 'Claude Code MCP Bridge exposes Claude Code as a single MCP tool. When
  an MCP client calls it with a prompt, the server runs Claude Code in one-shot mode,
  letting it execute file reads and writes, git operations, terminal commands, and
  multi-step refactoring. Best for Agent-in-agent orchestration where one model delegates
  coding to another Cursor, Windsurf, or custom pipeline users who want Claude Code
  as a sub-agent Complex multi-step file operations that benefit from Claude Code
  capabilities How it differs from Coding Agent Coding Agent is about running coding
  agents directly. This bridge is about embedding Claude Code inside another MCP workflow
  as infrastructure — orchestration, not direct assistance. Install notes Install
  the Claude CLI globally ( npm install -g @anthropic-ai/claude-code ), accept the
  permissions flag once, then configure: npx -y @steipete/claude-code-mcp@latest in
  your MCP client config. Requires Node.js v20+ and an authenticated Claude CLI. Source:
  github.com/steipete/claude-code-mcp'
verification: security_reviewed
source: https://github.com/steipete/claude-code-mcp
category:
- Developer Tools
framework:
- Claude Code
- MCP
tool_ecosystem:
  github_repo: steipete/claude-code-mcp
  github_stars: 1212
---

# Claude Code MCP Bridge

Claude Code MCP Bridge exposes Claude Code as a single MCP tool. When an MCP client calls it with a prompt, the server runs Claude Code in one-shot mode, letting it execute file reads and writes, git operations, terminal commands, and multi-step refactoring. Best for Agent-in-agent orchestration where one model delegates coding to another Cursor, Windsurf, or custom pipeline users who want Claude Code as a sub-agent Complex multi-step file operations that benefit from Claude Code capabilities How it differs from Coding Agent Coding Agent is about running coding agents directly. This bridge is about embedding Claude Code inside another MCP workflow as infrastructure — orchestration, not direct assistance. Install notes Install the Claude CLI globally ( npm install -g @anthropic-ai/claude-code ), accept the permissions flag once, then configure: npx -y @steipete/claude-code-mcp@latest in your MCP client config. Requires Node.js v20+ and an authenticated Claude CLI. Source: github.com/steipete/claude-code-mcp

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/claude-code-mcp-bridge/)
