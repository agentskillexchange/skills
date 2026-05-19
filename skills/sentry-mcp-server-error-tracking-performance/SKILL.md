---
name: "Sentry MCP Server for Error Tracking and Performance"
slug: "sentry-mcp-server-error-tracking-performance"
description: "The official Sentry MCP server gives AI agents access to Sentry error tracking, issue management, and performance telemetry through the Model Context Protocol, enabling automated incident triage, error analysis, and release monitoring workflows."
github_stars: 615
verification: "security_reviewed"
source: "https://github.com/getsentry/sentry-mcp"
author: "Sentry"
category: "Monitoring & Alerts"
framework: "MCP"
tool_ecosystem:
  github_repo: "getsentry/sentry-mcp"
  github_stars: 615
  npm_package: "@sentry/mcp-server"
  npm_weekly_downloads: 49643
---

# Sentry MCP Server for Error Tracking and Performance

The official Sentry MCP server gives AI agents access to Sentry error tracking, issue management, and performance telemetry through the Model Context Protocol, enabling automated incident triage, error analysis, and release monitoring workflows.

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

- https://github.com/getsentry/sentry-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server-error-tracking-performance/)
