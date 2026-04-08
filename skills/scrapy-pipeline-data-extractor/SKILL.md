---
title: Scrapy Pipeline Data Extractor
description: This skill creates production-ready web scraping pipelines using the
  Scrapy framework. It builds spiders with proper crawl scoping using scrapy.linkextractors.LinkExtractor
  with allow/deny regex patterns, and handles pagination through CrawlSpider rules
  or manual next-page following. Data extraction uses ItemLoader with input/output
  processors like MapCompose and TakeFirst for field normalization, handling common
  tasks like whitespace stripping, price parsing, date normalization, and HTML tag
  removal. Custom Item Pipeline classes handle data validation, deduplication via
  fingerprinting, and storage to multiple backends including PostgreSQL, MongoDB,
  and JSON Lines. The skill handles anti-scraping measures including rotating User-Agent
  headers via scrapy-fake-useragent, request throttling with AutoThrottle middleware,
  and proxy rotation. It supports JavaScript-rendered pages via scrapy-playwright
  integration for SPAs that require browser rendering.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/
category:
- Research &amp; Scraping
framework:
- Gemini
---

# Scrapy Pipeline Data Extractor

This skill creates production-ready web scraping pipelines using the Scrapy framework. It builds spiders with proper crawl scoping using scrapy.linkextractors.LinkExtractor with allow/deny regex patterns, and handles pagination through CrawlSpider rules or manual next-page following. Data extraction uses ItemLoader with input/output processors like MapCompose and TakeFirst for field normalization, handling common tasks like whitespace stripping, price parsing, date normalization, and HTML tag removal. Custom Item Pipeline classes handle data validation, deduplication via fingerprinting, and storage to multiple backends including PostgreSQL, MongoDB, and JSON Lines. The skill handles anti-scraping measures including rotating User-Agent headers via scrapy-fake-useragent, request throttling with AutoThrottle middleware, and proxy rotation. It supports JavaScript-rendered pages via scrapy-playwright integration for SPAs that require browser rendering.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/)
