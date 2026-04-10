---
name: Crawlee Smart Crawler Agent
description: Implements intelligent web crawling using the Crawlee framework with
  adaptive request routing between CheerioCrawler and PlaywrightCrawler. Manages request
  queues, handles anti-bot challenges, and exports structured data.
verification: security_reviewed
source: https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/
category:
- Research &amp; Scraping
framework:
- Cursor
---
# Crawlee Smart Crawler Agent

The Crawlee Smart Crawler Agent implements adaptive web crawling using the Crawlee framework to automatically select the optimal crawling strategy for each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot challenges are detected. Request queue management handles URL deduplication, priority scheduling, and depth-limited crawling to prevent infinite loops. The agent implements smart retry logic with automatic proxy rotation and browser fingerprint randomization for sites with bot detection. Structured data extraction uses configurable CSS selector maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables persistent crawl state that survives process restarts for long-running crawls. Data is exported through Crawlee Dataset handlers in multiple formats. The agent supports sitemap-based seeding for comprehensive site crawling and robots.txt compliance for ethical scraping. Rate limiting adapts to target site response patterns to avoid overloading servers.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/)
