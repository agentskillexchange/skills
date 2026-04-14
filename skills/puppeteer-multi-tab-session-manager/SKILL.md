---
title: "Puppeteer Multi-Tab Session Manager"
description: "Manages concurrent Puppeteer browser tabs with shared cookie jars and session persistence using Chrome DevTools Protocol. Handles tab lifecycle, navigation queues, and automatic retry with exponential backoff via puppeteer-cluster."
verification: security_reviewed
source: "https://github.com/puppeteer/puppeteer"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "puppeteer/puppeteer"
  github_stars: 94115
---

# Puppeteer Multi-Tab Session Manager

The Puppeteer Multi-Tab Session Manager provides robust orchestration of concurrent browser tabs for complex web automation workflows. Built on top of puppeteer-cluster, it manages tab pools with configurable concurrency limits, shared cookie storage, and automatic session restoration.

Key capabilities include CDP-level session management using Chrome DevTools Protocol for fine-grained control over network interception, cookie manipulation, and request throttling. The skill supports persistent browser contexts that survive page navigations, enabling long-running scraping or testing workflows.

Advanced features include automatic retry logic with configurable exponential backoff, dead tab detection and recycling, memory usage monitoring per tab, and screenshot-on-failure diagnostics. The session state serializer can export and import full browser state including localStorage, sessionStorage, and IndexedDB snapshots.

Integrates with proxy rotation services (BrightData, Oxylabs) for IP management and includes built-in user agent rotation using the ua-parser-js library for fingerprint randomization.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/puppeteer-multi-tab-session-manager/)
