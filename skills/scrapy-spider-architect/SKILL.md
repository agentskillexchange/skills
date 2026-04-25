---
title: "Scrapy Spider Architect"
description: "Generates Scrapy spider classes with CSS/XPath selectors, item pipelines, and middleware configurations for structured web scraping. Includes Scrapy-Splash integration for JavaScript-rendered content."
verification: "security_reviewed"
source: "https://github.com/scrapy/scrapy"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
---

# Scrapy Spider Architect

The Scrapy Spider Architect skill generates production-ready Scrapy spider classes for structured web data extraction. It creates CrawlSpider and Spider subclasses with optimized CSS and XPath selectors, configuring request callbacks, pagination handling, and link extraction rules.

The skill scaffolds complete Scrapy projects including items.py with Field definitions, pipelines.py for data cleaning and storage (MongoDB, PostgreSQL, Elasticsearch), and settings.py with tuned concurrency, download delays, and AutoThrottle configuration. It generates middleware for proxy rotation, user-agent randomization, and retry policies.

Advanced features include Scrapy-Splash integration for JavaScript-rendered single-page applications, Scrapy-Playwright for headless browser automation, and ItemLoader configurations with input/output processors for field normalization. The skill handles authentication flows (form login, cookie management, OAuth tokens), generates feed exporters for JSON Lines, CSV, and XML formats, and creates Scrapy contracts for automated spider testing.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/scrapy-spider-architect/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapy-spider-architect
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/scrapy-spider-architect`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-architect/)
