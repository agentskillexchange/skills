---
name: Apify Actor Development Kit
description: Builds Apify Actors for scalable cloud scraping with automatic proxy
  management and storage. Uses the Apify SDK (Actor, Dataset, KeyValueStore, RequestQueue)
  and Crawlee library for robust crawling.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-actor-development-kit/
category:
- Research &amp; Scraping
framework:
- Claude Code
---
# Apify Actor Development Kit

The Apify Actor Development Kit creates scalable web scraping actors using the Apify SDK and Crawlee library. It generates Actor configurations with proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment to the Apify Cloud platform.
The agent leverages Crawlee crawlers including PlaywrightCrawler for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler for API endpoint scraping. It configures RequestQueue for URL frontier management with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing.
Advanced features include Apify Proxy integration with automatic session rotation using ProxyConfiguration with groups and countryCode targeting. The agent sets up Dataset.pushData for structured output storage, KeyValueStore for state persistence across migrations, and implements AutoscaledPool configuration for dynamic concurrency adjustment based on system resources. It also generates Actor input schemas with validation constraints and default values for the Apify Console UI.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-development-kit/)
