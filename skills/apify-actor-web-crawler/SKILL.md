---
name: "Apify Actor Web Crawler"
description: "Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/apify-actor-web-crawler/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
---

# Apify Actor Web Crawler

The Apify Actor Web Crawler deploys custom web crawling Actors through the Apify API v2 for enterprise-scale data collection. Built on the CrawleeJS framework, it supports PlaywrightCrawler for JavaScript-rendered pages and CheerioCrawler for static HTML scraping with automatic scaling based on system resources and target site responsiveness. The RequestQueue manages URL frontier with built-in deduplication and retry logic. Apify proxy configuration supports datacenter and residential proxy pools with automatic rotation and session management. Extracted data flows into Apify Datasets with automatic schema validation and exports to formats including JSON, CSV, and Excel through the dataset API. The agent handles complex crawling patterns including infinite scroll detection, login session management with cookie persistence, and sitemap-based URL discovery. Actor runs are monitored through the Apify monitoring dashboard API with configurable alerts for run failures or anomalous result counts.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-crawler/)
