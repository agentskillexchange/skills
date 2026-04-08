---
title: Apify Actor Runner
description: The Apify Actor Runner skill interfaces with the Apify platform API to
  launch and manage cloud-based web scraping actors. It validates actor input against
  the published input schema, handles API token authentication, and monitors run status
  through the Apify Client SDK. The skill supports all Apify storage types including
  datasets, key-value stores, and request queues. Completed datasets are automatically
  exported to Amazon S3 using the AWS SDK with multipart upload for large extractions.
  Export formats include JSON, CSV, XML, and JSONL with configurable field mapping.
  Run management features include automatic retry on actor failures with configurable
  memory allocation scaling, webhook registration for run completion events via the
  Apify Webhooks API, and cost tracking through the usage endpoint. The skill can
  chain multiple actors in sequence, passing output datasets as input to downstream
  actors for multi-stage extraction pipelines.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-actor-runner/
category:
- Research &amp; Scraping
framework:
- Codex
---

# Apify Actor Runner

The Apify Actor Runner skill interfaces with the Apify platform API to launch and manage cloud-based web scraping actors. It validates actor input against the published input schema, handles API token authentication, and monitors run status through the Apify Client SDK. The skill supports all Apify storage types including datasets, key-value stores, and request queues. Completed datasets are automatically exported to Amazon S3 using the AWS SDK with multipart upload for large extractions. Export formats include JSON, CSV, XML, and JSONL with configurable field mapping. Run management features include automatic retry on actor failures with configurable memory allocation scaling, webhook registration for run completion events via the Apify Webhooks API, and cost tracking through the usage endpoint. The skill can chain multiple actors in sequence, passing output datasets as input to downstream actors for multi-stage extraction pipelines.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-runner/)
