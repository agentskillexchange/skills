---
title: "Scrapy Spider Generator"
description: "Generates production-ready Scrapy spiders with middleware configuration and item pipeline setup. Uses the Scrapy Framework API, Selector (XPath/CSS), and Twisted reactor for concurrent crawling."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
category:
  - "Research &amp; Scraping"
framework:
  - "ChatGPT Agents"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
---

# Scrapy Spider Generator

The Scrapy Spider Generator creates production-grade web scraping spiders using the Scrapy framework. It generates Spider classes with properly configured start_urls, parse methods, and Item definitions with Field declarations and ItemLoader processors.

The agent builds comprehensive Scrapy projects with settings.py configuration for CONCURRENT_REQUESTS, DOWNLOAD_DELAY, and AUTOTHROTTLE settings. It generates custom Downloader Middleware for request fingerprinting, proxy rotation via scrapy-rotating-proxies, and user-agent randomization using scrapy-fake-useragent.

Key features include CrawlSpider generation with Rule and LinkExtractor definitions for automated link following, SitemapSpider configuration for XML sitemap-based crawling, and Feed Export setup for JSON Lines, CSV, and direct database output via scrapy-djangoitem. The agent also configures Item Pipelines for data validation, deduplication using scrapy-deltafetch, and export to Elasticsearch, MongoDB, or PostgreSQL. Supports Splash integration for JavaScript-rendered content via scrapy-splash middleware.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-generator/)
