---
title: Sentry MCP Server for Error Tracking and Performance
description: The Sentry MCP Server is an official Model Context Protocol server maintained
  by Sentry (getsentry) that exposes Sentry’s error tracking and performance monitoring
  capabilities to LLMs and AI agents. It enables agents to query issues, analyze error
  patterns, inspect stack traces, and interact with Sentry’s project and release data
  through structured MCP tool calls. The server provides both a remote hosted version
  (available at mcp.sentry.dev) and a local stdio variant (sentry-mcp-stdio) for integration
  with coding tools. Authentication flows through Sentry’s OAuth system, ensuring
  agents operate under proper access controls and organization-scoped permissions.
  Key capabilities include querying and filtering issues by project, status, and time
  range; inspecting individual error events with full stack traces; analyzing error
  frequency and trends; accessing release information and deployment data; and reviewing
  performance telemetry. Agents can use these tools to automate incident triage workflows,
  correlate errors with recent deployments, identify regression patterns, and surface
  actionable insights from error data. The server integrates with the standard MCP
  client ecosystem including VS Code, Cursor, Claude Desktop, and other MCP-compatible
  tools. For the stdio variant, configuration follows the typical npx-based pattern
  with environment variables for authentication tokens. The remote version supports
  direct URL-based connection through the MCP inspector or any compatible client.
  With over 600 GitHub stars and active development from the Sentry engineering team,
  this server represents the canonical integration point between AI agents and Sentry’s
  observability platform. It is particularly valuable for on-call workflows where
  agents can help developers quickly understand error context, identify root causes,
  and determine the impact scope of production issues. The project is hosted at github.com/getsentry/sentry-mcp.
verification: security_reviewed
source: https://github.com/getsentry/sentry-mcp
category:
- Monitoring &amp; Alerts
framework:
- MCP
tool_ecosystem:
  github_repo: getsentry/sentry-mcp
  github_stars: 615
---

# Sentry MCP Server for Error Tracking and Performance

The Sentry MCP Server is an official Model Context Protocol server maintained by Sentry (getsentry) that exposes Sentry’s error tracking and performance monitoring capabilities to LLMs and AI agents. It enables agents to query issues, analyze error patterns, inspect stack traces, and interact with Sentry’s project and release data through structured MCP tool calls. The server provides both a remote hosted version (available at mcp.sentry.dev) and a local stdio variant (sentry-mcp-stdio) for integration with coding tools. Authentication flows through Sentry’s OAuth system, ensuring agents operate under proper access controls and organization-scoped permissions. Key capabilities include querying and filtering issues by project, status, and time range; inspecting individual error events with full stack traces; analyzing error frequency and trends; accessing release information and deployment data; and reviewing performance telemetry. Agents can use these tools to automate incident triage workflows, correlate errors with recent deployments, identify regression patterns, and surface actionable insights from error data. The server integrates with the standard MCP client ecosystem including VS Code, Cursor, Claude Desktop, and other MCP-compatible tools. For the stdio variant, configuration follows the typical npx-based pattern with environment variables for authentication tokens. The remote version supports direct URL-based connection through the MCP inspector or any compatible client. With over 600 GitHub stars and active development from the Sentry engineering team, this server represents the canonical integration point between AI agents and Sentry’s observability platform. It is particularly valuable for on-call workflows where agents can help developers quickly understand error context, identify root causes, and determine the impact scope of production issues. The project is hosted at github.com/getsentry/sentry-mcp.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sentry-mcp-server-error-tracking-performance/)
