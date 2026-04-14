---
title: "Puppeteer Scraping Framework"
description: "Headless Chrome scraping using Puppeteer with stealth plugin, request interception via page.setRequestInterception(), and automatic CAPTCHA detection. Supports CDP sessions for advanced protocol access."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Scraping Framework

The Puppeteer Scraping Framework skill provides advanced web scraping capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra with the stealth plugin to avoid bot detection by patching navigator.webdriver, chrome.runtime, and other fingerprinting vectors.

Core scraping features include request interception via page.setRequestInterception() for blocking unnecessary resources (images, fonts, stylesheets), cookie management with page.setCookie() for authenticated sessions, and automatic wait strategies using page.waitForSelector() and page.waitForNetworkIdle().

Advanced capabilities include Chrome DevTools Protocol (CDP) session access for low-level browser control, performance tracing via page.tracing.start(), and network condition emulation for mobile testing. The skill handles dynamic content rendering with configurable JavaScript execution timeouts and SPA navigation detection.

Anti-detection features include proxy chain rotation via –proxy-server launch arguments, user agent randomization, viewport and timezone spoofing, and WebGL renderer hash randomization. Output supports structured data extraction via page.evaluate() with DOM manipulation.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/)
