---
name: "ScrapingBee API Data Harvester"
description: "Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/"
---

# ScrapingBee API Data Harvester

Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving.

## Overview

The ScrapingBee API Data Harvester interfaces with the ScrapingBee REST API to handle complex web scraping scenarios without managing browser infrastructure. It uses the render_js parameter for full JavaScript execution on single-page applications and the wait_for CSS selector option to ensure dynamic content loads before extraction. The custom_google parameter enables structured Google SERP parsing with organic results, featured snippets, and People Also Ask data returned as clean JSON. For visual archiving, the screenshot endpoint captures full-page renders at configurable viewport dimensions. The agent manages API credit usage through intelligent request batching and response caching using node-cache with TTL-based expiration. Premium proxy geotargeting enables location-specific content extraction for SEO monitoring and price comparison tasks. Response data is processed through configurable extraction rules using CSS selectors and XPath expressions, with results validated against predefined schemas before storage.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapingbee-api-data-harvester
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapingbee-api-data-harvester -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapingbee-api-data-harvester -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapingbee-api-data-harvester -a codex
```

### OpenClaw

```bash
clawhub install scrapingbee-api-data-harvester
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/
