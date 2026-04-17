---
title: "Apify Web Scraper Orchestrator"
description: "This skill orchestrates web scraping workflows using the Apify platform and its Actor ecosystem. It manages the full lifecycle of scraping tasks through the Apify Client SDK, from actor selection and input configuration to dataset collection and export.\nThe skill interfaces with the Apify API v2 for programmatic actor execution, supporting both pre-built actors from the Apify Store and custom actors deployed via the Apify CLI. It handles proxy management through Apify Proxy with automatic residential and datacenter proxy rotation.\nData pipeline features include automatic dataset pagination, webhook-triggered exports to cloud storage (S3, GCS), and structured data validation using JSON Schema. The skill manages request queues for URL frontier management with configurable concurrency, retry policies, and crawl depth limits.\nMonitoring capabilities include real-time run status polling, memory and CPU usage tracking, and automatic actor restart on failure with exponential backoff."
verification: security_reviewed
source: "https://github.com/apify/apify-sdk-js"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  ase_npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Web Scraper Orchestrator

This skill orchestrates web scraping workflows using the Apify platform and its Actor ecosystem. It manages the full lifecycle of scraping tasks through the Apify Client SDK, from actor selection and input configuration to dataset collection and export.
The skill interfaces with the Apify API v2 for programmatic actor execution, supporting both pre-built actors from the Apify Store and custom actors deployed via the Apify CLI. It handles proxy management through Apify Proxy with automatic residential and datacenter proxy rotation.
Data pipeline features include automatic dataset pagination, webhook-triggered exports to cloud storage (S3, GCS), and structured data validation using JSON Schema. The skill manages request queues for URL frontier management with configurable concurrency, retry policies, and crawl depth limits.
Monitoring capabilities include real-time run status polling, memory and CPU usage tracking, and automatic actor restart on failure with exponential backoff.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-web-scraper-orchestrator-3
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/apify-web-scraper-orchestrator-3` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-web-scraper-orchestrator-3/)
