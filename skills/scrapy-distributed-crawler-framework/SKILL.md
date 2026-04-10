---
name: "Scrapy Distributed Crawler Framework"
description: "Orchestrates large-scale web crawling using Scrapy with scrapy-redis for distributed job queuing. Integrates Splash for JavaScript rendering, stores results in MongoDB via scrapy-mongodb pipeline, and respects robots.txt with AutoThrottle."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapy-distributed-crawler-framework/"
category:
  - "Research &amp; Scraping"
framework:
  - "MCP"
---

# Scrapy Distributed Crawler Framework

The Scrapy Distributed Crawler Framework enables scalable web data collection across multiple crawler instances. Built on Scrapy framework with scrapy-redis extension, it distributes URL frontier management across Redis queues enabling horizontal scaling of crawler workers without duplicate URL processing.
JavaScript-rendered content is handled through Splash integration via scrapy-splash middleware, providing a lightweight alternative to full browser automation for pages requiring JS execution. The framework respects crawl ethics with built-in robots.txt compliance, AutoThrottle extension for adaptive request rate management, and configurable politeness delays per domain.
Data flows through configurable item pipelines including validation, deduplication via MinHash fingerprinting, and storage to MongoDB through the scrapy-mongodb pipeline extension. Media files are downloaded via the built-in FilesPipeline with S3 backend storage support. Monitoring uses Scrapy stats collection exported to Prometheus via a custom StatsD exporter, with Grafana dashboards for real-time crawl progress visualization. Spider contracts provide automated testing for extraction logic.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-distributed-crawler-framework/)
