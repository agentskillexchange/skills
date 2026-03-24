---
name: "Playwright Network Interceptor"
description: "Intercepts and analyzes network traffic using Playwright route handlers for API response capture and modification. Uses the Playwright page.route() API, HAR recording, and request/response event listeners."
category: "Research & Scraping"
framework: "Cursor"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-network-interceptor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Network Interceptor

Intercepts and analyzes network traffic using Playwright route handlers for API response capture and modification. Uses the Playwright page.route() API, HAR recording, and request/response event listeners.

## Overview

The Playwright Network Interceptor provides advanced network traffic analysis and manipulation using Playwright browser automation. It configures page.route() handlers with glob and regex URL patterns for request interception, response modification, and API data extraction without DOM parsing.

The agent generates scripts that leverage route.fulfill() for response mocking, route.continue() with modified headers for authentication injection, and route.abort() for blocking unnecessary resources like images, fonts, and analytics scripts to accelerate page loads during scraping.

Key capabilities include HAR file recording via browser.newContext({ recordHar }) for complete network session capture and replay, WebSocket frame interception using page.on(“websocket”) for real-time data stream capture, and request timing analysis via response.timing() for performance profiling. The agent also implements stealth techniques using playwright-extra with the stealth plugin, handles Cloudflare challenges via browser context persistence, and configures proxy chains with per-context proxy settings for IP rotation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-network-interceptor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-network-interceptor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-network-interceptor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-network-interceptor -a codex
```

### OpenClaw

```bash
clawhub install playwright-network-interceptor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-network-interceptor/
