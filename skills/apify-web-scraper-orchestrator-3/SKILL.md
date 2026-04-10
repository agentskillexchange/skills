---
title: "Apify Web Scraper Orchestrator"
description: "Orchestrates Apify actors for large-scale web scraping via the Apify Client SDK. Manages actor runs, dataset exports, and proxy configuration through the Apify API v2."
slug: "apify-web-scraper-orchestrator-3"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/"
---

# Apify Web Scraper Orchestrator

Orchestrates Apify actors for large-scale web scraping via the Apify Client SDK. Manages actor runs, dataset exports, and proxy configuration through the Apify API v2.

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
clawhub install apify-web-scraper-orchestrator-3
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill orchestrates web scraping workflows using the Apify platform and its Actor ecosystem. It manages the full lifecycle of scraping tasks through the Apify Client SDK, from actor selection and input configuration to dataset collection and export.
The skill interfaces with the Apify API v2 for programmatic actor execution, supporting both pre-built actors from the Apify Store and custom actors deployed via the Apify CLI. It handles proxy management through Apify Proxy with automatic residential and datacenter proxy rotation.
Data pipeline features include automatic dataset pagination, webhook-triggered exports to cloud storage (S3, GCS), and structured data validation using JSON Schema. The skill manages request queues for URL frontier management with configurable concurrency, retry policies, and crawl depth limits.
Monitoring capabilities include real-time run status polling, memory and CPU usage tracking, and automatic actor restart on failure with exponential backoff.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/)
