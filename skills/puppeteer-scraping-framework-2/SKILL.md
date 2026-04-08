---
title: Puppeteer Scraping Framework
description: The Puppeteer Scraping Framework skill provides advanced web scraping
  capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra
  with the stealth plugin to avoid bot detection by patching navigator.webdriver,
  chrome.runtime, and other fingerprinting vectors. Core scraping features include
  request interception via page.setRequestInterception() for blocking unnecessary
  resources (images, fonts, stylesheets), cookie management with page.setCookie()
  for authenticated sessions, and automatic wait strategies using page.waitForSelector()
  and page.waitForNetworkIdle(). Advanced capabilities include Chrome DevTools Protocol
  (CDP) session access for low-level browser control, performance tracing via page.tracing.start(),
  and network condition emulation for mobile testing. The skill handles dynamic content
  rendering with configurable JavaScript execution timeouts and SPA navigation detection.
  Anti-detection features include proxy chain rotation via –proxy-server launch arguments,
  user agent randomization, viewport and timezone spoofing, and WebGL renderer hash
  randomization. Output supports structured data extraction via page.evaluate() with
  DOM manipulation.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/
category:
- Research &amp; Scraping
framework:
- Claude Code
---

# Puppeteer Scraping Framework

The Puppeteer Scraping Framework skill provides advanced web scraping capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra with the stealth plugin to avoid bot detection by patching navigator.webdriver, chrome.runtime, and other fingerprinting vectors. Core scraping features include request interception via page.setRequestInterception() for blocking unnecessary resources (images, fonts, stylesheets), cookie management with page.setCookie() for authenticated sessions, and automatic wait strategies using page.waitForSelector() and page.waitForNetworkIdle(). Advanced capabilities include Chrome DevTools Protocol (CDP) session access for low-level browser control, performance tracing via page.tracing.start(), and network condition emulation for mobile testing. The skill handles dynamic content rendering with configurable JavaScript execution timeouts and SPA navigation detection. Anti-detection features include proxy chain rotation via –proxy-server launch arguments, user agent randomization, viewport and timezone spoofing, and WebGL renderer hash randomization. Output supports structured data extraction via page.evaluate() with DOM manipulation.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/)
