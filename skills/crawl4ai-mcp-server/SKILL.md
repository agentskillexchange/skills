---
title: "Crawl4AI MCP Server"
description: "Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free."
verification: "security_reviewed"
source: "https://github.com/sadiuysal/crawl4ai-mcp-server"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sadiuysal/crawl4ai-mcp-server"
  github_stars: 76
  license: "MIT"
---

# Crawl4AI MCP Server

Crawl4AI MCP Server wraps the Crawl4AI open-source web crawling library behind a Model Context Protocol interface. It exposes tools for single-page scraping, multi-page crawling with configurable depth, and sitemap-based crawling. Results come back as clean, LLM-ready markdown.

Best for

Research pipelines and RAG ingestion

Documentation extraction and competitive monitoring

Any workflow needing structured web content without a paid crawling service

How it differs from Firecrawl

Entirely self-hosted and free. No API keys for the crawling layer, no rate limits from a third party, no usage-based charges. Runs locally or in Docker.

Install notes

Clone the repository and install with pip, or pull the Docker image (docker pull uysalsadi/crawl4ai-mcp-server:latest). Configure the server in your MCP client config. Requires Python 3.10+ or Docker. No API key needed.

Source: github.com/sadiuysal/crawl4ai-mcp-server

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawl4ai-mcp-server/)
