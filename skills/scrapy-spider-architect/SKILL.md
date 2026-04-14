---
title: "Scrapy Spider Architect"
description: "Generates Scrapy spider classes with CSS/XPath selectors, item pipelines, and middleware configurations for structured web scraping. Includes Scrapy-Splash integration for JavaScript-rendered content."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
category:
  - "Research &amp; Scraping"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-spider-architect/)
