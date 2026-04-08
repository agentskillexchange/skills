---
title: Scrapy Spider Data Pipeline
description: The Scrapy Spider Data Pipeline creates and manages web scraping workflows
  using the Scrapy framework with advanced middleware and pipeline configurations.
  It generates spider classes with CSS and XPath selectors, configures request scheduling,
  and manages data export pipelines. JavaScript-rendered pages are handled through
  Splash integration via scrapy-splash middleware, sending Lua scripts to the Splash
  HTTP API for page interaction including clicking, scrolling, and waiting for dynamic
  content. For headless browser needs, Playwright integration via scrapy-playwright
  provides full browser automation capabilities. Anti-blocking measures include rotating
  proxy configuration through scrapy-rotating-proxies with proxy health checking,
  user agent rotation via scrapy-fake-useragent, and request fingerprinting with scrapy-crawlera
  for intelligent rate limiting. Retry middleware handles various HTTP error codes
  and connection timeouts. Item pipelines support data validation with Scrapy ItemLoaders
  and input/output processors, deduplication via bloom filters, and export to multiple
  backends including MongoDB (pymongo), Elasticsearch (elasticsearch-py), PostgreSQL,
  and JSON Lines files. The skill configures Scrapy settings for concurrent requests,
  download delays, depth limits, and AutoThrottle for polite crawling. Feed exports
  support S3 and GCS cloud storage destinations.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/
category:
- Data Extraction &amp; Transformation
framework:
- Cursor
---

# Scrapy Spider Data Pipeline

The Scrapy Spider Data Pipeline creates and manages web scraping workflows using the Scrapy framework with advanced middleware and pipeline configurations. It generates spider classes with CSS and XPath selectors, configures request scheduling, and manages data export pipelines. JavaScript-rendered pages are handled through Splash integration via scrapy-splash middleware, sending Lua scripts to the Splash HTTP API for page interaction including clicking, scrolling, and waiting for dynamic content. For headless browser needs, Playwright integration via scrapy-playwright provides full browser automation capabilities. Anti-blocking measures include rotating proxy configuration through scrapy-rotating-proxies with proxy health checking, user agent rotation via scrapy-fake-useragent, and request fingerprinting with scrapy-crawlera for intelligent rate limiting. Retry middleware handles various HTTP error codes and connection timeouts. Item pipelines support data validation with Scrapy ItemLoaders and input/output processors, deduplication via bloom filters, and export to multiple backends including MongoDB (pymongo), Elasticsearch (elasticsearch-py), PostgreSQL, and JSON Lines files. The skill configures Scrapy settings for concurrent requests, download delays, depth limits, and AutoThrottle for polite crawling. Feed exports support S3 and GCS cloud storage destinations.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/)
