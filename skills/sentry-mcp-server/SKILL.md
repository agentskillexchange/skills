---
title: "Sentry MCP Server"
description: "Sentry’s official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session."
verification: security_reviewed
source: "https://github.com/getsentry/sentry-mcp"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "getsentry/sentry-mcp"
  github_stars: 635
  npm_package: "@sentry/mcp-server"
  npm_weekly_downloads: 40021
---

# Sentry MCP Server

The Sentry MCP Server is maintained by Sentry and designed for human-in-the-loop coding agents. It acts as middleware to the Sentry API, optimized for development workflows and debugging use cases.

Best for

Debugging stack traces in Cursor or Claude Code with production error context
Triaging Sentry issues through conversational commands
Automated error analysis pipelines with Sentry’s Seer AI root cause analysis
Accessing release health and performance data from within your agent workflow

Key capabilities

Issue search and triage: Search across projects, get detailed issue information with stack traces and breadcrumbs
Seer integration: AI-powered root cause analysis and debugging suggestions
Performance monitoring: Access trace data and performance metrics
Release management: View release health, deploy information, and regression data

Install notes
Remote (recommended): Configure your MCP client to connect to https://mcp.sentry.dev/sse and authenticate via OAuth. Local stdio: Run npx @sentry/mcp-server@latest --access-token=YOUR_TOKEN.

Source: github.com/getsentry/sentry-mcp

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server/)
