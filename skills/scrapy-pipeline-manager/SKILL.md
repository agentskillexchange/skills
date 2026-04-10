---
title: "Scrapy Pipeline Manager"
description: "Manages Scrapy spider deployments via Scrapyd API with custom item pipelines for MongoDB ingestion, deduplication via MinHash LSH, and rotating proxy middleware configuration."
slug: "scrapy-pipeline-manager"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/scrapy-pipeline-manager/"
listed: true
---

# Scrapy Pipeline Manager

Manages Scrapy spider deployments via Scrapyd API with custom item pipelines for MongoDB ingestion, deduplication via MinHash LSH, and rotating proxy middleware configuration.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install scrapy-pipeline-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling.
Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs.
The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-manager/)
