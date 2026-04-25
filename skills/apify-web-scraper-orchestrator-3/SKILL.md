---
title: "Apify Web Scraper Orchestrator"
description: "Orchestrates Apify actors for large-scale web scraping via the Apify Client SDK. Manages actor runs, dataset exports, and proxy configuration through the Apify API v2."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research & Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Web Scraper Orchestrator

This skill orchestrates web scraping workflows using the Apify platform and its Actor ecosystem. It manages the full lifecycle of scraping tasks through the Apify Client SDK, from actor selection and input configuration to dataset collection and export. The skill interfaces with the Apify API v2 for programmatic actor execution, supporting both pre-built actors from the Apify Store and custom actors deployed via the Apify CLI. It handles proxy management through Apify Proxy with automatic residential and datacenter proxy rotation. Data pipeline features include automatic dataset pagination, webhook-triggered exports to cloud storage (S3, GCS), and structured data validation using JSON Schema. The skill manages request queues for URL frontier management with configurable concurrency, retry policies, and crawl depth limits. Monitoring capabilities include real-time run status polling, memory and CPU usage tracking, and automatic actor restart on failure with exponential backoff.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-web-scraper-orchestrator-3
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apify-web-scraper-orchestrator-3`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/)
