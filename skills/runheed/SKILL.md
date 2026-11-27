---
name: "Runheed"
slug: "runheed"
description: "Read and resolve production errors through the Runheed remote MCP server (https://runheed.com/api/mcp): search error groups, read stack traces and breadcrumbs, fix the code and mark the error resolved with the fixing commit."
verification: "listed"
source: "https://github.com/getrunheed/runheed-plugin"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "getrunheed/runheed-plugin"
---

# Runheed

Runheed is error tracking built for coding agents. An app reports exceptions through the Node or Python SDK; the agent reads them over a remote MCP server instead of a dashboard.

The server exposes 13 tools: project health, recent errors, error search, trends, full error detail with stack trace and breadcrumbs, error context, resolve, ignore and unignore, merge, project listing (`runheed_list_projects`), project creation and a test event.

Use it when asked what is breaking in production, to fix the top error, to check whether a fix held, or to resolve an error with the commit that fixed it. It is not an APM: there is no tracing or session replay.

## Installation

### Claude Code

```bash
claude mcp add --transport http runheed https://runheed.com/api/mcp
```

Then run `/mcp` in Claude Code, select `runheed`, and choose **Authenticate** to sign in with OAuth.

### Other MCP clients (Codex, Gemini CLI, Cursor, ChatGPT)

Add the remote server URL `https://runheed.com/api/mcp` (Streamable HTTP). Clients that cannot open a sign-in window can send an agent key as a bearer token. Connect pages for each client are at https://runheed.com/docs.

### Try it without an account

A demo MCP server with invented sample errors needs no account or key: `https://runheed.com/api/mcp/demo`.

### Skill file

The agent skill is published at https://runheed.com/SKILL.md and in https://github.com/getrunheed/runheed-plugin.

## Pricing

Paid, from $29/month with a 7-day trial.
