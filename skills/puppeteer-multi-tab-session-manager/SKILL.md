---
name: "Puppeteer Multi-Tab Session Manager"
description: "Manages concurrent Puppeteer browser tabs with shared cookie jars and session persistence using Chrome DevTools Protocol. Handles tab lifecycle, navigation queues, and automatic retry with exponential backoff via puppeteer-cluster."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/"
tool_ecosystem:
  tool: "puppeteer"
  github_stars: 93932
  npm_weekly_downloads: 8696130
  github_repo: "puppeteer/puppeteer"
  license: "Apache-2.0"
  maintained: true
---

# Puppeteer Multi-Tab Session Manager

Manages concurrent Puppeteer browser tabs with shared cookie jars and session persistence using Chrome DevTools Protocol. Handles tab lifecycle, navigation queues, and automatic retry with exponential backoff via puppeteer-cluster.

## Overview

The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration.

Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows.

Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots.

Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill puppeteer-multi-tab-session-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill puppeteer-multi-tab-session-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill puppeteer-multi-tab-session-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill puppeteer-multi-tab-session-manager -a codex
```

### OpenClaw

```bash
clawhub install puppeteer-multi-tab-session-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/
