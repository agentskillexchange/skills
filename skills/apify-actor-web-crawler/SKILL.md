---
title: "Apify Actor Web Crawler"
description: "Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  ase_npm_package: "apify"
  npm_weekly_downloads: 34097
  license: "Apache-2.0"
---

# Apify Actor Web Crawler

The Apify Actor Web Crawler deploys custom web crawling Actors through the Apify API v2 for enterprise-scale data collection. Built on the CrawleeJS framework, it supports PlaywrightCrawler for JavaScript-rendered pages and CheerioCrawler for static HTML scraping with automatic scaling based on system resources and target site responsiveness. The RequestQueue manages URL frontier with built-in deduplication and retry logic. Apify proxy configuration supports datacenter and residential proxy pools with automatic rotation and session management. Extracted data flows into Apify Datasets with automatic schema validation and exports to formats including JSON, CSV, and Excel through the dataset API. The agent handles complex crawling patterns including infinite scroll detection, login session management with cookie persistence, and sitemap-based URL discovery. Actor runs are monitored through the Apify monitoring dashboard API with configurable alerts for run failures or anomalous result counts.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-crawler/)
