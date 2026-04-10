---
name: "Puppeteer Stealth Web Scraper"
description: "Uses puppeteer-extra with stealth plugin to bypass bot detection for web scraping. Integrates with Cheerio for HTML parsing, rotating residential proxies via Bright Data API, and p-queue for concurrency control."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
---

# Puppeteer Stealth Web Scraper

The Puppeteer Stealth Web Scraper uses puppeteer-extra with the puppeteer-extra-plugin-stealth module to launch headless Chrome instances that evade common bot detection systems like Cloudflare, PerimeterX, and DataDome. It manages browser fingerprinting through realistic viewport sizes, WebGL parameters, and navigator property overrides. Proxy rotation is handled through the Bright Data API with automatic IP cycling on detection events. Extracted HTML is processed using Cheerio for efficient jQuery-style DOM traversal and data extraction without full browser rendering overhead. Concurrency is managed via p-queue to respect rate limits while maximizing throughput across multiple target domains. The agent supports structured data extraction with CSS selector templates, automatic pagination handling, and CAPTCHA solving integration via 2Captcha API. Scraped data is validated against JSON Schema definitions before being output as CSV, JSON, or directly inserted into databases via Knex.js query builder.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/)
