---
title: "Apify Actor Web Intelligence Agent"
description: "Deploys intelligent web scraping actors on the Apify platform using the Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify CheerioCrawler and PlaywrightCrawler with automatic scaling."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research & Scraping"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Web Intelligence Agent

This skill builds and deploys web intelligence gathering actors on the Apify cloud platform using the Apify SDK. It leverages CheerioCrawler for fast static page processing and PlaywrightCrawler for JavaScript-heavy sites, with automatic crawler selection based on target site analysis. The RequestQueue API manages URL frontier with deduplication, priority ordering, and retry logic. Extracted data flows into Apify Datasets with automatic schema validation and export to formats including JSON, CSV, and Excel. The skill uses KeyValueStore for caching intermediate results and storing crawler state for resumable runs. Production features include automatic proxy rotation via Apify Proxy with residential and datacenter pools, session management for maintaining login state across requests, and auto-scaling that adjusts concurrency based on target site response times. Webhook integrations trigger downstream workflows when actor runs complete, enabling automated data pipelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-actor-web-intelligence-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apify-actor-web-intelligence-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/)
