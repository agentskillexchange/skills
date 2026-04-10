---
name: Puppeteer Web Scraper
description: Headless Chrome scraping via Puppeteer with automatic cookie handling,
  JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll
  and lazy-loaded content.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-web-scraper/
category:
- Research &amp; Scraping
framework:
- Cursor
---
# Puppeteer Web Scraper

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render.
The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states.
Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
