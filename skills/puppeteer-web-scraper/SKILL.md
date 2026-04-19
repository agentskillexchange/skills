---
title: "Puppeteer Web Scraper"
description: "This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render. The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states. Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Web Scraper

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render. The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states. Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
