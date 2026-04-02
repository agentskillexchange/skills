---
name: "Crawl4AI MCP Server"
description: "Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free."
category: "Data Extraction & Transformation"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/crawl4ai-mcp-server/"
tool_ecosystem:
  github_repo: "sadiuysal/crawl4ai-mcp-server"
  github_stars: 69
---
# Crawl4AI MCP Server

Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free.

## Overview

Crawl4AI MCP Server wraps the Crawl4AI open-source web crawling library behind a Model Context Protocol interface. It exposes tools for single-page scraping, multi-page crawling with configurable depth, and sitemap-based crawling. Results come back as clean, LLM-ready markdown.

Best for

- Research pipelines and RAG ingestion

- Documentation extraction and competitive monitoring

- Any workflow needing structured web content without a paid crawling service

How it differs from Firecrawl

Entirely self-hosted and free. No API keys for the crawling layer, no rate limits from a third party, no usage-based charges. Runs locally or in Docker.

Install notes

Clone the repository and install with pip, or pull the Docker image (`docker pull uysalsadi/crawl4ai-mcp-server:latest`). Configure the server in your MCP client config. Requires Python 3.10+ or Docker. No API key needed.

Source: github.com/sadiuysal/crawl4ai-mcp-server

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill crawl4ai-mcp-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill crawl4ai-mcp-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill crawl4ai-mcp-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill crawl4ai-mcp-server -a codex
```

### OpenClaw

```bash
clawhub install crawl4ai-mcp-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawl4ai-mcp-server/)
