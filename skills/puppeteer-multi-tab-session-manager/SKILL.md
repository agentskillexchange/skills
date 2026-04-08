---
title: Puppeteer Multi-Tab Session Manager
description: The Puppeteer Multi-Tab Session Manager provides robust orchestration
  of concurrent browser tabs for complex web automation workflows. Built on top of
  puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared
  cookie storage, and automatic session restoration. Key capabilities include CDP-level
  session management using Chrome DevTools Protocol for fine-grained control over
  network interception, cookie manipulation, and request throttling. The skill supports
  persistent browser contexts that survive page navigations, enabling long-running
  scraping or testing workflows. Advanced features include automatic retry logic with
  configurable exponential backoff, dead tab detection and recycling, memory usage
  monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer
  can export and import full browser state including localStorage, sessionStorage,
  and IndexedDB snapshots. Integrates with proxy rotation services (BrightData, Oxylabs)
  for IP management and includes built-in user agent rotation using the ua-parser-js
  library for fingerprint randomization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/
category:
- Browser Automation
framework:
- Claude Code
---

# Puppeteer Multi-Tab Session Manager

The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration. Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows. Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots. Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/)
