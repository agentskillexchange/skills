---
name: "Scrapy Spider Architect"
description: "Generates Scrapy spider classes with CSS/XPath selectors, item pipelines, and middleware configurations for structured web scraping. Includes Scrapy-Splash integration for JavaScript-rendered content."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapy-spider-architect/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "scrapy"  # from ase_tool_match
  github_stars: 60923  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "scrapy/scrapy"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Scrapy Spider Architect

Generates Scrapy spider classes with CSS/XPath selectors, item pipelines, and middleware configurations for structured web scraping. Includes Scrapy-Splash integration for JavaScript-rendered content.

## Overview

The Scrapy Spider Architect skill generates production-ready **Scrapy** spider classes for structured web data extraction. It creates CrawlSpider and Spider subclasses with optimized CSS and XPath selectors, configuring request callbacks, pagination handling, and link extraction rules.

The skill scaffolds complete Scrapy projects including items.py with Field definitions, pipelines.py for data cleaning and storage (MongoDB, PostgreSQL, Elasticsearch), and settings.py with tuned concurrency, download delays, and AutoThrottle configuration. It generates middleware for proxy rotation, user-agent randomization, and retry policies.

Advanced features include Scrapy-Splash integration for JavaScript-rendered single-page applications, Scrapy-Playwright for headless browser automation, and ItemLoader configurations with input/output processors for field normalization. The skill handles authentication flows (form login, cookie management, OAuth tokens), generates feed exporters for JSON Lines, CSV, and XML formats, and creates Scrapy contracts for automated spider testing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-architect
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-architect -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-architect -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-spider-architect -a codex
```

### OpenClaw

```bash
clawhub install scrapy-spider-architect
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapy-spider-architect/
