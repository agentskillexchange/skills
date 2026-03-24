---
name: "Puppeteer Stealth Web Scraper"
description: "Uses puppeteer-extra with stealth plugin to bypass bot detection for web scraping. Integrates with Cheerio for HTML parsing, rotating residential proxies via Bright Data API, and p-queue for concurrency control."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93912  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Puppeteer Stealth Web Scraper

Uses puppeteer-extra with stealth plugin to bypass bot detection for web scraping. Integrates with Cheerio for HTML parsing, rotating residential proxies via Bright Data API, and p-queue for concurrency control.

## Overview

The Puppeteer Stealth Web Scraper uses puppeteer-extra with the puppeteer-extra-plugin-stealth module to launch headless Chrome instances that evade common bot detection systems like Cloudflare, PerimeterX, and DataDome. It manages browser fingerprinting through realistic viewport sizes, WebGL parameters, and navigator property overrides. Proxy rotation is handled through the Bright Data API with automatic IP cycling on detection events. Extracted HTML is processed using Cheerio for efficient jQuery-style DOM traversal and data extraction without full browser rendering overhead. Concurrency is managed via p-queue to respect rate limits while maximizing throughput across multiple target domains. The agent supports structured data extraction with CSS selector templates, automatic pagination handling, and CAPTCHA solving integration via 2Captcha API. Scraped data is validated against JSON Schema definitions before being output as CSV, JSON, or directly inserted into databases via Knex.js query builder.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-web-scraper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-web-scraper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-web-scraper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-web-scraper -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-stealth-web-scraper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/
