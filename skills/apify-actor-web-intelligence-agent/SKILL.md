---
title: "Apify Actor Web Intelligence Agent"
description: "Deploys intelligent web scraping actors on the Apify platform using the Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify CheerioCrawler and PlaywrightCrawler with automatic scaling."
verification: security_reviewed
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research &amp; Scraping"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Web Intelligence Agent

This skill builds and deploys web intelligence gathering actors on the Apify cloud platform using the Apify SDK. It leverages CheerioCrawler for fast static page processing and PlaywrightCrawler for JavaScript-heavy sites, with automatic crawler selection based on target site analysis.

The RequestQueue API manages URL frontier with deduplication, priority ordering, and retry logic. Extracted data flows into Apify Datasets with automatic schema validation and export to formats including JSON, CSV, and Excel. The skill uses KeyValueStore for caching intermediate results and storing crawler state for resumable runs.

Production features include automatic proxy rotation via Apify Proxy with residential and datacenter pools, session management for maintaining login state across requests, and auto-scaling that adjusts concurrency based on target site response times. Webhook integrations trigger downstream workflows when actor runs complete, enabling automated data pipelines.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/)
