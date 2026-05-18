---
name: "Official Firecrawl MCP Server"
slug: "official-firecrawl-mcp-server"
description: "Official Firecrawl MCP Server exposes Firecrawl’s scraping, crawling, search, and deep research features to MCP clients. It is a strong choice for agents that need web extraction with a maintained API-backed service instead of hand-built scrapers."
github_stars: 6001
verification: "listed"
source: "https://github.com/firecrawl/firecrawl-mcp-server"
author: "firecrawl"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "firecrawl/firecrawl-mcp-server"
  github_stars: 6001
  npm_package: "firecrawl-mcp"
  npm_weekly_downloads: 28903
---

# Official Firecrawl MCP Server

Official Firecrawl MCP Server exposes Firecrawl’s scraping, crawling, search, and deep research features to MCP clients. It is a strong choice for agents that need web extraction with a maintained API-backed service instead of hand-built scrapers.

## Prerequisites

FIRECRAWL_API_KEY

## Installation

Use the upstream install or setup path that matches your environment:
- npm install -g firecrawl-mcp
- npx -y @smithery/cli install @mendableai/mcp-server-firecrawl --client claude
- [![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=firecrawl&inputs=%5B%7B%2...
- npm install

Requirements and caveats from upstream:
- Note: Requires Cursor version 0.45.6+
- If not provided, the cloud API will be used (requires API key)
- export FIRECRAWL_API_KEY=your-api-key # If your instance requires auth

Basic usage or getting-started notes:
- ### Running with npx
- bash
- env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp

- Source: https://github.com/firecrawl/firecrawl-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/official-firecrawl-mcp-server/)
