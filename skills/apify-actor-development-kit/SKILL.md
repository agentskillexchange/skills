---
title: "Apify Actor Development Kit"
description: "Builds Apify Actors for scalable cloud scraping with automatic proxy management and storage. Uses the Apify SDK (Actor, Dataset, KeyValueStore, RequestQueue) and Crawlee library for robust crawling."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Development Kit

The Apify Actor Development Kit creates scalable web scraping actors using the Apify SDK and Crawlee library. It generates Actor configurations with proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment to the Apify Cloud platform. The agent leverages Crawlee crawlers including PlaywrightCrawler for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler for API endpoint scraping. It configures RequestQueue for URL frontier management with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing. Advanced features include Apify Proxy integration with automatic session rotation using ProxyConfiguration with groups and countryCode targeting. The agent sets up Dataset.pushData for structured output storage, KeyValueStore for state persistence across migrations, and implements AutoscaledPool configuration for dynamic concurrency adjustment based on system resources. It also generates Actor input schemas with validation constraints and default values for the Apify Console UI.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apify-actor-development-kit/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-actor-development-kit
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apify-actor-development-kit`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-development-kit/)
