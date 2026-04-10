---
title: "Nodriver Async Undetected Chrome Browser Automation for Python"
description: "Nodriver is the official successor to Undetected-Chromedriver, providing async browser automation that communicates directly with Chrome DevTools Protocol without Selenium or WebDriver dependencies. Built for stealth web automation that bypasses anti-bot systems including Cloudflare and Imperva."
slug: "nodriver-undetected-chrome-automation"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/ultrafunkamsterdam/nodriver"
---

# Nodriver Async Undetected Chrome Browser Automation for Python

Nodriver is the official successor to Undetected-Chromedriver, providing async browser automation that communicates directly with Chrome DevTools Protocol without Selenium or WebDriver dependencies. Built for stealth web automation that bypasses anti-bot systems including Cloudflare and Imperva.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install nodriver-undetected-chrome-automation
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Nodriver is a Python library that provides direct CDP (Chrome DevTools Protocol) communication with Chromium-based browsers for web automation tasks. As the official successor to the widely-used Undetected-Chromedriver package, Nodriver eliminates the Selenium and WebDriver dependencies entirely, communicating directly with the browser for better stealth and performance.
How It Works
Unlike traditional browser automation tools that use the WebDriver protocol (which is easily detectable), Nodriver communicates through CDP directly. This approach provides better resistance against Web Application Firewalls while delivering a significant performance boost. The library is fully asynchronous, built on Python asyncio, making it suitable for concurrent scraping and automation tasks.
Key Capabilities
- Zero WebDriver Footprint: No chromedriver binary, no Selenium dependency. The browser appears as a normal user session to anti-bot systems.
- Smart Element Lookup: Find elements by text or CSS selector, including within iframes. The text search matches by closest text length, so searching for “accept all” finds the actual cookie button rather than a script tag.
- Cookie Persistence: Save and load cookies to files to avoid repeating login flows across sessions.
- Cross-Browser Support: Works with Chrome, Chromium, Edge, and Brave browsers.
- Auto Profile Cleanup: Uses fresh browser profiles by default and cleans up on exit, or can persist profiles for stateful workflows.
- CDP Event Access: Full access to all CDP domains, methods, and events for advanced use cases like network interception and console monitoring.
Integration Points
Install with pip install nodriver. The API is intentionally simple—two lines of code get a browser running. It requires Chrome or a Chromium-based browser installed on the machine. For headless environments like AWS or VPS, use Xvfb for display emulation or run in headless mode. The library supports connecting to existing Chrome debug sessions, making it compatible with various deployment architectures.
Agent Use Cases
Agents that need to scrape content from sites protected by Cloudflare, Imperva, or DataDome can use Nodriver as their browser backend. Login-required automation workflows benefit from cookie persistence. Research agents can navigate JavaScript-heavy sites that block traditional HTTP scrapers. The async-first design makes it efficient for agents that need to manage multiple browser tabs or sessions concurrently.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nodriver-undetected-chrome-automation/)
