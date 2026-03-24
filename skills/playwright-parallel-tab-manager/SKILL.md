---
name: "Playwright Parallel Tab Manager"
description: "Manages concurrent Playwright browser contexts with tab pooling and automatic resource cleanup. Integrates with Playwright BrowserContext API and chromium.launch() for parallel test execution across multiple viewports."
category: "Browser Automation"
framework: "Cursor"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-parallel-tab-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "playwright"  # from ase_tool_match
  github_stars: 84874  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 39806814  # from ase_npm_downloads
  github_repo: "microsoft/playwright"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Playwright Parallel Tab Manager

Manages concurrent Playwright browser contexts with tab pooling and automatic resource cleanup. Integrates with Playwright BrowserContext API and chromium.launch() for parallel test execution across multiple viewports.

## Overview

The Playwright Parallel Tab Manager skill orchestrates concurrent browser automation by managing pools of Playwright BrowserContext instances. It uses chromium.launch() with custom viewport configurations to spin up isolated browsing environments on demand.

Key capabilities include automatic tab lifecycle management through page.on(“close”) listeners, memory-aware context recycling that monitors process.memoryUsage(), and intelligent request interception via page.route() for blocking unnecessary assets during automation runs.

The skill integrates with Playwright’s built-in trace viewer (trace.zip) for debugging failed automation sequences and supports custom HAR recording through browser.newContext({ recordHar }) for network analysis. It handles cookie persistence across contexts using storageState and provides automatic retry logic with configurable backoff for flaky network conditions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill playwright-parallel-tab-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill playwright-parallel-tab-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill playwright-parallel-tab-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill playwright-parallel-tab-manager -a codex
```

### OpenClaw

```bash
clawhub install playwright-parallel-tab-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/playwright-parallel-tab-manager/
