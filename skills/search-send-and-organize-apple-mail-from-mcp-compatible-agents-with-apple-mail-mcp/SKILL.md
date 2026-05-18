---
name: "Search, send, and organize Apple Mail from MCP-compatible agents with Apple Mail MCP"
slug: "search-send-and-organize-apple-mail-from-mcp-compatible-agents-with-apple-mail-mcp"
description: "Lets an MCP-compatible agent read, search, send, thread, template, and organize Apple Mail on macOS so email work can stay inside a bounded agent workflow."
github_stars: 54
verification: "security_reviewed"
source: "https://github.com/s-morgan-jeffries/apple-mail-mcp"
author: "s-morgan-jeffries"
publisher_type: "individual"
category: "Calendar, Email & Productivity"
framework: "MCP"
tool_ecosystem:
  github_repo: "s-morgan-jeffries/apple-mail-mcp"
  github_stars: 54
---

# Search, send, and organize Apple Mail from MCP-compatible agents with Apple Mail MCP

Lets an MCP-compatible agent read, search, send, thread, template, and organize Apple Mail on macOS so email work can stay inside a bounded agent workflow.

## Prerequisites

macOS 10.15+ with Apple Mail configured, Python 3.10+, uv or pip, and an MCP-compatible client such as Claude Desktop.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/s-morgan-jeffries/apple-mail-mcp.git
- uv sync --dev
- uv run python -c "from apple_mail_mcp.mail_connector import AppleMailConnector; \
- make test # Run unit tests

Requirements and caveats from upstream:
- [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
- Python 3.10 or later
- "args": ["--directory", "/path/to/apple-mail-mcp", "run", "python", "-m", "apple_mail_mcp.server"]

Basic usage or getting-started notes:
- ⚠️ **Pre-1.0 — expect breaking changes.** The MCP tool surface (tool names, parameters, return shapes) is still evolving as the project matures. Pin to a specific version (for example, apple-mail-mcp==0.8.1) and revie...
- macOS 10.15 (Catalina) or later
- Apple Mail configured with at least one account

- Source: https://github.com/s-morgan-jeffries/apple-mail-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/s-morgan-jeffries/apple-mail-mcp/HEAD/README.md

## Documentation

- https://github.com/s-morgan-jeffries/apple-mail-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-send-and-organize-apple-mail-from-mcp-compatible-agents-with-apple-mail-mcp/)
