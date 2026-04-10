---
name: Crawlee Web Crawling and Scraping SDK
description: Crawlee is Apify&#8217;s open source web crawling and scraping library
  for Node.js. It combines request queueing, browser automation, proxy support, and
  storage primitives so agents can build reliable Playwright, Puppeteer, Cheerio,
  or HTTP crawlers from one toolkit.
verification: security_reviewed
source: https://github.com/apify/crawlee
category:
- Research &amp; Scraping
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: apify/crawlee
  github_stars: 22704
  ase_npm_package: '@crawlee/root'
---
# Crawlee Web Crawling and Scraping SDK

Crawlee is an open source web crawling and scraping toolkit maintained by Apify for Node.js and TypeScript workloads. The project bundles the core pieces most agent builders need for production crawling: a request queue, autoscaled concurrency, retry handling, proxy support, persistent datasets, and integrations with browser and HTML parsers. From the same package, an agent can switch between PlaywrightCrawler, PuppeteerCrawler, CheerioCrawler, JSDOMCrawler, or raw HTTP crawling depending on how dynamic the target site is.
That makes Crawlee a strong fit for research, monitoring, and extraction workflows where the job to be done is not just fetching a single page, but traversing a site safely and storing structured output. The upstream documentation shows both quick-start generation through the Crawlee CLI and manual installation with Playwright for browser-backed scraping. In practice, an agent can use Crawlee to collect listings, crawl documentation portals, monitor content changes, or feed downstream RAG pipelines with normalized page data. Because the library exposes queueing, link-enqueueing, datasets, and browser hooks directly, it also works well as an integration layer between AI agents and standard automation stacks.
Upstream signals are strong: the official GitHub repository is active, the npm package exists, the docs site is live, and the project publishes releases for current versions. That makes it a solid verified-metadata intake candidate for the marketplace.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-and-scraping-sdk/)
