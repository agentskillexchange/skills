---
name: "SerpAPI Search Intelligence Aggregator"
description: "Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/"
---

# SerpAPI Search Intelligence Aggregator

Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking.

## Overview

The SerpAPI Search Intelligence Aggregator connects to multiple SerpAPI endpoints to extract and analyze search engine results across Google, Bing, YouTube, Google Scholar, and Google Shopping. It uses the Locations API to execute geo-targeted searches from specific cities or regions, enabling local SEO monitoring and competitive analysis. The Searches Archive API provides access to historical SERP data for tracking ranking changes over time without consuming additional API credits. Real-time search results include organic listings, knowledge panels, featured snippets, local packs, image results, and related questions parsed into structured JSON. The agent supports automated keyword monitoring with configurable check frequencies and alert thresholds for ranking position changes. Batch search capabilities process hundreds of keywords efficiently through the Batch Searches API with callback URL notifications on completion. Data is aggregated into trend reports showing visibility scores, SERP feature ownership, and competitive positioning across tracked keyword clusters.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-intelligence-aggregator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-intelligence-aggregator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-intelligence-aggregator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-intelligence-aggregator -a codex
```

### OpenClaw

```bash
clawhub install serpapi-search-intelligence-aggregator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/
