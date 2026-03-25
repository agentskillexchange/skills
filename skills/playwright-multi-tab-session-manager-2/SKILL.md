---
name: "Playwright Multi-Tab Session Manager"
description: "Manages concurrent Playwright browser contexts with tab isolation and cookie partitioning. Uses Playwright BrowserContext API for parallel tab orchestration with SharedArrayBuffer synchronization."
category: "Browser Automation"
framework: "Claude Code"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-multi-tab-session-manager-2/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Multi-Tab Session Manager

Manages concurrent Playwright browser contexts with tab isolation and cookie partitioning. Uses Playwright BrowserContext API for parallel tab orchestration with SharedArrayBuffer synchronization.

## Overview

The Playwright Multi-Tab Session Manager provides advanced browser automation for agents that need to operate across multiple tabs simultaneously. Built on the Playwright BrowserContext API, it creates isolated browser contexts with independent cookie jars, localStorage, and session state. Each tab runs in its own execution context with SharedArrayBuffer-based synchronization to prevent race conditions during parallel form submissions or data extraction. The skill supports automatic tab lifecycle management including creation, focus switching, and graceful teardown. It integrates with Playwright’s network interception layer to mock API responses per-tab, enabling complex testing scenarios. Error recovery uses exponential backoff with jitter for flaky page loads. Supports Chromium, Firefox, and WebKit engines with automatic binary management via playwright install.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-tab-session-manager-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-tab-session-manager-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-tab-session-manager-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-multi-tab-session-manager-2 -a codex
```

### OpenClaw

```bash
clawhub install playwright-multi-tab-session-manager-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-multi-tab-session-manager-2/
