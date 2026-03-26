---
name: "Tavily MCP Server for AI-Powered Web Search and Extraction"
description: "An official MCP server from Tavily that provides AI agents with real-time web search, page extraction, site mapping, and web crawling capabilities. Connects to Tavily's search API to deliver structured, relevant results optimized for LLM consumption."
category: "Research & Scraping"
framework: "MCP"
verification: listed
source: "https://agentskillexchange.com/skills/tavily-mcp-server-ai-web-search-extraction/"
---

# Tavily MCP Server for AI-Powered Web Search and Extraction

An official MCP server from Tavily that provides AI agents with real-time web search, page extraction, site mapping, and web crawling capabilities. Connects to Tavily's search API to deliver structured, relevant results optimized for LLM consumption.

## Installation

### Any Agent (npx)
```bash
npx skills add "tavily-mcp-server-ai-web-search-extraction"
```

### Claude Code
```bash
npx skills add "tavily-mcp-server-ai-web-search-extraction" --claude
```

### Cursor
```bash
npx skills add "tavily-mcp-server-ai-web-search-extraction" --cursor
```

### Codex
```bash
npx skills add "tavily-mcp-server-ai-web-search-extraction" --codex
```

### OpenClaw
```bash
clawhub install "tavily-mcp-server-ai-web-search-extraction"
```

## Overview

The Tavily MCP Server is a production-ready Model Context Protocol server that gives AI agents direct access to Tavily's web intelligence API. Tavily is purpose-built for AI applications, providing search results that are pre-processed and structured for LLM consumption rather than raw HTML pages.

The MCP server exposes four core tools: tavily-search for real-time web search with configurable depth, result count, and domain filtering; tavily-extract for intelligent data extraction from specific URLs; tavily-map for creating structured maps of entire websites; and tavily-crawl for systematically exploring websites and gathering content across multiple pages.

Installation is straightforward via npm (npx tavily-mcp) or through the remote MCP endpoint at mcp.tavily.com. The server supports both stdio and HTTP transport modes, making it compatible with Claude Code, Cursor, Windsurf, VS Code, and other MCP-compatible clients.

Key technical features include configurable search depth, domain inclusion and exclusion filters, image result support, and customizable maximum result counts. The Tavily API key is required (available from tavily.com with a free tier).
