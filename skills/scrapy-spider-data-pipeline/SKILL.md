---
title: "Scrapy Spider Data Pipeline"
description: "Builds and manages Scrapy web scraping spiders with custom item pipelines. Supports Splash rendering for JavaScript pages, rotating proxies via scrapy-rotating-proxies, and export to MongoDB or Elasticsearch."
verification: "security_reviewed"
source: "https://github.com/scrapy/scrapy"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
  license: "BSD-3-Clause"
---

# Scrapy Spider Data Pipeline

The Scrapy Spider Data Pipeline creates and manages web scraping workflows using the Scrapy framework with advanced middleware and pipeline configurations. It generates spider classes with CSS and XPath selectors, configures request scheduling, and manages data export pipelines.

JavaScript-rendered pages are handled through Splash integration via scrapy-splash middleware, sending Lua scripts to the Splash HTTP API for page interaction including clicking, scrolling, and waiting for dynamic content. For headless browser needs, Playwright integration via scrapy-playwright provides full browser automation capabilities.

Anti-blocking measures include rotating proxy configuration through scrapy-rotating-proxies with proxy health checking, user agent rotation via scrapy-fake-useragent, and request fingerprinting with scrapy-crawlera for intelligent rate limiting. Retry middleware handles various HTTP error codes and connection timeouts.

Item pipelines support data validation with Scrapy ItemLoaders and input/output processors, deduplication via bloom filters, and export to multiple backends including MongoDB (pymongo), Elasticsearch (elasticsearch-py), PostgreSQL, and JSON Lines files. The skill configures Scrapy settings for concurrent requests, download delays, depth limits, and AutoThrottle for polite crawling. Feed exports support S3 and GCS cloud storage destinations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/)
