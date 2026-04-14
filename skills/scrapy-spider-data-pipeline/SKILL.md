---
title: "Scrapy Spider Data Pipeline"
description: "Builds and manages Scrapy web scraping spiders with custom item pipelines. Supports Splash rendering for JavaScript pages, rotating proxies via scrapy-rotating-proxies, and export to MongoDB or Elasticsearch."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
---

# Scrapy Spider Data Pipeline

The Scrapy Spider Data Pipeline creates and manages web scraping workflows using the Scrapy framework with advanced middleware and pipeline configurations. It generates spider classes with CSS and XPath selectors, configures request scheduling, and manages data export pipelines.

JavaScript-rendered pages are handled through Splash integration via scrapy-splash middleware, sending Lua scripts to the Splash HTTP API for page interaction including clicking, scrolling, and waiting for dynamic content. For headless browser needs, Playwright integration via scrapy-playwright provides full browser automation capabilities.

Anti-blocking measures include rotating proxy configuration through scrapy-rotating-proxies with proxy health checking, user agent rotation via scrapy-fake-useragent, and request fingerprinting with scrapy-crawlera for intelligent rate limiting. Retry middleware handles various HTTP error codes and connection timeouts.

Item pipelines support data validation with Scrapy ItemLoaders and input/output processors, deduplication via bloom filters, and export to multiple backends including MongoDB (pymongo), Elasticsearch (elasticsearch-py), PostgreSQL, and JSON Lines files. The skill configures Scrapy settings for concurrent requests, download delays, depth limits, and AutoThrottle for polite crawling. Feed exports support S3 and GCS cloud storage destinations.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/)
