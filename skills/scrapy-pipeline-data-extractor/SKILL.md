---
name: "Scrapy Pipeline Data Extractor"
description: "Builds production Scrapy spiders with custom Item Pipelines for data cleaning and storage. Uses scrapy.linkextractors.LinkExtractor for crawl scoping and ItemLoader with MapCompose processors for field normalization."
category: "Research & Scraping"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/"
---
# Scrapy Pipeline Data Extractor

Builds production Scrapy spiders with custom Item Pipelines for data cleaning and storage. Uses scrapy.linkextractors.LinkExtractor for crawl scoping and ItemLoader with MapCompose processors for field normalization.

## Overview

This skill creates production-ready web scraping pipelines using the Scrapy framework. It builds spiders with proper crawl scoping using scrapy.linkextractors.LinkExtractor with allow/deny regex patterns, and handles pagination through CrawlSpider rules or manual next-page following.

Data extraction uses ItemLoader with input/output processors like MapCompose and TakeFirst for field normalization, handling common tasks like whitespace stripping, price parsing, date normalization, and HTML tag removal. Custom Item Pipeline classes handle data validation, deduplication via fingerprinting, and storage to multiple backends including PostgreSQL, MongoDB, and JSON Lines.

The skill handles anti-scraping measures including rotating User-Agent headers via scrapy-fake-useragent, request throttling with AutoThrottle middleware, and proxy rotation. It supports JavaScript-rendered pages via scrapy-playwright integration for SPAs that require browser rendering.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-data-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-data-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-data-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-data-extractor -a codex
```

### OpenClaw

```bash
clawhub install scrapy-pipeline-data-extractor
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/)
