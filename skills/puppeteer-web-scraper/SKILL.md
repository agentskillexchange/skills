---
title: "Puppeteer Web Scraper"
description: "Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content."
slug: "puppeteer-web-scraper"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/puppeteer-web-scraper/"
---

# Puppeteer Web Scraper

Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content.

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
clawhub install puppeteer-web-scraper
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render.
The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states.
Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
