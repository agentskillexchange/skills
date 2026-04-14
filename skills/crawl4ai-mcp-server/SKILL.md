---
title: "Crawl4AI MCP Server"
description: "Self-hosted web crawling and content extraction exposed as MCP tools. Scrape pages, crawl sites with depth control, and extract clean markdown — all self-hosted and free."
verification: security_reviewed
source: "https://github.com/sadiuysal/crawl4ai-mcp-server"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "sadiuysal/crawl4ai-mcp-server"
  github_stars: 75
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawl4ai-mcp-server/)
