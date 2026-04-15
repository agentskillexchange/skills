---
title: "ScrapingBee API Data Harvester"
description: "Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
---

# ScrapingBee API Data Harvester

The ScrapingBee API Data Harvester interfaces with the ScrapingBee REST API to handle complex web scraping scenarios without managing browser infrastructure. It uses the render_js parameter for full JavaScript execution on single-page applications and the wait_for CSS selector option to ensure dynamic content loads before extraction. The custom_google parameter enables structured Google SERP parsing with organic results, featured snippets, and People Also Ask data returned as clean JSON. For visual archiving, the screenshot endpoint captures full-page renders at configurable viewport dimensions. The agent manages API credit usage through intelligent request batching and response caching using node-cache with TTL-based expiration. Premium proxy geotargeting enables location-specific content extraction for SEO monitoring and price comparison tasks. Response data is processed through configurable extraction rules using CSS selectors and XPath expressions, with results validated against predefined schemas before storage.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapingbee-api-data-harvester
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scrapingbee-api-data-harvester` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/)
