---
title: "Bright Data Web MCP Live Web Access and Scraping Tools"
description: "Bright Data Web MCP gives MCP-compatible agents live web search, scraping, and optional browser-automation access through Bright Data’s web-access platform. It is built for agents that need current information, anti-bot resilience, and structured extraction without maintaining their own scraping stack."
verification: "security_reviewed"
source: "https://github.com/browserbase/mcp-server-browserbase"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "browserbase/mcp-server-browserbase"
  github_stars: 3249
  ase_npm_package: "@browserbasehq/mcp"
  npm_weekly_downloads: 937
---

# Bright Data Web MCP Live Web Access and Scraping Tools

Bright Data Web MCP is an MCP server from Bright Data that gives agents direct access to real-time web search, scraping, extraction, and optional browser-control capabilities. Its main job-to-be-done is to provide dependable web access for research and scraping workflows where a standard fetch often fails because of anti-bot systems, rate limits, or geo restrictions. Instead of asking an agent to stitch together search, scraping, and browser tools manually, this project exposes a unified MCP surface that can be plugged into Claude, GPT, Gemini, Cursor, Windsurf, and similar agent setups.


The upstream project supports several operating modes. There is a hosted connector that needs only a URL with an API token, and there is also a local MCP configuration using npx @brightdata/mcp. The README documents tool groups for browser automation, advanced scraping, research, social, ecommerce, finance, business intelligence, code package metadata, and GEO-style AI brand visibility checks. That breadth makes it useful well beyond a simple search connector. A single agent workflow can search the web, scrape pages as markdown, extract structured data, inspect package metadata, or enable browser-oriented tools by selecting the right groups.


For ASE, this fits best as a Research & Scraping skill with an MCP framework mapping. It is source-backed, actively maintained, widely adopted, and has a clear integration story for teams that want live web capabilities without running their own unblocker infrastructure.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bright-data-web-mcp-live-web-access-scraping-tools/)
