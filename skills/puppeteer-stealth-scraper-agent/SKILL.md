---
title: "Puppeteer Stealth Scraper"
description: "Anti-detection web scraping using puppeteer-extra-plugin-stealth with residential proxy rotation. Implements Canvas fingerprint spoofing and WebGL vendor masking via puppeteer-extra."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
  ase_npm_package: "puppeteer"
---

# Puppeteer Stealth Scraper

The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/puppeteer-stealth-scraper-agent
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/puppeteer-stealth-scraper-agent` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/)
