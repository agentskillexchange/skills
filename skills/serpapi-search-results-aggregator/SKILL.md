---
title: "SerpAPI Search Results Aggregator"
description: "Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-results-aggregator/"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Results Aggregator

The SerpAPI Search Results Aggregator skill interfaces with the SerpAPI service to programmatically collect search engine results from Google, Bing, DuckDuckGo, Yahoo, and Baidu. It extracts structured data including organic results, featured snippets, knowledge panels, People Also Ask boxes, and local pack listings.

The skill constructs search queries with advanced parameters including geolocation targeting (gl, hl parameters), device type simulation (desktop/mobile/tablet), and safe search configuration. It handles pagination across multiple result pages and deduplicates results across search engines for comprehensive coverage.

Advanced features include SERP feature tracking over time for SEO monitoring, Knowledge Graph entity extraction with Wikidata cross-referencing, and Google Shopping results parsing for price comparison workflows. The skill supports batch query processing with rate limiting, exports results in structured JSON with source attribution, and generates competitive analysis reports comparing domain visibility across target keywords.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-results-aggregator/)
