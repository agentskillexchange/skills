---
name: "Tavily MCP Server for AI-Powered Web Search and Extraction"
description: "An official MCP server from Tavily that provides AI agents with real-time web search, page extraction, site mapping, and web crawling capabilities. Connects to Tavily's search API to deliver structured, relevant results optimized for LLM consumption."
verification: security_reviewed
source: "https://github.com/tavily-ai/tavily-mcp"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "tavily-ai/tavily-mcp"
  github_stars: 1615
  ase_npm_package: "tavily-mcp"
  npm_weekly_downloads: 47930
---

# Tavily MCP Server for AI-Powered Web Search and Extraction

The Tavily MCP Server is a production-ready Model Context Protocol server that gives AI agents direct access to Tavily's web intelligence API. Tavily is purpose-built for AI applications, providing search results that are pre-processed and structured for LLM consumption rather than raw HTML pages.
The MCP server exposes four core tools: tavily-search for real-time web search with configurable depth (basic or advanced), result count, and domain filtering; tavily-extract for intelligent data extraction from specific URLs, pulling structured content from web pages; tavily-map for creating structured maps of entire websites, useful for understanding site architecture; and tavily-crawl for systematically exploring websites and gathering content across multiple pages.
Installation is straightforward via npm (npx tavily-mcp) or through the remote MCP endpoint at mcp.tavily.com, which eliminates the need for local installation entirely. The server supports both stdio and HTTP transport modes, making it compatible with Claude Code, Cursor, Windsurf, VS Code, and other MCP-compatible clients.
Key technical features include configurable search depth, domain inclusion and exclusion filters, image result support, and customizable maximum result counts. The extract tool handles JavaScript-rendered pages and can pull content from multiple URLs in a single call. The crawl tool supports depth limits and path filtering to control scope.
The Tavily API key is required (available from tavily.com with a free tier). Authentication can be passed via environment variable (TAVILY_API_KEY), URL parameter, or Authorization header. The server is published on npm as tavily-mcp and maintained by the official Tavily AI team.
Common use cases include research agents that need current web information, content extraction pipelines, competitive analysis, and RAG (Retrieval-Augmented Generation) systems that need to ground responses in real-time web data.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tavily-mcp-server-ai-web-search-extraction/)
