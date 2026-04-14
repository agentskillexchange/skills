---
title: "Puppeteer Web Scraper"
description: "Headless Chrome scraping via Puppeteer with automatic cookie handling, JavaScript rendering, and Cheerio-based DOM extraction. Handles infinite scroll and lazy-loaded content."
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

# Puppeteer Web Scraper

This skill leverages Puppeteer to launch headless Chromium instances for scraping JavaScript-heavy websites that traditional HTTP clients cannot parse. It manages browser contexts, handles cookie consent dialogs, and waits for dynamic content to fully render.

The extraction pipeline uses Cheerio for fast DOM querying after page load, supporting CSS selectors and XPath expressions. Built-in strategies handle infinite scroll pages by monitoring DOM mutations and network idle states.

Features include proxy rotation via a configurable proxy pool, user-agent randomization from a curated list of real browser strings, and viewport emulation for responsive sites. The skill captures screenshots for debugging and exports data as JSON-LD, CSV, or feeds into a PostgreSQL database via pg-copy-streams for high-throughput ingestion.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraper/)
