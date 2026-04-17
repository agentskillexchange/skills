---
title: "ScrapyCloud Job Manager"
description: "The ScrapyCloud Job Manager skill automates the deployment and scheduling of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API client (python-scrapinghub) for programmatic spider management, job scheduling, and data retrieval.\nCore functionality includes spider deployment via shub CLI integration, job scheduling with cron-like periodic execution, and argument injection for parameterized spider runs. The skill manages job priorities, concurrency slots, and resource allocation across project units.\nData pipeline features include automatic item export to external storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API and feed exports. The skill monitors job states, handles log retrieval for debugging, and implements automatic retry logic for failed jobs with configurable backoff strategies.\nAdvanced capabilities include AutoThrottle configuration for polite crawling, Crawlera (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with rollback support through the Dash deployment system."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/scrapycloud-job-manager/"
framework:
  - "ChatGPT Agents"
---

# ScrapyCloud Job Manager

The ScrapyCloud Job Manager skill automates the deployment and scheduling of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API client (python-scrapinghub) for programmatic spider management, job scheduling, and data retrieval.
Core functionality includes spider deployment via shub CLI integration, job scheduling with cron-like periodic execution, and argument injection for parameterized spider runs. The skill manages job priorities, concurrency slots, and resource allocation across project units.
Data pipeline features include automatic item export to external storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API and feed exports. The skill monitors job states, handles log retrieval for debugging, and implements automatic retry logic for failed jobs with configurable backoff strategies.
Advanced capabilities include AutoThrottle configuration for polite crawling, Crawlera (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with rollback support through the Dash deployment system.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scrapycloud-job-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scrapycloud-job-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapycloud-job-manager/)
