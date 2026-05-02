---
title: "SerpAPI Search Intelligence Aggregator"
description: "Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking."
verification: "security_reviewed"
source: "https://serpapi.com/"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
---

# SerpAPI Search Intelligence Aggregator

The SerpAPI Search Intelligence Aggregator connects to multiple SerpAPI endpoints to extract and analyze search engine results across Google, Bing, YouTube, Google Scholar, and Google Shopping. It uses the Locations API to execute geo-targeted searches from specific cities or regions, enabling local SEO monitoring and competitive analysis. The Searches Archive API provides access to historical SERP data for tracking ranking changes over time without consuming additional API credits. Real-time search results include organic listings, knowledge panels, featured snippets, local packs, image results, and related questions parsed into structured JSON. The agent supports automated keyword monitoring with configurable check frequencies and alert thresholds for ranking position changes. Batch search capabilities process hundreds of keywords efficiently through the Batch Searches API with callback URL notifications on completion. Data is aggregated into trend reports showing visibility scores, SERP feature ownership, and competitive positioning across tracked keyword clusters.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-intelligence-aggregator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/serpapi-search-intelligence-aggregator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/)
