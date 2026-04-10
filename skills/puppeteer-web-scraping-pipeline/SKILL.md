---
title: "Puppeteer Web Scraping Pipeline"
description: "Builds web scraping pipelines with Puppeteer using page.evaluate, page.waitForSelector, and browser.newPage. Handles infinite scroll, cookie consent banners, and anti-bot detection with stealth plugin."
slug: "puppeteer-web-scraping-pipeline"
category:
  - "Browser Automation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/"
---

# Puppeteer Web Scraping Pipeline

Builds web scraping pipelines with Puppeteer using page.evaluate, page.waitForSelector, and browser.newPage. Handles infinite scroll, cookie consent banners, and anti-bot detection with stealth plugin.

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
clawhub install puppeteer-web-scraping-pipeline
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including –no-sandbox and –disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/)
