---
title: "SerpAPI Search Pipeline"
description: "The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer.\nKey capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content.\nThe skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically.\nConfiguration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-pipeline/"
framework:
  - "OpenClaw"
---

# SerpAPI Search Pipeline

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer.
Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content.
The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically.
Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/serpapi-search-pipeline
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/serpapi-search-pipeline` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-pipeline/)
