---
title: "Scrapy Distributed Crawler Framework"
description: "Orchestrates large-scale web crawling using Scrapy with scrapy-redis for distributed job queuing. Integrates Splash for JavaScript rendering, stores results in MongoDB via scrapy-mongodb pipeline, and respects robots.txt with AutoThrottle."
verification: "security_reviewed"
source: "https://github.com/scrapy/scrapy"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
  license: "BSD-3-Clause"
---

# Scrapy Distributed Crawler Framework

The Scrapy Distributed Crawler Framework enables scalable web data collection across multiple crawler instances. Built on Scrapy framework with scrapy-redis extension, it distributes URL frontier management across Redis queues enabling horizontal scaling of crawler workers without duplicate URL processing.

JavaScript-rendered content is handled through Splash integration via scrapy-splash middleware, providing a lightweight alternative to full browser automation for pages requiring JS execution. The framework respects crawl ethics with built-in robots.txt compliance, AutoThrottle extension for adaptive request rate management, and configurable politeness delays per domain.

Data flows through configurable item pipelines including validation, deduplication via MinHash fingerprinting, and storage to MongoDB through the scrapy-mongodb pipeline extension. Media files are downloaded via the built-in FilesPipeline with S3 backend storage support. Monitoring uses Scrapy stats collection exported to Prometheus via a custom StatsD exporter, with Grafana dashboards for real-time crawl progress visualization. Spider contracts provide automated testing for extraction logic.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-distributed-crawler-framework/)
