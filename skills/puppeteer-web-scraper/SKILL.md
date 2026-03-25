---
name: "Puppeteer Web Scraper"
description: "Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-web-scraper/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93912  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Puppeteer Web Scraper

Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content.

## Overview

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render.

The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states.

Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraper
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraper -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraper -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraper -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-web-scraper
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-web-scraper/
