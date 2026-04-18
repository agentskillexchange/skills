---
title: "Scrapy Pipeline Data Extractor"
description: "Builds production Scrapy spiders with custom Item Pipelines for data cleaning and storage. Uses scrapy.linkextractors.LinkExtractor for crawl scoping and ItemLoader with MapCompose processors for field normalization."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
category:
  - "Research & Scraping"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
---

# Scrapy Pipeline Data Extractor

This skill creates production-ready web scraping pipelines using the Scrapy framework. It builds spiders with proper crawl scoping using scrapy.linkextractors.LinkExtractor with allow/deny regex patterns, and handles pagination through CrawlSpider rules or manual next-page following.

Data extraction uses ItemLoader with input/output processors like MapCompose and TakeFirst for field normalization, handling common tasks like whitespace stripping, price parsing, date normalization, and HTML tag removal. Custom Item Pipeline classes handle data validation, deduplication via fingerprinting, and storage to multiple backends including PostgreSQL, MongoDB, and JSON Lines.

The skill handles anti-scraping measures including rotating User-Agent headers via scrapy-fake-useragent, request throttling with AutoThrottle middleware, and proxy rotation. It supports JavaScript-rendered pages via scrapy-playwright integration for SPAs that require browser rendering.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapy-pipeline-data-extractor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scrapy-pipeline-data-extractor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/)
