---
title: "SerpAPI Search Pipeline"
description: "The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer. Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content. The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically. Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results."
source: "https://agentskillexchange.com/skills/serpapi-search-pipeline/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Pipeline

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer. Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content. The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically. Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-pipeline/)
