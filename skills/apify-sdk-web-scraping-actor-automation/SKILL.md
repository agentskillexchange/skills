---
name: Apify SDK for Web Scraping and Actor Automation
description: Apify SDK is the official JavaScript SDK for building Actors, crawlers,
  and data extraction workflows on Apify. It gives agents a structured way to run
  scraping jobs, store outputs, manage inputs, and combine crawler logic with browser
  automation when needed.
verification: security_reviewed
source: https://github.com/apify/apify-sdk-js
category:
- Research &amp; Scraping
framework:
- Multi-Framework
---
# Apify SDK for Web Scraping and Actor Automation

Apify SDK is the official JavaScript toolkit from Apify for building data extraction and automation workloads as reusable Actors. It is designed for teams that need more than a single scraper script: input handling, output storage, retries, scheduling, and deployment can all be wrapped into a consistent Actor workflow. The SDK is published on npm as apify, documented on docs.apify.com, and maintained in Apify’s public GitHub repository.
A practical reason to list this skill is that Apify SDK sits at the intersection of scraping, browser automation, and productionized job execution. An agent can use it to collect product data, monitor pages for change, extract structured records from websites, or run repeatable research pipelines that save results for later use. The SDK works with Apify Actors and can also be combined with Crawlee-based crawlers. The upstream quick start explicitly notes Node.js 16 or later and the install command npm install apify. The docs also explain that teams can optionally add crawlee plus browser libraries like Playwright or Puppeteer depending on the crawler type they need.
For agent ecosystems, Apify SDK is valuable because it turns ad hoc scraping into a more operational workflow. Inputs, outputs, datasets, key-value stores, and actor lifecycle hooks are all first-class concepts, which makes it easier to plug scraping jobs into larger automations. That makes it a good fit for research assistants, competitive monitoring, lead generation pipelines, and recurring web data collection where reliability matters more than a one-off script.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-sdk-web-scraping-actor-automation/)
