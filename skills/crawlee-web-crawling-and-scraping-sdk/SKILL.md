---
title: "Crawlee Web Crawling and Scraping SDK"
description: "Crawlee is Apify’s open source web crawling and scraping library for Node.js. It combines request queueing, browser automation, proxy support, and storage primitives so agents can build reliable Playwright, Puppeteer, Cheerio, or HTTP crawlers from one toolkit."
verification: security_reviewed
source: "https://github.com/apify/crawlee"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22762
  npm_package: "crawlee"
  npm_weekly_downloads: 80765
  license: "Apache-2.0"
---

# Crawlee Web Crawling and Scraping SDK

Crawlee is an open source web crawling and scraping toolkit maintained by Apify for Node.js and TypeScript workloads. The project bundles the core pieces most agent builders need for production crawling: a request queue, autoscaled concurrency, retry handling, proxy support, persistent datasets, and integrations with browser and HTML parsers. From the same package, an agent can switch between PlaywrightCrawler, PuppeteerCrawler, CheerioCrawler, JSDOMCrawler, or raw HTTP crawling depending on how dynamic the target site is.

That makes Crawlee a strong fit for research, monitoring, and extraction workflows where the job to be done is not just fetching a single page, but traversing a site safely and storing structured output. The upstream documentation shows both quick-start generation through the Crawlee CLI and manual installation with Playwright for browser-backed scraping. In practice, an agent can use Crawlee to collect listings, crawl documentation portals, monitor content changes, or feed downstream RAG pipelines with normalized page data. Because the library exposes queueing, link-enqueueing, datasets, and browser hooks directly, it also works well as an integration layer between AI agents and standard automation stacks.

Upstream signals are strong: the official GitHub repository is active, the npm package exists, the docs site is live, and the project publishes releases for current versions. That makes it a solid verified-metadata intake candidate for the marketplace.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crawlee-web-crawling-and-scraping-sdk
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/crawlee-web-crawling-and-scraping-sdk` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-and-scraping-sdk/)
