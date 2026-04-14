---
title: "Apify Actor Development Kit"
description: "Builds Apify Actors for scalable cloud scraping with automatic proxy management and storage. Uses the Apify SDK (Actor, Dataset, KeyValueStore, RequestQueue) and Crawlee library for robust crawling."
verification: security_reviewed
source: "https://github.com/apify/apify-sdk-js"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "apify/apify-sdk-js"
  github_stars: 173
  npm_package: "apify"
  npm_weekly_downloads: 34097
---

# Apify Actor Development Kit

The Apify Actor Development Kit creates scalable web scraping actors using the Apify SDK and Crawlee library. It generates Actor configurations with proper Dockerfile, INPUT_SCHEMA.json, and .actor/actor.json manifests for deployment to the Apify Cloud platform.

The agent leverages Crawlee crawlers including PlaywrightCrawler for JavaScript-heavy sites, CheerioCrawler for lightweight HTML parsing, and HttpCrawler for API endpoint scraping. It configures RequestQueue for URL frontier management with maxRequestsPerCrawl limits and request uniqueness via uniqueKey hashing.

Advanced features include Apify Proxy integration with automatic session rotation using ProxyConfiguration with groups and countryCode targeting. The agent sets up Dataset.pushData for structured output storage, KeyValueStore for state persistence across migrations, and implements AutoscaledPool configuration for dynamic concurrency adjustment based on system resources. It also generates Actor input schemas with validation constraints and default values for the Apify Console UI.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/apify-actor-development-kit/)
