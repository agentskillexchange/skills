---
title: "Puppeteer Web Scraping Pipeline"
description: "Builds web scraping pipelines with Puppeteer using page.evaluate, page.waitForSelector, and browser.newPage. Handles infinite scroll, cookie consent banners, and anti-bot detection with stealth plugin."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Web Scraping Pipeline

This skill creates robust web scraping pipelines using Puppeteer with the puppeteer-extra-plugin-stealth module for anti-detection. It launches headless Chrome via puppeteer.launch() with custom args including –no-sandbox and –disable-setuid-sandbox for container environments. Page interactions use page.evaluate() for DOM extraction, page.waitForSelector() with timeout configurations, and page.click() for pagination. Infinite scroll handling uses page.evaluate to detect scroll height changes and window.scrollTo() calls in a loop. Cookie consent banners are automatically dismissed through pattern matching on common consent management platforms like OneTrust and Cookiebot. The agent manages request interception via page.setRequestInterception(true) to block unnecessary resources like images and fonts for faster scraping. Data extraction uses querySelectorAll with structured mapping to JSON. Rate limiting is implemented with configurable delays between requests. The skill includes proxy rotation support via page.authenticate() and handles CAPTCHAs through 2captcha API integration when needed. Results are streamed to NDJSON files for efficient processing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-web-scraping-pipeline/)
