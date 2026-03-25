---
name: "SerpAPI Search Aggregator"
description: "Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis."
category: "Research & Scraping"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-aggregator/"
tool_ecosystem:
  tool: "redis"
  github_stars: 73523
  npm_weekly_downloads: 8224050
  github_repo: "redis/redis"
  maintained: true
---

# SerpAPI Search Aggregator

Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis.

## Overview

The SerpAPI Search Aggregator skill connects to the SerpAPI service to pull search engine results from multiple providers simultaneously. It supports Google, Bing, Yahoo, and DuckDuckGo through a unified interface.

The skill handles pagination, location-based filtering (using Google’s uule parameter), and language targeting via the hl and gl parameters. Results are normalized into a consistent schema with fields for title, link, snippet, position, and rich snippet data.

Advanced features include automatic rate limiting with exponential backoff, result deduplication across engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph entities, People Also Ask questions, and Related Searches for comprehensive SERP analysis. Output formats include JSON, CSV, and Markdown tables.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-aggregator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-aggregator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-aggregator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-aggregator -a codex
```

### OpenClaw

```bash
clawhub install serpapi-search-aggregator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/serpapi-search-aggregator/
