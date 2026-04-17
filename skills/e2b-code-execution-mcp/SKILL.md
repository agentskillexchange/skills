---
title: "E2B Code Execution MCP"
description: "E2B Code Execution MCP connects AI assistants to the E2B Sandbox platform through the Model Context Protocol. Each execution runs inside an ephemeral, fully isolated cloud environment with its own filesystem, network access, and package manager.\nBest for\n\nData analysis pipelines requiring safe code execution\nCode generation testing in isolated sandboxes\nMulti-step tool chains where untrusted code must not run on the host\nAny MCP workflow needing Python, JavaScript, or shell execution\n\nInstall notes\nGet an E2B API key at e2b.dev (free tier available). Install via npx @smithery/cli install e2b --client claude or configure the MCP server entry manually in your client config. Requires Node.js v18+ or Python 3.10+.\nSource: github.com/e2b-dev/mcp-server"
verification: security_reviewed
source: "https://github.com/e2b-dev/mcp-server"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "e2b-dev/mcp-server"
  github_stars: 389
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/e2b-code-execution-mcp
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/e2b-code-execution-mcp` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/e2b-code-execution-mcp/)
