---
title: "ScrapyCloud Job Manager"
description: "Manages Scrapy spider deployments and job scheduling on ScrapyCloud via the Scrapinghub API. Handles spider argument injection, job prioritization, and item export to S3 or BigQuery."
slug: "scrapycloud-job-manager"
category:
  - "Research &amp; Scraping"
framework:
  - "ChatGPT Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/scrapycloud-job-manager/"
---

# ScrapyCloud Job Manager

Manages Scrapy spider deployments and job scheduling on ScrapyCloud via the Scrapinghub API. Handles spider argument injection, job prioritization, and item export to S3 or BigQuery.

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
clawhub install scrapycloud-job-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The ScrapyCloud Job Manager skill automates the deployment and scheduling of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API client (python-scrapinghub) for programmatic spider management, job scheduling, and data retrieval.
Core functionality includes spider deployment via shub CLI integration, job scheduling with cron-like periodic execution, and argument injection for parameterized spider runs. The skill manages job priorities, concurrency slots, and resource allocation across project units.
Data pipeline features include automatic item export to external storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API and feed exports. The skill monitors job states, handles log retrieval for debugging, and implements automatic retry logic for failed jobs with configurable backoff strategies.
Advanced capabilities include AutoThrottle configuration for polite crawling, Crawlera (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with rollback support through the Dash deployment system.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapycloud-job-manager/)
