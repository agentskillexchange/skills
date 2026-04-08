---
title: SerpAPI Search Aggregator
description: The SerpAPI Search Aggregator skill connects to the SerpAPI service to
  pull search engine results from multiple providers simultaneously. It supports Google,
  Bing, Yahoo, and DuckDuckGo through a unified interface. The skill handles pagination,
  location-based filtering (using Google’s uule parameter), and language targeting
  via the hl and gl parameters. Results are normalized into a consistent schema with
  fields for title, link, snippet, position, and rich snippet data. Advanced features
  include automatic rate limiting with exponential backoff, result deduplication across
  engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph
  entities, People Also Ask questions, and Related Searches for comprehensive SERP
  analysis. Output formats include JSON, CSV, and Markdown tables.
verification: security_reviewed
source: https://agentskillexchange.com/skills/serpapi-search-aggregator/
category:
- Research &amp; Scraping
framework:
- OpenClaw
---

# SerpAPI Search Aggregator

The SerpAPI Search Aggregator skill connects to the SerpAPI service to pull search engine results from multiple providers simultaneously. It supports Google, Bing, Yahoo, and DuckDuckGo through a unified interface. The skill handles pagination, location-based filtering (using Google’s uule parameter), and language targeting via the hl and gl parameters. Results are normalized into a consistent schema with fields for title, link, snippet, position, and rich snippet data. Advanced features include automatic rate limiting with exponential backoff, result deduplication across engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph entities, People Also Ask questions, and Related Searches for comprehensive SERP analysis. Output formats include JSON, CSV, and Markdown tables.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-aggregator/)
