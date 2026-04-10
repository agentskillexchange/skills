---
title: "Crawl4AI MCP Server"
description: "Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free."
slug: "crawl4ai-mcp-server"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://github.com/sadiuysal/crawl4ai-mcp-server"
tool_ecosystem:
  github_repo: "sadiuysal/crawl4ai-mcp-server"
  github_stars: 72
---

# Crawl4AI MCP Server

Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free.

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
clawhub install crawl4ai-mcp-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Crawl4AI MCP Server wraps the Crawl4AI open-source web crawling library behind a Model Context Protocol interface. It exposes tools for single-page scraping, multi-page crawling with configurable depth, and sitemap-based crawling. Results come back as clean, LLM-ready markdown.
Best for
- Research pipelines and RAG ingestion
- Documentation extraction and competitive monitoring
- Any workflow needing structured web content without a paid crawling service
How it differs from Firecrawl
Entirely self-hosted and free. No API keys for the crawling layer, no rate limits from a third party, no usage-based charges. Runs locally or in Docker.
Install notes
Clone the repository and install with pip, or pull the Docker image (docker pull uysalsadi/crawl4ai-mcp-server:latest). Configure the server in your MCP client config. Requires Python 3.10+ or Docker. No API key needed.
Source: github.com/sadiuysal/crawl4ai-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawl4ai-mcp-server/)
