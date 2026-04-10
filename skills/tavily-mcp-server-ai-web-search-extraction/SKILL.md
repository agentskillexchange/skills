---
title: "Tavily MCP Server for AI-Powered Web Search and Extraction"
description: "An official MCP server from Tavily that provides AI agents with real-time web search, page extraction, site mapping, and web crawling capabilities. Connects to Tavily’s search API to deliver structured, relevant results optimized for LLM consumption."
slug: "tavily-mcp-server-ai-web-search-extraction"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/tavily-ai/tavily-mcp"
tool_ecosystem:
  github_repo: "tavily-ai/tavily-mcp"
  github_stars: 1615
  npm_package: "tavily-mcp"
  npm_weekly_downloads: 47930
listed: true
---

# Tavily MCP Server for AI-Powered Web Search and Extraction

An official MCP server from Tavily that provides AI agents with real-time web search, page extraction, site mapping, and web crawling capabilities. Connects to Tavily’s search API to deliver structured, relevant results optimized for LLM consumption.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install tavily-mcp-server-ai-web-search-extraction
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Tavily MCP Server is a production-ready Model Context Protocol server that gives AI agents direct access to Tavily’s web intelligence API. Tavily is purpose-built for AI applications, providing search results that are pre-processed and structured for LLM consumption rather than raw HTML pages.
The MCP server exposes four core tools: tavily-search for real-time web search with configurable depth (basic or advanced), result count, and domain filtering; tavily-extract for intelligent data extraction from specific URLs, pulling structured content from web pages; tavily-map for creating structured maps of entire websites, useful for understanding site architecture; and tavily-crawl for systematically exploring websites and gathering content across multiple pages.
Installation is straightforward via npm (npx tavily-mcp) or through the remote MCP endpoint at mcp.tavily.com, which eliminates the need for local installation entirely. The server supports both stdio and HTTP transport modes, making it compatible with Claude Code, Cursor, Windsurf, VS Code, and other MCP-compatible clients.
Key technical features include configurable search depth, domain inclusion and exclusion filters, image result support, and customizable maximum result counts. The extract tool handles JavaScript-rendered pages and can pull content from multiple URLs in a single call. The crawl tool supports depth limits and path filtering to control scope.
The Tavily API key is required (available from tavily.com with a free tier). Authentication can be passed via environment variable (TAVILY_API_KEY), URL parameter, or Authorization header. The server is published on npm as tavily-mcp and maintained by the official Tavily AI team.
Common use cases include research agents that need current web information, content extraction pipelines, competitive analysis, and RAG (Retrieval-Augmented Generation) systems that need to ground responses in real-time web data.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tavily-mcp-server-ai-web-search-extraction/)
