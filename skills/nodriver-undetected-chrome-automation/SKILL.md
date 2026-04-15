---
title: "Nodriver Async Undetected Chrome Browser Automation for Python"
description: "Nodriver is the official successor to Undetected-Chromedriver, providing async browser automation that communicates directly with Chrome DevTools Protocol without Selenium or WebDriver dependencies. Built for stealth web automation that bypasses anti-bot systems including Cloudflare and Imperva."
verification: security_reviewed
source: "https://github.com/ultrafunkamsterdam/nodriver"
category:
  - "Browser Automation"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ultrafunkamsterdam/nodriver"
  github_stars: 4005
---

# Nodriver Async Undetected Chrome Browser Automation for Python

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/nodriver-undetected-chrome-automation
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/nodriver-undetected-chrome-automation` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nodriver-undetected-chrome-automation/)
