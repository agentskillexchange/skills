---
title: "ScrapingBee API Data Harvester"
description: "Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving."
slug: "scrapingbee-api-data-harvester"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/"
---

# ScrapingBee API Data Harvester

Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install scrapingbee-api-data-harvester
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ScrapingBee API Data Harvester interfaces with the ScrapingBee REST API to handle complex web scraping scenarios without managing browser infrastructure. It uses the render_js parameter for full JavaScript execution on single-page applications and the wait_for CSS selector option to ensure dynamic content loads before extraction. The custom_google parameter enables structured Google SERP parsing with organic results, featured snippets, and People Also Ask data returned as clean JSON. For visual archiving, the screenshot endpoint captures full-page renders at configurable viewport dimensions. The agent manages API credit usage through intelligent request batching and response caching using node-cache with TTL-based expiration. Premium proxy geotargeting enables location-specific content extraction for SEO monitoring and price comparison tasks. Response data is processed through configurable extraction rules using CSS selectors and XPath expressions, with results validated against predefined schemas before storage.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/)
