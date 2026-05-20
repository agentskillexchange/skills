---
name: "Brave Search MCP Server for AI Web Search"
slug: "brave-search-mcp-server-ai-web-search"
description: "The official Brave Search MCP server integrates the Brave Search API with AI assistants, providing comprehensive web search, local business search, image search, video search, news search, and AI-powered summarization capabilities through the Model Context Protocol."
github_stars: 854
verification: "security_reviewed"
source: "https://github.com/brave/brave-search-mcp-server"
author: "brave"
category: "Research & Scraping"
framework: "MCP"
tool_ecosystem:
  github_repo: "brave/brave-search-mcp-server"
  github_stars: 854
  npm_package: "@brave/brave-search-mcp-server"
  npm_weekly_downloads: 19173
---

# Brave Search MCP Server for AI Web Search

The official Brave Search MCP server integrates the Brave Search API with AI assistants, providing comprehensive web search, local business search, image search, video search, news search, and AI-powered summarization capabilities through the Model Context Protocol.

## Installation

Use the upstream install or setup path that matches your environment:
- [![Install with NPX in VS Code](https://img.shields.io/badge/VS_Code-NPM-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=brave-search&inputs=%5B%7...
- [![Install with Docker in VS Code](https://img.shields.io/badge/VS_Code-Docker-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=brave-search&inputs...
- docker build -t mcp/brave-search:latest .
- npm install

Requirements and caveats from upstream:
- **Note:** Requires Pro plan for full local search capabilities. Falls back to web search otherwise.
- node dist/index.js [options]
- #### Docker

Basic usage or getting-started notes:
- **Usage:** First perform a web search with summary: true, then use the returned summary key with this tool.
- Add this to your claude_desktop_config.json:
- json

- Source: https://github.com/brave/brave-search-mcp-server
- Extracted from upstream docs: https://raw.githubusercontent.com/brave/brave-search-mcp-server/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/brave-search-mcp-server-ai-web-search/)
