---
name: "Apify Actor Web Intelligence Agent"
description: "Deploys intelligent web scraping actors on the Apify platform using the Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify CheerioCrawler and PlaywrightCrawler with automatic scaling."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/"
---
# Apify Actor Web Intelligence Agent

Deploys intelligent web scraping actors on the Apify platform using the Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify CheerioCrawler and PlaywrightCrawler with automatic scaling.

## Overview

This skill builds and deploys web intelligence gathering actors on the Apify cloud platform using the Apify SDK. It leverages CheerioCrawler for fast static page processing and PlaywrightCrawler for JavaScript-heavy sites, with automatic crawler selection based on target site analysis.

The RequestQueue API manages URL frontier with deduplication, priority ordering, and retry logic. Extracted data flows into Apify Datasets with automatic schema validation and export to formats including JSON, CSV, and Excel. The skill uses KeyValueStore for caching intermediate results and storing crawler state for resumable runs.

Production features include automatic proxy rotation via Apify Proxy with residential and datacenter pools, session management for maintaining login state across requests, and auto-scaling that adjusts concurrency based on target site response times. Webhook integrations trigger downstream workflows when actor runs complete, enabling automated data pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-intelligence-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-intelligence-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-intelligence-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-intelligence-agent -a codex
```

### OpenClaw

```bash
clawhub install apify-actor-web-intelligence-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/)
