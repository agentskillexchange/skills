---
title: "SerpAPI Search Intelligence Aggregator"
description: "Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
---

# SerpAPI Search Intelligence Aggregator

The SerpAPI Search Intelligence Aggregator connects to multiple SerpAPI endpoints to extract and analyze search engine results across Google, Bing, YouTube, Google Scholar, and Google Shopping. It uses the Locations API to execute geo-targeted searches from specific cities or regions, enabling local SEO monitoring and competitive analysis. The Searches Archive API provides access to historical SERP data for tracking ranking changes over time without consuming additional API credits. Real-time search results include organic listings, knowledge panels, featured snippets, local packs, image results, and related questions parsed into structured JSON. The agent supports automated keyword monitoring with configurable check frequencies and alert thresholds for ranking position changes. Batch search capabilities process hundreds of keywords efficiently through the Batch Searches API with callback URL notifications on completion. Data is aggregated into trend reports showing visibility scores, SERP feature ownership, and competitive positioning across tracked keyword clusters.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-intelligence-aggregator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/serpapi-search-intelligence-aggregator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/)
