---
title: Official Firecrawl MCP Server
description: Official Firecrawl MCP Server is Firecrawl’s maintained MCP bridge for
  web scraping, search, crawl, and research workflows. It gives MCP-compatible assistants
  access to Firecrawl’s hosted or self-hosted capabilities, including single-page
  scraping, site crawling, URL discovery, search, batch scraping, and interactive
  browser-assisted flows. The point of the project is not generic browser control,
  but dependable access to web content extraction and discovery tools through a standard
  MCP interface. The upstream repository documents installation with npx -y firecrawl-mcp
  and the npm package is published separately as firecrawl-mcp . The server uses FIRECRAWL_API_KEY
  for the cloud service by default and also supports a custom FIRECRAWL_API_URL for
  self-hosted instances. The README includes configuration examples for Cursor, Windsurf,
  VS Code, Claude Desktop, and streamable HTTP mode, which makes the integration story
  clear for common agent clients. This listing fits Research & Scraping because the
  concrete job-to-be-done is harvesting and structuring information from the web rather
  than controlling arbitrary interfaces end to end. It also fits MCP because the Firecrawl
  functionality is delivered as MCP tools that an agent can call directly. The project
  has strong verification signals through its official GitHub repository, npm package,
  public docs, license, and recent maintenance activity, so it passes the intake gate
  for verified metadata publication.
verification: security_reviewed
source: https://github.com/firecrawl/firecrawl-mcp-server
category:
- Research &amp; Scraping
framework:
- MCP
---

# Official Firecrawl MCP Server

Official Firecrawl MCP Server is Firecrawl’s maintained MCP bridge for web scraping, search, crawl, and research workflows. It gives MCP-compatible assistants access to Firecrawl’s hosted or self-hosted capabilities, including single-page scraping, site crawling, URL discovery, search, batch scraping, and interactive browser-assisted flows. The point of the project is not generic browser control, but dependable access to web content extraction and discovery tools through a standard MCP interface. The upstream repository documents installation with npx -y firecrawl-mcp and the npm package is published separately as firecrawl-mcp . The server uses FIRECRAWL_API_KEY for the cloud service by default and also supports a custom FIRECRAWL_API_URL for self-hosted instances. The README includes configuration examples for Cursor, Windsurf, VS Code, Claude Desktop, and streamable HTTP mode, which makes the integration story clear for common agent clients. This listing fits Research & Scraping because the concrete job-to-be-done is harvesting and structuring information from the web rather than controlling arbitrary interfaces end to end. It also fits MCP because the Firecrawl functionality is delivered as MCP tools that an agent can call directly. The project has strong verification signals through its official GitHub repository, npm package, public docs, license, and recent maintenance activity, so it passes the intake gate for verified metadata publication.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/official-firecrawl-mcp-server/)
