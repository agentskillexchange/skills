---
title: Scrapy Spider Generator
description: The Scrapy Spider Generator creates production-grade web scraping spiders
  using the Scrapy framework. It generates Spider classes with properly configured
  start_urls, parse methods, and Item definitions with Field declarations and ItemLoader
  processors. The agent builds comprehensive Scrapy projects with settings.py configuration
  for CONCURRENT_REQUESTS, DOWNLOAD_DELAY, and AUTOTHROTTLE settings. It generates
  custom Downloader Middleware for request fingerprinting, proxy rotation via scrapy-rotating-proxies,
  and user-agent randomization using scrapy-fake-useragent. Key features include CrawlSpider
  generation with Rule and LinkExtractor definitions for automated link following,
  SitemapSpider configuration for XML sitemap-based crawling, and Feed Export setup
  for JSON Lines, CSV, and direct database output via scrapy-djangoitem. The agent
  also configures Item Pipelines for data validation, deduplication using scrapy-deltafetch,
  and export to Elasticsearch, MongoDB, or PostgreSQL. Supports Splash integration
  for JavaScript-rendered content via scrapy-splash middleware.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapy-spider-generator/
category:
- Research &amp; Scraping
framework:
- ChatGPT Agents
---

# Scrapy Spider Generator

The Scrapy Spider Generator creates production-grade web scraping spiders using the Scrapy framework. It generates Spider classes with properly configured start_urls, parse methods, and Item definitions with Field declarations and ItemLoader processors. The agent builds comprehensive Scrapy projects with settings.py configuration for CONCURRENT_REQUESTS, DOWNLOAD_DELAY, and AUTOTHROTTLE settings. It generates custom Downloader Middleware for request fingerprinting, proxy rotation via scrapy-rotating-proxies, and user-agent randomization using scrapy-fake-useragent. Key features include CrawlSpider generation with Rule and LinkExtractor definitions for automated link following, SitemapSpider configuration for XML sitemap-based crawling, and Feed Export setup for JSON Lines, CSV, and direct database output via scrapy-djangoitem. The agent also configures Item Pipelines for data validation, deduplication using scrapy-deltafetch, and export to Elasticsearch, MongoDB, or PostgreSQL. Supports Splash integration for JavaScript-rendered content via scrapy-splash middleware.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-generator/)
