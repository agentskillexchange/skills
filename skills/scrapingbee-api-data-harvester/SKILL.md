---
title: "ScrapingBee API Data Harvester"
description: "Interfaces with the ScrapingBee REST API for JavaScript rendering and Google SERP extraction. Uses custom_google parameter for search result parsing and screenshot endpoint for visual page archiving."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
---

# ScrapingBee API Data Harvester

The ScrapingBee API Data Harvester interfaces with the ScrapingBee REST API to handle complex web scraping scenarios without managing browser infrastructure. It uses the render_js parameter for full JavaScript execution on single-page applications and the wait_for CSS selector option to ensure dynamic content loads before extraction. The custom_google parameter enables structured Google SERP parsing with organic results, featured snippets, and People Also Ask data returned as clean JSON. For visual archiving, the screenshot endpoint captures full-page renders at configurable viewport dimensions. The agent manages API credit usage through intelligent request batching and response caching using node-cache with TTL-based expiration. Premium proxy geotargeting enables location-specific content extraction for SEO monitoring and price comparison tasks. Response data is processed through configurable extraction rules using CSS selectors and XPath expressions, with results validated against predefined schemas before storage.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapingbee-api-data-harvester/)
