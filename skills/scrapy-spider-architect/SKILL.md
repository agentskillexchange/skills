---
title: "Scrapy Spider Architect"
description: "The Scrapy Spider Architect skill generates production-ready Scrapy spider classes for structured web data extraction. It creates CrawlSpider and Spider subclasses with optimized CSS and XPath selectors, configuring request callbacks, pagination handling, and link extraction rules.\nThe skill scaffolds complete Scrapy projects including items.py with Field definitions, pipelines.py for data cleaning and storage (MongoDB, PostgreSQL, Elasticsearch), and settings.py with tuned concurrency, download delays, and AutoThrottle configuration. It generates middleware for proxy rotation, user-agent randomization, and retry policies.\nAdvanced features include Scrapy-Splash integration for JavaScript-rendered single-page applications, Scrapy-Playwright for headless browser automation, and ItemLoader configurations with input/output processors for field normalization. The skill handles authentication flows (form login, cookie management, OAuth tokens), generates feed exporters for JSON Lines, CSV, and XML formats, and creates Scrapy contracts for automated spider testing."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapy-spider-architect
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scrapy-spider-architect` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-architect/)
