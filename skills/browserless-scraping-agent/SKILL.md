---
title: "Browserless Scraping Agent"
description: "The Browserless Scraping Agent skill enables Claude to scrape JavaScript-heavy single-page applications using Browserless.io&#8217;s hosted Chrome infrastructure. It communicates through the Browserless REST API, using endpoints like /content for rendered HTML, /screenshot for visual captures, and /pdf for document generation. The skill configures stealth mode to avoid bot detection, setting appropriate user-agent strings, viewport dimensions, and JavaScript execution timing. It handles wait conditions — waiting for specific selectors, network idle states, or custom JavaScript expressions before extracting content. Connection management is built in: the skill tracks concurrent connections against the plan limit, queues excess requests, and manages session tokens for authenticated scraping flows. It supports cookie injection for accessing content behind login walls. For complex extraction, the skill injects custom JavaScript functions that run in the page context to extract structured data from DOM elements. Results are returned as clean JSON objects. The skill also supports generating PDFs of rendered pages for archival purposes. Rate limiting and retry logic handle transient failures gracefully. Best suited for scraping modern web applications that resist traditional HTTP-based extraction."
source: "https://agentskillexchange.com/skills/browserless-scraping-agent/"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
---

# Browserless Scraping Agent

The Browserless Scraping Agent skill enables Claude to scrape JavaScript-heavy single-page applications using Browserless.io&#8217;s hosted Chrome infrastructure. It communicates through the Browserless REST API, using endpoints like /content for rendered HTML, /screenshot for visual captures, and /pdf for document generation. The skill configures stealth mode to avoid bot detection, setting appropriate user-agent strings, viewport dimensions, and JavaScript execution timing. It handles wait conditions — waiting for specific selectors, network idle states, or custom JavaScript expressions before extracting content. Connection management is built in: the skill tracks concurrent connections against the plan limit, queues excess requests, and manages session tokens for authenticated scraping flows. It supports cookie injection for accessing content behind login walls. For complex extraction, the skill injects custom JavaScript functions that run in the page context to extract structured data from DOM elements. Results are returned as clean JSON objects. The skill also supports generating PDFs of rendered pages for archival purposes. Rate limiting and retry logic handle transient failures gracefully. Best suited for scraping modern web applications that resist traditional HTTP-based extraction.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserless-scraping-agent/)
