---
title: Playwright MCP Server for Browser Automation
description: The Playwright MCP Server, maintained by Microsoft, is a Model Context
  Protocol server that exposes Playwright’s browser automation capabilities to LLMs
  and AI agents. With nearly 30,000 GitHub stars, it is the second most popular MCP
  server on GitHub and a cornerstone of the emerging agentic browser automation ecosystem.
  Unlike screenshot-based approaches that require vision models to interpret pixel
  data, the Playwright MCP server operates on structured accessibility tree snapshots.
  This makes tool application deterministic and avoids the ambiguity that comes with
  visual interpretation. The server is fast, lightweight, and works purely on structured
  data that LLMs can reason about directly. The server supports integration with all
  major AI coding tools including VS Code, Cursor, Windsurf, Claude Desktop, Claude
  Code, Codex, Goose, Cline, and more. Configuration is straightforward through standard
  MCP server JSON configuration, typically just specifying the npx command with the
  @playwright/mcp package. Key capabilities include navigating to URLs, clicking elements,
  filling forms, taking screenshots, extracting page content, handling dialogs, managing
  tabs, and executing JavaScript on pages. The server exposes these as structured
  MCP tools that agents can invoke with well-defined parameters and return types.
  For coding agents that need high-throughput browser interaction, Microsoft also
  provides a companion Playwright CLI with SKILLS approach that is more token-efficient
  than MCP. The MCP server is better suited for specialized agentic loops that benefit
  from persistent state, rich introspection, and iterative reasoning over page structure.
  The server requires Node.js 18 or newer and is distributed as an npm package under
  the Apache-2.0 license.
verification: security_reviewed
source: https://github.com/microsoft/playwright-mcp
category:
- Browser Automation
framework:
- MCP
tool_ecosystem:
  github_repo: microsoft/playwright-mcp
  github_stars: 30110
---

# Playwright MCP Server for Browser Automation

The Playwright MCP Server, maintained by Microsoft, is a Model Context Protocol server that exposes Playwright’s browser automation capabilities to LLMs and AI agents. With nearly 30,000 GitHub stars, it is the second most popular MCP server on GitHub and a cornerstone of the emerging agentic browser automation ecosystem. Unlike screenshot-based approaches that require vision models to interpret pixel data, the Playwright MCP server operates on structured accessibility tree snapshots. This makes tool application deterministic and avoids the ambiguity that comes with visual interpretation. The server is fast, lightweight, and works purely on structured data that LLMs can reason about directly. The server supports integration with all major AI coding tools including VS Code, Cursor, Windsurf, Claude Desktop, Claude Code, Codex, Goose, Cline, and more. Configuration is straightforward through standard MCP server JSON configuration, typically just specifying the npx command with the @playwright/mcp package. Key capabilities include navigating to URLs, clicking elements, filling forms, taking screenshots, extracting page content, handling dialogs, managing tabs, and executing JavaScript on pages. The server exposes these as structured MCP tools that agents can invoke with well-defined parameters and return types. For coding agents that need high-throughput browser interaction, Microsoft also provides a companion Playwright CLI with SKILLS approach that is more token-efficient than MCP. The MCP server is better suited for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure. The server requires Node.js 18 or newer and is distributed as an npm package under the Apache-2.0 license.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-mcp-server-browser-automation/)
