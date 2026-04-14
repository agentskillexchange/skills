---
title: "SerpAPI Search Intelligence Aggregator"
description: "Connects to SerpAPI endpoints for Google, Bing, YouTube, and Google Scholar search result extraction. Uses the Locations API for geo-targeted queries and Searches Archive API for historical SERP tracking."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
---

# SerpAPI Search Intelligence Aggregator

The SerpAPI Search Intelligence Aggregator connects to multiple SerpAPI endpoints to extract and analyze search engine results across Google, Bing, YouTube, Google Scholar, and Google Shopping. It uses the Locations API to execute geo-targeted searches from specific cities or regions, enabling local SEO monitoring and competitive analysis. The Searches Archive API provides access to historical SERP data for tracking ranking changes over time without consuming additional API credits. Real-time search results include organic listings, knowledge panels, featured snippets, local packs, image results, and related questions parsed into structured JSON. The agent supports automated keyword monitoring with configurable check frequencies and alert thresholds for ranking position changes. Batch search capabilities process hundreds of keywords efficiently through the Batch Searches API with callback URL notifications on completion. Data is aggregated into trend reports showing visibility scores, SERP feature ownership, and competitive positioning across tracked keyword clusters.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/serpapi-search-intelligence-aggregator/)
