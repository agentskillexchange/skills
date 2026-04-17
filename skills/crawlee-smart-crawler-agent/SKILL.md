---
title: "Crawlee Smart Crawler Agent"
description: "The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/"
framework:
  - "Cursor"
---

# Crawlee Smart Crawler Agent

The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/crawlee-smart-crawler-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/crawlee-smart-crawler-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/)
