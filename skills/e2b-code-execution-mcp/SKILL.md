---
name: E2B Code Execution MCP
description: Add sandboxed code execution to any MCP-compatible AI client. E2B gives
  agents access to secure, internet-connected Linux environments for running Python,
  JavaScript, and shell commands without touching your local machine.
verification: security_reviewed
source: https://github.com/e2b-dev/mcp-server
category:
- Developer Tools
framework:
- MCP
tool_ecosystem:
  github_repo: e2b-dev/mcp-server
  github_stars: 386
---
# E2B Code Execution MCP

E2B Code Execution MCP connects AI assistants to the E2B Sandbox platform through the Model Context Protocol. Each execution runs inside an ephemeral, fully isolated cloud environment with its own filesystem, network access, and package manager.
Best for

Data analysis pipelines requiring safe code execution
Code generation testing in isolated sandboxes
Multi-step tool chains where untrusted code must not run on the host
Any MCP workflow needing Python, JavaScript, or shell execution

Install notes
Get an E2B API key at e2b.dev (free tier available). Install via npx @smithery/cli install e2b --client claude or configure the MCP server entry manually in your client config. Requires Node.js v18+ or Python 3.10+.
Source: github.com/e2b-dev/mcp-server

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/e2b-code-execution-mcp/)
