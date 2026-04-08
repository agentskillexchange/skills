---
title: Puppeteer Stealth Scraper
description: The Puppeteer Stealth Scraper enables agents to navigate websites protected
  by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra
  with the stealth plugin to mask automation signals including navigator.webdriver,
  Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures
  Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer
  spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential
  IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows.
  It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via
  2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable
  burst capacity. Supports screenshot-on-failure debugging and HAR file generation
  for network analysis.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/
category:
- Browser Automation
framework:
- OpenClaw
---

# Puppeteer Stealth Scraper

The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/)
