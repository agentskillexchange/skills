---
name: "Puppeteer Web Scraper"
description: "Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content."
category: "Research &amp; Scraping"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-web-scraper/"
---
# Puppeteer Web Scraper

Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
