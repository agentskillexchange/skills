---
name: "Crawlee Smart Crawler Agent"
description: "Implements intelligent web crawling using the Crawlee framework with adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request queues, handles anti-bot challenges, and exports structured data."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/"
---

# Crawlee Smart Crawler Agent

Implements intelligent web crawling using the Crawlee framework with adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request queues, handles anti-bot challenges, and exports structured data.

## Overview

The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill crawlee-smart-crawler-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill crawlee-smart-crawler-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill crawlee-smart-crawler-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill crawlee-smart-crawler-agent -a codex
```

### OpenClaw

```bash
clawhub install crawlee-smart-crawler-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/
