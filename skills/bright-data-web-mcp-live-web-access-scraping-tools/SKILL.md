---
title: "Bright Data Web MCP Live Web Access and Scraping Tools"
description: "Bright Data Web MCP is an MCP server from Bright Data that gives agents direct access to real-time web search, scraping, extraction, and optional browser-control capabilities. Its main job-to-be-done is to provide dependable web access for research and scraping workflows where a standard fetch often fails because of anti-bot systems, rate limits, or geo restrictions. Instead of asking an agent to stitch together search, scraping, and browser tools manually, this project exposes a unified MCP surface that can be plugged into Claude, GPT, Gemini, Cursor, Windsurf, and similar agent setups. The upstream project supports several operating modes. There is a hosted connector that needs only a URL with an API token, and there is also a local MCP configuration using npx @brightdata/mcp . The README documents tool groups for browser automation, advanced scraping, research, social, ecommerce, finance, business intelligence, code package metadata, and GEO-style AI brand visibility checks. That breadth makes it useful well beyond a simple search connector. A single agent workflow can search the web, scrape pages as markdown, extract structured data, inspect package metadata, or enable browser-oriented tools by selecting the right groups. For ASE, this fits best as a Research & Scraping skill with an MCP framework mapping. It is source-backed, actively maintained, widely adopted, and has a clear integration story for teams that want live web capabilities without running their own unblocker infrastructure."
source: "https://github.com/browserbase/mcp-server-browserbase"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "browserbase/mcp-server-browserbase"
  github_stars: 3249
  npm_package: "@browserbasehq/mcp"
  npm_weekly_downloads: 937
---

# Bright Data Web MCP Live Web Access and Scraping Tools

Bright Data Web MCP is an MCP server from Bright Data that gives agents direct access to real-time web search, scraping, extraction, and optional browser-control capabilities. Its main job-to-be-done is to provide dependable web access for research and scraping workflows where a standard fetch often fails because of anti-bot systems, rate limits, or geo restrictions. Instead of asking an agent to stitch together search, scraping, and browser tools manually, this project exposes a unified MCP surface that can be plugged into Claude, GPT, Gemini, Cursor, Windsurf, and similar agent setups. The upstream project supports several operating modes. There is a hosted connector that needs only a URL with an API token, and there is also a local MCP configuration using npx @brightdata/mcp . The README documents tool groups for browser automation, advanced scraping, research, social, ecommerce, finance, business intelligence, code package metadata, and GEO-style AI brand visibility checks. That breadth makes it useful well beyond a simple search connector. A single agent workflow can search the web, scrape pages as markdown, extract structured data, inspect package metadata, or enable browser-oriented tools by selecting the right groups. For ASE, this fits best as a Research & Scraping skill with an MCP framework mapping. It is source-backed, actively maintained, widely adopted, and has a clear integration story for teams that want live web capabilities without running their own unblocker infrastructure.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bright-data-web-mcp-live-web-access-scraping-tools/)
