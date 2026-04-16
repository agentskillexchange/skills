---
title: "Scrapy Spider Architect"
description: "Generates Scrapy spider classes with CSS/XPath selectors, item pipelines, and middleware configurations for structured web scraping. Includes Scrapy-Splash integration for JavaScript-rendered content."
verification: "security_reviewed"
source: "https://github.com/scrapy/scrapy"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
  license: "BSD-3-Clause"
---

# Scrapy Spider Architect

The Scrapy Spider Architect skill generates production-ready Scrapy spider classes for structured web data extraction. It creates CrawlSpider and Spider subclasses with optimized CSS and XPath selectors, configuring request callbacks, pagination handling, and link extraction rules.

The skill scaffolds complete Scrapy projects including items.py with Field definitions, pipelines.py for data cleaning and storage (MongoDB, PostgreSQL, Elasticsearch), and settings.py with tuned concurrency, download delays, and AutoThrottle configuration. It generates middleware for proxy rotation, user-agent randomization, and retry policies.

Advanced features include Scrapy-Splash integration for JavaScript-rendered single-page applications, Scrapy-Playwright for headless browser automation, and ItemLoader configurations with input/output processors for field normalization. The skill handles authentication flows (form login, cookie management, OAuth tokens), generates feed exporters for JSON Lines, CSV, and XML formats, and creates Scrapy contracts for automated spider testing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-architect/)
