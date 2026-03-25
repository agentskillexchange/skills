---
name: "Apify Actor Web Intelligence Agent"
description: "Deploys intelligent web scraping actors on the Apify platform using the Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify CheerioCrawler and PlaywrightCrawler with automatic scaling."
category: "Research & Scraping"
framework: "Custom Agents"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "apify"  # from ase_tool_match
  github_stars: 172  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 44900  # from ase_npm_downloads
  github_repo: "apify/apify-sdk-js"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/
