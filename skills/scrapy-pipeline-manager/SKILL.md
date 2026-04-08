---
title: Scrapy Pipeline Manager
description: The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments
  through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider
  scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling.
  Custom item pipelines are configured for downstream data processing including MongoDB
  ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing
  via the bulk API, and file download pipelines for media assets. Deduplication uses
  MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate
  detection across crawl runs. The middleware stack includes rotating proxy support
  via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with
  exponential backoff, and AutoThrottle configuration for polite crawling. The skill
  manages robots.txt compliance, generates crawl statistics dashboards, and supports
  Splash integration for JavaScript rendering through the scrapy-splash middleware.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapy-pipeline-manager/
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# Scrapy Pipeline Manager

The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling. Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs. The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-manager/)
