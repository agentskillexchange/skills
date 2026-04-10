---
title: "Puppeteer Multi-Tab Session Manager"
description: "Manages concurrent Puppeteer browser tabs with shared cookie jars and session persistence using Chrome DevTools Protocol. Handles tab lifecycle, navigation queues, and automatic retry with exponential backoff via puppeteer-cluster."
slug: "puppeteer-multi-tab-session-manager"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/"
---

# Puppeteer Multi-Tab Session Manager

Manages concurrent Puppeteer browser tabs with shared cookie jars and session persistence using Chrome DevTools Protocol. Handles tab lifecycle, navigation queues, and automatic retry with exponential backoff via puppeteer-cluster.

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
clawhub install puppeteer-multi-tab-session-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration.
Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows.
Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots.
Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/)
