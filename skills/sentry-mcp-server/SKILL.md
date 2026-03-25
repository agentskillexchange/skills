---
name: "Sentry MCP Server"
description: "Sentry’s official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session."
category: "Monitoring & Alerts"
framework: "MCP-compatible"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sentry-mcp-server/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "sentry"  # from ase_tool_match
  github_stars: 43437  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 16379655  # from ase_npm_downloads
  github_repo: "getsentry/sentry"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Sentry MCP Server

Sentry’s official MCP server connects your error monitoring stack to any MCP client. Search issues, analyze stack traces, investigate performance bottlenecks, and get AI-powered root cause analysis — all without leaving your editor or agent session.

## Overview

The Sentry MCP Server is maintained by Sentry and designed for human-in-the-loop coding agents. It acts as middleware to the Sentry API, optimized for development workflows and debugging use cases.

Best for

Debugging stack traces in Cursor or Claude Code with production error context

Triaging Sentry issues through conversational commands

Automated error analysis pipelines with Sentry’s Seer AI root cause analysis

Accessing release health and performance data from within your agent workflow

Key capabilities

**Issue search and triage:** Search across projects, get detailed issue information with stack traces and breadcrumbs

**Seer integration:** AI-powered root cause analysis and debugging suggestions

**Performance monitoring:** Access trace data and performance metrics

**Release management:** View release health, deploy information, and regression data

Install notes

**Remote (recommended):** Configure your MCP client to connect to `https://mcp.sentry.dev/sse` and authenticate via OAuth. **Local stdio:** Run `npx @sentry/mcp-server@latest --access-token=YOUR_TOKEN`.

**Source:** [github.com/getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp)

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sentry-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sentry-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sentry-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sentry-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install sentry-mcp-server
```

## Source

- Marketplace: https://agentskillexchange.com/skills/sentry-mcp-server/
