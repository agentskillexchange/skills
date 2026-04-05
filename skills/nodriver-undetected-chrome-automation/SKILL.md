---
name: "Nodriver Async Undetected Chrome Browser Automation for Python"
description: "Nodriver is the official successor to Undetected-Chromedriver, providing async browser automation that communicates directly with Chrome DevTools Protocol without Selenium or WebDriver dependencies. Built for stealth web automation that bypasses anti-bot systems including Cloudflare and Imperva."
category: "Browser Automation"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/ultrafunkamsterdam/nodriver"
---
# Nodriver Async Undetected Chrome Browser Automation for Python

Nodriver is the official successor to Undetected-Chromedriver, providing async browser automation that communicates directly with Chrome DevTools Protocol without Selenium or WebDriver dependencies. Built for stealth web automation that bypasses anti-bot systems including Cloudflare and Imperva.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nodriver-undetected-chrome-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nodriver-undetected-chrome-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nodriver-undetected-chrome-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nodriver-undetected-chrome-automation -a codex
```

### OpenClaw

```bash
clawhub install nodriver-undetected-chrome-automation
```

## Details

Nodriver is a Python library that provides direct CDP (Chrome DevTools Protocol) communication with Chromium-based browsers for web automation tasks. As the official successor to the widely-used Undetected-Chromedriver package, Nodriver eliminates the Selenium and WebDriver dependencies entirely, communicating directly with the browser for better stealth and performance.

How It Works
Unlike traditional browser automation tools that use the WebDriver protocol (which is easily detectable), Nodriver communicates through CDP directly. This approach provides better resistance against Web Application Firewalls while delivering a significant performance boost. The library is fully asynchronous, built on Python asyncio, making it suitable for concurrent scraping and automation tasks.

Key Capabilities

Zero WebDriver Footprint: No chromedriver binary, no Selenium dependency. The browser appears as a normal user session to anti-bot systems.
Smart Element Lookup: Find elements by text or CSS selector, including within iframes. The text search matches by closest text length, so searching for “accept all” finds the actual cookie button rather than a script tag.
Cookie Persistence: Save and load cookies to files to avoid repeating login flows across sessions.
Cross-Browser Support: Works with Chrome, Chromium, Edge, and Brave browsers.
Auto Profile Cleanup: Uses fresh browser profiles by default and cleans up on exit, or can persist profiles for stateful workflows.
CDP Event Access: Full access to all CDP domains, methods, and events for advanced use cases like network interception and console monitoring.

Integration Points
Install with pip install nodriver. The API is intentionally simple—two lines of code get a browser running. It requires Chrome or a Chromium-based browser installed on the machine. For headless environments like AWS or VPS, use Xvfb for display emulation or run in headless mode. The library supports connecting to existing Chrome debug sessions, making it compatible with various deployment architectures.

Agent Use Cases
Agents that need to scrape content from sites protected by Cloudflare, Imperva, or DataDome can use Nodriver as their browser backend. Login-required automation workflows benefit from cookie persistence. Research agents can navigate JavaScript-heavy sites that block traditional HTTP scrapers. The async-first design makes it efficient for agents that need to manage multiple browser tabs or sessions concurrently.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nodriver-undetected-chrome-automation/)
