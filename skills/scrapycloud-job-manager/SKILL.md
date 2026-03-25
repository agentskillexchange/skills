---
name: "ScrapyCloud Job Manager"
description: "Manages Scrapy spider deployments and job scheduling on ScrapyCloud via the Scrapinghub API. Handles spider argument injection, job prioritization, and item export to S3 or BigQuery."
category: "Research & Scraping"
framework: "ChatGPT Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapycloud-job-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "scrapy"  # from ase_tool_match
  github_stars: 60923  # from ase_github_stars (integer, not string)
  github_repo: "scrapy/scrapy"  # from ase_github_repo
  license: "BSD-3-Clause"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# ScrapyCloud Job Manager

Manages Scrapy spider deployments and job scheduling on ScrapyCloud via the Scrapinghub API. Handles spider argument injection, job prioritization, and item export to S3 or BigQuery.

## Overview

The ScrapyCloud Job Manager skill automates the deployment and scheduling of Scrapy spiders on the ScrapyCloud (Zyte) platform. It uses the Scrapinghub API client (python-scrapinghub) for programmatic spider management, job scheduling, and data retrieval.

Core functionality includes spider deployment via shub CLI integration, job scheduling with cron-like periodic execution, and argument injection for parameterized spider runs. The skill manages job priorities, concurrency slots, and resource allocation across project units.

Data pipeline features include automatic item export to external storage (Amazon S3, Google BigQuery, Azure Blob Storage) via the Collections API and feed exports. The skill monitors job states, handles log retrieval for debugging, and implements automatic retry logic for failed jobs with configurable backoff strategies.

Advanced capabilities include AutoThrottle configuration for polite crawling, Crawlera (Zyte Smart Proxy) integration for anti-ban measures, and spider versioning with rollback support through the Dash deployment system.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapycloud-job-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapycloud-job-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapycloud-job-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapycloud-job-manager -a codex
```

### OpenClaw

```bash
clawhub install scrapycloud-job-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapycloud-job-manager/
