---
name: Scrapy Spider Architect
description: Generates Scrapy spider classes with CSS/XPath selectors, item pipelines,
  and middleware configurations for structured web scraping. Includes Scrapy-Splash
  integration for JavaScript-rendered content.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapy-spider-architect/
category:
- Research &amp; Scraping
framework:
- Custom Agents
---
# Scrapy Spider Architect

The Scrapy Spider Architect skill generates production-ready Scrapy spider classes for structured web data extraction. It creates CrawlSpider and Spider subclasses with optimized CSS and XPath selectors, configuring request callbacks, pagination handling, and link extraction rules.
The skill scaffolds complete Scrapy projects including items.py with Field definitions, pipelines.py for data cleaning and storage (MongoDB, PostgreSQL, Elasticsearch), and settings.py with tuned concurrency, download delays, and AutoThrottle configuration. It generates middleware for proxy rotation, user-agent randomization, and retry policies.
Advanced features include Scrapy-Splash integration for JavaScript-rendered single-page applications, Scrapy-Playwright for headless browser automation, and ItemLoader configurations with input/output processors for field normalization. The skill handles authentication flows (form login, cookie management, OAuth tokens), generates feed exporters for JSON Lines, CSV, and XML formats, and creates Scrapy contracts for automated spider testing.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-architect/)
