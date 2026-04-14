---
title: "Apify Actor Web Crawler"
description: "Deploys custom Apify Actors via the Apify API v2 for large-scale web crawling using CrawleeJS. Leverages Apify dataset storage, RequestQueue, and proxy configuration for distributed scraping at scale."
verification: security_reviewed
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Web Crawler

The Apify Actor Web Crawler deploys custom web crawling Actors through the Apify API v2 for enterprise-scale data collection. Built on the CrawleeJS framework, it supports PlaywrightCrawler for JavaScript-rendered pages and CheerioCrawler for static HTML scraping with automatic scaling based on system resources and target site responsiveness. The RequestQueue manages URL frontier with built-in deduplication and retry logic. Apify proxy configuration supports datacenter and residential proxy pools with automatic rotation and session management. Extracted data flows into Apify Datasets with automatic schema validation and exports to formats including JSON, CSV, and Excel through the dataset API. The agent handles complex crawling patterns including infinite scroll detection, login session management with cookie persistence, and sitemap-based URL discovery. Actor runs are monitored through the Apify monitoring dashboard API with configurable alerts for run failures or anomalous result counts.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-crawler/)
