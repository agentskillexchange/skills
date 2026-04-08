---
title: Crawlee Smart Crawler Agent
description: The Crawlee Smart Crawler Agent implements adaptive web crawling using
  the Crawlee framework to automatically select the optimal crawling strategy for
  each target. It starts with CheerioCrawler for lightweight HTML parsing and automatically
  escalates to PlaywrightCrawler when JavaScript rendering is required or anti-bot
  challenges are detected. Request queue management handles URL deduplication, priority
  scheduling, and depth-limited crawling to prevent infinite loops. The agent implements
  smart retry logic with automatic proxy rotation and browser fingerprint randomization
  for sites with bot detection. Structured data extraction uses configurable CSS selector
  maps and JSON-LD parsing for schema.org structured data. The RequestQueue API enables
  persistent crawl state that survives process restarts for long-running crawls. Data
  is exported through Crawlee Dataset handlers in multiple formats. The agent supports
  sitemap-based seeding for comprehensive site crawling and robots.txt compliance
  for ethical scraping. Rate limiting adapts to target site response patterns to avoid
  overloading servers.
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

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/crawlee-smart-crawler-agent/)
