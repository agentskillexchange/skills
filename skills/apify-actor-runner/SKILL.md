---
title: "Apify Actor Runner"
description: "Executes Apify cloud actors for structured web scraping with automatic dataset export to S3. Supports actor input schema validation and webhook-based run completion notifications."
slug: "apify-actor-runner"
category:
  - "Research &amp; Scraping"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apify-actor-runner/"
---

# Apify Actor Runner

Executes Apify cloud actors for structured web scraping with automatic dataset export to S3. Supports actor input schema validation and webhook-based run completion notifications.

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
clawhub install apify-actor-runner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apify Actor Runner skill interfaces with the Apify platform API to launch and manage cloud-based web scraping actors. It validates actor input against the published input schema, handles API token authentication, and monitors run status through the Apify Client SDK.
The skill supports all Apify storage types including datasets, key-value stores, and request queues. Completed datasets are automatically exported to Amazon S3 using the AWS SDK with multipart upload for large extractions. Export formats include JSON, CSV, XML, and JSONL with configurable field mapping.
Run management features include automatic retry on actor failures with configurable memory allocation scaling, webhook registration for run completion events via the Apify Webhooks API, and cost tracking through the usage endpoint. The skill can chain multiple actors in sequence, passing output datasets as input to downstream actors for multi-stage extraction pipelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-runner/)
