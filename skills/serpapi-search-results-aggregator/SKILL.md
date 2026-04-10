---
title: "SerpAPI Search Results Aggregator"
description: "Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis."
slug: "serpapi-search-results-aggregator"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-search-results-aggregator/"
---

# SerpAPI Search Results Aggregator

Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis.

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
clawhub install serpapi-search-results-aggregator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SerpAPI Search Results Aggregator skill interfaces with the SerpAPI service to programmatically collect search engine results from Google, Bing, DuckDuckGo, Yahoo, and Baidu. It extracts structured data including organic results, featured snippets, knowledge panels, People Also Ask boxes, and local pack listings.
The skill constructs search queries with advanced parameters including geolocation targeting (gl, hl parameters), device type simulation (desktop/mobile/tablet), and safe search configuration. It handles pagination across multiple result pages and deduplicates results across search engines for comprehensive coverage.
Advanced features include SERP feature tracking over time for SEO monitoring, Knowledge Graph entity extraction with Wikidata cross-referencing, and Google Shopping results parsing for price comparison workflows. The skill supports batch query processing with rate limiting, exports results in structured JSON with source attribution, and generates competitive analysis reports comparing domain visibility across target keywords.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-results-aggregator/)
