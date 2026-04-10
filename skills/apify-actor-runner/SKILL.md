---
name: Apify Actor Runner
description: Executes Apify cloud actors for structured web scraping with automatic
  dataset export to S3. Supports actor input schema validation and webhook-based run
  completion notifications.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-actor-runner/
category:
- Research &amp; Scraping
framework:
- Codex
---
# Apify Actor Runner

The Apify Actor Runner skill interfaces with the Apify platform API to launch and manage cloud-based web scraping actors. It validates actor input against the published input schema, handles API token authentication, and monitors run status through the Apify Client SDK.
The skill supports all Apify storage types including datasets, key-value stores, and request queues. Completed datasets are automatically exported to Amazon S3 using the AWS SDK with multipart upload for large extractions. Export formats include JSON, CSV, XML, and JSONL with configurable field mapping.
Run management features include automatic retry on actor failures with configurable memory allocation scaling, webhook registration for run completion events via the Apify Webhooks API, and cost tracking through the usage endpoint. The skill can chain multiple actors in sequence, passing output datasets as input to downstream actors for multi-stage extraction pipelines.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-runner/)
