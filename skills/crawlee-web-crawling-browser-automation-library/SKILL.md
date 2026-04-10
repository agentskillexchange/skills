---
name: "Crawlee Web Crawling and Browser Automation Library"
description: "Builds scalable web collection pipelines with Crawlee, Apify’s open-source crawling and browser automation library. Useful for request queue management, Playwright or Puppeteer crawling, structured dataset export, and resilient scraping across large sets of pages."
verification: security_reviewed
source: "https://github.com/apify/crawlee"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22591
  ase_npm_package: "crawlee"
  npm_weekly_downloads: 72475
---

# Crawlee Web Crawling and Browser Automation Library

Crawlee Web Crawling and Browser Automation Library is designed for large-scale collection jobs where a single-page scraper is not enough. It is grounded in the real Crawlee project from Apify and its crawler stack, including CheerioCrawler, PlaywrightCrawler, PuppeteerCrawler, request queues, autoscaled concurrency, session pools, router handlers, proxy configuration, and dataset exports. That gives agents a real toolkit for moving from “grab this page” to “crawl this site reliably and keep the data organized.”
The skill helps choose the right crawler type for the target site, define routing rules for list pages versus detail pages, manage retries, and avoid wasting headless-browser resources on pages that only need HTTP parsing. It also helps structure output so downstream systems receive normalized records instead of a pile of ad hoc HTML fragments. For research and scraping workloads, that distinction matters because the expensive part is rarely the first request; it is maintaining quality and throughput across thousands of URLs.
Outputs can include JSON datasets, cleaned page records, crawl logs, request queue state, extracted entities, and evidence about failures such as blocked requests or selector drift. Integration points include Node.js data pipelines, Apify Actors, Playwright-based extraction steps, proxy layers, and downstream analytics or retrieval systems that ingest crawl results. Use this skill when the task requires coordinated crawling, browser-aware extraction, and repeatable collection architecture rather than a one-off scrape script.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-web-crawling-browser-automation-library/)
