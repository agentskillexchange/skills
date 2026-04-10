---
name: Official Firecrawl MCP Server
description: Official Firecrawl MCP Server exposes Firecrawl’s scraping, crawling,
  search, and deep research features to MCP clients. It is a strong choice for agents
  that need web extraction with a maintained API-backed service instead of hand-built
  scrapers.
verification: security_reviewed
source: https://github.com/firecrawl/firecrawl-mcp-server
category:
- Research &amp; Scraping
framework:
- MCP
tool_ecosystem:
  github_repo: firecrawl/firecrawl-mcp-server
  github_stars: 5994
  ase_npm_package: firecrawl-mcp
  npm_weekly_downloads: 29131
---
# Official Firecrawl MCP Server

Official Firecrawl MCP Server is Firecrawl’s maintained MCP bridge for web scraping, search, crawl, and research workflows. It gives MCP-compatible assistants access to Firecrawl’s hosted or self-hosted capabilities, including single-page scraping, site crawling, URL discovery, search, batch scraping, and interactive browser-assisted flows. The point of the project is not generic browser control, but dependable access to web content extraction and discovery tools through a standard MCP interface.
The upstream repository documents installation with npx -y firecrawl-mcp and the npm package is published separately as firecrawl-mcp. The server uses FIRECRAWL_API_KEY for the cloud service by default and also supports a custom FIRECRAWL_API_URL for self-hosted instances. The README includes configuration examples for Cursor, Windsurf, VS Code, Claude Desktop, and streamable HTTP mode, which makes the integration story clear for common agent clients.
This listing fits Research & Scraping because the concrete job-to-be-done is harvesting and structuring information from the web rather than controlling arbitrary interfaces end to end. It also fits MCP because the Firecrawl functionality is delivered as MCP tools that an agent can call directly. The project has strong verification signals through its official GitHub repository, npm package, public docs, license, and recent maintenance activity, so it passes the intake gate for verified metadata publication.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/official-firecrawl-mcp-server/)
