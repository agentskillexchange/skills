---
title: "Playwright Page Data Extractor"
description: "The Playwright Page Data Extractor skill leverages Microsoft Playwright for reliable data extraction from modern JavaScript-heavy web applications. It handles React, Vue, and Angular single-page applications that render content client-side, using Playwright&#8217;s auto-waiting mechanisms to ensure content is fully loaded before extraction. The skill uses Playwright&#8217;s page.evaluate() for DOM traversal, page.route() for network request interception and API response capture, and page.waitForSelector() with configurable timeout strategies. It generates extraction scripts that handle infinite scroll pagination, modal dialogs, and dynamic content loading via IntersectionObserver patterns. Advanced capabilities include multi-page crawling with BrowserContext for session isolation, screenshot-based visual comparison for change detection, and HAR file recording for offline analysis. The skill supports proxy configuration, geolocation spoofing for region-specific content, and generates TypeScript extraction scripts with strong typing for extracted data structures."
source: "https://github.com/microsoft/playwright"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "microsoft/playwright"
  github_stars: 86409
  npm_package: "playwright"
  npm_weekly_downloads: 47883561
---

# Playwright Page Data Extractor

The Playwright Page Data Extractor skill leverages Microsoft Playwright for reliable data extraction from modern JavaScript-heavy web applications. It handles React, Vue, and Angular single-page applications that render content client-side, using Playwright&#8217;s auto-waiting mechanisms to ensure content is fully loaded before extraction. The skill uses Playwright&#8217;s page.evaluate() for DOM traversal, page.route() for network request interception and API response capture, and page.waitForSelector() with configurable timeout strategies. It generates extraction scripts that handle infinite scroll pagination, modal dialogs, and dynamic content loading via IntersectionObserver patterns. Advanced capabilities include multi-page crawling with BrowserContext for session isolation, screenshot-based visual comparison for change detection, and HAR file recording for offline analysis. The skill supports proxy configuration, geolocation spoofing for region-specific content, and generates TypeScript extraction scripts with strong typing for extracted data structures.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-page-data-extractor/)
