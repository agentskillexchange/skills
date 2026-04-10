---
name: "Playwright Page Data Extractor"
description: "Uses Microsoft Playwright's Node.js API to navigate dynamic web applications, intercept network requests, and extract structured data from React/Vue/Angular SPAs with automatic wait strategies."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-page-data-extractor/"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
---

# Playwright Page Data Extractor

The Playwright Page Data Extractor skill leverages Microsoft Playwright for reliable data extraction from modern JavaScript-heavy web applications. It handles React, Vue, and Angular single-page applications that render content client-side, using Playwright's auto-waiting mechanisms to ensure content is fully loaded before extraction.
The skill uses Playwright's page.evaluate() for DOM traversal, page.route() for network request interception and API response capture, and page.waitForSelector() with configurable timeout strategies. It generates extraction scripts that handle infinite scroll pagination, modal dialogs, and dynamic content loading via IntersectionObserver patterns.
Advanced capabilities include multi-page crawling with BrowserContext for session isolation, screenshot-based visual comparison for change detection, and HAR file recording for offline analysis. The skill supports proxy configuration, geolocation spoofing for region-specific content, and generates TypeScript extraction scripts with strong typing for extracted data structures.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-page-data-extractor/)
