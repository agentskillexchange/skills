---
title: "Puppeteer Stealth Web Scraper"
description: "Uses puppeteer-extra with stealth plugin to bypass bot detection for web scraping. Integrates with Cheerio for HTML parsing, rotating residential proxies via Bright Data API, and p-queue for concurrency control."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Stealth Web Scraper

The Puppeteer Stealth Web Scraper uses puppeteer-extra with the puppeteer-extra-plugin-stealth module to launch headless Chrome instances that evade common bot detection systems like Cloudflare, PerimeterX, and DataDome. It manages browser fingerprinting through realistic viewport sizes, WebGL parameters, and navigator property overrides. Proxy rotation is handled through the Bright Data API with automatic IP cycling on detection events. Extracted HTML is processed using Cheerio for efficient jQuery-style DOM traversal and data extraction without full browser rendering overhead. Concurrency is managed via p-queue to respect rate limits while maximizing throughput across multiple target domains. The agent supports structured data extraction with CSS selector templates, automatic pagination handling, and CAPTCHA solving integration via 2Captcha API. Scraped data is validated against JSON Schema definitions before being output as CSV, JSON, or directly inserted into databases via Knex.js query builder.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-web-scraper/)
