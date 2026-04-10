---
title: "Playwright Network Interceptor"
description: "Intercepts and analyzes network traffic using Playwright route handlers for API response capture and modification. Uses the Playwright page.route() API, HAR recording, and request/response event listeners."
slug: "playwright-network-interceptor"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/playwright-network-interceptor/"
---

# Playwright Network Interceptor

Intercepts and analyzes network traffic using Playwright route handlers for API response capture and modification. Uses the Playwright page.route() API, HAR recording, and request/response event listeners.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install playwright-network-interceptor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Playwright Network Interceptor provides advanced network traffic analysis and manipulation using Playwright browser automation. It configures page.route() handlers with glob and regex URL patterns for request interception, response modification, and API data extraction without DOM parsing.
The agent generates scripts that leverage route.fulfill() for response mocking, route.continue() with modified headers for authentication injection, and route.abort() for blocking unnecessary resources like images, fonts, and analytics scripts to accelerate page loads during scraping.
Key capabilities include HAR file recording via browser.newContext({ recordHar }) for complete network session capture and replay, WebSocket frame interception using page.on(“websocket”) for real-time data stream capture, and request timing analysis via response.timing() for performance profiling. The agent also implements stealth techniques using playwright-extra with the stealth plugin, handles Cloudflare challenges via browser context persistence, and configures proxy chains with per-context proxy settings for IP rotation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-interceptor/)
