---
name: "Runheed"
slug: "runheed"
description: "Read and resolve production errors through the Runheed remote MCP server (https://runheed.com/api/mcp): search error groups, read stack traces and breadcrumbs, fix the code and mark the error resolved with the fixing commit."
github_stars: 0
verification: "listed"
source: "https://github.com/getrunheed/runheed-plugin"
author: "Runheed"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "getrunheed/runheed-plugin"
  github_stars: 0
---

# Runheed

Runheed is error tracking built for coding agents. An app reports exceptions through the Node or Python SDK; the agent reads them over a remote MCP server instead of a dashboard.

The server exposes 13 tools: project health, recent errors, error search, trends, full error detail with stack trace and breadcrumbs, error context, resolve, ignore and unignore, merge, project listing (`runheed_list_projects`), project creation and a test event.

Use it when asked what is breaking in production, to fix the top error, to check whether a fix held, or to resolve an error with the commit that fixed it. It is not an APM: there is no tracing or session replay.

## Installation

Install or set up from the source-backed instructions:

/plugin marketplace add getrunheed/runheed-plugin
/plugin install runheed@runheed

- Source: https://github.com/getrunheed/runheed-plugin

## Pricing

Paid, from $29/month with a 7-day trial.
