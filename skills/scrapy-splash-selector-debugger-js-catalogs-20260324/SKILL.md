---
name: "Scrapy Splash Selector Debugger for JS Catalogs"
description: "Helps debug Scrapy plus Splash spiders on JavaScript-heavy catalog pages by comparing rendered DOM output, response HTML, Lua scripts, and CSS/XPath selector results. It is useful when product grids, filters, or lazy-loaded details behave differently in browser and crawler contexts."
category: "Research & Scraping"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/scrapy-splash-selector-debugger-js-catalogs-20260324/"
---

# Scrapy Splash Selector Debugger for JS Catalogs

Helps debug Scrapy plus Splash spiders on JavaScript-heavy catalog pages by comparing rendered DOM output, response HTML, Lua scripts, and CSS/XPath selector results. It is useful when product grids, filters, or lazy-loaded details behave differently in browser and crawler contexts.

## Overview

This skill focuses on a classic scraping failure mode: a site looks correct in a browser, but a **Scrapy** spider returns incomplete or misleading HTML. By pairing Scrapy with **Splash**, rendered requests, and selector diagnostics, the skill helps identify where JavaScript hydration, delayed API calls, or client-side filtering break an extraction workflow. It compares raw responses with Splash-rendered responses, checks CSS and XPath selectors against both versions, and records where product cards, price blocks, stock indicators, or pagination links diverge. That is especially useful for legacy e-commerce stacks and catalog systems that are not fully headless but still depend on client-side rendering for critical data.

The workflow can emit a debugging bundle with the request URL, Lua render script, wait timings, HAR-like network notes, extracted selector matches, and screenshots for each test page. It also recommends whether a spider should stay in Scrapy, move to Splash, or escalate to Playwright or Selenium for more complex interaction. Integration points include Scrapyd deployment, Docker Compose services for Splash, GitHub Actions for regression tests, and JSON exports that can feed dbt or warehouse ingestion jobs later. The outputs are concrete: corrected selectors, a working Lua script, a spider patch plan, and a short report explaining which elements were available in raw HTML versus rendered DOM. That turns trial-and-error scraping into a documented debugging process.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill scrapy-splash-selector-debugger-js-catalogs-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill scrapy-splash-selector-debugger-js-catalogs-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill scrapy-splash-selector-debugger-js-catalogs-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill scrapy-splash-selector-debugger-js-catalogs-20260324 -a codex
```

### OpenClaw

```bash
clawhub install scrapy-splash-selector-debugger-js-catalogs-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/scrapy-splash-selector-debugger-js-catalogs-20260324/
