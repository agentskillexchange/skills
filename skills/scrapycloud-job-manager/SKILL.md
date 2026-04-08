---
title: ScrapyCloud Job Manager
description: The ScrapyCloud Job Manager skill automates the deployment and scheduling
  of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API
  client (python-scrapinghub) for programmatic spider management, job scheduling,
  and data retrieval. Core functionality includes spider deployment via shub CLI integration,
  job scheduling with cron-like periodic execution, and argument injection for parameterized
  spider runs. The skill manages job priorities, concurrency slots, and resource allocation
  across project units. Data pipeline features include automatic item export to external
  storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API
  and feed exports. The skill monitors job states, handles log retrieval for debugging,
  and implements automatic retry logic for failed jobs with configurable backoff strategies.
  Advanced capabilities include AutoThrottle configuration for polite crawling, Crawlera
  (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with
  rollback support through the Dash deployment system.
verification: security_reviewed
source: https://agentskillexchange.com/skills/scrapycloud-job-manager/
category:
- Research &amp; Scraping
framework:
- ChatGPT Agents
---

# ScrapyCloud Job Manager

The ScrapyCloud Job Manager skill automates the deployment and scheduling of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API client (python-scrapinghub) for programmatic spider management, job scheduling, and data retrieval. Core functionality includes spider deployment via shub CLI integration, job scheduling with cron-like periodic execution, and argument injection for parameterized spider runs. The skill manages job priorities, concurrency slots, and resource allocation across project units. Data pipeline features include automatic item export to external storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API and feed exports. The skill monitors job states, handles log retrieval for debugging, and implements automatic retry logic for failed jobs with configurable backoff strategies. Advanced capabilities include AutoThrottle configuration for polite crawling, Crawlera (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with rollback support through the Dash deployment system.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scrapycloud-job-manager/)
