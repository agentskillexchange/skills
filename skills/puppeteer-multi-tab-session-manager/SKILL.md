---
title: "Puppeteer Multi-Tab Session Manager"
description: "The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration. Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows. Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots. Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization."
source: "https://github.com/puppeteer/puppeteer"
verification: "security_reviewed"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Multi-Tab Session Manager

The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration. Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows. Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots. Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/)
