---
title: "Scrapy Spider Generator"
description: "Generates production-ready Scrapy spiders with middleware configuration and item pipeline setup. Uses the Scrapy Framework API, Selector (XPath/CSS), and Twisted reactor for concurrent crawling."
slug: "scrapy-spider-generator"
category:
  - "Research &amp; Scraping"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/scrapy-spider-generator/"
---

# Scrapy Spider Generator

Generates production-ready Scrapy spiders with middleware configuration and item pipeline setup. Uses the Scrapy Framework API, Selector (XPath/CSS), and Twisted reactor for concurrent crawling.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install scrapy-spider-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Scrapy Spider Generator creates production-grade web scraping spiders using the Scrapy framework. It generates Spider classes with properly configured start_urls, parse methods, and Item definitions with Field declarations and ItemLoader processors.
The agent builds comprehensive Scrapy projects with settings.py configuration for CONCURRENT_REQUESTS, DOWNLOAD_DELAY, and AUTOTHROTTLE settings. It generates custom Downloader Middleware for request fingerprinting, proxy rotation via scrapy-rotating-proxies, and user-agent randomization using scrapy-fake-useragent.
Key features include CrawlSpider generation with Rule and LinkExtractor definitions for automated link following, SitemapSpider configuration for XML sitemap-based crawling, and Feed Export setup for JSON Lines, CSV, and direct database output via scrapy-djangoitem. The agent also configures Item Pipelines for data validation, deduplication using scrapy-deltafetch, and export to Elasticsearch, MongoDB, or PostgreSQL. Supports Splash integration for JavaScript-rendered content via scrapy-splash middleware.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-generator/)
