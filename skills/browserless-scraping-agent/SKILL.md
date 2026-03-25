---
name: "Browserless Scraping Agent"
description: "Drives headless Chrome via the Browserless.io API for scraping dynamic SPAs. Uses /content, /screenshot, and /pdf endpoints with stealth mode. Manages session tokens and concurrent connection limits."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/browserless-scraping-agent/"
---

# Browserless Scraping Agent

Drives headless Chrome via the Browserless.io API for scraping dynamic SPAs. Uses /content, /screenshot, and /pdf endpoints with stealth mode. Manages session tokens and concurrent connection limits.

## Overview

The Browserless Scraping Agent skill enables Claude to scrape JavaScript-heavy single-page applications using Browserless.io’s hosted Chrome infrastructure. It communicates through the Browserless REST API, using endpoints like /content for rendered HTML, /screenshot for visual captures, and /pdf for document generation.

The skill configures stealth mode to avoid bot detection, setting appropriate user-agent strings, viewport dimensions, and JavaScript execution timing. It handles wait conditions — waiting for specific selectors, network idle states, or custom JavaScript expressions before extracting content.

Connection management is built in: the skill tracks concurrent connections against the plan limit, queues excess requests, and manages session tokens for authenticated scraping flows. It supports cookie injection for accessing content behind login walls.

For complex extraction, the skill injects custom JavaScript functions that run in the page context to extract structured data from DOM elements. Results are returned as clean JSON objects. The skill also supports generating PDFs of rendered pages for archival purposes. Rate limiting and retry logic handle transient failures gracefully. Best suited for scraping modern web applications that resist traditional HTTP-based extraction.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill browserless-scraping-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill browserless-scraping-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill browserless-scraping-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill browserless-scraping-agent -a codex
```

### OpenClaw

```bash
clawhub install browserless-scraping-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/browserless-scraping-agent/
