---
title: "SerpAPI Search Aggregator"
description: "Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis."
slug: "serpapi-search-aggregator"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-search-aggregator/"
---

# SerpAPI Search Aggregator

Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis.

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
clawhub install serpapi-search-aggregator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SerpAPI Search Aggregator skill connects to the SerpAPI service to pull search engine results from multiple providers simultaneously. It supports Google, Bing, Yahoo, and DuckDuckGo through a unified interface.
The skill handles pagination, location-based filtering (using Google’s uule parameter), and language targeting via the hl and gl parameters. Results are normalized into a consistent schema with fields for title, link, snippet, position, and rich snippet data.
Advanced features include automatic rate limiting with exponential backoff, result deduplication across engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph entities, People Also Ask questions, and Related Searches for comprehensive SERP analysis. Output formats include JSON, CSV, and Markdown tables.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-aggregator/)
