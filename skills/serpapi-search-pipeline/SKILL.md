---
title: SerpAPI Search Pipeline
description: The SerpAPI Search Pipeline skill provides a comprehensive interface
  for automated web research through the SerpAPI service. It connects to Google Search,
  Bing, DuckDuckGo, and Yahoo engines via a unified API layer. Key capabilities include
  automatic pagination handling across result sets, geographic targeting using UULE
  parameters for location-specific results, and intelligent result deduplication using
  MinHash Locality-Sensitive Hashing to eliminate near-duplicate content. The skill
  supports structured output in JSON, CSV, and Markdown table formats. It includes
  rate limiting with exponential backoff, proxy rotation support, and cached result
  storage using SQLite for repeat queries. SERP feature extraction captures knowledge
  panels, featured snippets, and People Also Ask data automatically. Configuration
  supports custom extraction rules via CSS selectors and XPath expressions for specialized
  data capture beyond standard search results.
verification: security_reviewed
source: https://agentskillexchange.com/skills/serpapi-search-pipeline/
category:
- Research &amp; Scraping
framework:
- OpenClaw
---

# SerpAPI Search Pipeline

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer. Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content. The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically. Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-pipeline/)
