---
title: "SerpAPI Search Pipeline"
description: "Automates multi-engine searches via SerpAPI (Google, Bing, DuckDuckGo) with structured JSON extraction. Supports pagination, location targeting, and result deduplication using MinHash LSH."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-pipeline/"
category:
  - "Research &amp; Scraping"
framework:
  - "OpenClaw"
---

# SerpAPI Search Pipeline

The SerpAPI Search Pipeline skill provides a comprehensive interface for automated web research through the SerpAPI service. It connects to Google Search, Bing, DuckDuckGo, and Yahoo engines via a unified API layer.

Key capabilities include automatic pagination handling across result sets, geographic targeting using UULE parameters for location-specific results, and intelligent result deduplication using MinHash Locality-Sensitive Hashing to eliminate near-duplicate content.

The skill supports structured output in JSON, CSV, and Markdown table formats. It includes rate limiting with exponential backoff, proxy rotation support, and cached result storage using SQLite for repeat queries. SERP feature extraction captures knowledge panels, featured snippets, and People Also Ask data automatically.

Configuration supports custom extraction rules via CSS selectors and XPath expressions for specialized data capture beyond standard search results.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-pipeline/)
