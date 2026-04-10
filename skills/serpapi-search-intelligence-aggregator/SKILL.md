---
title: "SerpAPI Search Intelligence Aggregator"
description: "Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking."
slug: "serpapi-search-intelligence-aggregator"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/"
---

# SerpAPI Search Intelligence Aggregator

Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking.

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
clawhub install serpapi-search-intelligence-aggregator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The SerpAPI Search Intelligence Aggregator connects to multiple SerpAPI endpoints to extract and analyze search engine results across Google, Bing, YouTube, Google Scholar, and Google Shopping. It uses the Locations API to execute geo-targeted searches from specific cities or regions, enabling local SEO monitoring and competitive analysis. The Searches Archive API provides access to historical SERP data for tracking ranking changes over time without consuming additional API credits. Real-time search results include organic listings, knowledge panels, featured snippets, local packs, image results, and related questions parsed into structured JSON. The agent supports automated keyword monitoring with configurable check frequencies and alert thresholds for ranking position changes. Batch search capabilities process hundreds of keywords efficiently through the Batch Searches API with callback URL notifications on completion. Data is aggregated into trend reports showing visibility scores, SERP feature ownership, and competitive positioning across tracked keyword clusters.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/)
