---
name: "Puppeteer Scraping Framework"
description: "Headless Chrome scraping using Puppeteer with stealth plugin, request interception via page.setRequestInterception(), and automatic CAPTCHA detection. Supports CDP sessions for advanced protocol access."
category: "Research & Scraping"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/"
---
# Puppeteer Scraping Framework

Headless Chrome scraping using Puppeteer with stealth plugin, request interception via page.setRequestInterception(), and automatic CAPTCHA detection. Supports CDP sessions for advanced protocol access.

The Puppeteer Scraping Framework skill provides advanced web scraping capabilities using Puppeteer with headless Chrome. It integrates puppeteer-extra with the stealth plugin to avoid bot detection by patching navigator.webdriver, chrome.runtime, and other fingerprinting vectors.



Core scraping features include request interception via page.setRequestInterception() for blocking unnecessary resources (images, fonts, stylesheets), cookie management with page.setCookie() for authenticated sessions, and automatic wait strategies using page.waitForSelector() and page.waitForNetworkIdle().



Advanced capabilities include Chrome DevTools Protocol (CDP) session access for low-level browser control, performance tracing via page.tracing.start(), and network condition emulation for mobile testing. The skill handles dynamic content rendering with configurable JavaScript execution timeouts and SPA navigation detection.



Anti-detection features include proxy chain rotation via –proxy-server launch arguments, user agent randomization, viewport and timezone spoofing, and WebGL renderer hash randomization. Output supports structured data extraction via page.evaluate() with DOM manipulation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-scraping-framework-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-scraping-framework-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-scraping-framework-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-scraping-framework-2 -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-scraping-framework-2
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-scraping-framework-2/)
