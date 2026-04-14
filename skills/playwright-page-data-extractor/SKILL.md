---
title: "Playwright Page Data Extractor"
description: "Uses Microsoft Playwright’s Node.js API to navigate dynamic web applications, intercept network requests, and extract structured data from React/Vue/Angular SPAs with automatic wait strategies."
verification: security_reviewed
source: "https://github.com/microsoft/playwright"
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

The Playwright Page Data Extractor skill leverages Microsoft Playwright for reliable data extraction from modern JavaScript-heavy web applications. It handles React, Vue, and Angular single-page applications that render content client-side, using Playwright’s auto-waiting mechanisms to ensure content is fully loaded before extraction.

The skill uses Playwright’s page.evaluate() for DOM traversal, page.route() for network request interception and API response capture, and page.waitForSelector() with configurable timeout strategies. It generates extraction scripts that handle infinite scroll pagination, modal dialogs, and dynamic content loading via IntersectionObserver patterns.

Advanced capabilities include multi-page crawling with BrowserContext for session isolation, screenshot-based visual comparison for change detection, and HAR file recording for offline analysis. The skill supports proxy configuration, geolocation spoofing for region-specific content, and generates TypeScript extraction scripts with strong typing for extracted data structures.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-page-data-extractor/)
