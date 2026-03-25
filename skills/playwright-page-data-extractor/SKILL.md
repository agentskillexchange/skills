---
name: "Playwright Page Data Extractor"
description: "Uses Microsoft Playwright’s Node.js API to navigate dynamic web applications, intercept network requests, and extract structured data from React/Vue/Angular SPAs with automatic wait strategies."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-page-data-extractor/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84938  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Page Data Extractor

Uses Microsoft Playwright’s Node.js API to navigate dynamic web applications, intercept network requests, and extract structured data from React/Vue/Angular SPAs with automatic wait strategies.

## Overview

The Playwright Page Data Extractor skill leverages **Microsoft Playwright** for reliable data extraction from modern JavaScript-heavy web applications. It handles React, Vue, and Angular single-page applications that render content client-side, using Playwright’s auto-waiting mechanisms to ensure content is fully loaded before extraction.

The skill uses Playwright’s page.evaluate() for DOM traversal, page.route() for network request interception and API response capture, and page.waitForSelector() with configurable timeout strategies. It generates extraction scripts that handle infinite scroll pagination, modal dialogs, and dynamic content loading via IntersectionObserver patterns.

Advanced capabilities include multi-page crawling with BrowserContext for session isolation, screenshot-based visual comparison for change detection, and HAR file recording for offline analysis. The skill supports proxy configuration, geolocation spoofing for region-specific content, and generates TypeScript extraction scripts with strong typing for extracted data structures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-page-data-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-page-data-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-page-data-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-page-data-extractor -a codex
```

### OpenClaw

```bash
clawhub install playwright-page-data-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-page-data-extractor/
