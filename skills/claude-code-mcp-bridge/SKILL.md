---
title: "Claude Code MCP Bridge"
description: "Run Claude Code as a one-shot MCP tool so other agents and editors can delegate coding tasks to it. An agent-in-agent orchestration bridge."
slug: "claude-code-mcp-bridge"
category:
  - "Developer Tools"
framework:
  - "Claude Code"
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/steipete/claude-code-mcp"
tool_ecosystem:
  github_repo: "steipete/claude-code-mcp"
  github_stars: 1225
---

# Claude Code MCP Bridge

Run Claude Code as a one-shot MCP tool so other agents and editors can delegate coding tasks to it. An agent-in-agent orchestration bridge.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install claude-code-mcp-bridge
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Claude Code MCP Bridge exposes Claude Code as a single MCP tool. When an MCP client calls it with a prompt, the server runs Claude Code in one-shot mode, letting it execute file reads and writes, git operations, terminal commands, and multi-step refactoring.
Best for
- Agent-in-agent orchestration where one model delegates coding to another
- Cursor, Windsurf, or custom pipeline users who want Claude Code as a sub-agent
- Complex multi-step file operations that benefit from Claude Code capabilities
How it differs from Coding Agent
Coding Agent is about running coding agents directly. This bridge is about embedding Claude Code inside another MCP workflow as infrastructure — orchestration, not direct assistance.
Install notes
Install the Claude CLI globally (npm install -g @anthropic-ai/claude-code), accept the permissions flag once, then configure: npx -y @steipete/claude-code-mcp@latest in your MCP client config. Requires Node.js v20+ and an authenticated Claude CLI.
Source: github.com/steipete/claude-code-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/claude-code-mcp-bridge/)
