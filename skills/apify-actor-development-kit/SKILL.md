---
name: "Apify Actor Development Kit"
description: "Builds Apify Actors for scalable cloud scraping with automatic proxy management and storage. Uses the Apify SDK (Actor, Dataset, KeyValueStore, RequestQueue) and Crawlee library for robust crawling."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apify-actor-development-kit/"
tool_ecosystem:
  tool: apify
  github_stars: 172
  npm_weekly_downloads: 44900
  github_repo: apify/apify-sdk-js
  license: Apache-2.0
  maintained: true
---

# Apify Actor Development Kit

Builds Apify Actors for scalable cloud scraping with automatic proxy management and storage. Uses the Apify SDK (Actor, Dataset, KeyValueStore, RequestQueue) and Crawlee library for robust crawling.

## Overview

The Apify Actor Development Kit creates scalable web scraping actors using the Apify SDK and Crawlee library. It generates Actor configurations with proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment to the Apify Cloud platform.

The agent leverages Crawlee crawlers including PlaywrightCrawler for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler for API endpoint scraping. It configures RequestQueue for URL frontier management with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing.

Advanced features include Apify Proxy integration with automatic session rotation using ProxyConfiguration with groups and countryCode targeting. The agent sets up Dataset.pushData for structured output storage, KeyValueStore for state persistence across migrations, and implements AutoscaledPool configuration for dynamic concurrency adjustment based on system resources. It also generates Actor input schemas with validation constraints and default values for the Apify Console UI.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apify-actor-development-kit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apify-actor-development-kit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apify-actor-development-kit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apify-actor-development-kit -a codex
```

### OpenClaw

```bash
clawhub install apify-actor-development-kit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/apify-actor-development-kit/
