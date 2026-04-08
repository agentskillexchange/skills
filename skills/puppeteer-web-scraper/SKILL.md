---
title: Puppeteer Web Scraper
description: This skill leverages Puppeteer to launch headless Chromium instances
  for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse.
  It manages browser contexts, handles cookie consent dialogs, and waits for dynamic
  content to fully render. The extraction pipeline uses Cheerio for fast DOM querying
  after page load, supporting CSS selectors and XPath expressions. Built-in strategies
  handle infinite scroll pages by monitoring DOM mutations and network idle states.
  Features include proxy rotation via a configurable proxy pool, user-agent randomization
  from a curated list of real browser strings, and viewport emulation for responsive
  sites. The skill captures screenshots for debugging and exports data as JSON-LD,
  CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput
  ingestion.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-web-scraper/
category:
- Research &amp; Scraping
framework:
- Cursor
---

# Puppeteer Web Scraper

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render. The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states. Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
