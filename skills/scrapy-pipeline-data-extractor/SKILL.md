---
name: "Scrapy Pipeline Data Extractor"
description: "Builds production Scrapy spiders with custom Item Pipelines for data cleaning and storage. Uses scrapy.linkextractors.LinkExtractor for crawl scoping and ItemLoader with MapCompose processors for field normalization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/"
category:
  - "Research &amp; Scraping"
framework:
  - "Gemini"
---

# Scrapy Pipeline Data Extractor

This skill creates production-ready web scraping pipelines using the Scrapy framework. It builds spiders with proper crawl scoping using scrapy.linkextractors.LinkExtractor with allow/deny regex patterns, and handles pagination through CrawlSpider rules or manual next-page following.
Data extraction uses ItemLoader with input/output processors like MapCompose and TakeFirst for field normalization, handling common tasks like whitespace stripping, price parsing, date normalization, and HTML tag removal. Custom Item Pipeline classes handle data validation, deduplication via fingerprinting, and storage to multiple backends including PostgreSQL, MongoDB, and JSON Lines.
The skill handles anti-scraping measures including rotating User-Agent headers via scrapy-fake-useragent, request throttling with AutoThrottle middleware, and proxy rotation. It supports JavaScript-rendered pages via scrapy-playwright integration for SPAs that require browser rendering.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/)
