---
title: "SerpAPI Search Aggregator"
description: "Aggregates search results from Google, Bing, and DuckDuckGo via the SerpAPI REST endpoint. Parses organic results, knowledge panels, and People Also Ask data into structured JSON for downstream analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-aggregator/"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Aggregator

The SerpAPI Search Aggregator skill connects to the SerpAPI service to pull search engine results from multiple providers simultaneously. It supports Google, Bing, Yahoo, and DuckDuckGo through a unified interface.

The skill handles pagination, location-based filtering (using Google’s uule parameter), and language targeting via the hl and gl parameters. Results are normalized into a consistent schema with fields for title, link, snippet, position, and rich snippet data.

Advanced features include automatic rate limiting with exponential backoff, result deduplication across engines, and caching via Redis or filesystem. The skill can extract Knowledge Graph entities, People Also Ask questions, and Related Searches for comprehensive SERP analysis. Output formats include JSON, CSV, and Markdown tables.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-aggregator/)
