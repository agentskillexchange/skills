---
name: "Puppeteer Stealth Scraper"
description: "Anti-detection web scraping using puppeteer-extra-plugin-stealth with residential proxy rotation. Implements Canvas fingerprint spoofing and WebGL vendor masking via puppeteer-extra."
category: "Browser Automation"
framework: "OpenClaw"
verification: verified_metadata  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "puppeteer"  # from ase_tool_match
  github_stars: 93912  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 8696130  # from ase_npm_downloads
  github_repo: "puppeteer/puppeteer"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/
