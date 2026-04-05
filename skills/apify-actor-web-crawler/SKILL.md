---
name: "Apify Actor Web Crawler"
description: "Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale."
category: "Research &amp; Scraping"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apify-actor-web-crawler/"
---
# Apify Actor Web Crawler

Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-crawler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-crawler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-crawler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill apify-actor-web-crawler -a codex
```

### OpenClaw

```bash
clawhub install apify-actor-web-crawler
```

## Details

The Apify Actor Web Crawler deploys custom web crawling Actors through the Apify API v2 for enterprise-scale data collection. Built on the CrawleeJS framework, it supports PlaywrightCrawler for JavaScript-rendered pages and CheerioCrawler for static HTML scraping with automatic scaling based on system resources and target site responsiveness. The RequestQueue manages URL frontier with built-in deduplication and retry logic. Apify proxy configuration supports datacenter and residential proxy pools with automatic rotation and session management. Extracted data flows into Apify Datasets with automatic schema validation and exports to formats including JSON, CSV, and Excel through the dataset API. The agent handles complex crawling patterns including infinite scroll detection, login session management with cookie persistence, and sitemap-based URL discovery. Actor runs are monitored through the Apify monitoring dashboard API with configurable alerts for run failures or anomalous result counts.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-crawler/)
