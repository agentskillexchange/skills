---
title: "SerpAPI Search Pipeline"
description: "Automates multi-engine searches via SerpAPI (Google, Bing, DuckDuckGo) with structured JSON extraction. Supports pagination, location targeting, and result deduplication using MinHash LSH."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/serpapi-search-pipeline/"
category:
  - "Research & Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Pipeline

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer. Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content. The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically. Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/serpapi-search-pipeline/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-pipeline
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/serpapi-search-pipeline`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-pipeline/)
