---
title: "Scrapy Pipeline Manager"
description: "Manages Scrapy spider deployments via Scrapyd API with custom item pipelines for MongoDB ingestion, deduplication via MinHash LSH, and rotating proxy middleware configuration."
verification: security_reviewed
source: "https://github.com/scrapy/scrapy"
category:
  - "Research & Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "scrapy/scrapy"
  github_stars: 61314
  license: "BSD-3-Clause"
---

# Scrapy Pipeline Manager

The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling.

Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs.

The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapy-pipeline-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scrapy-pipeline-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-manager/)
