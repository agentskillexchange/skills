---
title: "Playwright Network Interceptor"
description: "The Playwright Network Interceptor provides advanced network traffic analysis and manipulation using Playwright browser automation. It configures page.route() handlers with glob and regex URL patterns for request interception, response modification, and API data extraction without DOM parsing.\nThe agent generates scripts that leverage route.fulfill() for response mocking, route.continue() with modified headers for authentication injection, and route.abort() for blocking unnecessary resources like images, fonts, and analytics scripts to accelerate page loads during scraping.\nKey capabilities include HAR file recording via browser.newContext({ recordHar }) for complete network session capture and replay, WebSocket frame interception using page.on(“websocket”) for real-time data stream capture, and request timing analysis via response.timing() for performance profiling. The agent also implements stealth techniques using playwright-extra with the stealth plugin, handles Cloudflare challenges via browser context persistence, and configures proxy chains with per-context proxy settings for IP rotation."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  ase_npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Network Interceptor

The Playwright Network Interceptor provides advanced network traffic analysis and manipulation using Playwright browser automation. It configures page.route() handlers with glob and regex URL patterns for request interception, response modification, and API data extraction without DOM parsing.
The agent generates scripts that leverage route.fulfill() for response mocking, route.continue() with modified headers for authentication injection, and route.abort() for blocking unnecessary resources like images, fonts, and analytics scripts to accelerate page loads during scraping.
Key capabilities include HAR file recording via browser.newContext({ recordHar }) for complete network session capture and replay, WebSocket frame interception using page.on(“websocket”) for real-time data stream capture, and request timing analysis via response.timing() for performance profiling. The agent also implements stealth techniques using playwright-extra with the stealth plugin, handles Cloudflare challenges via browser context persistence, and configures proxy chains with per-context proxy settings for IP rotation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/playwright-network-interceptor
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/playwright-network-interceptor` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-interceptor/)
