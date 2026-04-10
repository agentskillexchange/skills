---
title: "Sentry MCP Server"
description: "Sentry’s official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session."
slug: "sentry-mcp-server"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/getsentry/sentry-mcp"
tool_ecosystem:
  github_repo: "getsentry/sentry-mcp"
  github_stars: 626
  npm_package: "@sentry/mcp-server"
  npm_weekly_downloads: 41729
---

# Sentry MCP Server

Sentry’s official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install sentry-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Sentry MCP Server is maintained by Sentry and designed for human-in-the-loop coding agents. It acts as middleware to the Sentry API, optimized for development workflows and debugging use cases.
Best for
- Debugging stack traces in Cursor or Claude Code with production error context
- Triaging Sentry issues through conversational commands
- Automated error analysis pipelines with Sentry’s Seer AI root cause analysis
- Accessing release health and performance data from within your agent workflow
Key capabilities
- Issue search and triage: Search across projects, get detailed issue information with stack traces and breadcrumbs
- Seer integration: AI-powered root cause analysis and debugging suggestions
- Performance monitoring: Access trace data and performance metrics
- Release management: View release health, deploy information, and regression data
Install notes
Remote (recommended): Configure your MCP client to connect to https://mcp.sentry.dev/sse and authenticate via OAuth. Local stdio: Run npx @sentry/mcp-server@latest --access-token=YOUR_TOKEN.
Source: github.com/getsentry/sentry-mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server/)
