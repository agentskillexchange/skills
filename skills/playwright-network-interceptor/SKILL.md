---
title: "Playwright Network Interceptor"
description: "Intercepts and analyzes network traffic using Playwright route handlers for API response capture and modification. Uses the Playwright page.route() API, HAR recording, and request/response event listeners."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
category:
  - "Research &amp; Scraping"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Network Interceptor

The Playwright Network Interceptor provides advanced network traffic analysis and manipulation using Playwright browser automation. It configures page.route() handlers with glob and regex URL patterns for request interception, response modification, and API data extraction without DOM parsing.

The agent generates scripts that leverage route.fulfill() for response mocking, route.continue() with modified headers for authentication injection, and route.abort() for blocking unnecessary resources like images, fonts, and analytics scripts to accelerate page loads during scraping.

Key capabilities include HAR file recording via browser.newContext({ recordHar }) for complete network session capture and replay, WebSocket frame interception using page.on(“websocket”) for real-time data stream capture, and request timing analysis via response.timing() for performance profiling. The agent also implements stealth techniques using playwright-extra with the stealth plugin, handles Cloudflare challenges via browser context persistence, and configures proxy chains with per-context proxy settings for IP rotation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-network-interceptor/)
