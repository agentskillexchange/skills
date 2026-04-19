---
title: "Puppeteer Web Scraping Pipeline"
description: "This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including &#8211;no-sandbox and &#8211;disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Web Scraping Pipeline

This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including &#8211;no-sandbox and &#8211;disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/)
