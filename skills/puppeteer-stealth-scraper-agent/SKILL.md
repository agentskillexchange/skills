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
---

# Puppeteer Stealth Scraper

The Puppeteer Stealth Scraper enables agents to navigate websites protected by bot detection systems like Cloudflare, DataDome, and PerimeterX. It uses puppeteer-extra with the stealth plugin to mask automation signals including navigator.webdriver, Chrome DevTools Protocol indicators, and headless Chrome signatures. The skill configures Canvas fingerprint randomization via canvas.toDataURL interception and WebGL vendor/renderer spoofing through ANGLE backend manipulation. Proxy rotation cycles through residential IP pools using luminati-proxy SDK with sticky sessions for multi-page workflows. It includes automatic CAPTCHA detection with hCaptcha and reCAPTCHA v2 solving via 2captcha-solver API. Rate limiting uses a token bucket algorithm with configurable burst capacity. Supports screenshot-on-failure debugging and HAR file generation for network analysis.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-stealth-scraper-agent/)
