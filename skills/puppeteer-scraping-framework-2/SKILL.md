---
title: "Puppeteer Scraping Framework"
description: "The Puppeteer Scraping Framework skill provides advanced web scraping capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra with the stealth plugin to avoid bot detection by patching navigator.webdriver, chrome.runtime, and other fingerprinting vectors. Core scraping features include request interception via page.setRequestInterception() for blocking unnecessary resources (images, fonts, stylesheets), cookie management with page.setCookie() for authenticated sessions, and automatic wait strategies using page.waitForSelector() and page.waitForNetworkIdle(). Advanced capabilities include Chrome DevTools Protocol (CDP) session access for low-level browser control, performance tracing via page.tracing.start(), and network condition emulation for mobile testing. The skill handles dynamic content rendering with configurable JavaScript execution timeouts and SPA navigation detection. Anti-detection features include proxy chain rotation via &#8211;proxy-server launch arguments, user agent randomization, viewport and timezone spoofing, and WebGL renderer hash randomization. Output supports structured data extraction via page.evaluate() with DOM manipulation."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Research &amp; Scraping"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Scraping Framework

The Puppeteer Scraping Framework skill provides advanced web scraping capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra with the stealth plugin to avoid bot detection by patching navigator.webdriver, chrome.runtime, and other fingerprinting vectors. Core scraping features include request interception via page.setRequestInterception() for blocking unnecessary resources (images, fonts, stylesheets), cookie management with page.setCookie() for authenticated sessions, and automatic wait strategies using page.waitForSelector() and page.waitForNetworkIdle(). Advanced capabilities include Chrome DevTools Protocol (CDP) session access for low-level browser control, performance tracing via page.tracing.start(), and network condition emulation for mobile testing. The skill handles dynamic content rendering with configurable JavaScript execution timeouts and SPA navigation detection. Anti-detection features include proxy chain rotation via &#8211;proxy-server launch arguments, user agent randomization, viewport and timezone spoofing, and WebGL renderer hash randomization. Output supports structured data extraction via page.evaluate() with DOM manipulation.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/)
