---
title: "SerpAPI Search Results Aggregator"
description: "Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis."
verification: "security_reviewed"
source: "https://serpapi.com/"
category:
  - "Research & Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Results Aggregator

The SerpAPI Search Results Aggregator skill interfaces with the SerpAPI service to programmatically collect search engine results from Google, Bing, DuckDuckGo, Yahoo, and Baidu. It extracts structured data including organic results, featured snippets, knowledge panels, People Also Ask boxes, and local pack listings.

The skill constructs search queries with advanced parameters including geolocation targeting (gl, hl parameters), device type simulation (desktop/mobile/tablet), and safe search configuration. It handles pagination across multiple result pages and deduplicates results across search engines for comprehensive coverage.

Advanced features include SERP feature tracking over time for SEO monitoring, Knowledge Graph entity extraction with Wikidata cross-referencing, and Google Shopping results parsing for price comparison workflows. The skill supports batch query processing with rate limiting, exports results in structured JSON with source attribution, and generates competitive analysis reports comparing domain visibility across target keywords.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/serpapi-search-results-aggregator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-results-aggregator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/serpapi-search-results-aggregator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-results-aggregator/)
