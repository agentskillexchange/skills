---
title: "Puppeteer Stealth Scraper"
description: "The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
  npm_package: "puppeteer"
---

# Puppeteer Stealth Scraper

The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/)
