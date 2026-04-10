---
title: "Crawlee Web Crawling and Scraping SDK"
description: "Crawlee is Apify’s open source web crawling and scraping library for Node.js. It combines request queueing, browser automation, proxy support, and storage primitives so agents can build reliable Playwright, Puppeteer, Cheerio, or HTTP crawlers from one toolkit."
slug: "crawlee-web-crawling-and-scraping-sdk"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/apify/crawlee"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22704
  npm_package: "@crawlee/root"
listed: true
---

# Crawlee Web Crawling and Scraping SDK

Crawlee is Apify’s open source web crawling and scraping library for Node.js. It combines request queueing, browser automation, proxy support, and storage primitives so agents can build reliable Playwright, Puppeteer, Cheerio, or HTTP crawlers from one toolkit.

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
clawhub install crawlee-web-crawling-and-scraping-sdk
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Crawlee is an open source web crawling and scraping toolkit maintained by Apify for Node.js and TypeScript workloads. The project bundles the core pieces most agent builders need for production crawling: a request queue, autoscaled concurrency, retry handling, proxy support, persistent datasets, and integrations with browser and HTML parsers. From the same package, an agent can switch between PlaywrightCrawler, PuppeteerCrawler, CheerioCrawler, JSDOMCrawler, or raw HTTP crawling depending on how dynamic the target site is.
That makes Crawlee a strong fit for research, monitoring, and extraction workflows where the job to be done is not just fetching a single page, but traversing a site safely and storing structured output. The upstream documentation shows both quick-start generation through the Crawlee CLI and manual installation with Playwright for browser-backed scraping. In practice, an agent can use Crawlee to collect listings, crawl documentation portals, monitor content changes, or feed downstream RAG pipelines with normalized page data. Because the library exposes queueing, link-enqueueing, datasets, and browser hooks directly, it also works well as an integration layer between AI agents and standard automation stacks.
Upstream signals are strong: the official GitHub repository is active, the npm package exists, the docs site is live, and the project publishes releases for current versions. That makes it a solid verified-metadata intake candidate for the marketplace.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-and-scraping-sdk/)
