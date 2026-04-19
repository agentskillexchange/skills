---
title: "Scrapy Pipeline Manager"
description: "The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling. Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs. The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware."
source: "https://github.com/scrapy/scrapy"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
---

# Scrapy Pipeline Manager

The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling. Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs. The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-manager/)
