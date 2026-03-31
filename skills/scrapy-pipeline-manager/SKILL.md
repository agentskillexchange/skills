---
name: "Scrapy Pipeline Manager"
description: "Manages Scrapy spider deployments via Scrapyd API with custom item pipelines for MongoDB ingestion, deduplication via MinHash LSH, and rotating proxy middleware configuration."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapy-pipeline-manager/"
---
# Scrapy Pipeline Manager

Manages Scrapy spider deployments via Scrapyd API with custom item pipelines for MongoDB ingestion, deduplication via MinHash LSH, and rotating proxy middleware configuration.

## Overview

The Scrapy Pipeline Manager skill orchestrates Scrapy spider deployments through the Scrapyd HTTP API. It handles egg packaging, project deployment, spider scheduling, and log retrieval across multiple Scrapyd nodes for distributed crawling.

Custom item pipelines are configured for downstream data processing including MongoDB ingestion via PyMongo with automatic collection sharding, Elasticsearch indexing via the bulk API, and file download pipelines for media assets. Deduplication uses MinHash LSH (Locality Sensitive Hashing) via the datasketch library for near-duplicate detection across crawl runs.

The middleware stack includes rotating proxy support via scrapy-rotating-proxies with dead proxy detection, custom retry middleware with exponential backoff, and AutoThrottle configuration for polite crawling. The skill manages robots.txt compliance, generates crawl statistics dashboards, and supports Splash integration for JavaScript rendering through the scrapy-splash middleware.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-pipeline-manager -a codex
```

### OpenClaw

```bash
clawhub install scrapy-pipeline-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapy-pipeline-manager/)
