---
title: "SerpAPI Search Aggregator"
description: "Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-aggregator/"
category:
  - "Research & Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Aggregator

The SerpAPI Search Aggregator skill connects to the SerpAPI service to pull search engine results from multiple providers simultaneously. It supports Google, Bing, Yahoo, and DuckDuckGo through a unified interface.

The skill handles pagination, location-based filtering (using Google’s uule parameter), and language targeting via the hl and gl parameters. Results are normalized into a consistent schema with fields for title, link, snippet, position, and rich snippet data.

Advanced features include automatic rate limiting with exponential backoff, result deduplication across engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph entities, People Also Ask questions, and Related Searches for comprehensive SERP analysis. Output formats include JSON, CSV, and Markdown tables.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-aggregator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/serpapi-search-aggregator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-aggregator/)
