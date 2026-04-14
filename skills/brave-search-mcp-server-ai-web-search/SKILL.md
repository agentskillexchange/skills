---
title: "Brave Search MCP Server for AI Web Search"
description: "The official Brave Search MCP server integrates the Brave Search API with AI assistants, providing comprehensive web search, local business search, image search, video search, news search, and AI-powered summarization capabilities through the Model Context Protocol."
verification: security_reviewed
source: "https://github.com/brave/brave-search-mcp-server"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "brave/brave-search-mcp-server"
  github_stars: 854
---

# Brave Search MCP Server for AI Web Search

The Brave Search MCP Server is the official Model Context Protocol integration for the Brave Search API, maintained by Brave Software. It provides AI assistants and coding agents with comprehensive search capabilities including web search, local business discovery, image search, video search, news search, and AI-powered answer summarization — all through standard MCP tool calls.

The server exposes several specialized search tools. brave_web_search performs comprehensive web searches with rich result types and advanced filtering including country, language, safe search, freshness, and custom Goggles re-ranking definitions. brave_local_search finds local businesses and places with detailed ratings, hours, and AI-generated descriptions. brave_image_search and brave_video_search provide targeted media search with comprehensive metadata. brave_news_search surfaces current events, while brave_summarize delivers AI-generated summaries grounded on search results for reduced hallucination.

Version 2.x improved performance by removing base64-encoded image data from responses, returning a leaner response object that closely mirrors the original Brave Search API structure. The server supports both STDIO (default) and HTTP transports, configurable via the BRAVE_MCP_TRANSPORT environment variable or --transport runtime argument. Installation is available through npm (npx @anthropic-ai/brave-search-mcp) or Docker, and it requires a Brave Search API key from the developer dashboard.

This MCP server is particularly valuable for AI agents that need grounded, real-time information retrieval. By providing search results through the standardized MCP protocol, it enables any MCP-compatible client — Claude Desktop, Cursor, VS Code Copilot, Windsurf, and others — to perform web research without custom API integration code. The Pro plan unlocks additional features like extra snippets and full local search capabilities.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/brave-search-mcp-server-ai-web-search/)
