---
title: "Puppeteer Stealth Web Scraper"
description: "Uses puppeteer-extra with stealth plugin to bypass bot detection for web scraping. Integrates with Cheerio for HTML parsing, rotating residential proxies via Bright Data API, and p-queue for concurrency control."
verification: "security_reviewed"
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
  license: "Apache-2.0"
---

# Puppeteer Stealth Web Scraper

The Puppeteer Stealth Web Scraper uses puppeteer-extra with the puppeteer-extra-plugin-stealth module to launch headless Chrome instances that evade common bot detection systems like Cloudflare, PerimeterX, and DataDome. It manages browser fingerprinting through realistic viewport sizes, WebGL parameters, and navigator property overrides. Proxy rotation is handled through the Bright Data API with automatic IP cycling on detection events. Extracted HTML is processed using Cheerio for efficient jQuery-style DOM traversal and data extraction without full browser rendering overhead. Concurrency is managed via p-queue to respect rate limits while maximizing throughput across multiple target domains. The agent supports structured data extraction with CSS selector templates, automatic pagination handling, and CAPTCHA solving integration via 2Captcha API. Scraped data is validated against JSON Schema definitions before being output as CSV, JSON, or directly inserted into databases via Knex.js query builder.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/)
