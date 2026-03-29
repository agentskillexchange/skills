---
name: "Puppeteer Stealth Scraper"
description: "Anti-detection web scraping using puppeteer-extra-plugin-stealth with residential proxy rotation. Implements Canvas fingerprint spoofing and WebGL vendor masking via puppeteer-extra."
category: "Browser Automation"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
tool_ecosystem:
  tool: puppeteer
  github_stars: 93932
  npm_weekly_downloads: 8696130
  github_repo: puppeteer/puppeteer
  license: Apache-2.0
  maintained: true
---
# Puppeteer Stealth Scraper

Anti-detection web scraping using puppeteer-extra-plugin-stealth with residential proxy rotation. Implements Canvas fingerprint spoofing and WebGL vendor masking via puppeteer-extra.

## Overview

The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-scraper-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-scraper-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-scraper-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-stealth-scraper-agent -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-stealth-scraper-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/)
