---
title: "Browserless Scraping Agent"
description: "Drives headless Chrome via the Browserless.io API for scraping dynamic SPAs. Uses /content, /screenshot, and /pdf endpoints with stealth mode. Manages session tokens and concurrent connection limits."
verification: "security_reviewed"
source: "https://docs.browserless.io/"
category:
  - "Research & Scraping"
framework:
  - "Cursor"
---

# Browserless Scraping Agent

The Browserless Scraping Agent skill enables Claude to scrape JavaScript-heavy single-page applications using Browserless.io’s hosted Chrome infrastructure. It communicates through the Browserless REST API, using endpoints like /content for rendered HTML, /screenshot for visual captures, and /pdf for document generation.

The skill configures stealth mode to avoid bot detection, setting appropriate user-agent strings, viewport dimensions, and JavaScript execution timing. It handles wait conditions — waiting for specific selectors, network idle states, or custom JavaScript expressions before extracting content.

Connection management is built in: the skill tracks concurrent connections against the plan limit, queues excess requests, and manages session tokens for authenticated scraping flows. It supports cookie injection for accessing content behind login walls.

For complex extraction, the skill injects custom JavaScript functions that run in the page context to extract structured data from DOM elements. Results are returned as clean JSON objects. The skill also supports generating PDFs of rendered pages for archival purposes. Rate limiting and retry logic handle transient failures gracefully. Best suited for scraping modern web applications that resist traditional HTTP-based extraction.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/browserless-scraping-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/browserless-scraping-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/browserless-scraping-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/browserless-scraping-agent/)
