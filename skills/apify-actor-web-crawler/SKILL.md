---
title: "Apify Actor Web Crawler"
description: "Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale."
slug: "apify-actor-web-crawler"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/apify-actor-web-crawler/"
listed: true
---

# Apify Actor Web Crawler

Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale.

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
clawhub install apify-actor-web-crawler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Apify Actor Web Crawler deploys custom web crawling Actors through the Apify API v2 for enterprise-scale data collection. Built on the CrawleeJS framework, it supports PlaywrightCrawler for JavaScript-rendered pages and CheerioCrawler for static HTML scraping with automatic scaling based on system resources and target site responsiveness. The RequestQueue manages URL frontier with built-in deduplication and retry logic. Apify proxy configuration supports datacenter and residential proxy pools with automatic rotation and session management. Extracted data flows into Apify Datasets with automatic schema validation and exports to formats including JSON, CSV, and Excel through the dataset API. The agent handles complex crawling patterns including infinite scroll detection, login session management with cookie persistence, and sitemap-based URL discovery. Actor runs are monitored through the Apify monitoring dashboard API with configurable alerts for run failures or anomalous result counts.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-crawler/)
