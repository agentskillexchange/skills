---
title: Puppeteer Web Scraping Pipeline
description: This skill creates robust web scraping pipelines using Puppeteer with
  the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless
  Chrome via puppeteer.launch() with custom args including –no-sandbox and –disable-setuid-sandbox
  for container environments. Page interactions use page.evaluate() for DOM extraction,
  page.waitForSelector() with timeout configurations, and page.click() for pagination.
  Infinite scroll handling uses page.evaluate to detect scroll height changes and
  window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed
  through pattern matching on common consent management platforms like OneTrust and
  Cookiebot. The agent manages request interception via page.setRequestInterception(true)
  to block unnecessary resources like images and fonts for faster scraping. Data extraction
  uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented
  with configurable delays between requests. The skill includes proxy rotation support
  via page.authenticate() and handles CAPTCHAs through 2captcha API integration when
  needed. Results are streamed to NDJSON files for efficient processing.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/
category:
- Browser Automation
framework:
- Gemini
---

# Puppeteer Web Scraping Pipeline

This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including –no-sandbox and –disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/)
