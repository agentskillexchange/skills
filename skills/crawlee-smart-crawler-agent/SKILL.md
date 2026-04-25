---
title: "Crawlee Smart Crawler Agent"
description: "Implements intelligent web crawling using the Crawlee framework with adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request queues, handles anti-bot challenges, and exports structured data."
verification: "security_reviewed"
source: "https://github.com/apify/crawlee"
category:
  - "Research & Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "apify/crawlee"
  github_stars: 22922
---

# Crawlee Smart Crawler Agent

The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crawlee-smart-crawler-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/crawlee-smart-crawler-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/)
