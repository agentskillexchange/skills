---
name: "Scrapy Spider Generator"
description: "Generates production-ready Scrapy spiders with middleware configuration and item pipeline setup. Uses the Scrapy Framework API, Selector (XPath/CSS), and Twisted reactor for concurrent crawling."
category: "Research & Scraping"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapy-spider-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "scrapy"  # from ase_tool_match
  github_stars: 60923  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 10909882  # from ase_npm_downloads
  github_repo: "scrapy/scrapy"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Scrapy Spider Generator

Generates production-ready Scrapy spiders with middleware configuration and item pipeline setup. Uses the Scrapy Framework API, Selector (XPath/CSS), and Twisted reactor for concurrent crawling.

## Overview

The Scrapy Spider Generator creates production-grade web scraping spiders using the Scrapy framework. It generates Spider classes with properly configured start_urls, parse methods, and Item definitions with Field declarations and ItemLoader processors.

The agent builds comprehensive Scrapy projects with settings.py configuration for CONCURRENT_REQUESTS, DOWNLOAD_DELAY, and AUTOTHROTTLE settings. It generates custom Downloader Middleware for request fingerprinting, proxy rotation via scrapy-rotating-proxies, and user-agent randomization using scrapy-fake-useragent.

Key features include CrawlSpider generation with Rule and LinkExtractor definitions for automated link following, SitemapSpider configuration for XML sitemap-based crawling, and Feed Export setup for JSON Lines, CSV, and direct database output via scrapy-djangoitem. The agent also configures Item Pipelines for data validation, deduplication using scrapy-deltafetch, and export to Elasticsearch, MongoDB, or PostgreSQL. Supports Splash integration for JavaScript-rendered content via scrapy-splash middleware.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-generator -a codex
```

### OpenClaw

```bash
clawhub install scrapy-spider-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapy-spider-generator/
