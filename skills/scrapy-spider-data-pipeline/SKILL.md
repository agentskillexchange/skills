---
name: "Scrapy Spider Data Pipeline"
description: "Builds and manages Scrapy web scraping spiders with custom item pipelines. Supports Splash rendering for JavaScript pages, rotating proxies via scrapy-rotating-proxies, and export to MongoDB or Elasticsearch."
category: "Data Extraction & Transformation"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "scrapy"  # from ase_tool_match
  github_stars: 60923  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "scrapy/scrapy"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Scrapy Spider Data Pipeline

Builds and manages Scrapy web scraping spiders with custom item pipelines. Supports Splash rendering for JavaScript pages, rotating proxies via scrapy-rotating-proxies, and export to MongoDB or Elasticsearch.

## Overview

The Scrapy Spider Data Pipeline creates and manages web scraping workflows using the Scrapy framework with advanced middleware and pipeline configurations. It generates spider classes with CSS and XPath selectors, configures request scheduling, and manages data export pipelines.

JavaScript-rendered pages are handled through Splash integration via scrapy-splash middleware, sending Lua scripts to the Splash HTTP API for page interaction including clicking, scrolling, and waiting for dynamic content. For headless browser needs, Playwright integration via scrapy-playwright provides full browser automation capabilities.

Anti-blocking measures include rotating proxy configuration through scrapy-rotating-proxies with proxy health checking, user agent rotation via scrapy-fake-useragent, and request fingerprinting with scrapy-crawlera for intelligent rate limiting. Retry middleware handles various HTTP error codes and connection timeouts.

Item pipelines support data validation with Scrapy ItemLoaders and input/output processors, deduplication via bloom filters, and export to multiple backends including MongoDB (pymongo), Elasticsearch (elasticsearch-py), PostgreSQL, and JSON Lines files. The skill configures Scrapy settings for concurrent requests, download delays, depth limits, and AutoThrottle for polite crawling. Feed exports support S3 and GCS cloud storage destinations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-data-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-data-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-data-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-data-pipeline -a codex
```

### OpenClaw

```bash
clawhub install scrapy-spider-data-pipeline
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapy-spider-data-pipeline/
