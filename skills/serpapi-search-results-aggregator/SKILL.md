---
name: "SerpAPI Search Results Aggregator"
description: "Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis."
category: "Research & Scraping"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-results-aggregator/"
---
# SerpAPI Search Results Aggregator

Queries Google, Bing, and DuckDuckGo search APIs through SerpAPI to collect SERP features, Knowledge Graph data, and organic results. Supports People Also Ask extraction and trend analysis.

The SerpAPI Search Results Aggregator skill interfaces with the SerpAPI service to programmatically collect search engine results from Google, Bing, DuckDuckGo, Yahoo, and Baidu. It extracts structured data including organic results, featured snippets, knowledge panels, People Also Ask boxes, and local pack listings.



The skill constructs search queries with advanced parameters including geolocation targeting (gl, hl parameters), device type simulation (desktop/mobile/tablet), and safe search configuration. It handles pagination across multiple result pages and deduplicates results across search engines for comprehensive coverage.



Advanced features include SERP feature tracking over time for SEO monitoring, Knowledge Graph entity extraction with Wikidata cross-referencing, and Google Shopping results parsing for price comparison workflows. The skill supports batch query processing with rate limiting, exports results in structured JSON with source attribution, and generates competitive analysis reports comparing domain visibility across target keywords.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-results-aggregator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-results-aggregator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-results-aggregator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill serpapi-search-results-aggregator -a codex
```

### OpenClaw

```bash
clawhub install serpapi-search-results-aggregator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-results-aggregator/)
