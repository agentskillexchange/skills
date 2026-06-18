---
name: "Sentry MCP Server"
slug: "sentry-mcp-server"
description: "Sentry's official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session."
github_stars: 712
verification: "security_reviewed"
source: "https://github.com/getsentry/sentry-mcp"
author: "Sentry"
publisher_type: "company"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "getsentry/sentry-mcp"
  github_stars: 712
  npm_package: "@sentry/mcp-server"
  npm_weekly_downloads: 70526
---

# Sentry MCP Server

Sentry's official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session.

## Prerequisites

MCP-compatible client (Claude Code, Cursor, VS Code), Sentry account with active projects, Node.js (for stdio mode)

## Installation

Use the upstream install or setup path that matches your environment:
- npx @sentry/mcp-server@latest --access-token=sentry-user-token
- npx @sentry/mcp-server@latest --access-token=TOKEN --host=sentry.example.com --disable-skills=seer
- npx @sentry/mcp-server@latest --access-token=TOKEN --host=sentry.internal:9000 --insecure-http
- pnpm inspector

Requirements and caveats from upstream:
- **Note:** The AI-powered search tools (search_events, search_issues, etc.) require an LLM provider (OpenAI or Anthropic). These tools use natural language processing to translate queries into Sentry's query syntax. Wi...
- **Evaluations** require a .env file in the project root with some config:

Basic usage or getting-started notes:
- You'll find everything you need to know by visiting the deployed service in production:
- <https://mcp.sentry.dev>
- If you're looking to contribute, learn how it works, or to run this for self-hosted Sentry, continue below.

- Source: https://github.com/getsentry/sentry-mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/getsentry/sentry-mcp/HEAD/README.md

## Documentation

- https://docs.sentry.io/product/sentry-mcp/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server/)
