---
title: "Apify SDK for Web Scraping and Actor Automation"
description: "Apify SDK is the official JavaScript SDK for building Actors, crawlers, and data extraction workflows on Apify. It gives agents a structured way to run scraping jobs, store outputs, manage inputs, and combine crawler logic with browser automation when needed."
verification: "security_reviewed"
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
---

# Apify SDK for Web Scraping and Actor Automation

Apify SDK is the official JavaScript toolkit from Apify for building data extraction and automation workloads as reusable Actors. It is designed for teams that need more than a single scraper script: input handling, output storage, retries, scheduling, and deployment can all be wrapped into a consistent Actor workflow. The SDK is published on npm as apify, documented on docs.apify.com, and maintained in Apify’s public GitHub repository. A practical reason to list this skill is that Apify SDK sits at the intersection of scraping, browser automation, and productionized job execution. An agent can use it to collect product data, monitor pages for change, extract structured records from websites, or run repeatable research pipelines that save results for later use. The SDK works with Apify Actors and can also be combined with Crawlee-based crawlers. The upstream quick start explicitly notes Node.js 16 or later and the install command npm install apify. The docs also explain that teams can optionally add crawlee plus browser libraries like Playwright or Puppeteer depending on the crawler type they need. For agent ecosystems, Apify SDK is valuable because it turns ad hoc scraping into a more operational workflow. Inputs, outputs, datasets, key-value stores, and actor lifecycle hooks are all first-class concepts, which makes it easier to plug scraping jobs into larger automations. That makes it a good fit for research assistants, competitive monitoring, lead generation pipelines, and recurring web data collection where reliability matters more than a one-off script.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/apify-sdk-web-scraping-actor-automation/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/apify-sdk-web-scraping-actor-automation
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/apify-sdk-web-scraping-actor-automation`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-sdk-web-scraping-actor-automation/)
