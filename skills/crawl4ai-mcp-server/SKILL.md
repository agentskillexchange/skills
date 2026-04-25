---
title: "Crawl4AI MCP Server"
description: "Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free."
verification: "security_reviewed"
source: "https://github.com/sadiuysal/crawl4ai-mcp-server"
category:
  - "Data Extraction & Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sadiuysal/crawl4ai-mcp-server"
  github_stars: 82
---

# Crawl4AI MCP Server

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

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/crawl4ai-mcp-server/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crawl4ai-mcp-server
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/crawl4ai-mcp-server`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawl4ai-mcp-server/)
