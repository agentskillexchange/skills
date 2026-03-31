---
name: "E2B Code Execution MCP"
description: "Add sandboxed code execution to any MCP-compatible AI client. E2B gives agents access to secure, internet-connected Linux environments for running Python, JavaScript, and shell commands without touching your local machine."
category: "Developer Tools"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/e2b-code-execution-mcp/"
---
# E2B Code Execution MCP

Add sandboxed code execution to any MCP-compatible AI client. E2B gives agents access to secure, internet-connected Linux environments for running Python, JavaScript, and shell commands without touching your local machine.

## Overview

E2B Code Execution MCP connects AI assistants to the E2B Sandbox platform through the Model Context Protocol. Each execution runs inside an ephemeral, fully isolated cloud environment with its own filesystem, network access, and package manager.

Best for

- Data analysis pipelines requiring safe code execution

- Code generation testing in isolated sandboxes

- Multi-step tool chains where untrusted code must not run on the host

- Any MCP workflow needing Python, JavaScript, or shell execution

Install notes

Get an E2B API key at e2b.dev (free tier available). Install via `npx @smithery/cli install e2b --client claude` or configure the MCP server entry manually in your client config. Requires Node.js v18+ or Python 3.10+.

Source: github.com/e2b-dev/mcp-server

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill e2b-code-execution-mcp
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill e2b-code-execution-mcp -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill e2b-code-execution-mcp -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill e2b-code-execution-mcp -a codex
```

### OpenClaw

```bash
clawhub install e2b-code-execution-mcp
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/e2b-code-execution-mcp/)
