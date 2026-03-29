---
name: "Scrapy Distributed Crawler Framework"
description: "Orchestrates large-scale web crawling using Scrapy with scrapy-redis for distributed job queuing. Integrates Splash for JavaScript rendering, stores results in MongoDB via scrapy-mongodb pipeline, and respects robots.txt with AutoThrottle."
category: "Research & Scraping"
framework: "MCP"
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
tool_ecosystem:
  tool: scrapy
  github_stars: 60923
  npm_weekly_downloads: 8224050
  github_repo: scrapy/scrapy
  license: BSD-3-Clause
  maintained: true
---
# Scrapy Distributed Crawler Framework

Orchestrates large-scale web crawling using Scrapy with scrapy-redis for distributed job queuing. Integrates Splash for JavaScript rendering, stores results in MongoDB via scrapy-mongodb pipeline, and respects robots.txt with AutoThrottle.

## Overview

The Scrapy Distributed Crawler Framework enables scalable web data collection across multiple crawler instances. Built on Scrapy framework with scrapy-redis extension, it distributes URL frontier management across Redis queues enabling horizontal scaling of crawler workers without duplicate URL processing.

JavaScript-rendered content is handled through Splash integration via scrapy-splash middleware, providing a lightweight alternative to full browser automation for pages requiring JS execution. The framework respects crawl ethics with built-in robots.txt compliance, AutoThrottle extension for adaptive request rate management, and configurable politeness delays per domain.

Data flows through configurable item pipelines including validation, deduplication via MinHash fingerprinting, and storage to MongoDB through the scrapy-mongodb pipeline extension. Media files are downloaded via the built-in FilesPipeline with S3 backend storage support. Monitoring uses Scrapy stats collection exported to Prometheus via a custom StatsD exporter, with Grafana dashboards for real-time crawl progress visualization. Spider contracts provide automated testing for extraction logic.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-distributed-crawler-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-distributed-crawler-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-distributed-crawler-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-distributed-crawler-framework -a codex
```

### OpenClaw

```bash
clawhub install scrapy-distributed-crawler-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-distributed-crawler-framework/)
