---
title: "Sentry MCP Server"
description: "The Sentry MCP Server is maintained by Sentry and designed for human-in-the-loop coding agents. It acts as middleware to the Sentry API, optimized for development workflows and debugging use cases. Best for Debugging stack traces in Cursor or Claude Code with production error context Triaging Sentry issues through conversational commands Automated error analysis pipelines with Sentry&#8217;s Seer AI root cause analysis Accessing release health and performance data from within your agent workflow Key capabilities Issue search and triage: Search across projects, get detailed issue information with stack traces and breadcrumbs Seer integration: AI-powered root cause analysis and debugging suggestions Performance monitoring: Access trace data and performance metrics Release management: View release health, deploy information, and regression data Install notes Remote (recommended): Configure your MCP client to connect to https://mcp.sentry.dev/sse and authenticate via OAuth. Local stdio: Run npx @sentry/mcp-server@latest --access-token=YOUR_TOKEN . Source: github.com/getsentry/sentry-mcp"
source: "https://github.com/getsentry/sentry-mcp"
verification: "security_reviewed"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "getsentry/sentry-mcp"
  github_stars: 645
  npm_package: "@sentry/mcp-server"
  npm_weekly_downloads: 46885
---

# Sentry MCP Server

The Sentry MCP Server is maintained by Sentry and designed for human-in-the-loop coding agents. It acts as middleware to the Sentry API, optimized for development workflows and debugging use cases. Best for Debugging stack traces in Cursor or Claude Code with production error context Triaging Sentry issues through conversational commands Automated error analysis pipelines with Sentry&#8217;s Seer AI root cause analysis Accessing release health and performance data from within your agent workflow Key capabilities Issue search and triage: Search across projects, get detailed issue information with stack traces and breadcrumbs Seer integration: AI-powered root cause analysis and debugging suggestions Performance monitoring: Access trace data and performance metrics Release management: View release health, deploy information, and regression data Install notes Remote (recommended): Configure your MCP client to connect to https://mcp.sentry.dev/sse and authenticate via OAuth. Local stdio: Run npx @sentry/mcp-server@latest --access-token=YOUR_TOKEN . Source: github.com/getsentry/sentry-mcp

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server/)
