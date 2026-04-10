---
title: "Crawlee Smart Crawler Agent"
description: "Implements intelligent web crawling using the Crawlee framework with adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request queues, handles anti-bot challenges, and exports structured data."
slug: "crawlee-smart-crawler-agent"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/"
---

# Crawlee Smart Crawler Agent

Implements intelligent web crawling using the Crawlee framework with adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request queues, handles anti-bot challenges, and exports structured data.

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
clawhub install crawlee-smart-crawler-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/)
