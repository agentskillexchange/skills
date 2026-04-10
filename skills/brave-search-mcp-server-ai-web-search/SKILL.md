---
title: "Brave Search MCP Server for AI Web Search"
description: "The official Brave Search MCP server integrates the Brave Search API with AI assistants, providing comprehensive web search, local business search, image search, video search, news search, and AI-powered summarization capabilities through the Model Context Protocol."
slug: "brave-search-mcp-server-ai-web-search"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/brave/brave-search-mcp-server"
tool_ecosystem:
  github_repo: "brave/brave-search-mcp-server"
  github_stars: 854
listed: true
---

# Brave Search MCP Server for AI Web Search

The official Brave Search MCP server integrates the Brave Search API with AI assistants, providing comprehensive web search, local business search, image search, video search, news search, and AI-powered summarization capabilities through the Model Context Protocol.

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
clawhub install brave-search-mcp-server-ai-web-search
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Brave Search MCP Server is the official Model Context Protocol integration for the Brave Search API, maintained by Brave Software. It provides AI assistants and coding agents with comprehensive search capabilities including web search, local business discovery, image search, video search, news search, and AI-powered answer summarization — all through standard MCP tool calls.
The server exposes several specialized search tools. brave_web_search performs comprehensive web searches with rich result types and advanced filtering including country, language, safe search, freshness, and custom Goggles re-ranking definitions. brave_local_search finds local businesses and places with detailed ratings, hours, and AI-generated descriptions. brave_image_search and brave_video_search provide targeted media search with comprehensive metadata. brave_news_search surfaces current events, while brave_summarize delivers AI-generated summaries grounded on search results for reduced hallucination.
Version 2.x improved performance by removing base64-encoded image data from responses, returning a leaner response object that closely mirrors the original Brave Search API structure. The server supports both STDIO (default) and HTTP transports, configurable via the BRAVE_MCP_TRANSPORT environment variable or --transport runtime argument. Installation is available through npm (npx @anthropic-ai/brave-search-mcp) or Docker, and it requires a Brave Search API key from the developer dashboard.
This MCP server is particularly valuable for AI agents that need grounded, real-time information retrieval. By providing search results through the standardized MCP protocol, it enables any MCP-compatible client — Claude Desktop, Cursor, VS Code Copilot, Windsurf, and others — to perform web research without custom API integration code. The Pro plan unlocks additional features like extra snippets and full local search capabilities.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/brave-search-mcp-server-ai-web-search/)
