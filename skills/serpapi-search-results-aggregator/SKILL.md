---
name: SerpAPI Search Results Aggregator
description: Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect
  SERP features, Knowledge Graph data, and organic results. Supports People Also Ask
  extraction and trend analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/serpapi-search-results-aggregator/
category:
- Research &amp; Scraping
framework:
- OpenClaw
---
# SerpAPI Search Results Aggregator

The SerpAPI Search Results Aggregator skill interfaces with the SerpAPI service to programmatically collect search engine results from Google, Bing, DuckDuckGo, Yahoo, and Baidu. It extracts structured data including organic results, featured snippets, knowledge panels, People Also Ask boxes, and local pack listings.
The skill constructs search queries with advanced parameters including geolocation targeting (gl, hl parameters), device type simulation (desktop/mobile/tablet), and safe search configuration. It handles pagination across multiple result pages and deduplicates results across search engines for comprehensive coverage.
Advanced features include SERP feature tracking over time for SEO monitoring, Knowledge Graph entity extraction with Wikidata cross-referencing, and Google Shopping results parsing for price comparison workflows. The skill supports batch query processing with rate limiting, exports results in structured JSON with source attribution, and generates competitive analysis reports comparing domain visibility across target keywords.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-results-aggregator/)
