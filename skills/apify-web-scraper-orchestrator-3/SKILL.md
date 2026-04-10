---
name: Apify Web Scraper Orchestrator
description: Orchestrates Apify actors for large-scale web scraping via the Apify
  Client SDK. Manages actor runs, dataset exports, and proxy configuration through
  the Apify API v2.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/
category:
- Research &amp; Scraping
framework:
- Cursor
---
# Apify Web Scraper Orchestrator

This skill orchestrates web scraping workflows using the Apify platform and its Actor ecosystem. It manages the full lifecycle of scraping tasks through the Apify Client SDK, from actor selection and input configuration to dataset collection and export.
The skill interfaces with the Apify API v2 for programmatic actor execution, supporting both pre-built actors from the Apify Store and custom actors deployed via the Apify CLI. It handles proxy management through Apify Proxy with automatic residential and datacenter proxy rotation.
Data pipeline features include automatic dataset pagination, webhook-triggered exports to cloud storage (S3, GCS), and structured data validation using JSON Schema. The skill manages request queues for URL frontier management with configurable concurrency, retry policies, and crawl depth limits.
Monitoring capabilities include real-time run status polling, memory and CPU usage tracking, and automatic actor restart on failure with exponential backoff.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/)
