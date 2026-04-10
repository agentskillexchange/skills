---
name: "Playwright Multi-Tab Session Manager"
description: "Manages concurrent Playwright browser contexts with tab isolation and cookie partitioning. Uses Playwright BrowserContext API for parallel tab orchestration with SharedArrayBuffer synchronization."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/playwright-multi-tab-session-manager-2/"
category:
  - "Browser Automation"
framework:
  - "Claude Code"
---

# Playwright Multi-Tab Session Manager

The Playwright Multi-Tab Session Manager provides advanced browser automation for agents that need to operate across multiple tabs simultaneously. Built on the Playwright BrowserContext API, it creates isolated browser contexts with independent cookie jars, localStorage, and session state. Each tab runs in its own execution context with SharedArrayBuffer-based synchronization to prevent race conditions during parallel form submissions or data extraction. The skill supports automatic tab lifecycle management including creation, focus switching, and graceful teardown. It integrates with Playwright's network interception layer to mock API responses per-tab, enabling complex testing scenarios. Error recovery uses exponential backoff with jitter for flaky page loads. Supports Chromium, Firefox, and WebKit engines with automatic binary management via playwright install.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-multi-tab-session-manager-2/)
