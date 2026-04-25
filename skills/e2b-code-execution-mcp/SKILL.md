---
title: "E2B Code Execution MCP"
description: "Add sandboxed code execution to any MCP-compatible AI client. E2B gives agents access to secure, internet-connected Linux environments for running Python, JavaScript, and shell commands without touching your local machine."
verification: "security_reviewed"
source: "https://github.com/e2b-dev/mcp-server"
category:
  - "Developer Tools"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "e2b-dev/mcp-server"
  github_stars: 393
---

# E2B Code Execution MCP

E2B Code Execution MCP connects AI assistants to the E2B Sandbox platform through the Model Context Protocol. Each execution runs inside an ephemeral, fully isolated cloud environment with its own filesystem, network access, and package manager.

Best for

- Data analysis pipelines requiring safe code execution

- Code generation testing in isolated sandboxes

- Multi-step tool chains where untrusted code must not run on the host

- Any MCP workflow needing Python, JavaScript, or shell execution

Install notes
Get an E2B API key at e2b.dev (free tier available). Install via npx @smithery/cli install e2b --client claude or configure the MCP server entry manually in your client config. Requires Node.js v18+ or Python 3.10+.

Source: github.com/e2b-dev/mcp-server

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/e2b-code-execution-mcp/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/e2b-code-execution-mcp
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/e2b-code-execution-mcp`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/e2b-code-execution-mcp/)
