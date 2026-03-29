---
name: "Apify Actor Runner"
description: "Executes Apify cloud actors for structured web scraping with automatic dataset export to S3. Supports actor input schema validation and webhook-based run completion notifications."
category: "Research & Scraping"
framework: "Codex"
verification: security_reviewed
source: "https://github.com/apify/apify-sdk-js"
tool_ecosystem:
  tool: apify
  github_stars: 172
  npm_weekly_downloads: 44900
  github_repo: apify/apify-sdk-js
  license: Apache-2.0
  maintained: true
---
# Apify Actor Runner

Executes Apify cloud actors for structured web scraping with automatic dataset export to S3. Supports actor input schema validation and webhook-based run completion notifications.

## Overview

The Apify Actor Runner skill interfaces with the Apify platform API to launch and manage cloud-based web scraping actors. It validates actor input against the published input schema, handles API token authentication, and monitors run status through the Apify Client SDK.

The skill supports all Apify storage types including datasets, key-value stores, and request queues. Completed datasets are automatically exported to Amazon S3 using the AWS SDK with multipart upload for large extractions. Export formats include JSON, CSV, XML, and JSONL with configurable field mapping.

Run management features include automatic retry on actor failures with configurable memory allocation scaling, webhook registration for run completion events via the Apify Webhooks API, and cost tracking through the usage endpoint. The skill can chain multiple actors in sequence, passing output datasets as input to downstream actors for multi-stage extraction pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apify-actor-runner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apify-actor-runner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apify-actor-runner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apify-actor-runner -a codex
```

### OpenClaw

```bash
clawhub install apify-actor-runner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-runner/)
