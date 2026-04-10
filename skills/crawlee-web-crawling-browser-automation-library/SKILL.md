---
title: "Crawlee Web Crawling and Browser Automation Library"
description: "Builds scalable web collection pipelines with Crawlee, Apify’s open-source crawling and browser automation library. Useful for request queue management, Playwright or Puppeteer crawling, structured dataset export, and resilient scraping across large sets of pages."
slug: "crawlee-web-crawling-browser-automation-library"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/apify/crawlee"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22591
  npm_package: "crawlee"
  npm_weekly_downloads: 72475
listed: true
---

# Crawlee Web Crawling and Browser Automation Library

Builds scalable web collection pipelines with Crawlee, Apify’s open-source crawling and browser automation library. Useful for request queue management, Playwright or Puppeteer crawling, structured dataset export, and resilient scraping across large sets of pages.

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
clawhub install crawlee-web-crawling-browser-automation-library
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Crawlee Web Crawling and Browser Automation Library is designed for large-scale collection jobs where a single-page scraper is not enough. It is grounded in the real Crawlee project from Apify and its crawler stack, including CheerioCrawler, PlaywrightCrawler, PuppeteerCrawler, request queues, autoscaled concurrency, session pools, router handlers, proxy configuration, and dataset exports. That gives agents a real toolkit for moving from “grab this page” to “crawl this site reliably and keep the data organized.”
The skill helps choose the right crawler type for the target site, define routing rules for list pages versus detail pages, manage retries, and avoid wasting headless-browser resources on pages that only need HTTP parsing. It also helps structure output so downstream systems receive normalized records instead of a pile of ad hoc HTML fragments. For research and scraping workloads, that distinction matters because the expensive part is rarely the first request; it is maintaining quality and throughput across thousands of URLs.
Outputs can include JSON datasets, cleaned page records, crawl logs, request queue state, extracted entities, and evidence about failures such as blocked requests or selector drift. Integration points include Node.js data pipelines, Apify Actors, Playwright-based extraction steps, proxy layers, and downstream analytics or retrieval systems that ingest crawl results. Use this skill when the task requires coordinated crawling, browser-aware extraction, and repeatable collection architecture rather than a one-off scrape script.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-browser-automation-library/)
