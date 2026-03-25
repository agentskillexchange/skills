---
name: "Scrapy Pipeline Data Extractor"
description: "Builds production Scrapy spiders with custom Item Pipelines for data cleaning and storage. Uses scrapy.linkextractors.LinkExtractor for crawl scoping and ItemLoader with MapCompose processors for field normalization."
category: "Research & Scraping"
framework: "Gemini"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "scrapy"  # from ase_tool_match
  github_stars: 60923  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "scrapy/scrapy"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/scrapy-pipeline-data-extractor/
