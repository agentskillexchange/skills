---
name: "Use Apify MCP for agent web extraction"
slug: "use-apify-mcp-for-agent-web-extraction"
description: "Use the Apify MCP server to let MCP-compatible agents run Apify Actors for structured extraction from search, maps, ecommerce, social platforms, and arbitrary websites."
github_stars: 1962
verification: "security_reviewed"
source: "https://github.com/apify/apify-mcp-server"
author: "Apify contributors"
publisher_type: "open_source"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "apify/apify-mcp-server"
  github_stars: 1962
  npm_package: "@apify/actors-mcp-server"
  npm_weekly_downloads: 5657
---

# Use Apify MCP for agent web extraction

Use the Apify MCP server to let MCP-compatible agents run Apify Actors for structured extraction from search, maps, ecommerce, social platforms, and arbitrary websites.

## Prerequisites

MCP-compatible client such as Claude Desktop, Claude.ai, VS Code, Cursor, or Claude Code; hosted Apify MCP endpoint or @apify/actors-mcp-server; Apify account or API token where required; selected Apify Actors

## Installation

Use the upstream install or setup path that matches your environment:
- npx @apify/actors-mcp-server --tools actors,docs,apify/rag-web-browser
- npx @apify/actors-mcp-server --tools apify/my-actor
- npx @apify/actors-mcp-server --ui true
- npx @apify/actors-mcp-server

Requirements and caveats from upstream:
- **Skyfire** pays with PAY tokens and requires a Skyfire account with a funded wallet. It does not require a special MCP client; the entire payment flow is handled directly through the MCP tool call parameters.
- [Node.js](https://nodejs.org/en) (v22 or higher)

Basic usage or getting-started notes:
- [💬 Usage examples](#-usage-examples)
- For example, it can:
- Actor run costs vary, so both payment methods use a prepaid balance model. The payment flow happens in four steps:

- Source: https://github.com/apify/apify-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/apify/apify-mcp-server/HEAD/README.md

## Documentation

- https://docs.apify.com/platform/integrations/mcp

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/use-apify-mcp-for-agent-web-extraction/)
