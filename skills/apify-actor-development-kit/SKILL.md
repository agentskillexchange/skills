---
title: Apify Actor Development Kit
description: The Apify Actor Development Kit creates scalable web scraping actors
  using the Apify SDK and Crawlee library. It generates Actor configurations with
  proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment
  to the Apify Cloud platform. The agent leverages Crawlee crawlers including PlaywrightCrawler
  for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler
  for API endpoint scraping. It configures RequestQueue for URL frontier management
  with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing. Advanced
  features include Apify Proxy integration with automatic session rotation using ProxyConfiguration
  with groups and countryCode targeting. The agent sets up Dataset.pushData for structured
  output storage, KeyValueStore for state persistence across migrations, and implements
  AutoscaledPool configuration for dynamic concurrency adjustment based on system
  resources. It also generates Actor input schemas with validation constraints and
  default values for the Apify Console UI.
verification: security_reviewed
source: https://agentskillexchange.com/skills/apify-actor-development-kit/
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# Apify Actor Development Kit

The Apify Actor Development Kit creates scalable web scraping actors using the Apify SDK and Crawlee library. It generates Actor configurations with proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment to the Apify Cloud platform. The agent leverages Crawlee crawlers including PlaywrightCrawler for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler for API endpoint scraping. It configures RequestQueue for URL frontier management with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing. Advanced features include Apify Proxy integration with automatic session rotation using ProxyConfiguration with groups and countryCode targeting. The agent sets up Dataset.pushData for structured output storage, KeyValueStore for state persistence across migrations, and implements AutoscaledPool configuration for dynamic concurrency adjustment based on system resources. It also generates Actor input schemas with validation constraints and default values for the Apify Console UI.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-development-kit/)
