---
title: "Crawlee Web Crawling and Scraping Library by Apify"
description: "Crawlee is Apify’s open source crawling and scraping framework for Node.js. It unifies HTTP scraping and browser automation, adds queues, storage, retries, proxies, and lets developers switch between Playwright, Puppeteer, Cheerio, and JSDOM without rebuilding the whole pipeline."
slug: "crawlee-web-crawling-and-scraping-library-by-apify"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/apify/crawlee"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22677
---

# Crawlee Web Crawling and Scraping Library by Apify

Crawlee is Apify’s open source crawling and scraping framework for Node.js. It unifies HTTP scraping and browser automation, adds queues, storage, retries, proxies, and lets developers switch between Playwright, Puppeteer, Cheerio, and JSDOM without rebuilding the whole pipeline.

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
clawhub install crawlee-web-crawling-and-scraping-library-by-apify
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Crawlee is an open source web crawling and scraping library from Apify for JavaScript and TypeScript teams that need something more robust than ad hoc scripts. It gives developers a single framework for collecting pages, files, and structured data across both lightweight HTTP requests and full browser automation. In practice, that means one project can start with fast HTTP extraction and then move specific routes to Playwright or Puppeteer when JavaScript rendering, screenshots, or session handling are required.
The library’s core job-to-be-done is reliable extraction at scale. Crawlee includes persistent request queues, retries, routing, storage, proxy rotation, session management, hooks, and autoscaling so a crawler can keep moving without every site-specific edge case turning into custom infrastructure. The project documentation also highlights support for Cheerio and JSDOM, which makes it useful when an agent or internal tool needs to mix low-cost HTML parsing with targeted browser work.
For AI and automation workflows, Crawlee fits naturally into pipelines that collect product catalogs, documentation, site maps, or research corpora before passing the output into downstream analysis. It integrates with Playwright and Puppeteer for browser-based steps, writes datasets and files to disk, and can be run locally or deployed in containerized environments. Teams already using Node.js can install the main package and add Playwright when they need a browser-backed crawler.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-and-scraping-library-by-apify/)
