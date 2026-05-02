---
title: "Apify Actor Runner"
description: "Executes Apify cloud actors for structured web scraping with automatic dataset export to S3. Supports actor input schema validation and webhook-based run completion notifications."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research & Scraping"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Runner

The Apify Actor Runner skill interfaces with the Apify platform API to launch and manage cloud-based web scraping actors. It validates actor input against the published input schema, handles API token authentication, and monitors run status through the Apify Client SDK.

The skill supports all Apify storage types including datasets, key-value stores, and request queues. Completed datasets are automatically exported to Amazon S3 using the AWS SDK with multipart upload for large extractions. Export formats include JSON, CSV, XML, and JSONL with configurable field mapping.

Run management features include automatic retry on actor failures with configurable memory allocation scaling, webhook registration for run completion events via the Apify Webhooks API, and cost tracking through the usage endpoint. The skill can chain multiple actors in sequence, passing output datasets as input to downstream actors for multi-stage extraction pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apify-actor-runner/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-actor-runner
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apify-actor-runner`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-runner/)
