---
name: "Puppeteer Web Scraping Pipeline"
description: "Builds web scraping pipelines with Puppeteer using page.evaluate, page.waitForSelector, and browser.newPage. Handles infinite scroll, cookie consent banners, and anti-bot detection with stealth plugin."
category: "Browser Automation"
framework: "Gemini"
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  tool: puppeteer
  github_repo: puppeteer/puppeteer
  github_stars: 93971
  license: Apache-2.0
  maintained: true
---
# Puppeteer Web Scraping Pipeline

Builds web scraping pipelines with Puppeteer using page.evaluate, page.waitForSelector, and browser.newPage. Handles infinite scroll, cookie consent banners, and anti-bot detection with stealth plugin.

## Overview

This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including -no-sandbox and -disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraping-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraping-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraping-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-web-scraping-pipeline -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-web-scraping-pipeline
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/)
