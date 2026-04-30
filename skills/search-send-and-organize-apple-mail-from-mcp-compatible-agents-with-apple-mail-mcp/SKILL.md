---
title: "Search, send, and organize Apple Mail from MCP-compatible agents with Apple Mail MCP"
description: "Lets an MCP-compatible agent read, search, send, thread, template, and organize Apple Mail on macOS so email work can stay inside a bounded agent workflow."
verification: "security_reviewed"
source: "https://github.com/s-morgan-jeffries/apple-mail-mcp"
author: "s-morgan-jeffries"
publisher_type: "individual"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "s-morgan-jeffries/apple-mail-mcp"
  github_stars: 54
---

# Search, send, and organize Apple Mail from MCP-compatible agents with Apple Mail MCP

Lets an MCP-compatible agent read, search, send, thread, template, and organize Apple Mail on macOS so email work can stay inside a bounded agent workflow.

## Prerequisites

macOS 10.15+ with Apple Mail configured, Python 3.10+, uv or pip, and an MCP-compatible client such as Claude Desktop.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Clone the repository, run <code>uv sync --dev</code> (or install with <code>pip</code>), then register the server in your MCP client config using <code>uv --directory /path/to/apple-mail-mcp run python -m apple_mail_mcp.server</code>. On first run, grant macOS Automation permission so the server can control Apple Mail.</p>
```

## Documentation

- https://github.com/s-morgan-jeffries/apple-mail-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-send-and-organize-apple-mail-from-mcp-compatible-agents-with-apple-mail-mcp/)
