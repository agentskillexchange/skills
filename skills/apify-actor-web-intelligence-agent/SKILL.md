---
name: Apify Actor Web Intelligence Agent
description: Deploys intelligent web scraping actors on the Apify platform using the
  Apify SDK with RequestQueue and Dataset APIs. Handles dynamic content via Apify
  CheerioCrawler and PlaywrightCrawler with automatic scaling.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/
category:
- Research &amp; Scraping
framework:
- Custom Agents
---
# Apify Actor Web Intelligence Agent

This skill builds and deploys web intelligence gathering actors on the Apify cloud platform using the Apify SDK. It leverages CheerioCrawler for fast static page processing and PlaywrightCrawler for JavaScript-heavy sites, with automatic crawler selection based on target site analysis.
The RequestQueue API manages URL frontier with deduplication, priority ordering, and retry logic. Extracted data flows into Apify Datasets with automatic schema validation and export to formats including JSON, CSV, and Excel. The skill uses KeyValueStore for caching intermediate results and storing crawler state for resumable runs.
Production features include automatic proxy rotation via Apify Proxy with residential and datacenter pools, session management for maintaining login state across requests, and auto-scaling that adjusts concurrency based on target site response times. Webhook integrations trigger downstream workflows when actor runs complete, enabling automated data pipelines.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-web-intelligence-agent/)
